// The Wednesday Globe — entry point.
// Copies the pre-rendered front page (entry.png, built by draw25-wed.py)
// into MAKEFUN_OUTPUT_DIR and checks it before and after the copy.
// No network, no cwd reads: every path is resolved from this file's folder.

import { createHash } from "node:crypto";
import { copyFileSync, mkdirSync, readFileSync, statSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const SRC = join(HERE, "entry.png");
const OUT_DIR = process.env.MAKEFUN_OUTPUT_DIR;
if (!OUT_DIR) {
  throw new Error("MAKEFUN_OUTPUT_DIR is not set");
}
mkdirSync(OUT_DIR, { recursive: true });
const DEST = join(OUT_DIR, "entry.png");

function sha256(bytes: Buffer): string {
  return createHash("sha256").update(bytes).digest("hex");
}

function checkPng(bytes: Buffer, label: string): void {
  const magic = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
  if (bytes.length < 33 || !bytes.subarray(0, 8).equals(magic)) {
    throw new Error(label + ": not a PNG file");
  }
  const width = bytes.readUInt32BE(16);
  const height = bytes.readUInt32BE(20);
  if (width !== 1024 || height !== 1024) {
    throw new Error(label + ": expected 1024x1024, got " + width + "x" + height);
  }
  if (bytes.length > 1024 * 1024) {
    throw new Error(label + ": over 1 MiB (" + bytes.length + " bytes)");
  }
}

const original = readFileSync(SRC);
checkPng(original, "entry.png");
const before = sha256(original);

copyFileSync(SRC, DEST);

const written = readFileSync(DEST);
checkPng(written, "output entry.png");
const after = sha256(written);
if (before !== after) {
  throw new Error("sha256 mismatch after copy: " + before + " vs " + after);
}

const size = statSync(DEST).size;
if (size !== original.length) {
  throw new Error("size mismatch after copy: " + size + " vs " + original.length);
}
writeFileSync(join(OUT_DIR, "entry.sha256"), before + "  entry.png\n");
console.log("entry.png copied: " + size + " bytes, 1024x1024, sha256 " + before);
