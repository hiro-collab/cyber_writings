# cyber_writings

このリポジトリは、過去の思索・症状記録・サイバーに関する考察を、
断片から再構成し、最終的に論考・書籍レベルの原稿へ整理するための作業場である。

## 目的
- 自身に起きた症状の進行を、後から検証できる形で記録する
- 症状と向き合う中で調べた脳機能・認知・サイバーに関する考察を整理する
- 個人的記録を、読めるエッセイ・論考・書籍原稿へ育てる
- 公開や収益化を見据えつつ、公開してよい情報と残すだけの情報を分ける

## ディレクトリ構成
- `00_fragments`: ChatGPT履歴やメモから切り出した断片
- `01_curated`: 断片を整理し、意味や論点ごとにまとめた文書
- `02_manuscript`: 公開・構成済みの原稿
- `docs`: 編集方針、運用ルール、公開戦略
- `tools`: ChatGPT履歴の閲覧など、整理作業を補助するローカルツール
- `.codex`: Codex運用用情報

## 基本ワークフロー
1. ChatGPTエクスポートなどの生データは、Gitに載せない場所へ置く
2. 重要な発言・症状記録・思考の変化を `00_fragments` に抜き出す
3. 重複や時系列を整理して `01_curated` に主題別のノートを作る
4. 読者に伝える順番へ組み替え、`02_manuscript` で原稿化する
5. 公開前に、個人情報・医療情報・推測と事実の混同を確認する

## 編集方針
- 元文の意味を勝手に変えない
- 推定を事実として補わない
- 重複は整理するが、重要な揺れは消しすぎない
- 症状・診断・医学的説明は、事実、記憶、推測、仮説を分けて書く
- 公開版では、他者の個人情報や自分の機微情報を必要以上に出さない

## 最初に読むもの
- [docs/workflow.md](docs/workflow.md): 取り込みから原稿化までの流れ
- [docs/editorial_policy.md](docs/editorial_policy.md): 記録とエッセイの編集方針
- [docs/publishing_strategy.md](docs/publishing_strategy.md): GitHub公開と収益化の考え方
- [02_manuscript/outline.md](02_manuscript/outline.md): 仮の章立て
- [tools/chatgpt_export_viewer.html](tools/chatgpt_export_viewer.html): ChatGPTエクスポート閲覧用ビューア
