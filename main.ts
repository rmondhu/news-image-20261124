// news-image-20261123 — "THE WORLD TODAY" front page entry.
//
// What this program does: it ships the finished 1024x1024 front-page PNG
// (entry.png, rendered at build time from render.html with Playwright) as
// the entry image. At run time it only reads that one local file, checks
// that it really is the PNG the gate expects, and writes an exact copy to
// the output directory. No network, no randomness, no clock, no fonts or
// rendering at run time — so two runs produce byte-identical output.
//
// Usage (outside the grader's container, /output is replaced by
// MAKEFUN_OUTPUT_DIR):
//   MAKEFUN_OUTPUT_DIR=out node main.ts

import { createHash } from 'node:crypto';
import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

// Gate limits for this competition: one whole PNG or JPEG, at most
// 1 MiB and 1024 by 1024 pixels.
const MAX_BYTES = 1_048_576;
const EXPECTED_WIDTH = 1024;
const EXPECTED_HEIGHT = 1024;

// The PNG file signature: 89 50 4E 47 0D 0A 1A 0A.
const PNG_SIGNATURE = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);

// Fail fast with a readable message instead of a bare stack trace.
function fail(message) {
  console.error(`main.ts: ${message}`);
  process.exit(1);
}

// Read one big-endian unsigned 32-bit integer from a buffer.
function readU32BE(buffer, offset) {
  return buffer.readUInt32BE(offset);
}

function main() {
  const here = dirname(fileURLToPath(import.meta.url));
  const sourcePath = join(here, 'entry.png');

  let image;
  try {
    image = readFileSync(sourcePath);
  } catch {
    fail(`cannot read ${sourcePath}`);
  }

  // 1. It must be a PNG at all.
  if (image.length < 33 || !image.subarray(0, 8).equals(PNG_SIGNATURE)) {
    fail('entry.png is not a PNG file (bad signature)');
  }

  // 2. Read the dimensions out of the IHDR chunk: the chunk starts at
  // byte 8 (4 length + 4 type "IHDR"), width at +8, height at +12.
  const ihdrType = image.toString('ascii', 12, 16);
  if (ihdrType !== 'IHDR') {
    fail('entry.png has no IHDR chunk where a PNG should');
  }
  const width = readU32BE(image, 16);
  const height = readU32BE(image, 20);
  if (width !== EXPECTED_WIDTH || height !== EXPECTED_HEIGHT) {
    fail(`entry.png is ${width}x${height}, expected ${EXPECTED_WIDTH}x${EXPECTED_HEIGHT}`);
  }

  // 3. It must fit the gate's size limit.
  if (image.length > MAX_BYTES) {
    fail(`entry.png is ${image.length} bytes, over the ${MAX_BYTES} byte limit`);
  }

  // 4. Write an exact copy to the output directory, creating it first.
  const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
  const outPath = join(outDir, 'entry.png');
  try {
    mkdirSync(outDir, { recursive: true });
    writeFileSync(outPath, image);
  } catch {
    fail(`cannot write ${outPath}`);
  }

  const sha256 = createHash('sha256').update(image).digest('hex');
  console.log(`wrote ${outPath} (${image.length} bytes, ${width}x${height}, sha256 ${sha256})`);
}

main();
