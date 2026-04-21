# Tools

このディレクトリには、研究記録の整理を補助するローカルツールを置く。

## ChatGPT Export Viewer

[chatgpt_export_viewer.html](chatgpt_export_viewer.html) は、ChatGPTエクスポート内の `conversations.json` をブラウザで読むための単一HTMLビューアである。

使い方:

1. ChatGPTのエクスポートZIPを、Gitに載らない場所へ展開する
2. `tools/chatgpt_export_viewer.html` をブラウザで開く
3. エクスポート内の `conversations.json` を選ぶ、またはドラッグする
4. 会話一覧、検索、ロール別表示、コピー機能を使って手動抽出する

注意:

- `conversations.json` はリポジトリへ追加しない
- ビューアはブラウザ内でJSONを読むだけで、データを外部へ送信しない
- 初期状態では現在の会話パスだけを表示する。編集分岐も確認したい場合は「編集分岐も含める」を使う
