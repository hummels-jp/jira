# AI モデルの基礎と大規模モデル技術

> 面接準備ドキュメント —— AI モデルの原理、ファインチューニング技術、Agent の概念

**言語ナビ：** [[中]](03_ai_model.md) | [日] | [[英]](03_ai_model_en.md)

---

## 目次

1. [AI モデルの基本原理](#q1)
   - CNN（畳み込みニューラルネットワーク）
   - RNN（再帰型ニューラルネットワーク）
   - Transformer
2. [AI 大規模モデルのファインチューニング技術](#q2)
   - Fine-Tuning（全パラメータ微調整）
   - HFRL / RLHF（人間フィードバック強化学習）
   - Prompt Engineering（プロンプトエンジニアリング）
   - LoRA（低ランク適応）
   - Instruction Tuning（指示微調整）
3. [よく使われる AI Agent の概念](#q3)
   - プロンプトテンプレート（Prompt Template）
   - Tool（ツール呼び出し）
   - Skills（スキル）

---

<a id="q1"></a>

## 1. AI モデルの基本原理

### 1.1 CNN（Convolutional Neural Network、畳み込みニューラルネットワーク）

**中核となる考え方：** 畳み込みカーネルを入力データ（通常は画像）上でスライドさせて局所特徴を抽出する。**局所結合**と**重み共有**という特徴を持つ。

**主要コンポーネント：**
- **畳み込み層（Convolution Layer）：** カーネルで特徴マップ（Feature Map）を抽出し、空間情報を保持。
- **プーリング層（Pooling Layer）：** Max Pooling や Average Pooling で次元削減し、平行移動不変性を強化。
- **全結合層（Fully Connected Layer）：** 最終的に分類や回帰の出力に使用。
- **活性化関数：** ReLU、Sigmoid など、非線形性を導入。

**典型的な応用：** 画像分類（ResNet、VGG）、物体検出（YOLO、Faster R-CNN）、セマンティックセグメンテーション（U-Net）、自動運転の認識。

**利点：** パラメータが少なく、画像の平行移動やスケーリングに頑健。
**限界：** 長距離依存や系列データの処理が難しい。

---

### 1.2 RNN（Recurrent Neural Network、再帰型ニューラルネットワーク）

**中核となる考え方：** **時間方向の循環結合**を導入し、前時刻の隠れ状態を現時刻の入力とすることで「記憶」能力を持たせる。

**数式表現：**
```
h_t = f(W_hh · h_{t-1} + W_xh · x_t + b)
y_t = W_hy · h_t
```

**バリエーション：**
- **LSTM（Long Short-Term Memory）：** 忘却ゲート・入力ゲート・出力ゲートを導入し、長期依存問題を解決。
- **GRU（Gated Recurrent Unit）：** LSTM の簡略版。更新ゲートとリセットゲートのみで、パラメータが少なく学習も速い。

**典型的な応用：** 機械翻訳、音声認識、時系列予測、テキスト生成。

**限界：**
- **勾配消失・爆発** 問題（LSTM/GRU で一部緩和）。
- **並列化困難**：時間ステップ順に計算する必要があり、訓練効率が低い。
- 長距離依存の扱いはやはり限定的。

---

### 1.3 Transformer

**中核となる考え方：** 完全に **Self-Attention（自己注意機構）** に基づき、RNN の循環構造を廃止して**完全並列計算**を実現し、任意距離の依存関係を捉える。

**中核コンポーネント：**

#### （1）Self-Attention（自己注意）
```
Attention(Q, K, V) = softmax(Q·K^T / √d_k) · V
```
- **Q（Query）、K（Key）、V（Value）** は入力の線形変換で得る。
- 各トークンが系列内のすべてのトークンと関連度を計算し、文脈重み付き表現を形成。

#### （2）Multi-Head Attention（マルチヘッド注意）
Q/K/V を複数の「ヘッド」に分割して並列計算し、異なる部分空間の意味情報を捉える。

#### （3）Positional Encoding（位置エンコーディング）
Self-Attention 自体は位置情報を含まないため、sin/cos または学習可能な位置埋め込みで系列順序を注入。

#### （4）Encoder-Decoder アーキテクチャ
- **Encoder：** 多層 Self-Attention + Feed Forward で文脈表現を出力。
- **Decoder：** Masked Self-Attention + Cross-Attention でトークンを逐次生成。

**派生モデル：**
- **BERT**（Encoder-Only、双方向エンコード、理解タスク向け）
- **GPT シリーズ**（Decoder-Only、自己回帰生成）
- **T5 / BART**（完全な Encoder-Decoder、翻訳・要約向け）
- **ViT**（Vision Transformer、画像を patch に分割して Transformer に入力）

**利点：**
- 完全並列で訓練効率が高い。
- 長距離依存の捕捉能力が強い。
- 拡張性が極めて高く、現在の大規模言語モデル（LLM）の基盤アーキテクチャ。

**限界：** 計算量とメモリが O(N²) で、長系列に不向き（FlashAttention や Sparse Attention などの最適化が派生）。

---

<a id="q2"></a>

## 2. AI 大規模モデルのファインチューニング技術

### 2.1 Fine-Tuning（全パラメータ微調整）

**定義：** 事前学習モデル（Pretrained Model）をベースに、下流タスクのデータで**全パラメータを更新**する。

**流れ：**
1. 事前学習の重み（LLaMA、GPT など）をロード。
2. 特定領域のデータセットで継続学習。
3. 小さめの学習率（1e-5 ～ 5e-5）で破滅的忘却を回避。

**利点：** 通常最も高い性能が得られ、モデルが下流タスクに完全適応。
**欠点：**
- GPU メモリ・計算コストが極めて高い（数十億パラメータには A100/H100 クラスターが必要）。
- タスクごとに完全なモデルコピーを保存する必要があり、ストレージコスト高。
- 小規模データでは過学習しやすい。

---

### 2.2 HFRL / RLHF（Reinforcement Learning from Human Feedback、人間フィードバック強化学習）

**定義：** **人間の選好データ**で報酬モデル（Reward Model）を学習し、強化学習（通常は PPO）で言語モデルを最適化することで、出力を人間の価値観により合致させる。

**3 段階フロー：**
1. **SFT（Supervised Fine-Tuning）：** 高品質な人手ラベル対話データで教師あり微調整。
2. **Reward Model 学習：** 「同一プロンプトへの複数回答 + 人手ランキング」データを集め、回答にスコアを付ける報酬モデルを訓練。
3. **PPO（Proximal Policy Optimization）強化学習：** Reward Model をフィードバック信号として、SFT モデルの生成方策を最適化。

**代表例：** ChatGPT、Claude、Gemini はいずれも RLHF/RLAIF を採用。

**発展方向：**
- **DPO（Direct Preference Optimization）：** Reward Model を省略し、選好データから直接最適化。訓練がより安定。
- **RLAIF：** 人間の代わりに AI がラベル付けし、コストを削減。

**意義：** LLM をより「有用（Helpful）・誠実（Honest）・無害（Harmless）」——すなわち 3H 原則に近づける。

---

### 2.3 Prompt Engineering（プロンプトエンジニアリング）

**定義：** **モデルパラメータを変更せず**、入力プロンプトを工夫することで期待する出力へと誘導する。

**よく使うテクニック：**
- **Zero-Shot：** 直接指示を与える。
- **Few-Shot：** プロンプト内に数個の例を提供（In-Context Learning）。
- **Chain-of-Thought（CoT）：** モデルに「段階的に考えさせる」ことで推論能力を大幅向上（"Let's think step by step" を追加）。
- **ReAct：** Reasoning + Acting、思考とツール呼び出しを交互に行う。
- **Self-Consistency：** 複数の推論パスを生成し、多数決で最適解を選ぶ。
- **Role Prompting：** 「あなたはベテランの Python エンジニアです……」。

**利点：** 訓練コストゼロで素早くイテレーション可能。
**欠点：** 効果の上限はモデル本体の能力に依存、プロンプトが脆い（小さな変更で出力が大きく変わる）。

---

### 2.4 LoRA（Low-Rank Adaptation、低ランク適応）

**中核となる考え方：** 事前学習モデルの元の重み W を凍結し、その横に**低ランク行列 A と B の 2 つ**（A × B のランク r は元行列の次元より遥かに小さい）を追加し、A と B のみを学習する。

**数式表現：**
```
W_new = W + ΔW = W + B·A     ここで A ∈ R^(r×d), B ∈ R^(d×r), r << d
```

**利点：**
- **パラメータ量が大幅に削減**（通常は元モデルの 0.1% ～ 1%）。消費者向け GPU（RTX 4090 など）で 7B ～ 13B モデルの微調整が可能。
- **学習/推論時にプラグ可能**：同じ base モデルに異なる LoRA アダプタをロードしてマルチタスク切替。
- 効果は全パラメータ微調整に近い。

**派生手法：**
- **QLoRA：** base モデルを 4-bit（NF4）に量子化し、さらにメモリを削減。24GB GPU で 65B モデルを微調整可能。
- **AdaLoRA：** ランク r を適応的に調整。
- **DoRA：** 重み分解 LoRA、効果がより良い。

**代表ツール：** HuggingFace **PEFT** ライブラリ。

---

### 2.5 Instruction Tuning（指示微調整）

**定義：** 大量の**「指示-回答」形式**のデータセットでモデルを微調整し、自然言語の指示に従えるようにする。

**データ形式例：**
```json
{
  "instruction": "以下の中国語を英語に翻訳してください",
  "input": "今日天气很好",
  "output": "The weather is nice today."
}
```

**代表データセット：** Alpaca、Dolly、FLAN、ShareGPT、OpenAssistant。

**中核的価値：**
- base model を「テキスト続き書き」から「指示を理解して実行する」へと進化させる。
- ChatGPT 系対話モデルの鍵となるステップ（通常 RLHF の前段）。

**Fine-Tuning との関係：** Instruction Tuning は SFT（教師あり微調整）の特殊形態で、指示-応答形式に特化したもの。

---

<a id="q3"></a>

## 3. よく使われる AI Agent の概念

**AI Agent の定義：** LLM を中核の「脳」とし、**メモリ（Memory）・プランニング（Planning）・ツール（Tool）** を組み合わせて、自律的に環境を認識・意思決定・実行できる知能エージェント。

古典的アーキテクチャ：**Agent = LLM + Memory + Planning + Tools**

---

### 3.1 プロンプトテンプレート（Prompt Template）

**定義：** **プレースホルダー（変数）** を含むプロンプトテンプレートを事前設計し、実行時に具体的なパラメータを埋め込んで最終プロンプトを生成する。

**例（LangChain スタイル）：**
```python
template = """
あなたは{role}の専門家です。ユーザーの質問に回答してください：
質問：{question}
{language}で回答し、{max_words}字以内でお願いします。
"""
```

**役割：**
- **標準化**：入力形式を統一し、再利用と保守を容易に。
- **パラメータ化**：シーンごとに異なる変数を入れて開発効率アップ。
- **モジュール化**：複雑な Chain / Workflow に組み合わせ可能。

**主要フレームワーク：** LangChain `PromptTemplate`、LlamaIndex、Semantic Kernel。

**発展形：**
- **Few-Shot Template：** 例を埋め込む。
- **Chat Template：** system / user / assistant のロール分離。
- **動的 Template：** 文脈に応じて自動組み立て。

---

### 3.2 Tool（ツール呼び出し）

**定義：** Agent は LLM が出力する**構造化された呼び出し要求**（通常 JSON）を通じて外部関数/API を実行し、結果を LLM に返して推論を継続させる。

**典型的なツール：**
- **検索ツール：** Google Search、Bing API、DuckDuckGo。
- **コード実行：** Python REPL、Code Interpreter。
- **データクエリ：** SQL データベース、ベクトル DB（RAG）。
- **ファイル操作：** ファイル読み書き、Excel / PDF 操作。
- **外部 API：** 天気、地図、カレンダー、メール。

**動作フロー（Function Calling）：**
1. LLM がユーザー要求からどの Tool を呼ぶか判断。
2. スキーマに準拠した JSON（ツール名 + パラメータ）を出力。
3. Agent フレームワークがパースして実行。
4. 結果を LLM に戻し、最終回答を生成（次の Tool 呼び出しが発生することも）。

**代表実装：**
- OpenAI **Function Calling / Tools API**
- Anthropic **Tool Use**
- LangChain **Tools & Agents**
- **MCP（Model Context Protocol）：** Anthropic が提唱するツールプロトコル標準。

**ReAct ループ：**
```
Thought → Action（Tool 呼び出し）→ Observation（結果）→ Thought → ... → Final Answer
```

---

### 3.3 Skills（スキル）

**定義：** Tool よりも一段上の抽象——**Prompt + Tool + フロー**をカプセル化した再利用可能な能力モジュール。1 つの Skill は通常、特定タスクの完全なソリューションに対応する。

**Skill vs Tool 対比：**

| 観点 | Tool | Skill |
|------|------|-------|
| 粒度 | 単一関数/API | 完全なタスクフロー |
| 内容 | 純粋な実行ロジック | Prompt + Tool + 手順 + 例 |
| 再利用 | 原子レベル | シーンレベル |
| 例 | `web_search()` | 「週報作成」「文書翻訳」「コードレビュー」 |

**代表実装：**
- **Microsoft Semantic Kernel Skills：** フォルダで Prompt + Function を整理し、プラグ可能にロード。
- **Anthropic Claude Skills：** `SKILL.md`（frontmatter + Markdown 指示）でタスクフローを定義、Agent が必要に応じてロード。
- **Hermes Agent Skills：** Claude Skills と類似の仕組み、`skill_view()` で必要時にロード。

**Skill の価値：**
- **手続き的記憶（Procedural Memory）：** Agent の「スキル庫」。類似タスクに直接使える。
- **プロンプト文脈の削減：** 必要時のみロードしてトークン節約。
- **反復的な保守：** 使用中に問題を発見したら書き戻して更新（"skill patching"）。

**SKILL.md 構造例：**
```markdown
---
name: translate-doc
description: Markdown 文書を書式を保ったまま翻訳
---

## トリガー条件
ユーザーが .md ファイルの翻訳を要求したとき使用。

## 手順
1. ソースファイルを読み込む
2. 段落ごとに翻訳（コードブロックとリンクは保持）
3. 対象言語ファイルに書き出す
4. 言語間ナビゲーションリンクを生成

## 注意事項
- コードブロック内は翻訳しない
- YAML frontmatter の元フィールド名は保持
```

---

## まとめ

| トピック | ポイント |
|------|--------|
| **CNN** | 局所受容野 + 重み共有、画像タスクの第一候補 |
| **RNN / LSTM** | 時系列モデリング、ただし並列化困難 |
| **Transformer** | Self-Attention + 並列化、LLM の礎 |
| **Fine-Tuning** | 全パラメータ微調整、性能最良だがコスト高 |
| **RLHF** | 人間フィードバックで整合性、LLM を人間の価値観に近づける |
| **Prompt Engineering** | 訓練コストゼロ、CoT / ReAct / Few-Shot |
| **LoRA / QLoRA** | パラメータ効率化、消費者向け GPU で大規模モデル学習可能 |
| **Instruction Tuning** | base model に指示追従を学ばせる |
| **Prompt Template** | パラメータ化・モジュール化されたプロンプト再利用 |
| **Tool** | 原子レベルの外部関数呼び出し（Function Calling） |
| **Skills** | 上位抽象、Prompt + Tool + フローのカプセル化 |

---

**言語ナビ：** [[中]](03_ai_model.md) | [日] | [[英]](03_ai_model_en.md)
