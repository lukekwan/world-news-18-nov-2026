import { chromium } from 'playwright-core';
import { fileURLToPath } from 'url';
import path from 'path';

const dir = path.dirname(fileURLToPath(import.meta.url));

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1024, height: 1024 } });
await page.goto('file://' + path.join(dir, 'poster.html'));
await page.waitForTimeout(400);
await page.screenshot({ path: path.join(dir, 'entry.png') });
await browser.close();
console.log('wrote entry.png');
