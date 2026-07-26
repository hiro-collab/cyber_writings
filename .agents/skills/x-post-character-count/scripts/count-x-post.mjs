#!/usr/bin/env node

import fs from 'node:fs/promises';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const twitter = require('twitter-text');

const MAX_WEIGHTED_LENGTH = 280;

function printUsage() {
  console.error(`Usage:
  node scripts/count-x-post.mjs --text "post text" [--json]
  node scripts/count-x-post.mjs --file path/to/post.txt [--json]
  printf '%s' "post text" | node scripts/count-x-post.mjs [--json]
`);
}

function parseArgs(argv) {
  const args = { text: null, file: null, json: false };

  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];

    if (arg === '--json') {
      args.json = true;
      continue;
    }

    if (arg === '--text') {
      if (index + 1 >= argv.length) {
        throw new Error('--text requires a value.');
      }
      args.text = argv[index + 1];
      index += 1;
      continue;
    }

    if (arg === '--file') {
      if (index + 1 >= argv.length) {
        throw new Error('--file requires a path.');
      }
      args.file = argv[index + 1];
      index += 1;
      continue;
    }

    if (arg === '--help' || arg === '-h') {
      printUsage();
      process.exit(0);
    }

    throw new Error(`Unknown argument: ${arg}`);
  }

  if (args.text !== null && args.file !== null) {
    throw new Error('Use only one of --text or --file.');
  }

  return args;
}

async function readStdin() {
  const chunks = [];
  for await (const chunk of process.stdin) {
    chunks.push(chunk);
  }
  return Buffer.concat(chunks).toString('utf8');
}

async function loadText(args) {
  if (args.text !== null) {
    return args.text;
  }

  if (args.file !== null) {
    return fs.readFile(args.file, 'utf8');
  }

  if (!process.stdin.isTTY) {
    return readStdin();
  }

  throw new Error('No text supplied. Use --text, --file, or stdin.');
}

function classifyZone(weightedLength) {
  if (weightedLength <= 260) return 'safe';
  if (weightedLength <= 270) return 'caution';
  if (weightedLength <= 280) return 'tight';
  return 'over';
}

function extractUrls(text) {
  if (typeof twitter.extractUrlsWithIndices === 'function') {
    return twitter.extractUrlsWithIndices(text).map((item) => item.url);
  }
  if (typeof twitter.extractUrls === 'function') {
    return twitter.extractUrls(text);
  }
  return [];
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const rawText = await loadText(args);
  const text = rawText.replace(/\r\n/g, '\n').normalize('NFC');
  const parsed = twitter.parseTweet(text);
  const weightedLength = parsed.weightedLength;
  const remaining = MAX_WEIGHTED_LENGTH - weightedLength;
  const urls = extractUrls(text);

  const result = {
    weightedLength,
    maxWeightedLength: MAX_WEIGHTED_LENGTH,
    remaining,
    valid: parsed.valid,
    zone: classifyZone(weightedLength),
    urlCount: urls.length,
    urls,
    normalized: text !== rawText,
  };

  if (args.json) {
    console.log(JSON.stringify(result, null, 2));
    return;
  }

  const zoneLabels = {
    safe: '安全域',
    caution: '注意域',
    tight: '限界域',
    over: '超過',
  };

  console.log(`概算：${weightedLength} / ${MAX_WEIGHTED_LENGTH}（残り${remaining}・${zoneLabels[result.zone]}）`);
  if (!parsed.valid) {
    process.exitCode = 2;
  }
}

main().catch((error) => {
  console.error(`Error: ${error.message}`);
  printUsage();
  process.exit(1);
});
