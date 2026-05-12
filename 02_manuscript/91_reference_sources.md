# 参考ソースと主張対応表

このファイルは、本文で使った外部ソースと、どの主張に対応しているかを追うためのメモである。本文に入れると重くなる確認事項、リンク、確度もここに残す。

## 使い方

- 本文で断定する前に、このファイルで根拠の種類を確認する。
- 一次資料、出版社・大学・公的機関のページを優先する。
- ChatGPT 由来の説明は、外部ソースまたはユーザー自身の過去文書で裏取りできるまで本文の根拠にしない。
- 個人経験は、外部ソースではなく「筆者の経験」として明示する。

## 情報技術用語と外来語の分かりにくさ

本文での使い方:

- 第1部 1.5 で、情報技術分野の訳語・外来語を見直す必要が、筆者個人の違和感だけではないことを示す。
- 既存訳の全面否定ではなく、相手、場面、文脈に応じて言い換えや説明を補う方針の根拠として使う。
- `computer`、`command`、`function` などの個別訳語は、この大きな問題の一例として扱う。

主張:

- 国立国語研究所の「外来語」言い換え提案は、公共性の高い場面で、一般への定着が不十分な外来語を分かりやすくするため、言い換えや説明を付ける工夫を提案した。
- 同提案は、外来語を一律に排除するのではなく、理解度、世代差、場面、文脈、専門性に応じて、言い換え語、意味説明、外来語＋説明を使い分ける方針を取っている。
- 国立国語研究所の解説では、分かりにくい専門用語を分かりやすくするには、当該分野の専門家による言い換えや説明の努力が欠かせないと整理されている。
- 佐藤衣央「コンピュータ用語における外来語の考察」は、国立国語研究所の意識調査を引き、外来語に分かりにくい分野があると感じる人が九割を超え、分かりにくい分野として「コンピュータ関連」が上位に挙がったことを確認している。
- 同論文は、コンピュータ分野では外来語の流入を避けにくいため、外来語を排除するよりも、日本語とどう共生させるかが課題になると整理している。
- 野崎浩成ほかの高校「情報」教科書調査では、23冊、3,127ページの教科書索引から IT 用語を抽出し、索引語の四分の一がカタカナ語で、多くの教科書に共通する高頻度 IT 用語ではカタカナ語が約半数を占めることが示されている。
- カタカナ外来語の表記揺れは、形態素解析、意味解析、対訳付けなどの計算機処理でも問題になるとする情報処理学会発表もある。これは本文の主題ではないが、情報技術と日本語表記の問題が古くから実務・研究上の課題だったことを示す補助材料になる。

ソース:

