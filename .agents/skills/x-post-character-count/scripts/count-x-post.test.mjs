import test from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const currentDir = path.dirname(fileURLToPath(import.meta.url));
const scriptPath = path.join(currentDir, 'count-x-post.mjs');

function count(text) {
  const output = execFileSync(process.execPath, [scriptPath, '--text', text, '--json'], {
    encoding: 'utf8',
  });
  return JSON.parse(output);
}

test('counts ASCII as weight 1', () => {
  const result = count('Hello');
  assert.equal(result.weightedLength, 5);
  assert.equal(result.zone, 'safe');
});

test('counts Japanese characters as weight 2', () => {
  const result = count('日本語');
  assert.equal(result.weightedLength, 6);
});

test('counts a URL as the t.co fixed length', () => {
  const result = count('https://example.com/very/long/path');
  assert.equal(result.weightedLength, 23);
  assert.equal(result.urlCount, 1);
});

test('counts a ZWJ emoji sequence as weight 2', () => {
  const result = count('👨‍👩‍👧‍👦');
  assert.equal(result.weightedLength, 2);
});

test('marks more than 280 weighted characters as over', () => {
  const result = count('あ'.repeat(141));
  assert.equal(result.weightedLength, 282);
  assert.equal(result.zone, 'over');
  assert.equal(result.valid, false);
});
