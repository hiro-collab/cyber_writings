---
name: x-post-character-count
description: >
  Create, rewrite, shorten, translate, or review posts for X/Twitter and verify each finished post with X's weighted character-count rules. Use whenever the user asks for an X post, tweet, reply, quote-post text, caption for X, or a multi-post thread. Count URLs as t.co URLs, account for Japanese/CJK text and emoji weighting, keep a safety margin below 280, and report the count after every reusable draft.
compatibility: Requires Node.js 18 or later. Run npm install once in the skill directory to install twitter-text.
metadata:
  author: hiro-collab
  version: "1.0.0"
---

# X投稿の作成・文字数確認

## 目的

X/Twitter向けの投稿文を作成・修正するとき、文章の完成度だけでなく、Xの weighted character count に基づいて投稿可能かを必ず確認する。

単純な文字数は使わない。日本語・CJK文字・絵文字・URLを含む場合も、Xの規則に沿って検算する。

## 発動条件

次の依頼では、このSkillを使用する。

- X/Twitterの投稿文、ツイート、返信、引用投稿を作る
- 既存の投稿文を修正、校正、短縮、翻訳する
- 画像や動画に添えるX向け説明文を作る
- 複数投稿のスレッドに分割する
- 「280字に入るか」「文字数を数えて」と確認される

単なる記事本文、メール、Slack、note記事など、Xへの投稿を目的としていない文章には使わない。

## 基本ルール

1. ユーザーの主張、順序、語調を先に守る。
2. 完成した投稿文ごとに、必ず `scripts/count-x-post.mjs` で検算する。
3. 文字数の目安は次の通り。
   - 0〜260: 安全域
   - 261〜270: 注意域。意味を損なわず短くできるなら短縮する
   - 271〜280: 限界域。原則として短縮版を優先して提示する
   - 281以上: 投稿不可。内容を保った短縮版を作り直す
4. 280ぎりぎりを狙わない。特段の理由がなければ260以内を目標とする。
5. URLは見た目の長さではなく、t.co短縮後の固定長として扱う。
6. 添付画像・動画・GIF自体は文字数に含めない。
7. 返信冒頭にXが自動挿入するメンションなど、投稿欄の実際の状態で差が出る場合は、その不確実性を明記する。
8. スレッドは各投稿を独立して検算する。`1/3`などの番号を本文に含める場合、その番号も含めて数える。
9. 複数案を出す場合は、すべての案を個別に検算する。
10. 投稿文の後に、必ず次の形式で結果を添える。

```text
概算：234 / 280（残り46）
```

261以上の場合は、次のように注意も添える。

```text
概算：274 / 280（残り6・限界域）
```

## 検算手順

### 初回のみ

Skillディレクトリで依存関係を導入する。

```bash
npm install
```

### 投稿文を標準入力から検算

```bash
printf '%s' "$POST_TEXT" | node scripts/count-x-post.mjs --json
```

改行を含む文章は、一時ファイルに保存して検算してもよい。

```bash
node scripts/count-x-post.mjs --file /path/to/post.txt --json
```

短い文章は直接渡せる。

```bash
node scripts/count-x-post.mjs --text '投稿文' --json
```

### 結果の読み方

- `weightedLength`: X換算文字数
- `remaining`: 280までの残り
- `valid`: Xの文字数規則上、投稿可能か
- `zone`: `safe` / `caution` / `tight` / `over`
- `urlCount`: 検出されたURL数

## 作成ワークフロー

1. ユーザーの原文から、投稿の中心となる主張を特定する。
2. 説明を足しすぎず、Xで一読して流れが追える文章に整える。
3. URL、ハッシュタグ、メンションが必要か確認する。
4. 完成案を検算する。
5. 261以上なら、語調と意味を保ったまま短縮を試み、再検算する。
6. 投稿文を再利用可能な完成稿として提示する。
7. 各案の直後に検算結果を添える。
8. 自動メンション、投稿欄固有の挙動などで差が出そうな場合だけ、投稿欄での最終確認を促す。

## 出力例

```text
過去にTouchDesignerで作ったエフェクトの処理をCodexに読み取らせ、別のプロジェクトでも同じ技を使えるように試しています。

ノードグラフもGLSLへコード化すれば、Three.jsなど他のシステム向けに組み替えやすくなりそうです。

概算：XXX / 280（残りXXX）
```

`XXX`を推測で埋めてはならない。必ずスクリプトの出力を使う。

## 注意点

- JavaScriptの `string.length`、Pythonの `len()`、目視による単純計数を最終判定に使わない。
- URLを元の長さで数えない。
- 絵文字のコードポイント数をそのまま足さない。ZWJで結合された絵文字もXの規則で扱う。
- 「日本語はすべて2、英数字はすべて1」という簡略計算だけで最終値を断定しない。
- ライブラリを実行できなかった場合は、概算であることを明示し、Xの投稿欄で最終確認するよう伝える。

## 参照

Xの文字数規則と採用した判定方針は、`references/counting-rules.md`を参照する。
