#!/usr/bin/env node
const fs = require('fs');
const os = require('os');
const path = require('path');
const { pathToFileURL } = require('url');
const { createRequire } = require('module');
const { spawnSync } = require('child_process');

const SKILL_ROOT = path.resolve(__dirname, '..');
const DEFAULT_RUNTIME = path.join(os.homedir(), '.cache', 'kali-skill');
const RUNTIME_ROOT = process.env.KALI_SKILL_RUNTIME || DEFAULT_RUNTIME;
const PLAYWRIGHT_ROOT = path.join(RUNTIME_ROOT, 'playwright');

function usage() {
  console.log(`Reusable CTF browser tooling

Commands:
  check-env
  snapshot --case-dir DIR --url URL [--label LABEL] [--storage-state FILE] [--user-data-dir DIR]
  video-captures --case-dir DIR --url URL [--label LABEL] [--times 1,8,16,30]
  contact-sheet --case-dir DIR --match REGEX [--label LABEL]

Options:
  --cookie COOKIE           add a browser cookie, repeatable; accepts name=value or Set-Cookie style text
  --capture-bodies          save small non-video response bodies from browser network events
  --body-max-bytes N        max captured response body size, default 262144
  --columns N              contact sheet columns, default 5
  --wait-ms N              extra wait after navigation, default 1500
  --timeout-ms N           navigation timeout, default 60000
  --width N                viewport width, default 1365
  --height N               viewport height, default 900
  --save-storage-state F   write updated browser storage state
  --no-full-page           disable full-page screenshot
`);
}

function getArg(name, fallback = null) {
  const index = process.argv.indexOf(name);
  if (index === -1 || index + 1 >= process.argv.length) return fallback;
  return process.argv[index + 1];
}

function getArgs(name) {
  const values = [];
  for (let index = 0; index < process.argv.length; index += 1) {
    if (process.argv[index] === name && index + 1 < process.argv.length) {
      values.push(process.argv[index + 1]);
    }
  }
  return values;
}

function hasArg(name) {
  return process.argv.includes(name);
}

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function slug(value) {
  return String(value || 'browser').toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_+|_+$/g, '') || 'browser';
}

function readJson(file, fallback = {}) {
  if (!file || !fs.existsSync(file)) return fallback;
  return JSON.parse(fs.readFileSync(file, 'utf8'));
}

function writeJson(file, value) {
  ensureDir(path.dirname(file));
  fs.writeFileSync(file, JSON.stringify(value, null, 2) + '\n');
}

function extensionForContentType(contentType) {
  const value = String(contentType || '').toLowerCase();
  if (value.includes('application/json')) return '.json';
  if (value.includes('text/html')) return '.html';
  if (value.includes('javascript')) return '.js';
  if (value.includes('text/css')) return '.css';
  if (value.includes('text/plain')) return '.txt';
  return '.body';
}

