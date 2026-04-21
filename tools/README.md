# Tools

このディレクトリには、研究記録の整理を補助するローカルツールを置く。

## ChatGPT Export / Markdown Viewer

[chatgpt_export_viewer.html](chatgpt_export_viewer.html) は、ChatGPTエクスポート内の `conversations.json` と、過去メモのMarkdownファイルをブラウザで読むための単一HTMLビューアである。

使い方:

1. ChatGPTのエクスポートZIPを、Gitに載らない場所へ展開する
2. `tools/chatgpt_export_viewer.html` をブラウザで開く
3. エクスポート内の `conversations.json` を選ぶ、またはドラッグする
4. Markdownメモを見る場合は「MDフォルダ」からフォルダを選ぶか、`.md` ファイルをドラッグする
5. 資料一覧、検索、ロール別表示、コピー機能を使って手動抽出する

注意:

- `conversations.json` はリポジトリへ追加しない
- 公開前レビューが済んでいない生メモは、GitHubへ追加しない
- ビューアはブラウザ内でJSON/Markdownを読むだけで、データを外部へ送信しない
- 初期状態では現在の会話パスだけを表示する。編集分岐も確認したい場合は「編集分岐も含める」を使う
