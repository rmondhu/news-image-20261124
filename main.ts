// Entry runner — "THE WORLD TODAY", Tuesday 24 November 2026.
//
// The finished front page already exists beside this file as entry.png; it
// was painted at build time from render.html with a headless browser. When
// this program runs under the grader it only has to prove that picture is
// the one the competition asks for, then hand over a byte-for-byte copy.
// Nothing is downloaded, nothing is drawn, nothing reads the clock, so two
// runs always agree exactly.
//
// Give it a destination folder like this:
//   MAKEFUN_OUTPUT_DIR=out node main.ts

import * as crypto from 'node:crypto';
import * as fs from 'node:fs';
import * as path from 'node:path';
import { fileURLToPath as urlToPath } from 'node:url';

// The picture must be square, 1024 pixels on a side, and fit in a mebibyte.
const SIDE_PX = 1024;
const BYTE_CAP = 1024 * 1024;
const OUT_NAME = 'entry.png';

// Every PNG file opens with these eight bytes, written here as hex.
const MAGIC_HEX = '89504e470d0a1a0a';

function die(why: string): never {
  console.error(`entry runner: ${why}`);
  throw new Error(why);
}

function folderOfThisFile(): string {
  return path.dirname(urlToPath(import.meta.url));
}

function loadPicture(): Buffer {
  const target = path.join(folderOfThisFile(), OUT_NAME);
  try {
    return fs.readFileSync(target);
  } catch {
    die(`cannot open ${target}`);
  }
}

function pictureSize(bytes: Buffer): { w: number; h: number } {
  const magic = Buffer.from(MAGIC_HEX, 'hex');
  if (bytes.length < 8 + 25 || !bytes.subarray(0, 8).equals(magic)) {
    die('entry.png does not open with the PNG magic bytes');
  }
  const chunkTag = bytes.subarray(12, 16).toString('latin1');
  if (chunkTag !== 'IHDR') {
    die('entry.png has no IHDR chunk where one belongs');
  }
  const view = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
  return { w: view.getUint32(16, false), h: view.getUint32(20, false) };
}

function run(): void {
  const bytes = loadPicture();
  const { w, h } = pictureSize(bytes);
  if (w !== SIDE_PX || h !== SIDE_PX) {
    die(`entry.png measures ${w}x${h}, but the gate wants ${SIDE_PX}x${SIDE_PX}`);
  }
  if (bytes.length > BYTE_CAP) {
    die(`entry.png weighs ${bytes.length} bytes, past the ${BYTE_CAP} byte cap`);
  }
  const outDir = process.env['MAKEFUN_OUTPUT_DIR'] ?? '/output';
  const outPath = path.join(outDir, OUT_NAME);
  try {
    fs.mkdirSync(outDir, { recursive: true });
    fs.writeFileSync(outPath, bytes);
  } catch {
    die(`cannot write ${outPath}`);
  }
  const digest = crypto.createHash('sha256').update(bytes).digest('hex');
  console.log(`wrote ${outPath} — ${bytes.length} bytes, ${w}x${h}, sha256 ${digest}`);
}

run();