function makeResponseRecorder(label, responsesDir) {
  const captureBodies = hasArg('--capture-bodies');
  const bodyMaxBytes = Number(getArg('--body-max-bytes', '262144'));
  const network = [];
  const pending = [];
  const onResponse = async response => {
    const request = response.request();
    const headers = response.headers();
    const contentType = headers['content-type'] || '';
    const entry = {
      url: response.url(),
      status: response.status(),
      method: request.method(),
      resourceType: request.resourceType(),
      contentType,
    };
    network.push(entry);
    if (!captureBodies) return;
    if (/video\//i.test(contentType)) return;
    if (!['document', 'xhr', 'fetch', 'script'].includes(request.resourceType())) return;
    const contentLength = Number(headers['content-length'] || '0');
    if (contentLength > bodyMaxBytes) {
      entry.bodySkipped = `content-length ${contentLength} exceeds ${bodyMaxBytes}`;
      return;
    }
    const index = network.length;
    const work = response.body()
      .then(buffer => {
        if (buffer.length > bodyMaxBytes) {
          entry.bodySkipped = `body ${buffer.length} exceeds ${bodyMaxBytes}`;
          return;
        }
        const output = path.join(responsesDir, `${label}-net-${String(index).padStart(3, '0')}${extensionForContentType(contentType)}`);
        fs.writeFileSync(output, buffer);
        entry.bodyPath = output;
        entry.bodySize = buffer.length;
      })
      .catch(error => {
        entry.bodyError = String(error);
      });
    pending.push(work);
  };
  return { network, pending, onResponse };
}

function resolveCaseUrl(caseDir, value) {
  if (/^https?:\/\//i.test(value)) return value;
  const meta = readJson(path.join(caseDir, 'case.json'), {});
  if (!meta.url) throw new Error('relative URL needs case.json with url');
  return new URL(value, meta.url).toString();
}

function requirePlaywright() {
  try {
    return require('playwright');
  } catch (_) {}

  const packageJson = path.join(PLAYWRIGHT_ROOT, 'package.json');
  try {
    return createRequire(packageJson)('playwright');
  } catch (_) {}

  ensureDir(PLAYWRIGHT_ROOT);
  const npm = spawnSync('npm', ['install', '--prefix', PLAYWRIGHT_ROOT, 'playwright'], {
    stdio: 'inherit',
  });
  if (npm.status !== 0) {
    throw new Error('failed to install playwright into runtime cache');
  }
  return createRequire(packageJson)('playwright');
}

function parseCookie(raw, targetUrl) {
  const url = new URL(targetUrl);
  const parts = String(raw || '').split(';').map(part => part.trim()).filter(Boolean);
  if (!parts.length || !parts[0].includes('=')) return null;
  const [name, ...valueParts] = parts[0].split('=');
  const cookie = {
    name: name.trim(),
    value: valueParts.join('=').trim(),
    domain: url.hostname,
    path: '/',
    secure: url.protocol === 'https:',
    httpOnly: false,
    sameSite: 'Lax',
  };
  for (const attr of parts.slice(1)) {
    const [attrNameRaw, ...attrValueParts] = attr.split('=');
    const attrName = attrNameRaw.trim().toLowerCase();
    const attrValue = attrValueParts.join('=').trim();
    if (attrName === 'domain' && attrValue) cookie.domain = attrValue.replace(/^\./, '');
    if (attrName === 'path' && attrValue) cookie.path = attrValue;
    if (attrName === 'secure') cookie.secure = true;
    if (attrName === 'httponly') cookie.httpOnly = true;
    if (attrName === 'samesite' && attrValue) {
      const normalized = attrValue.toLowerCase();
      if (normalized === 'strict') cookie.sameSite = 'Strict';
      else if (normalized === 'none') cookie.sameSite = 'None';
      else cookie.sameSite = 'Lax';
    }
  }
  return cookie;
}

async function addArgCookies(context, url) {
  const cookies = getArgs('--cookie').map(raw => parseCookie(raw, url)).filter(Boolean);
  if (cookies.length) {
    await context.addCookies(cookies);
  }
  return cookies;
}

function checkEnv() {
  let npmAvailable = spawnSync('npm', ['--version'], { encoding: 'utf8' });
  let playwrightAvailable = false;
  try {
    requirePlaywright();
    playwrightAvailable = true;
  } catch (_) {}
  console.log(JSON.stringify({
    node: process.version,
    npm: npmAvailable.status === 0 ? npmAvailable.stdout.trim() : null,
    skillRoot: SKILL_ROOT,
    runtimeRoot: RUNTIME_ROOT,
    playwrightRoot: PLAYWRIGHT_ROOT,
    playwrightAvailable,
  }, null, 2));
}

async function snapshot() {
  const caseDir = path.resolve(getArg('--case-dir') || '');
  const rawUrl = getArg('--url');
  if (!caseDir || !rawUrl) throw new Error('snapshot requires --case-dir and --url');
  const label = slug(getArg('--label', 'browser'));
  const url = resolveCaseUrl(caseDir, rawUrl);
  const width = Number(getArg('--width', '1365'));
  const height = Number(getArg('--height', '900'));
  const waitMs = Number(getArg('--wait-ms', '1500'));
  const timeoutMs = Number(getArg('--timeout-ms', '60000'));
  const artifactsDir = path.join(caseDir, 'artifacts');
  const responsesDir = path.join(caseDir, 'responses');
  ensureDir(artifactsDir);
  ensureDir(responsesDir);

  const { chromium } = requirePlaywright();
  const userDataDir = getArg('--user-data-dir');
  const storageState = getArg('--storage-state');
  const contextOptions = {
    viewport: { width, height },
    ignoreHTTPSErrors: true,
  };
  if (storageState && fs.existsSync(storageState)) {
    contextOptions.storageState = storageState;
  }

  let browser = null;
  let context = null;
  if (userDataDir) {
    ensureDir(userDataDir);
    context = await chromium.launchPersistentContext(userDataDir, {
      headless: true,
      ...contextOptions,
    });
  } else {
    browser = await chromium.launch({ headless: true });
    context = await browser.newContext(contextOptions);
  }

  const injectedCookies = await addArgCookies(context, url);
  const page = await context.newPage();
  const responseRecorder = makeResponseRecorder(label, responsesDir);
  const consoleMessages = [];
  page.on('response', responseRecorder.onResponse);
  page.on('console', message => {
    consoleMessages.push({ type: message.type(), text: message.text() });
  });

  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: timeoutMs });
    try { await page.waitForLoadState('networkidle', { timeout: Math.min(timeoutMs, 15000) }); } catch (_) {}
    if (waitMs > 0) await page.waitForTimeout(waitMs);
    await Promise.allSettled(responseRecorder.pending);

    const title = await page.title().catch(() => '');
    const bodyText = await page.locator('body').innerText({ timeout: 5000 }).catch(() => '');
    const html = await page.content().catch(() => '');
    const localStorage = await page.evaluate(() => Object.fromEntries(Object.entries(window.localStorage || {}))).catch(() => ({}));
    const sessionStorage = await page.evaluate(() => Object.fromEntries(Object.entries(window.sessionStorage || {}))).catch(() => ({}));
    const cookies = await context.cookies().catch(() => []);

    const screenshotPath = path.join(artifactsDir, `${label}.png`);
    const htmlPath = path.join(responsesDir, `${label}.html`);
    const textPath = path.join(artifactsDir, `${label}-body.txt`);
    const summaryPath = path.join(artifactsDir, `${label}-browser-summary.json`);
    await page.screenshot({ path: screenshotPath, fullPage: !hasArg('--no-full-page') });
    fs.writeFileSync(htmlPath, html, 'utf8');
    fs.writeFileSync(textPath, bodyText, 'utf8');
    if (getArg('--save-storage-state')) {
      await context.storageState({ path: getArg('--save-storage-state') });
    }
    const flags = Array.from(new Set(`${bodyText}\n${html}`.match(/flag\{[^}\s]+\}/gi) || []));
    const summary = {
      time: new Date().toISOString(),
      url: page.url(),
      title,
      flags,
      screenshot: screenshotPath,
      html: htmlPath,
      text: textPath,
      bodySample: bodyText.slice(0, 2000),
      localStorage,
      sessionStorage,
      cookies: cookies.map(cookie => ({
        name: cookie.name,
        domain: cookie.domain,
        path: cookie.path,
        expires: cookie.expires,
        httpOnly: cookie.httpOnly,
        secure: cookie.secure,
        sameSite: cookie.sameSite,
      })),
      injectedCookies: injectedCookies.map(cookie => ({
        name: cookie.name,
        domain: cookie.domain,
        path: cookie.path,
        secure: cookie.secure,
        httpOnly: cookie.httpOnly,
        sameSite: cookie.sameSite,
      })),
      network: responseRecorder.network,
      console: consoleMessages,
    };
    writeJson(summaryPath, summary);
    console.log(JSON.stringify({ status: 'ok', summary: summaryPath, screenshot: screenshotPath, flags }, null, 2));
  } finally {
    await context.close();
    if (browser) await browser.close();
  }
}