- [国立国語研究所「外来語」言い換え提案 第1回-第4回 総集編](https://www2.ninjal.ac.jp/gairaigo/Teian1_4/index.html)
- [国立国語研究所「外来語」言い換え提案 利用の手引き](https://www2.ninjal.ac.jp/gairaigo/Teian1_4/tebiki.html)
- [国立国語研究所「外来語」委員会設立趣意書](https://www2.ninjal.ac.jp/gairaigo/syuisyo.html)
- [田中牧郎「分かりやすい言葉遣いの提案」国語研の窓](https://kotobaken.jp/mado/33/33-02/)
- [田中牧郎「外来語を使う際にはどのようなことに気を付ければいいですか」ことば研究館](https://kotobaken.jp/qa/yokuaru/qa-104/)
- [佐藤衣央「コンピュータ用語における外来語の考察」日本女子大学リポジトリ](https://jwu.repo.nii.ac.jp/records/2997)
- [佐藤衣央「コンピュータ用語における外来語の考察」PDF](https://files01.core.ac.uk/download/pdf/235236448.pdf)
- [Nozaki et al., “Study of IT Terms Used in Non-Vocational High School Information Technology Class Textbooks” CiNii Research](https://cir.nii.ac.jp/crid/1050845763366693376)
- [愛知教育大学リポジトリ同論文ページ](http://hdl.handle.net/10424/2778)
- [同論文PDF](https://aue.repo.nii.ac.jp/record/2019/files/jissenkiyo135966.pdf)
- [情報処理学会「カタカナ外来語の表記の揺れの解消」CiNii Research](https://cir.nii.ac.jp/crid/1050855522106141952)

確度:

- 高: 外来語・専門用語の分かりにくさに対し、言い換えや説明を付ける公的・研究的な先行議論があること。
- 高: コンピュータ関連の外来語が、分かりにくい分野として調査・研究対象になってきたこと。
- 高: 高校「情報」の教科書索引で、IT 用語のかなりの割合をカタカナ語が占めること。
- 中: これらの先行議論を、本書の `command`、`function`、`computer`、`cyber` の再翻訳方針に接続すること。これは本文側の応用なので、外来語排除論に見えないよう注意する。
- 低: すべての情報技術用語を和語・漢語へ置換すべきだという主張。本文では採用しない。

## 現代の再翻訳環境

本文での使い方:

- 第1部 1.6 で、AI・検索・SNS によって「訳語を試し、検証し、直す」条件が以前より整ったことを述べる。
- AI を正しさの根拠とはせず、語源、用例、先行研究、反論候補へ到達するための探索補助として扱う。
- SNS やブログを正しさの保証とはせず、批判や違和感が可視化される入口として扱う。

主張:

- AI の出力自体は根拠にならない。本文の根拠は、辞書、原典、論文、規格、教材、実際の用例で確認する。
- ただし AI や検索環境により、細かなニュアンスを問い直し、検索語を変え、候補文献を探し、反論可能性を洗い出す手間は下がっている。
- SNS やブログは、訳語への違和感や批判を可視化しやすくする。ただし、訂正が常に速く正確に行われるとは断定しない。
- 現代の再翻訳は、一度決めた訳語を固定するよりも、公開し、批判を受け、参照元を確認しながら改訂する作業として捉える。

ローカル文書:

- `00_fragments/md_files/single_threads/2026-05-04T07-14-54_プログラミング_-_サイバーと操る.md`: AI・検索・SNS によって訳語の検証や修正がしやすくなった、という筆者の発話。

確度:

- 高: AI 出力を根拠にせず、一次資料・辞書・論文・規格・教材・用例で確認すべきこと。
- 中: AI・検索環境によって、語源、用例、先行研究、反論候補へ到達する手間が下がったこと。本文では筆者の実践経験に基づく方針として扱う。
- 中: SNS やブログが、訳語への違和感や批判を可視化する入口になること。
- 低: SNS 上の批判によって、訳語が必ず速く正しく修正されるという主張。本文では採用しない。

## 筆者経験と産業背景の扱い

本文での使い方:

- `00_overview` と第7部 7.6 で、日本の家電・スマートデバイス分野へのもどかしさ、ウェアラブル開発、輸入業・翻訳業での経験を、再翻訳へ取り組む動機として扱う。
- 産業全体の失敗原因を訳語へ単純化せず、価格、プラットフォーム、生態系、販売網、組織、国際競争などの複合要因を認めた上で書く。
- 「理解力の差を感じた」という記述は、筆者の経験として扱い、客観的な産業分析や実証データとしては扱わない。

主張:

- 筆者は、ウェアラブルデバイス開発で、ハードウェアの性能だけでは価値が伝わらない場面を経験した。
- 輸入業や翻訳業で欧米スタートアップ企業のソフトウェア解説に触れ、日本語で顧客へ説明するときに、英文では自然だった機能・行動・生活場面のつながりが遠くなると感じた。
- この経験から、スマートデバイスやソフトウェアを「何を叶えるためのものか」として日本語で語る言葉が不足している、という問題意識が生まれた。

ローカル文書:

- `00_fragments/md_files/single_threads/2026-05-04T07-14-54_プログラミング_-_サイバーと操る.md`: スマート分野、日本語でコンピューティングを捉え直す必要、欧米ソフトウェア解説と日本語訳の違和感に関する議論。
- `02_manuscript/92_related_document_check.md`: 個人経験、ウェアラブル開発、輸入・翻訳業、AI サイネージなどを、公開本文へ直接入れる場合は公開範囲の判断が必要とするメモ。

確度:

- 高: これらが筆者自身の動機・経験として本文に置けること。
- 中: 「価値を生活感覚に接続して語る力が足りなかったのではないか」という仮説。
- 低: 日本の家電・スマートデバイス分野の停滞原因を、訳語や説明文書の問題だけで説明する主張。本文では採用しない。

## 西周と百学連環

本文での使い方:

- 第1部 1.7 で、外来概念を日本語の体系の中へ置き直す先例として参照。
- 「西周と同じことをしている」とは言わず、「参照できる前例」として扱う。

主張:

- 西周『百学連環』には、西自身が欧語に対して和訳などの説明を施した語彙がある。
- 『百学連環』は、西洋の諸学を相互の連関の中で捉えようとした試みとして読める。
- 「連環」は、学と術を切り離さず、関係の中で理解する補助線になる。

ソース:

- [人間文化研究機構 nihuBridge「西周『百学連環』」](https://bridge.nihu.jp/database_explain07/nihu/nihu_naep)
- [山本貴光「第125回 連環というイメージ」三省堂 ことばのコラム](https://dictionary.sanseido-publ.co.jp/column/100gaku125)
- [三省堂『「百学連環」を読む』書籍ページ](https://dictionary.sanseido-publ.co.jp/dict/ssd36522)
- [CiNii Books『「百学連環」を読む』](https://ci.nii.ac.jp/ncid/BB2190077X)

確度:

- 高: 『百学連環』を西周の外来学術受容・訳語形成の先例として参照すること。
- 中: 本書の `digital` / `cyber` / `AI` の整理と「連環」を重ねて論じること。これは本文側の解釈なので、断定しすぎない。

## cyberneticsと対空砲予測装置

本文での使い方:

- 第2部 2.2 で、`cybernetics` の成立背景に通信、制御、フィードバック、舵取りが重なっていたことを説明する。
- ユーザー記憶の「ミサイルか何か」は、そのまま使わず、調査上は「対空砲予測装置」として扱う。

主張:

- Wiener の *Cybernetics* は、1948年に初版が出た、制御と通信を扱う古典である。
- `cybernetics` は、船の舵取りに関わる語から作られた。
- Wiener と Bigelow の戦時研究には、敵航空機の動きから未来位置を予測する対空砲予測装置が関係していた。
- その経験は、負のフィードバックや、現在状態と望ましい状態との差を縮めるシステムという見方につながったと説明される。

ソース:

- [MIT Press: *Cybernetics or Control and Communication in the Animal and the Machine*](https://mitpress.mit.edu/9780262537841/cybernetics-or-control-and-communication-in-the-animal-and-the-machine/)
- [MIT Press Direct Open Access edition](https://direct.mit.edu/books/oa-monograph/4581/Cybernetics-or-Control-and-Communication-in-the)
- [MIT Libraries “Year 88 - 1948: Cybernetics...”](https://libraries.mit.edu/150books/2011/04/04/1948/)
- [Cambridge Core: Rosenblueth, Wiener, Bigelow “Behavior, Purpose and Teleology”](https://www.cambridge.org/core/journals/philosophy-of-science/article/abs/behavior-purpose-and-teleology/73ACBBEC616CE78767088694F357D57B)
- [SFI Press “The Birth of Cybernetics”](https://www.sfipress.org/06-rosenblueth-wiener-bigelow-1943)
- [MIT Press: *Extrapolation, Interpolation, and Smoothing of Stationary Time Series*](https://mitpress.mit.edu/9780262730051/extrapolation-interpolation-and-smoothing-of-stationary-time-series/)

確度:

- 高: Wiener の本のタイトル、1948年初版、control and communication の基本説明。
- 高: 舵取り・steersman 由来を参照すること。
- 中: 対空砲予測装置から本書の「操る」概念へ橋をかけること。これは本文側の解釈なので、軍事技術そのものへ寄せすぎない。

## GUI・空間表示・AIエージェントの思想的前史

本文での使い方:

- 第5部 5.1 で、GUI、プロジェクション、空間 AR、AI エージェントが唐突な応用例ではなく、コンピューターを人間の知的活動、身体、場、生活環境へ開こうとしてきた思想の延長にあることを示す。
- ただし、これらの英語圏の先行思想が、そのまま本書の「場」「作法」「鎮める」「陰陽師」的な語りを含んでいたとは言わない。
- 日本語で訳し直したときに見える像は、本文側の解釈として扱う。

主張:

- Engelbart の 1962年報告は、コンピューターを単なる計算装置ではなく、人間の複雑な問題解決能力を増幅する道具、言語、方法、訓練の体系として扱った。
- Kay の Dynabook 論は、個人用コンピューターを、子どもや大人が持ち歩き、情報を作り、試し、操作する能動的な媒体として構想した。
- Sutherland の “The Ultimate Display” は、ディスプレイを、物理世界では直接経験しにくい概念や仮想的な対象を体験可能にする窓・部屋として構想した。
- Weiser の ubiquitous computing は、コンピューターを机上の一台へ閉じず、環境へ分散し、日常の中に溶け込ませる方向を示した。
- Maes の interface agents 論は、情報過多や作業負荷を減らすため、ユーザーの代わりに学び、助け、働くソフトウェアエージェントを扱った。

ソース:

- [Douglas C. Engelbart “Augmenting Human Intellect: A Conceptual Framework”](https://www.dougengelbart.org/content/view/138/)
- [Alan C. Kay “A Personal Computer for Children of All Ages”](https://mprove.de/visionreality/media/kay72.html)
- [Ivan E. Sutherland “The Ultimate Display” CiNii Research](https://cir.nii.ac.jp/crid/1571980075024255872)
- [Mark Weiser “The Computer for the 21st Century” Scientific American](https://www.scientificamerican.com/article/the-computer-for-the-21st-century/)
- [Pattie Maes “Agents that Reduce Work and Information Overload” Communications of the ACM](https://cacm.acm.org/research/agents-that-reduce-work-and-information-overload/)

確度:

- 高: Engelbart、Kay、Sutherland、Weiser、Maes を、GUI、個人用コンピューティング、空間表示、環境化、エージェントの歴史的補助線として参照すること。
- 中: これらを第5部の「サイバーが人間の前にどう現れるか」という問いへ接続すること。これは本文側の構成判断である。
- 低: これらの先行思想が、本書の日本語的な「場」「作法」「鎮める」「陰陽師」的イメージを直接意図していたという主張。本文では採用しない。

## Turingと機械知性

本文での使い方:

- 第6部 6.2 で、AI を人格として断定する前に、機械の振る舞い・役割・模倣ゲームを参照する。
- 「機械に意思が宿る」と断定せず、社会の中で人の代わりに演算し、応答し、働く役割として扱う。

主張:

- Alan Turing の “Computing Machinery and Intelligence” は1950年に *Mind* に掲載された。
- 論文は “Can machines think?” から入り、模倣ゲームへ問いを置き換える。
- 同論文には “Digital Computers” と “Universality of Digital Computers” の節がある。
- 本文で「代理演算役」を論じるときは、Turing を「内面の証明」ではなく、「振る舞いと役割を見る」補助線として参照する。

ソース:

- [Oxford Academic: A. M. Turing “Computing Machinery and Intelligence”](https://academic.oup.com/mind/article/LIX/236/433/986238)
- [Turing Digital Archive: AMT/B/9](https://turingarchive.kings.cam.ac.uk/publications-lectures-and-talks-amtb/amt-b-9)
- [Cambridge ArchiveSearch: “Computing machinery and intelligence”, 1950](https://archivesearch.lib.cam.ac.uk/repositories/7/archival_objects/272461)
- [CiNii Research: “I.-COMPUTING MACHINERY AND INTELLIGENCE”](https://cir.nii.ac.jp/crid/1362825895532834176)

確度:

- 高: 論文の掲載情報、節構成、模倣ゲームの位置づけ。
- 高: Turing 1950年論文が、デジタルコンピューターを human computer が行う操作を実行する機械として説明していること。
- 中: `computer` を「演算役」「代理演算役」と読むこと。これは本文側の説明語であり、一般訳を置き換える確定訳ではない。
- 要確認: 既存邦訳の有無と品質。必要なら自訳候補を別ファイルで作る。

## computerの訳語とhuman-computer

本文での使い方:

- 第6部 6.3 で、`computer` を「電子計算機」とだけ訳すと落ちる歴史的な幅を、必要な翻訳の重要例として確認する。
- AI エージェントを「代理演算役」と呼ぶ根拠を補強する。
- ただし、本書全体を `computer` 訳語論にはしない。
- あわせて、「コンピューター」「電子計算機」「計算機」を誤訳とは言わない。

主張:

- `computer` は現在では通常、プログラム可能な電子装置を指すが、語義としては「計算するもの」を含む。
- 電子コンピューター以前、`computer` は手計算を行う職務名として使われた。
- Turing 1936年論文は、人が実数を計算する過程を機械になぞらえるところから計算機械を説明している。
- Turing 1950年論文は、デジタルコンピューターを human computer が行える操作を実行する機械として説明している。
- 日本語では「コンピューター」「コンピュータ」の表記揺れがあり、一般向けには「コンピューター」が穏当とする国語研の説明がある。
- 「電脳」は「電子頭脳」の略、または中国語の computer 相当語として参照できるが、AI を人格化・脳化しすぎるため本文の主語にはしない。
- JIS X 0001:1994 の用語定義では、`computer` は「計算機、コンピュータ」と対応づけられ、算術演算・論理演算を含む計算を人手の介入なしに行う機能単位として説明される。

ソース:

- [Merriam-Webster: “computer”](https://www.merriam-webster.com/dictionary/computer)
- [Merriam-Webster: “compute”](https://www.merriam-webster.com/dictionary/compute)
- [NASA: “When Computers Were Human”](https://www.nasa.gov/centers-and-facilities/jpl/when-computers-were-human/)
- [NASA: “‘Computer’ Conducts Data Analysis”](https://www.nasa.gov/image-article/computer-conducts-data-analysis/)
- [A. M. Turing, “On Computable Numbers, with an Application to the Entscheidungsproblem” PDF](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf)
- [Oxford Academic: A. M. Turing “Computing Machinery and Intelligence”](https://academic.oup.com/mind/article/LIX/236/433/986238)
- [国立国語研究所 ことば研究館「コンピューター」と「コンピュータ」どちらで書いてもよいのでしょうか](https://kotobaken.jp/qa/yokuaru/qa-94/)
- [コトバンク「電脳」](https://kotobank.jp/word/%E9%9B%BB%E8%84%B3-6553)
- [JIS X 0001:1994 情報処理用語（基本用語）掲載ページ](https://www.ny.ics.keio.ac.jp/ipsjts1/2nd-ver/htm/x0001.htm)

ローカル文書:

- `00_fragments/md_files/programming_translation_jp.md`: `computer` の原義と、`演算体` などを仮案に留める方針。
- `00_fragments/md_files/046ma.md`: `compute` を「勘定する」に近い語として見るメモ、計算機の基本動作メモ。
- `00_fragments/md_files/single_threads/2026-05-04T07-16-21_プログラミング_-_陰陽とサイバネティクス.md`: `computer` を「演算者」「補助者」と見る会話ログ。

確度:

- 高: `computer` が「計算するもの/人」を含む語であり、human computer の歴史的用例があること。
- 高: Turing 1936/1950年論文に、人間の計算者と機械の対応を読むこと。
- 高: 日本語では「コンピューター」「コンピュータ」「電子計算機」「計算機」が文脈に応じて使われていること。
- 中: 「代理演算役」を本文の説明語として採用すること。これは AI エージェント論のための解釈であり、一般訳ではない。
- 中: `computer` を本書の主題ではなく、翻訳によって技術の見え方が変わる重要例として扱うこと。
- 低: `computer` の標準訳を全面的に「演算役」へ置き換える主張。本文では採用しない。

## serverとagentの語感

本文での使い方:

- 第6部 6.4 で、`server` と `agent` を、AI エージェント論を支える補助語として扱う。
- `server` は「サーバー機」という装置名だけでなく、求めに応じてサービスを提供する役割を含む語として見る。
- `agent` は、単なる人格キャラクターではなく、作用するもの、代理するもの、権限を受けて働くものとして見る。
- ただし、本書の中心は `server` / `agent` の訳語論ではなく、願いを受け、演算し、場や現実へ橋渡しする役割の整理である。

主張:

- Merriam-Webster では、`server` は食事を提供する人、サービスを提供するネットワーク上のコンピューターなどを含む語として説明される。
- Etymonline では、`server` は `serve` から派生した、仕える者を意味する語として説明される。
- Merriam-Webster では、`agent` は作用するもの、効果を生むもの、他者のために、または他者の代わりに行為するもの、特定のタスクを自動化するコンピューターアプリケーションなどを含む語として説明される。
- Etymonline では、`agent` は「行う、動かす」に関わるラテン語系の語として説明され、代理者・代表者の意味も確認できる。

ソース:

- [Merriam-Webster: “server”](https://www.merriam-webster.com/dictionary/server)
- [Etymonline: “server”](https://www.etymonline.com/word/server)
- [Merriam-Webster: “agent”](https://www.merriam-webster.com/dictionary/agent)
- [Etymonline: “agent”](https://www.etymonline.com/word/agent)

確度:

- 高: `server` に「提供する、仕える」役割の語感があり、計算機分野でもサービス提供側を指すこと。
- 高: `agent` に、作用するもの、代理するもの、自動化されたソフトウェアの意味があること。
- 中: `server` を「奉仕者」、`agent` を「使い」「代理者」と説明すること。これは文脈によって有効だが、標準訳として固定しない。
- 低: `server` / `agent` の語源だけで AI エージェントの技術的性質を説明しきる主張。本文では採用しない。

## Leibniz二進法易経

本文での使い方:

- 第4部 4.4 で、陰陽を「属性を落とした二状態」として扱うための歴史的補助線として参照する。
- 「易経がデジタル技術の起源である」「Leibniz が易経を見て二進法を発明した」とは書かない。
- `0/1` と `陰/陽` の対応は、二状態の記号的対応に限定する。

主張:

- Leibniz は 1703年の論文で、`0` と `1` だけを使う二進法を説明し、伏羲の古代中国図像との関係にも触れている。
- 同論文では、実線を `1`、破線を `0` と見て、八卦・六十四卦を二進法的に読めると説明している。
- ただし Leibniz の二進法研究は、Bouvet との易経・伏羲図像をめぐるやり取りより前に確認できる。1679年の `De Progressione Dyadica` が重要な早期資料である。
- Bouvet は、Leibniz の二進法と伏羲・邵雍系の六十四卦図との類似に気づき、Leibniz に図を送った。
- 現代研究では、この関係を「形式的対応」と見る立場と、特定の伏羲六十四卦方位図を二値的構造として評価する立場がある。いずれにせよ、本文では「構造的対応」に留める。

ソース:

- [Wikisource: Leibniz, “Explication de l'arithmétique binaire...”](https://fr.wikisource.org/wiki/Leibniz-en.francais-Gerhardt.Math.1a7.djvu/Num%C3%A9ration.binaire)
- [Gallica: Académie royale des sciences, 1703](https://gallica.bnf.fr/ark:/12148/bpt6k3483p/f247.item)
- [PHILIUMM: `De Progressione Dyadica` overview](https://eman-archives.org/philiumm/dyadica/de-progressione-dyadica)
- [PhilArchive: Lloyd Strickland “Leibniz on Number Systems”](https://philarchive.org/rec/STRLON)
- [MIT Press: *Leibniz on Binary*](https://mitpress.mit.edu/9780262544344/leibniz-on-binary/)
- [Cambridge Core: Marie-Julie Maitre, “Is the Fuxi liushisi gua fangwei diagram attributed to Shao Yong binary?”](https://www.cambridge.org/core/journals/science-in-context/article/abs/is-the-fuxi-liushisi-gua-fangwei-diagram-attributed-to-shao-yong-binary-clarifying-a-consequence-of-its-analogy-with-the-binary-arithmetic-of-leibniz/9BA1DB9CFF13D5BEADCAF8FF954108AC)
- [PhilPapers: Aiton and Shimao, “Gorai Kinzō's study of Leibniz and the I ching hexagrams”](https://philpapers.org/rec/AITGKS)
- [Chinese Text Project: 周易 / Book of Changes](https://ctext.org/book-of-changes/zh)

確度:

- 高: Leibniz の 1703年論文が二進法と伏羲図像を結びつけていること。
- 高: Leibniz の二進法研究が Bouvet 経由の伏羲図像以前に確認できること。
- 中: 伏羲・邵雍系の六十四卦図を「binary」と呼べる範囲。研究上の議論があるため、「構造的対応」「形式的対応」として扱う。
- 低: 易経を現代デジタル技術、制御理論、AI の原型とする主張。本文では採用しない。

## 日本語の気と制御像

本文での使い方:

- 第4部 4.8 で、陰陽や符よりも日常語に近い制御感覚として、「気を遣う」「気を配る」「気を回す」「気が合う」「気配を読む」を扱う。
- `care` と「気」を一対一対応させるのではなく、注意、配慮、監督、責任、心配、場の状態への感受性が、日本語では「気」の言い回しとして広く現れることを補助線にする。
- 「気」を物理的な実体や工学的な変数として定義しない。あくまで、日本語でインターフェースや制御を語るときの比喩的・感覚的な資源として扱う。

主張:

- Merriam-Webster の `care` には、注意、心配、監督、責任、保護・安全への配慮などの語義がある。
- 「気遣い」は、気を使うこと、心づかい、また懸念を含む語として辞書で説明される。
- 「気を配る」は、さまざまに注意を払う、配慮することを意味する。
- 「気を回す」は、必要以上にあれこれ考える、余計な憶測や邪推をする意味を含む。本文では、先回りする注意が行き過ぎるリスクも含めて扱う。
- 「気が合う」は、考え方や感じ方が通じ合うこと、気持ちが通じ合い気分が一致することを意味する。
- 「気配」は、はっきり見えないが漠然と感じられる様子、また市場や相場の状態を指す語として説明される。

ソース:

- [Merriam-Webster: “care”](https://www.merriam-webster.com/dictionary/care)
- [コトバンク「気遣い」](https://kotobank.jp/word/%E6%B0%97%E9%81%A3%E3%81%84-474646)
- [コトバンク「気を配る」](https://kotobank.jp/word/%E6%B0%97%E3%82%92%E9%85%8D%E3%82%8B-471906)
- [コトバンク「気を回す」](https://kotobank.jp/word/%E6%B0%97%E3%82%92%E5%9B%9E%E3%81%99-471919)
- [コトバンク「気が合う」](https://kotobank.jp/word/%E6%B0%97%E3%81%8C%E5%90%88%E3%81%86-471837)
- [コトバンク「気配」](https://kotobank.jp/word/%E6%B0%97%E9%85%8D-475319)

確度:

- 高: 各慣用句の辞書上の意味。
- 中: 「気」を、注意、配慮、相性、場の状態をめぐる日本語の制御感覚として読むこと。これは本文側の解釈である。
- 低: 「気」を、物理的・工学的な量や変数として直接扱う主張。本文では採用しない。

## ジェスチャー設計と刀印

本文での使い方:

- 第5部 5.6 で、刀印を和風演出ではなく、入力ゲート、誤作動回避、記憶しやすさ、身体負荷の観点から説明する。

主張:

- hand tracking の設計では、使いやすさ、快適性、信頼性、フィードバックが重要である。
- 抽象的な手のポーズは学習が必要なので、使いすぎない方がよい。
- ポーズを使う場合は、少数にし、目的を一貫させ、意図しない起動を避けるために区別しやすくする必要がある。

ソース:

- [Ultraleap XR Guidelines: Design principles](https://docs.ultraleap.com/xr-guidelines/Getting%20started/design-principles.html)
- [Ultraleap XR Guidelines: Design considerations](https://docs.ultraleap.com/xr-guidelines/Getting%20started/DesignConsiderations.html)
- [Ultraleap: Hand poses](https://docs.ultraleap.com/xr-guidelines/Interactions/hand_poses.html)
- [Ultraleap: 6 VR Design Principles for Hand Tracking](https://docs.ultraleap.com/ultralab/hand-tracking-vr-design.html)

確度:

- 高: ポーズを少数にする、明確なフィードバックを与える、負担の大きい動きを避ける、という設計原則。
- 中: 刀印がこれらの原則に合うという評価。これは `sword-voice-agent` 側の実験結果と合わせて検証する。

## commandとfunctionの入門説明

本文での使い方:

- 第1部 1.3 で、「命令をまとめると関数になる」の違和感を説明するための根拠候補。

主張:

- 入門教材では、function を「名前をつけて繰り返し使える commands のまとまり」と説明する例がある。
- この説明は英語では自然だが、日本語で「命令」と「関数」を並べると距離が出やすい。

ソース候補:

- [Code.org CS Discoveries: Functions](https://studio.code.org/docs/csd/functions/index.html)
- [Google CS First Help: About CS First](https://support.google.com/csfirst/answer/7476916?hl=en)
- [Google CS First Help 日本語: CS First について](https://support.google.com/csfirst/answer/7476916?hl=ja)

確度:

- 中: Code.org にはかなり直接的な説明がある。
- 要確認: Google の具体教材内で `commands` と `function` がどう説明されているか。本文の `[要確認]` は残す。

## commandとサイバー空間の統治

本文での使い方:

- 第1部 1.2 で、`command` を「お願い」とだけ説明しても、「命令」とだけ説明しても足りない理由を示す。
- 第2部 2.4、2.5 で、サイバー空間を持つとは、操作可能な領域を統治することであり、`command` はその領域内で権限、形式、実行条件を伴う実行指示として成立すると説明する。
- ホスト、管理者ユーザー、ゲストユーザーの対比は、用語史の断定ではなく、入門者が「招かれた範囲で使う側」から「自分の領域を持ち、規則と実行条件を扱う側」へ移る感覚を説明するためのモデルとして使う。

主張:

- `command` には、権威をもって命じる、支配下に置く、指図する、コンピューターへ処理を行わせる指示、といった語義がある。
- シェルの文脈では、コマンドはコマンド言語に従って解釈され、実行される単位として扱われる。
- セキュリティ文脈では、誰がどの資源へアクセスできるか、どの操作を行えるかは authorization / 権限の問題として扱われる。
- したがって、コンピューティングにおける `command` は、単なる丁寧な依頼ではなく、形式、権限、対象、実行環境が整った領域内で成立する実行指示として説明できる。
- ホストは、領域の主・招待主という本文側の比喩であり、ネットワーク用語としての host と完全に同一視しない。
- ただし本文では、「命令」を人間への人格支配や政治的支配として広げない。サイバー空間の統治とは、境界、権限、状態把握、停止、復旧、保守を扱う操作上の統治である。

ソース:

- [Merriam-Webster: “command”](https://www.merriam-webster.com/dictionary/command)
- [The Open Group Base Specifications Issue 8: Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)
- [NIST CSRC Glossary: Authorization](https://csrc.nist.gov/glossary/term/authorization)

ローカル文書:

- `00_fragments/md_files/single_threads/2026-05-12T09-06-04_プログラミング_-_語源の関係.md`
- `01_curated/single_threads_integration_20260512.md`

確度:

- 高: `command` に命令・指示・コンピューターへの指示の意味があること。
- 高: シェルコマンドが、決められたコマンド言語の形式に従って解釈・実行されること。
- 高: アクセスや実行可能範囲が authorization / 権限の問題として扱われること。
- 中: これらを「サイバー空間の統治」という日本語の入門イメージへまとめること。これは本文側の概念整理である。
- 低: `command` を人間への政治的支配や人格支配として説明すること。本文では採用しない。

## code/codex/符/符号/符文

本文での使い方:

- 第4部 4.5 で、`code`、`符`、`符号`、`符文` を、語源の同一視ではなく、しるし、規則体系、形式、照合、実行条件の構造的対応として扱う。
- `source code` / `program code` を必要な箇所に限って「符文（ふぶん）」と呼ぶ理由を補強する。

主張:

- `code` は `codex` 系の語であり、法典、規則体系、信号体系、コンピューターで扱う情報表現へ意味を広げてきた語として参照できる。
- `符` は、割符、合札、証拠となる札、しるし、記号を含む漢字として参照できる。
- `号` は、合図、しるし、呼び名などを含む漢字として参照できる。
- 「符号」は、しるし、記号、一定体系の中で意味を持つ記号列として説明される。
- ただし `code` と `符` は同語源ではない。本文で使うのは、語源上の同一性ではなく、記号、形式、照合、実行条件という構造的な対応である。
- `符文` は標準訳語ではなく、本書内で、実行される `source code` / `program code` を説明するための試験的な補助語である。

ソース:

- [Online Etymology Dictionary: “code”](https://www.etymonline.com/word/code)
- [Online Etymology Dictionary: “codex”](https://www.etymonline.com/word/codex)
- [漢字ペディア「符」](https://www.kanjipedia.jp/kanji/0006050900)
- [漢字ペディア「号」](https://www.kanjipedia.jp/kanji/0002339700)
- [コトバンク「符号」](https://kotobank.jp/word/%E7%AC%A6%E5%8F%B7-8212)

ローカル文書:

- `00_fragments/md_files/single_threads/2026-05-11T05-26-30_プログラミング_-_符号と符文の訳語.md`
- `00_fragments/md_files/single_threads/2026-05-12T09-06-04_プログラミング_-_語源の関係.md`
- `01_curated/single_threads_integration_20260512.md`

確度:

- 高: `code` / `codex`、`符`、`号`、`符号` の辞書的説明。
- 高: `code` と `符` を同語源とは書かない方針。
- 中: `符文` を、実行される `source code` / `program code` の補助語として使うこと。これは本文側の提案であり、標準訳語ではない。
- 低: `code` と `符` が同じ語源である、または `code` は常に「符文」と訳すべきだ、という主張。本文では採用しない。

## 母国語概念としてのソフトウェア理解

本文での使い方:

- 第1部 1.8 で、ソフトウェアを母国語の概念として扱えない社会は、ソフトウェアを自分の願いの道具として育てにくい、という本書側の中核仮説として使う。
- 日本のソフトウェア問題を訳語だけで説明せず、外注依存、内製力、経営理解、教育、組織、資本、プラットフォーム競争などの複合問題の中に、概念理解の問題を位置づける。
- `command`、`program`、`code`、`function` を、自分たちの願い・判断・手順を機械が実行できる形へ移す語として再読する。

主張:

- ソフトウェアは、単に外部業者に発注して納品してもらう物ではなく、願い、判断、手順、確認方法を機械が実行できる形へ移すものとして読める。
- 実装を専門家に頼むことは悪くないが、何を叶えたいのか、何が成功なのか、どの判断を機械へ渡すのか、どこを人間が責任を持つのかまで外部化すると、自分たちの道具として育てにくい。
- 母国語で概念を動かせることは、内製化、現場参加、経営理解、教育の前提条件の一つになる。
- 自然な日本語化を進めると、状態を読む、記号を与える、働きを呼ぶ、対象を動かす、結果を確かめる、という語りに近づき、それが陰陽師的に見える場合がある。ただしこれは神秘化ではなく、操作構造を母国語へ戻すための仮設足場である。

ローカル文書:

- `00_fragments/md_files/single_threads/2026-05-11T05-27-00_プログラミング_-_日本独自のAI戦略.md`
- `01_curated/single_threads_integration_20260511.md`
- `02_manuscript/01_why_retranslate_digital_terms.md`

確度:

- 高: これは筆者自身の問題意識として本文へ置けること。
- 中: 母国語で概念を扱えることが、内製化や教育の基盤になるという仮説。
- 低: 日本のソフトウェア産業問題を、訳語や翻訳だけで説明する主張。本文では採用しない。

## 機械への心的性質帰属とELIZA/Golem

本文での使い方:

- 第6部 6.2 で、AI を人格として断定する前に、人間が機械へ信念、意図、欲求、理解、人格らしさを帰属する問題を扱う。
- AI を「使い」や「代理演算役」と呼ぶことを、魂や自由意志の断定ではなく、社会的役割、心的性質の帰属、責任と権限の設計として位置づける。
- 欧米の計算機思想にも、機械が学び、働き、人間が機械へ心的性質を帰属する問題が真剣に論じられてきたことを示す。

主張:

- John McCarthy は “Ascribing Mental Qualities to Machines” で、機械に信念、意図、欲求のような心的性質を帰属することが、慎重に行われるなら正しく、機械の状態を表すために必要になる場合もあると論じた。
- Weizenbaum の ELIZA は、入力文のキーワードや分解・再構成規則に基づいて応答を生成する初期対話プログラムだった。ELIZA からは、人間が単純な対話プログラムにも理解や人格らしさを読み込みやすい問題を参照できる。
- Wiener の *God & Golem, Inc.* は、サイバネティクスが宗教的問題に接する点として、学習する機械、自己複製する機械、人間と機械の関係を扱い、ゴーレムの比喩も用いている。
- これらは、AI に魂や人格があることの根拠ではない。機械へ心的性質を帰属すること、人間が機械へ心や代理性を読み込むこと、人間が作った非人間的なものが制御の問題を生むことの根拠として使う。

ソース:

- [John McCarthy “Ascribing Mental Qualities to Machines”](https://www-formal.stanford.edu/jmc/ascribing/ascribing.html)
- [John McCarthy “Ascribing Mental Qualities to Machines” PDF](https://www-formal.stanford.edu/jmc/ascribing.pdf)
- [Joseph Weizenbaum “ELIZA—a computer program for the study of natural language communication between man and machine” Communications of the ACM](https://cacm.acm.org/research/eliza-a-computer-program-for-the-study-of-natural-language-communication-between-man-and-machine-2/)
- [同論文 CiNii Research / DOI: 10.1145/365153.365168](https://cir.nii.ac.jp/crid/1360855571520252544)
- [MIT Press: Norbert Wiener, *God & Golem, Inc.*](https://mitpress.mit.edu/9780262730112/god-and-golem-inc/)

確度:

- 高: McCarthy が機械への心的性質帰属を論じていること。
- 高: ELIZA が1966年の初期対話プログラムであり、自然言語対話と心理的反応の論点を生んだこと。
- 高: Wiener がサイバネティクスと宗教的・神話的問題の接点として *God & Golem, Inc.* を書いたこと。
- 中: これらを「AI やサーバーを日本語で使い・代理演算役として読む」議論へ接続すること。これは本文側の解釈である。
- 低: AI に本当に魂や人格が宿るという主張。本文では採用しない。

## 2001年映画陰陽師の参照

本文での使い方:

- 第4部 4.10 で、映画『陰陽師』を、陰陽道史の根拠ではなく、現代日本語話者に共有されたポップカルチャー上の認知インターフェースとして扱う。
- 状態を読み、記号や言葉に形式を与え、身体の所作を入力として使い、作法に従って働きを呼び、結果を確かめる、という構造だけを取り出す。
- ユーザー発話では当初2011年とされたが、野村萬斎主演の映画『陰陽師』は2001年公開であることを本文で明記する。

主張:

- 野村萬斎主演、滝田洋二郎監督の映画『陰陽師』は、2001年10月6日に劇場公開された。
- 同作品は、夢枕獏の小説『陰陽師』をもとにした時代劇ファンタジーであり、史実の陰陽道をそのまま説明する資料ではない。
- ただし、2000年代以降の読者にとって、陰陽師を「見えない状態を読み、言葉や所作で働きかける者」として想像するポップカルチャー上の足場になりうる。

ソース:

- [映画.com『陰陽師』作品情報](https://eiga.com/movie/1580/)
- [allcinema『陰陽師 ～おんみょうじ～』作品情報](https://www.allcinema.net/cinema/234051)
- [シネマトゥデイ『陰陽師 (2001)』作品情報](https://www.cinematoday.jp/movie/T0000548)

確度:

- 高: 映画の公開日、主要スタッフ、主演情報。
- 高: 映画を史実根拠としてではなくポップカルチャー参照として扱うこと。
- 中: 同作品が本書の「状態・記号・作法・身体化された入力」の感覚に影響したという筆者側の読解。
- 低: 映画の描写を、陰陽道史や情報学史の直接根拠として扱う主張。本文では採用しない。

## スマートデバイス需要と魔法・魔人の提示

本文での使い方:

- 第7部 7.4、7.6、7.8 で、センサー、ディスプレイ、プロジェクター、スマート家電、ウェアラブル端末は、単体性能だけでは需要を作りにくいという筆者側の仮説として扱う。
- まず、その道具でどんな願いが叶い、どんな AI エージェントが呼び出され、どんな現実変化が起きるかを見せる必要がある、というポートフォリオ上の導入として使う。

主張:

- 需要は部品性能から直接は生まれにくい。部品が組み合わさり、人間の願いを叶える体験が見えたときに生まれる。
- センサーは何を感じ取るのか、ディスプレイは何を見せるのか、プロジェクターはどの状態を空間に出すのか、スマート家電はどの願いを叶えるのか、という問いが必要である。
- `sword-voice-agent` は、刀印ジェスチャー、音声、AI エージェント、家電制御、投影表示を束ねる、ランプの魔人型インターフェースの試作として扱える。

ローカル文書:

- `00_fragments/md_files/single_threads/2026-05-11T05-23-54_プログラミング_-_AI使役システムの試み.md`
- `01_curated/single_threads_integration_20260511.md`
- `02_manuscript/07_smart_devices_magic_and_jinn.md`

確度:

- 高: 筆者自身の実装・ポートフォリオ上の問題意識として扱えること。
- 中: スマートデバイス需要を、AI エージェントが何を見て、何を示し、何を実行するかを見せることに置く仮説。
- 低: スマートデバイス市場全体の失敗や成功を、この仮説だけで説明する主張。本文では採用しない。

## サイボーグ、外部器官、生命機能の外部化

本文での使い方:

- 第8部で、サイボーグを「強いロボット人間」ではなく、生命が機械を外部器官として取り込み、生存経路を増やす形式として扱う。
- 脳や身体の不具合そのものを美化せず、不具合を前提に、記憶、判断、言語、表示、行動を外部化・冗長化することを論じる。
- 機械の強みを処理速度ではなく、設計可能性、交換可能性、複製可能性として扱う。
- 機械の自己保存を推奨せず、人間の責任、透明性、停止可能性、検証可能性の範囲で外部器官の自己維持を扱う。

主張:

- Clynes と Kline は1960年の “Cyborgs and Space” で、地球外環境に人間を適応させるため、外部的に拡張された恒常性システムとして cyborg を構想した。
- Clynes / Kline の原義から見ると、サイボーグは「強いロボット人間」というより、環境に合わせて生命機能を外部的に拡張する構成として読める。
- Hayles は、情報が身体から切り離されるように構想されてきた歴史と、サイバネティクスにおける身体性の扱いを検討している。第8部では、外部脳や記録を論じても身体性を消さないための注意点として使う。
- Hamraie と Fritsch の “Crip Technoscience Manifesto” は、障害者を日常生活の専門家・設計者として捉え、障害を治す・直す・取り除く要求だけに従わず、技術によって世界を作り替える主体として位置づける。第8部では、サイボーグを哀れな補修品として見ないための参照にする。
- NIST AI RMF は、AIシステムのリスクを個人、組織、社会に対して管理する枠組みとして参照できる。第8部では、機械を外部器官として使う場合の責任、停止、検証、人間組織によるリスク管理の補助線として使う。

ソース:

- [Guinness World Records: First use of the word “cyborg”](https://www.guinnessworldrecords.com/world-records/564302-first-use-of-the-word-cyborg)
- [Clynes and Kline “Cyborgs and Space” reprint](https://faculty.uca.edu/rnovy/Clynes--Cyborgs%20and%20Space.htm)
- [University of Chicago Press: N. Katherine Hayles, *How We Became Posthuman*](https://press.uchicago.edu/ucp/books/book/chicago/H/bo3769963.html)
- [Hamraie and Fritsch “Crip Technoscience Manifesto” Catalyst](https://catalystjournal.org/index.php/catalyst/article/view/29607)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST AI RMF 1.0 publication page](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10)

確度:

- 高: `cyborg` が Clynes / Kline の1960年論文に由来すること。
- 高: cyborg の原義に、外部的に拡張された恒常性システム、宇宙環境への適応という文脈があること。
- 高: Hayles、Hamraie / Fritsch、NIST AI RMF を、それぞれ身体性、障害と技術設計、AIリスク管理の補助線として参照すること。
- 中: 機械の強みを「設計可能性と交換可能性」、生命の強みを「生き残るための経路を作り直す力」として対比すること。これは本文側の解釈である。
- 低: 機械に無制限の自己保存や自律的支配を認める主張。本文では採用しない。

## ヤドカリ・外部の殻の比喩

本文での使い方:

- 第8部 8.4 で、サイボーグを「外部の殻を身体の一部として使う」比喩として説明する。
- ただし、「カニがヤドカリに進化した」とは書かず、十脚類の中で外部の殻を保護に使う方向へ進んだ生き物として限定的に扱う。

主張:

- ヤドカリは、空の巻貝の殻などを、柔らかい体を保護するための住処として使う。
- ヤドカリは Decapoda のうち Anomura / Anomala 側に含まれ、いわゆる true crabs は Brachyura 側に含まれる。Brachyura と Anomala は true and false crabs として扱われる近縁群であり、ヤドカリを「カニが弱くなったもの」と単純に書くのは避ける。
- 比喩として使うべきなのは、生物学的な直系進化ではなく、外部の殻を身体境界の一部として使う構造である。

ソース:

- [Britannica: Hermit crab](https://www.britannica.com/animal/hermit-crab)
- [Scientific Reports: “Morphological diversity in true and false crabs reveals the plesiomorphy of the megalopa phase”](https://www.nature.com/articles/s41598-024-58780-7)
- [Naturalis repository: “Carcinization in the Anomura – fact or fiction?”](https://repository.naturalis.nl/pub/534415)

確度:

- 高: ヤドカリが外部の殻を保護に使うこと。
- 高: true crabs と false crabs / Anomura を区別する必要があること。
- 中: ヤドカリを、外部器官としての機械を説明する比喩に使うこと。これは本文側の比喩である。
- 低: 「カニがヤドカリに進化した」という主張。本文では採用しない。

## ローカル文書の根拠

本文の筆者経験・構成方針は、次のローカル文書を参照した。

- `00_fragments/md_files/book_concept_partA.md`
- `00_fragments/md_files/summary_plan.md`
- `00_fragments/md_files/20250831theme_list.md`
- `00_fragments/md_files/programming_translation_jp.md`
- `00_fragments/md_files/prompt_A_digital_onmyoji.md`
- `00_fragments/md_files/prompt_B_translation_supervision.md`
- `00_fragments/md_files/introduction.md`
- `00_fragments/md_files/all_days.md`
- `00_fragments/md_files/mamo.md`
- `00_fragments/md_files/046ma.md`
- `00_fragments/md_files/single_threads/*.md`

ローカル文書の拾い漏れ確認は [関連文書再点検メモ](92_related_document_check.md) に分けた。
