# RAGボット構築計画（GitHub `days` リポジトリを活用）

## 🎯 目的
GitHubリポジトリ `days/` 配下のMarkdown（日々の記録）をRAG（Retrieval Augmented Generation）のデータベース化。
過去の思想や知見を基に「今日のつぶやき」を自動生成し、X（Twitter）、Slack、Gmailに配信。
配信は毎日3回（9時、13時、20時）、事前にSlackで承認・修正可能。

---

## 💡 全体構成
- **データソース**：GitHub `days/`（git pullで同期）
- **前処理**：Markdown見出し単位で200〜500トークンのチャンク化＋メタデータ付与
- **ベクトルDB**：Chroma（ローカル常駐、SQLiteベース）
- **埋め込みモデル**：`intfloat/multilingual-e5-large`（日本語安定）
- **再ランク**：`bge-reranker-v2-m3`（任意、CPUでも可）
- **生成モデル**：ローカル（ollama / LM Studioの `Qwen2.5-7B/14B-Instruct`）＋失敗時APIフォールバック
- **配信先**：X（FreeティアAPI）、Slack Bot、Gmail API
- **スケジューラ**：APScheduler（JST 09:00 / 13:00 / 20:00）
- **承認UI**：Slack DMのインタラクティブメッセージ（Approve / Edit / Skip）

---

## 🔄 データフロー
1. **Git同期**：`git pull`でリポジトリ更新
2. **チャンク化**：Markdownを見出しで分割、メタデータ（day/タイトル/タグ/日付）付与
3. **インデックス**：Chromaに `(embedding, text, metadata)` 格納
4. **RAG検索**：テーマに基づき関連チャンク取得（最近日の重み＋タグ一致）
5. **下書き生成**：テンプレートに沿った「今日のつぶやき」生成（300〜600字、日本語、関西弁可）
6. **承認フロー**：Slack DMでプレビュー送信 → Approve/Edit/Skip
7. **配信**：X、Slackチャンネル、Gmail送信
8. **ログ保存**：使用チャンクと最終投稿内容を保存

---

## 🛠 技術スタック
- **ベクトルDB**：Chroma
- **埋め込み**：`multilingual-e5-large`
- **Rerank**（任意）：`bge-reranker-v2-m3`
- **生成モデル**：ollama / LM Studio（ローカルLLM）
- **APIアダプタ**：
  - X投稿：公式API（Freeティア）
  - Slack送信＆承認UI：Block Kit
  - Gmail送信：Gmail API（`messages.send`）
- **スケジューラ**：APScheduler

---

## 📂 ディレクトリ構成案
```
rag-bot/
  ingest/
    fetch_repo.py          # git pull
    split_markdown.py      # 見出しチャンク化
    build_index.py         # 埋め込み→Chroma格納
  rag/
    retriever.py           # 検索処理
    generator.py           # つぶやき生成
    prompts/daily_ja.txt   # 「今日のつぶやき」テンプレ
  adapters/
    post_x.py              # X投稿
    post_slack.py          # Slack送信・ボタンWebhook
    send_gmail.py          # Gmail送信
  serve/
    app.py                 # FastAPI（Slack interactivity webhook等）
    scheduler.py           # APScheduler（JST）
  storage/
    chroma/                # ベクトルDB
    logs/
  .env.example             # APIトークン類
```

---

## 📝 「今日のつぶやき」テンプレ例
1. **今日の問い**（短く）
2. **過去知見**（1〜2行、Day/セクション引用）
3. **今日の一歩**（読者が真似できる具体）
4. **ハッシュタグ**（2〜4個）

例：
> 環境はプロジェクトの“ミニ世界”。`pyenv+pipx+poetry` で“名づけ”と“パス”を整えると再現性が上がる。今日は `pyproject.toml` を最小で…

---

## 📅 実装ステップ
1. GitHubからローカルへの同期スクリプト作成
2. Markdownチャンク化＋メタデータ付与
3. Chromaインデックス作成
4. RAG検索＋生成処理
5. Slack承認フロー実装
6. X/Slack/Gmailへの配信アダプタ作成
7. スケジューリング設定（3回/日）
8. テスト運用（手動承認→自動投稿へ移行）

---

## 💰 コスト見積り
- **X API**：Freeティア（0円、月500投稿以内）
- **Slack Bot**：0円
- **Gmail API**：0円
- **モデル実行**：ローカルCPU/GPU（0円）
- **ホスティング**：ローカルPC or 格安VPS（500〜1000円/月）

---

## 使用PC
- デバイス名	DESKTOP G-GEAR
- プロセッサ	12th Gen Intel(R) Core(TM) i7-12700KF (3.60 GHz)
- 実装 RAM	32.0 GB
- グラフィックボード NVIDIA GeForce RTX 3070
- VRAM 8 GB

## ✅ 次に決めること（次回チャット用）
- X/Slack/GmailのAPIキー取得方法
- 承認フローのSlackチャンネル/DMの仕様
- 「今日のつぶやき」プロンプト詳細（関西弁モードの有無）
- GitHub `days/` の更新頻度と同期方法（手動 or Webhook）