function parseTimes(raw) {
  return String(raw || '1,8,16,20,30')
    .split(',')
    .map(value => Number(value.trim()))
    .filter(value => Number.isFinite(value) && value >= 0);
}

async function videoCaptures() {
  const caseDir = path.resolve(getArg('--case-dir') || '');
  const rawUrl = getArg('--url');
  if (!caseDir || !rawUrl) throw new Error('video-captures requires --case-dir and --url');
  const label = slug(getArg('--label', 'video'));
  const url = resolveCaseUrl(caseDir, rawUrl);
  const width = Number(getArg('--width', '1365'));
  const height = Number(getArg('--height', '900'));
  const waitMs = Number(getArg('--wait-ms', '2500'));
  const timeoutMs = Number(getArg('--timeout-ms', '60000'));
  const times = parseTimes(getArg('--times', '1,8,16,20,30'));
  const artifactsDir = path.join(caseDir, 'artifacts');
  const responsesDir = path.join(caseDir, 'responses');
  ensureDir(artifactsDir);
  ensureDir(responsesDir);

  const { chromium } = requirePlaywright();
  const contextOptions = {
    viewport: { width, height },
    ignoreHTTPSErrors: true,
  };
  const storageState = getArg('--storage-state');
  if (storageState && fs.existsSync(storageState)) {
    contextOptions.storageState = storageState;
  }

  let browser = null;
  let context = null;
  const userDataDir = getArg('--user-data-dir');
  if (userDataDir) {
    ensureDir(userDataDir);
    context = await chromium.launchPersistentContext(userDataDir, {
      headless: true,
      ...contextOptions,
    });
  } else {
    browser = await chromium.launch({ headless: true });
    context = await browser.newContext(contextOptions);
  }

  const injectedCookies = await addArgCookies(context, url);
  const page = await context.newPage();
  const responseRecorder = makeResponseRecorder(label, responsesDir);
  const consoleMessages = [];
  page.on('response', responseRecorder.onResponse);
  page.on('console', message => {
    consoleMessages.push({ type: message.type(), text: message.text() });
  });

  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: timeoutMs });
    try { await page.waitForLoadState('networkidle', { timeout: Math.min(timeoutMs, 15000) }); } catch (_) {}
    if (waitMs > 0) await page.waitForTimeout(waitMs);
    await page.locator('video').first().waitFor({ state: 'attached', timeout: 20000 }).catch(() => {});
    await page.mouse.click(Math.floor(width / 2), Math.floor(height / 2)).catch(() => {});

    const captures = [];
    for (const time of times) {
      const probe = await page.evaluate(async seekTime => {
        const video = document.querySelector('video');
        if (!video) return { error: 'no video element' };
        video.muted = true;
        const duration = Number.isFinite(video.duration) ? video.duration : null;
        const target = duration ? Math.max(0, Math.min(seekTime, duration - 0.05)) : seekTime;
        let seekResult = {};
        try {
          seekResult = await new Promise(resolve => {
            let settled = false;
            const finish = result => {
              if (settled) return;
              settled = true;
              clearTimeout(timer);
              video.removeEventListener('seeked', onSeeked);
              resolve(result);
            };
            const onSeeked = () => finish({ seeked: true });
            const timer = setTimeout(() => finish({ seeked: false, timeout: true }), 6000);
            video.addEventListener('seeked', onSeeked, { once: true });
            video.currentTime = target;
          });
          await video.play().catch(() => {});
          await new Promise(resolve => setTimeout(resolve, 900));
        } catch (error) {
          seekResult = { error: String(error) };
        }
        return {
          requestedTime: seekTime,
          targetTime: target,
          currentTime: video.currentTime,
          duration,
          readyState: video.readyState,
          paused: video.paused,
          seekResult,
        };
      }, time).catch(error => ({ error: String(error), requestedTime: time }));

      const timeSlug = String(time).replace(/[^0-9.]+/g, '_').replace(/\./g, '_');
      const pageShot = path.join(artifactsDir, `${label}-t${timeSlug}-page.png`);
      const videoShot = path.join(artifactsDir, `${label}-t${timeSlug}-video.png`);
      await page.screenshot({ path: pageShot, fullPage: false }).catch(() => {});
      let videoCapture = null;
      try {
        await page.locator('video').first().screenshot({ path: videoShot });
        videoCapture = videoShot;
      } catch (_) {}
      captures.push({ time, probe, pageShot, videoShot: videoCapture });
    }
    await Promise.allSettled(responseRecorder.pending);

    const bodyText = await page.locator('body').innerText({ timeout: 5000 }).catch(() => '');
    const html = await page.content().catch(() => '');
    const htmlPath = path.join(responsesDir, `${label}.html`);
    const textPath = path.join(artifactsDir, `${label}-body.txt`);
    const summaryPath = path.join(artifactsDir, `${label}-video-captures.json`);
    fs.writeFileSync(htmlPath, html, 'utf8');
    fs.writeFileSync(textPath, bodyText, 'utf8');
    if (getArg('--save-storage-state')) {
      await context.storageState({ path: getArg('--save-storage-state') });
    }
    const flags = Array.from(new Set(`${bodyText}\n${html}`.match(/flag\{[^}\s]+\}/gi) || []));
    const cookies = await context.cookies().catch(() => []);
    const summary = {
      time: new Date().toISOString(),
      url: page.url(),
      title: await page.title().catch(() => ''),
      flags,
      html: htmlPath,
      text: textPath,
      injectedCookies: injectedCookies.map(cookie => ({
        name: cookie.name,
        domain: cookie.domain,
        path: cookie.path,
        secure: cookie.secure,
        httpOnly: cookie.httpOnly,
        sameSite: cookie.sameSite,
      })),
      cookies: cookies.map(cookie => ({
        name: cookie.name,
        domain: cookie.domain,
        path: cookie.path,
        expires: cookie.expires,
        httpOnly: cookie.httpOnly,
        secure: cookie.secure,
        sameSite: cookie.sameSite,
      })),
      captures,
      network: responseRecorder.network,
      console: consoleMessages,
    };
    writeJson(summaryPath, summary);
    console.log(JSON.stringify({ status: 'ok', summary: summaryPath, captures: captures.length, flags }, null, 2));
  } finally {
    await context.close();
    if (browser) await browser.close();
  }
}

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

