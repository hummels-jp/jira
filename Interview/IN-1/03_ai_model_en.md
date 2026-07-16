# AI Model Fundamentals and Large Model Techniques

> Interview prep doc — AI model principles, fine-tuning techniques, and Agent concepts

**Language nav:** [[中]](03_ai_model.md) | [[日]](03_ai_model_ja.md) | [英]

---

## Table of Contents

1. [Fundamentals of AI Models](#q1)
   - CNN (Convolutional Neural Network)
   - RNN (Recurrent Neural Network)
   - Transformer
2. [Fine-Tuning Techniques for Large Models](#q2)
   - Fine-Tuning (full-parameter)
   - HFRL / RLHF (Reinforcement Learning from Human Feedback)
   - Prompt Engineering
   - LoRA (Low-Rank Adaptation)
   - Instruction Tuning
3. [Common AI Agent Concepts](#q3)
   - Prompt Template
   - Tool (tool calling)
   - Skills

---

<a id="q1"></a>

## 1. Fundamentals of AI Models

<a id="cnn"></a>
### 1.1 CNN (Convolutional Neural Network)
[[中]](03_ai_model.md#cnn) | [[日]](03_ai_model_ja.md#cnn) | [英](#cnn)

**Core idea:** Slide convolution kernels over input data (typically images) to extract local features. Characterized by **local connectivity** and **weight sharing**.

**Key components:**
- **Convolution layer:** Applies kernels to extract feature maps, preserving spatial information.
- **Pooling layer:** Reduces dimensionality via Max/Average Pooling, boosting translation invariance.
- **Fully Connected layer:** Produces the final classification or regression output.
- **Activation function:** ReLU, Sigmoid, etc., introducing non-linearity.

**Typical applications:** Image classification (ResNet, VGG), object detection (YOLO, Faster R-CNN), semantic segmentation (U-Net), perception in autonomous driving.

**Pros:** Few parameters, robust to image translation and scaling.
**Cons:** Struggles with long-range dependencies and sequential data.

---

<a id="rnn"></a>
### 1.2 RNN (Recurrent Neural Network)
[[中]](03_ai_model.md#rnn) | [[日]](03_ai_model_ja.md#rnn) | [英](#rnn)

**Core idea:** Introduces a **recurrent connection along the time dimension**, feeding the previous hidden state into the current step to endow the network with "memory."

**Formulation:**
```
h_t = f(W_hh · h_{t-1} + W_xh · x_t + b)
y_t = W_hy · h_t
```

**Variants:**
- **LSTM (Long Short-Term Memory):** Adds forget, input, and output gates to solve long-term dependency issues.
- **GRU (Gated Recurrent Unit):** A simplified LSTM with only update and reset gates — fewer parameters, faster training.

**Typical applications:** Machine translation, speech recognition, time-series forecasting, text generation.

**Limitations:**
- **Vanishing / exploding gradients** (partially mitigated by LSTM/GRU).
- **Hard to parallelize:** Must be computed step by step, so training is slow.
- Long-range dependencies remain limited.

---

<a id="transformer"></a>
### 1.3 Transformer
[[中]](03_ai_model.md#transformer) | [[日]](03_ai_model_ja.md#transformer) | [英](#transformer)

**Core idea:** Built entirely on **Self-Attention**, discarding RNN recurrence for **fully parallel computation** and capturing dependencies at arbitrary distances.

**Core components:**

#### (1) Self-Attention
```
Attention(Q, K, V) = softmax(Q·K^T / √d_k) · V
```
- **Q (Query), K (Key), V (Value)** are obtained via linear projections of the input.
- Each token computes relevance with every other token in the sequence, forming a context-weighted representation.

#### (2) Multi-Head Attention
Split Q/K/V into multiple "heads" for parallel computation, capturing semantics in different subspaces.

#### (3) Positional Encoding
Since Self-Attention itself carries no positional information, sequence order is injected via sin/cos or learned position embeddings.

#### (4) Encoder-Decoder Architecture
- **Encoder:** Stacked Self-Attention + Feed Forward layers outputting contextual representations.
- **Decoder:** Masked Self-Attention + Cross-Attention, generating tokens autoregressively.

**Derived models:**
- **BERT** (Encoder-Only, bidirectional, suited for understanding tasks)
- **GPT family** (Decoder-Only, autoregressive generation)
- **T5 / BART** (Full Encoder-Decoder, good for translation and summarization)
- **ViT** (Vision Transformer — image split into patches fed to a Transformer)

**Pros:**
- Fully parallel, high training efficiency.
- Strong at capturing long-range dependencies.
- Highly scalable — the foundation of today's Large Language Models (LLMs).

**Cons:** O(N²) compute and memory complexity, unfriendly to long sequences (motivating FlashAttention, Sparse Attention, etc.).

---

<a id="q2"></a>

## 2. Fine-Tuning Techniques for Large Models

<a id="fine-tuning"></a>
### 2.1 Fine-Tuning (Full-Parameter)
[[中]](03_ai_model.md#fine-tuning) | [[日]](03_ai_model_ja.md#fine-tuning) | [英](#fine-tuning)

**Definition:** Start from a pretrained model and **update all parameters** using downstream task data.

**Process:**
1. Load pretrained weights (e.g., LLaMA, GPT).
2. Continue training on domain-specific datasets.
3. Use a small learning rate (1e-5 ~ 5e-5) to avoid catastrophic forgetting.

**Pros:** Typically the best performance — the model fully adapts to the downstream task.
**Cons:**
- Extremely high GPU/compute cost (billions of parameters need A100/H100 clusters).
- Requires storing a full model copy per task — high storage cost.
- Prone to overfitting on small datasets.

---

<a id="rlhf"></a>
### 2.2 HFRL / RLHF (Reinforcement Learning from Human Feedback)
[[中]](03_ai_model.md#rlhf) | [[日]](03_ai_model_ja.md#rlhf) | [英](#rlhf)

**Definition:** Train a Reward Model on **human preference data**, then use reinforcement learning (usually PPO) to optimize the language model so its outputs better align with human values.

**Three-stage pipeline:**
1. **SFT (Supervised Fine-Tuning):** Supervised fine-tuning on high-quality human-annotated dialogue data.
2. **Reward Model training:** Collect "multiple answers per prompt + human rankings" and train a reward model to score responses.
3. **PPO (Proximal Policy Optimization):** Use the Reward Model as a feedback signal to optimize the SFT model's generation policy.

**Representative models:** ChatGPT, Claude, and Gemini all use RLHF / RLAIF.

**Evolutions:**
- **DPO (Direct Preference Optimization):** Skips the reward model and optimizes directly from preference data — more stable training.
- **RLAIF:** Uses AI instead of humans for labeling, reducing cost.

**Significance:** Makes LLMs more **Helpful, Honest, Harmless** — the "3H" principle.

---

<a id="prompt-eng"></a>
### 2.3 Prompt Engineering
[[中]](03_ai_model.md#prompt-eng) | [[日]](03_ai_model_ja.md#prompt-eng) | [英](#prompt-eng)

**Definition:** **Without modifying model parameters**, carefully craft input prompts to steer the model toward the desired output.

**Common techniques:**
- **Zero-Shot:** Give the instruction directly.
- **Few-Shot:** Provide a few examples inside the prompt (In-Context Learning).
- **Chain-of-Thought (CoT):** Have the model "think step by step" — significantly boosts reasoning ("Let's think step by step").
- **ReAct:** Reasoning + Acting — interleave thinking and tool calls.
- **Self-Consistency:** Generate multiple reasoning paths and vote for the best answer.
- **Role Prompting:** "You are a senior Python engineer..."

**Pros:** Zero training cost, fast iteration.
**Cons:** Upper bound is capped by the model's own ability; prompts are fragile (small edits can shift outputs drastically).

---

<a id="lora"></a>
### 2.4 LoRA (Low-Rank Adaptation)
[[中]](03_ai_model.md#lora) | [[日]](03_ai_model_ja.md#lora) | [英](#lora)

**Core idea:** Freeze the pretrained weight W and add **two low-rank matrices A and B** alongside it (with rank r ≪ original dimension). Only A and B are trained.

**Formulation:**
```
W_new = W + ΔW = W + B·A     where A ∈ R^(r×d), B ∈ R^(d×r), r << d
```

**Pros:**
- **Massive parameter reduction** (typically 0.1% ~ 1% of the original model) — you can fine-tune 7B ~ 13B models on consumer GPUs like an RTX 4090.
- **Pluggable at training/inference:** The same base model can load different LoRA adapters for multi-task switching.
- Performance close to full fine-tuning.

**Derivatives:**
- **QLoRA:** Quantize the base model to 4-bit (NF4) to further reduce memory — a 24GB GPU can fine-tune a 65B model.
- **AdaLoRA:** Adaptively adjusts rank r.
- **DoRA:** Weight-decomposed LoRA, better performance.

**Popular tool:** HuggingFace **PEFT** library.

---

<a id="instruction-tuning"></a>
### 2.5 Instruction Tuning
[[中]](03_ai_model.md#instruction-tuning) | [[日]](03_ai_model_ja.md#instruction-tuning) | [英](#instruction-tuning)

**Definition:** Fine-tune a model on large amounts of **"instruction–response"** data so it learns to follow natural language instructions.

**Data format example:**
```json
{
  "instruction": "Translate the following Chinese into English",
  "input": "今天天气很好",
  "output": "The weather is nice today."
}
```

**Representative datasets:** Alpaca, Dolly, FLAN, ShareGPT, OpenAssistant.

**Core value:**
- Transforms a base model from "text continuation" to "understanding and executing instructions."
- A key step for ChatGPT-style chat models (usually before RLHF).

**Relation to Fine-Tuning:** Instruction Tuning is a specific form of SFT (Supervised Fine-Tuning), specialized on instruction–response format.

---

<a id="q3"></a>

## 3. Common AI Agent Concepts

**AI Agent definition:** An intelligent entity that uses an LLM as its "brain," combined with **Memory, Planning, and Tools**, capable of autonomously perceiving its environment, making decisions, and executing tasks.

Classic architecture: **Agent = LLM + Memory + Planning + Tools**

---

<a id="prompt-template"></a>
### 3.1 Prompt Template
[[中]](03_ai_model.md#prompt-template) | [[日]](03_ai_model_ja.md#prompt-template) | [英](#prompt-template)

**Definition:** A pre-designed prompt containing **placeholders (variables)** that get filled in at runtime to produce the final prompt.

**Example (LangChain style):**
```python
template = """
You are an expert in {role}. Please answer the user's question:
Question: {question}
Answer in {language}, no more than {max_words} words.
"""
```

**Purpose:**
- **Standardization:** Unified input format, easy to reuse and maintain.
- **Parameterization:** Different values per scenario, boosting dev efficiency.
- **Modularization:** Composable into complex Chains / Workflows.

**Common frameworks:** LangChain `PromptTemplate`, LlamaIndex, Semantic Kernel.

**Advanced:**
- **Few-Shot Template:** Embeds examples.
- **Chat Template:** Distinguishes system / user / assistant roles.
- **Dynamic Template:** Assembled on the fly based on context.

---

<a id="tool"></a>
### 3.2 Tool (Tool Calling)
[[中]](03_ai_model.md#tool) | [[日]](03_ai_model_ja.md#tool) | [英](#tool)

**Definition:** The Agent has the LLM emit a **structured call request** (usually JSON) that triggers an external function/API. The result is returned to the LLM to continue reasoning.

**Typical tools:**
- **Search:** Google Search, Bing API, DuckDuckGo.
- **Code execution:** Python REPL, Code Interpreter.
- **Data queries:** SQL databases, vector DBs (RAG).
- **File operations:** Read/write files, manipulate Excel / PDF.
- **External APIs:** Weather, maps, calendar, email.

**Workflow (Function Calling):**
1. The LLM decides which Tool is needed based on the user request.
2. It emits schema-compliant JSON (tool name + arguments).
3. The Agent framework parses and executes.
4. The result flows back to the LLM, which produces the final answer (possibly triggering more tool calls).

**Representative implementations:**
- OpenAI **Function Calling / Tools API**
- Anthropic **Tool Use**
- LangChain **Tools & Agents**
- **MCP (Model Context Protocol):** Anthropic's proposed standard tool protocol.

**ReAct loop:**
```
Thought → Action (call Tool) → Observation (result) → Thought → ... → Final Answer
```

---

<a id="skills"></a>
### 3.3 Skills
[[中]](03_ai_model.md#skills) | [[日]](03_ai_model_ja.md#skills) | [英](#skills)

**Definition:** A higher-level abstraction than Tool — a reusable capability module that encapsulates **Prompt + Tool + workflow**. Each Skill typically corresponds to a full solution for a specific task.

**Skill vs Tool comparison:**

| Aspect | Tool | Skill |
|------|------|-------|
| Granularity | Single function/API | Full task workflow |
| Content | Pure execution logic | Prompt + Tool + steps + examples |
| Reuse | Atomic level | Scenario level |
| Example | `web_search()` | "Write weekly report", "Translate doc", "Code review" |

**Representative implementations:**
- **Microsoft Semantic Kernel Skills:** Organize Prompt + Function in folders, pluggably loaded.
- **Anthropic Claude Skills:** Define task workflows via `SKILL.md` (frontmatter + Markdown instructions), loaded on demand by the Agent.
- **Hermes Agent Skills:** Similar mechanism to Claude Skills, loaded on demand via `skill_view()`.

**Value of Skills:**
- **Procedural memory:** The Agent's "skill library" — reusable directly for similar tasks.
- **Reduced prompt context:** Loaded only when needed, saving tokens.
- **Iterative maintenance:** Issues discovered during use can be written back ("skill patching").

**Sample SKILL.md structure:**
```markdown
---
name: translate-doc
description: Translate Markdown documents while preserving formatting
---

## Trigger
Use when the user requests translation of a .md file.

## Steps
1. Read the source file
2. Translate paragraph by paragraph (preserve code blocks and links)
3. Write out to the target-language file
4. Generate cross-language navigation links

## Notes
- Do not translate content inside code blocks
- Preserve original YAML frontmatter field names
```

---

## Summary

| Topic | Key points |
|------|--------|
| **CNN** | Local receptive field + weight sharing — go-to for image tasks |
| **RNN / LSTM** | Sequence modeling, but hard to parallelize |
| **Transformer** | Self-Attention + parallelism — foundation of LLMs |
| **Fine-Tuning** | Full-parameter tuning, best quality but costly |
| **RLHF** | Human-feedback alignment — makes LLMs match human values |
| **Prompt Engineering** | Zero training cost — CoT / ReAct / Few-Shot |
| **LoRA / QLoRA** | Parameter-efficient tuning — train big models on consumer GPUs |
| **Instruction Tuning** | Teach base models to follow instructions |
| **Prompt Template** | Parameterized, modular prompt reuse |
| **Tool** | Atomic external function calls (Function Calling) |
| **Skills** | Higher abstraction — encapsulates Prompt + Tool + workflow |

---

**Language nav:** [[中]](03_ai_model.md) | [[日]](03_ai_model_ja.md) | [英]