async function contactSheet() {
  const caseDir = path.resolve(getArg('--case-dir') || '');
  const rawMatch = getArg('--match');
  if (!caseDir || !rawMatch) throw new Error('contact-sheet requires --case-dir and --match');
  const label = slug(getArg('--label', 'contact-sheet'));
  const columns = Number(getArg('--columns', '5'));
  const width = Number(getArg('--width', '1600'));
  const artifactsDir = path.join(caseDir, 'artifacts');
  const responsesDir = path.join(caseDir, 'responses');
  ensureDir(artifactsDir);
  ensureDir(responsesDir);

  const matcher = new RegExp(rawMatch);
  const images = fs.readdirSync(artifactsDir)
    .filter(name => /\.(png|jpe?g|webp)$/i.test(name) && matcher.test(name))
    .sort((left, right) => left.localeCompare(right, undefined, { numeric: true }))
    .map(name => path.join(artifactsDir, name));
  if (!images.length) throw new Error(`no images matched ${rawMatch}`);

  const htmlPath = path.join(responsesDir, `${label}-contact-sheet.html`);
  const sheetPath = path.join(artifactsDir, `${label}-contact-sheet.png`);
  const summaryPath = path.join(artifactsDir, `${label}-contact-sheet.json`);
  const htmlDir = path.dirname(htmlPath);
  const html = `<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body { margin: 0; background: #111; color: #eee; font-family: Arial, sans-serif; }
    .grid { display: grid; grid-template-columns: repeat(${Math.max(1, columns)}, 1fr); gap: 8px; padding: 8px; }
    .cell { background: #1b1b1b; border: 1px solid #333; }
    .cell img { display: block; width: 100%; height: auto; background: #000; }
    .label { font-size: 14px; line-height: 1.3; padding: 5px 6px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  </style>
</head>
<body>
  <div class="grid">
    ${images.map(file => {
      const src = path.relative(htmlDir, file).split(path.sep).join('/');
      return `<div class="cell"><img src="${escapeHtml(src)}"><div class="label">${escapeHtml(path.basename(file))}</div></div>`;
    }).join('\n    ')}
  </div>
</body>
</html>
`;
  fs.writeFileSync(htmlPath, html, 'utf8');

  const { chromium } = requirePlaywright();
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width, height: 900 }, deviceScaleFactor: 1 });
  try {
    await page.goto(pathToFileURL(htmlPath).toString(), { waitUntil: 'load', timeout: 60000 });
    await page.waitForTimeout(Number(getArg('--wait-ms', '500')));
    await page.screenshot({ path: sheetPath, fullPage: true });
  } finally {
    await browser.close();
  }
  const summary = {
    time: new Date().toISOString(),
    match: rawMatch,
    images,
    sheet: sheetPath,
    html: htmlPath,
  };
  writeJson(summaryPath, summary);
  console.log(JSON.stringify({ status: 'ok', summary: summaryPath, sheet: sheetPath, images: images.length }, null, 2));
}

async function main() {
  const command = process.argv[2];
  if (!command || command === '-h' || command === '--help') {
    usage();
    return;
  }
  if (command === 'check-env') {
    checkEnv();
    return;
  }
  if (command === 'snapshot') {
    await snapshot();
    return;
  }
  if (command === 'video-captures') {
    await videoCaptures();
    return;
  }
  if (command === 'contact-sheet') {
    await contactSheet();
    return;
  }
  throw new Error(`unknown command: ${command}`);
}

main().catch(error => {
  console.error(error.stack || String(error));
  process.exit(1);
});
