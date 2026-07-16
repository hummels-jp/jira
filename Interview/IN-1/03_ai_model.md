# AI 模型基础与大模型技术

> 面试准备文档 —— AI 模型原理、微调技术与 Agent 概念

**语言导航：** [中] | [[日]](03_ai_model_ja.md) | [[英]](03_ai_model_en.md)

---

## 目录

1. [AI 模型的基本原理](#q1)
   - CNN（卷积神经网络）
   - RNN（循环神经网络）
   - Transformer
2. [AI 大模型的微调技术](#q2)
   - Fine-Tuning（全参数微调）
   - HFRL / RLHF（人类反馈强化学习）
   - Prompt Engineering（提示词工程）
   - LoRA（低秩适配）
   - Instruction Tuning（指令微调）
3. [常用的 AI Agent 概念](#q3)
   - 指令模板（Prompt Template）
   - Tool（工具调用）
   - Skills（技能）

---

<a id="q1"></a>

## 1. AI 模型的基本原理

### 1.1 CNN（Convolutional Neural Network，卷积神经网络）

**核心思想：** 通过卷积核在输入数据（通常是图像）上滑动，提取局部特征，具有**局部连接**和**权值共享**的特点。

**关键组件：**
- **卷积层（Convolution Layer）：** 使用卷积核提取特征图（Feature Map），保留空间信息。
- **池化层（Pooling Layer）：** 通过 Max Pooling 或 Average Pooling 降低维度，增强平移不变性。
- **全连接层（Fully Connected Layer）：** 最终用于分类或回归输出。
- **激活函数：** ReLU、Sigmoid 等，引入非线性。

**典型应用：** 图像分类（ResNet、VGG）、目标检测（YOLO、Faster R-CNN）、语义分割（U-Net）、自动驾驶感知。

**优点：** 参数少、对图像平移/缩放具有鲁棒性。
**局限：** 难以处理长距离依赖和序列数据。

---

### 1.2 RNN（Recurrent Neural Network，循环神经网络）

**核心思想：** 引入**时间维度的循环连接**，将上一时刻的隐藏状态作为当前时刻的输入，从而具备"记忆"能力。

**数学表达：**
```
h_t = f(W_hh · h_{t-1} + W_xh · x_t + b)
y_t = W_hy · h_t
```

**变体：**
- **LSTM（长短期记忆网络）：** 引入遗忘门、输入门、输出门，解决长期依赖问题。
- **GRU（门控循环单元）：** LSTM 的简化版本，只有更新门和重置门，参数更少、训练更快。

**典型应用：** 机器翻译、语音识别、时序预测、文本生成。

**局限：**
- **梯度消失/爆炸** 问题（LSTM/GRU 部分缓解）。
- **难以并行**：必须按时间步顺序计算，训练效率低。
- 长距离依赖依然处理有限。

---

### 1.3 Transformer

**核心思想：** 完全基于**自注意力机制（Self-Attention）**，摒弃 RNN 的循环结构，实现**全并行计算**，捕捉任意距离的依赖关系。

**核心组件：**

#### （1）Self-Attention（自注意力）
```
Attention(Q, K, V) = softmax(Q·K^T / √d_k) · V
```
- **Q（Query）、K（Key）、V（Value）** 由输入线性变换得到。
- 每个 token 与序列中所有 token 计算相关性，形成上下文加权表示。

#### （2）Multi-Head Attention（多头注意力）
将 Q/K/V 拆分为多个"头"并行计算，捕捉不同子空间的语义信息。

#### （3）Positional Encoding（位置编码）
因为 Self-Attention 本身不含位置信息，通过 sin/cos 或可学习的位置嵌入注入序列顺序。

#### （4）Encoder-Decoder 架构
- **Encoder：** 多层 Self-Attention + Feed Forward，输出上下文表示。
- **Decoder：** 带 Masked Self-Attention + Cross-Attention，逐 token 生成输出。

**衍生模型：**
- **BERT**（Encoder-Only，双向编码，适合理解任务）
- **GPT 系列**（Decoder-Only，自回归生成）
- **T5 / BART**（完整 Encoder-Decoder，适合翻译、摘要）
- **ViT**（Vision Transformer，将图像切分为 patch 输入 Transformer）

**优点：**
- 完全并行，训练效率高。
- 长距离依赖捕捉能力强。
- 可扩展性极强，是当前大语言模型（LLM）的基础架构。

**局限：** 计算和显存复杂度 O(N²)，对长序列不友好（衍生出 FlashAttention、Sparse Attention 等优化）。

---

<a id="q2"></a>

## 2. AI 大模型的微调技术

### 2.1 Fine-Tuning（全参数微调）

**定义：** 在预训练模型（Pretrained Model）基础上，使用下游任务数据**更新全部参数**。

**流程：**
1. 加载预训练权重（如 LLaMA、GPT）。
2. 在特定领域数据集上继续训练。
3. 使用较小学习率（如 1e-5 ~ 5e-5）避免灾难性遗忘。

**优点：** 效果通常最好，模型完全适配下游任务。
**缺点：**
- 显存/算力成本极高（数十亿参数需要 A100/H100 集群）。
- 每个任务需保存一份完整模型副本，存储成本高。
- 容易过拟合小数据集。

---

### 2.2 HFRL / RLHF（Reinforcement Learning from Human Feedback，人类反馈强化学习）

**定义：** 利用**人类偏好数据**训练奖励模型（Reward Model），再通过强化学习（通常是 PPO）优化语言模型，使输出更符合人类价值观。

**三阶段流程：**
1. **SFT（Supervised Fine-Tuning）：** 用高质量人工标注对话数据做监督微调。
2. **Reward Model 训练：** 收集"同一 prompt 的多个回答 + 人工排序"数据，训练奖励模型给回答打分。
3. **PPO（Proximal Policy Optimization）强化学习：** 用 Reward Model 作为反馈信号，优化 SFT 模型的生成策略。

**典型代表：** ChatGPT、Claude、Gemini 都使用了 RLHF/RLAIF。

**演进方向：**
- **DPO（Direct Preference Optimization）：** 跳过 Reward Model，直接从偏好数据优化，训练更稳定。
- **RLAIF：** 用 AI 代替人类做标注，降低成本。

**意义：** 使 LLM 更"有用（Helpful）、诚实（Honest）、无害（Harmless）"—— 即 3H 原则。

---

### 2.3 Prompt Engineering（提示词工程）

**定义：** **不修改模型参数**，仅通过精心设计输入提示（Prompt）来引导模型输出期望结果。

**常用技巧：**
- **Zero-Shot：** 直接给指令。
- **Few-Shot：** 在 prompt 中提供几个示例（In-Context Learning）。
- **Chain-of-Thought（CoT）：** 让模型"逐步思考"，显著提升推理能力（在 prompt 加入 "Let's think step by step"）。
- **ReAct：** Reasoning + Acting，交替进行思考和调用工具。
- **Self-Consistency：** 生成多条推理路径，投票选出最优答案。
- **Role Prompting：** "你是一个资深的 Python 工程师……"

**优点：** 零训练成本、快速迭代。
**缺点：** 效果上限受模型本身能力限制、prompt 脆弱（微小改动可能导致输出差异大）。

---

### 2.4 LoRA（Low-Rank Adaptation，低秩适配）

**核心思想：** 冻结预训练模型的原始权重 W，在旁边添加**两个低秩矩阵 A 和 B**（A × B 的秩 r 远小于原矩阵维度），只训练 A 和 B。

**数学表达：**
```
W_new = W + ΔW = W + B·A     其中 A ∈ R^(r×d), B ∈ R^(d×r), r << d
```

**优点：**
- **参数量大幅减少**（通常仅原模型的 0.1% ~ 1%），可在消费级 GPU（如 RTX 4090）上微调 7B ~ 13B 模型。
- **训练/推理时可插拔**：同一个 base 模型可加载不同 LoRA 适配器实现多任务切换。
- 效果接近全参数微调。

**衍生方法：**
- **QLoRA：** 将 base 模型量化为 4-bit（NF4），进一步降低显存，24GB 显卡可微调 65B 模型。
- **AdaLoRA：** 自适应调整秩 r。
- **DoRA：** 权重分解 LoRA，效果更好。

**典型工具：** HuggingFace **PEFT** 库。

---

### 2.5 Instruction Tuning（指令微调）

**定义：** 用**大量"指令-回答"格式**的数据集微调模型，使模型学会遵循自然语言指令。

**数据格式示例：**
```json
{
  "instruction": "把下面的中文翻译成英文",
  "input": "今天天气很好",
  "output": "The weather is nice today."
}
```

**代表数据集：** Alpaca、Dolly、FLAN、ShareGPT、OpenAssistant。

**核心价值：**
- 让 base model 从"续写文本"进化为"听懂指令并执行"。
- 是 ChatGPT 类对话模型的关键一步（通常在 RLHF 之前）。

**与 Fine-Tuning 的关系：** 指令微调是 SFT（监督微调）的一种特殊形式，专门针对指令-响应格式。

---

<a id="q3"></a>

## 3. 常用的 AI Agent 概念

**AI Agent 定义：** 以 LLM 为核心"大脑"，结合**记忆（Memory）、规划（Planning）、工具（Tool）**，能够自主感知环境、决策并执行任务的智能体。

经典架构：**Agent = LLM + Memory + Planning + Tools**

---

### 3.1 指令模板（Prompt Template）

**定义：** 预先设计的、含有**占位符（变量）**的 Prompt 模板，运行时填入具体参数生成最终 Prompt。

**示例（LangChain 风格）：**
```python
template = """
你是一位{role}专家，请回答用户的问题：
问题：{question}
请用{language}回答，字数不超过{max_words}字。
"""
```

**作用：**
- **标准化**：统一输入格式，方便复用和维护。
- **参数化**：不同场景填不同变量，提升开发效率。
- **模块化**：可组合成复杂的 Chain / Workflow。

**常用框架：** LangChain `PromptTemplate`、LlamaIndex、Semantic Kernel。

**进阶：**
- **Few-Shot Template：** 内嵌示例。
- **Chat Template：** 区分 system / user / assistant 角色。
- **动态 Template：** 根据上下文自动组装。

---

### 3.2 Tool（工具调用）

**定义：** Agent 通过 LLM 输出**结构化调用请求**（通常是 JSON），触发外部函数/API 执行，然后将结果返回给 LLM 继续推理。

**典型工具：**
- **搜索工具：** Google Search、Bing API、DuckDuckGo。
- **代码执行：** Python REPL、Code Interpreter。
- **数据查询：** SQL 数据库、向量数据库（RAG）。
- **文件操作：** 读写文件、操作 Excel / PDF。
- **外部 API：** 天气、地图、日历、邮件。

**工作流程（Function Calling）：**
1. LLM 根据用户请求判断需要调用哪个 Tool。
2. 输出符合 schema 的 JSON（工具名 + 参数）。
3. Agent 框架解析并执行工具。
4. 结果返回 LLM，生成最终回答（可能触发下一次工具调用）。

**代表实现：**
- OpenAI **Function Calling / Tools API**
- Anthropic **Tool Use**
- LangChain **Tools & Agents**
- **MCP（Model Context Protocol）：** Anthropic 提出的工具协议标准。

**ReAct 循环：**
```
Thought → Action（调用 Tool）→ Observation（结果）→ Thought → ... → Final Answer
```

---

### 3.3 Skills（技能）

**定义：** 比 Tool 更高一层的抽象——**封装了 Prompt + Tool + 流程**的可复用能力模块。一个 Skill 通常对应一个特定任务的完整解决方案。

**Skill vs Tool 对比：**

| 维度 | Tool | Skill |
|------|------|-------|
| 粒度 | 单个函数/API | 完整任务流程 |
| 内容 | 纯执行逻辑 | Prompt + Tool + 步骤 + 示例 |
| 复用 | 原子级 | 场景级 |
| 例子 | `web_search()` | "写周报"、"翻译文档"、"代码审查" |

**典型实现：**
- **Microsoft Semantic Kernel Skills：** 用文件夹组织 Prompt + Function，可插拔加载。
- **Anthropic Claude Skills：** 通过 `SKILL.md`（含 frontmatter + Markdown 指令）定义任务流程，Agent 按需加载。
- **Hermes Agent Skills：** 类似 Claude Skills 的机制，通过 `skill_view()` 按需加载。

**Skill 的价值：**
- **过程性记忆（Procedural Memory）：** Agent 的"技能库"，遇到相似任务直接调用。
- **降低 Prompt 上下文：** 只在需要时加载，节省 token。
- **可迭代维护：** 使用过程中发现问题可回写更新（"skill patching"）。

**示例 SKILL.md 结构：**
```markdown
---
name: translate-doc
description: 翻译 Markdown 文档并保留格式
---

## 触发条件
用户请求翻译 .md 文件时使用。

## 步骤
1. 读取源文件
2. 分段翻译（保留代码块和链接）
3. 写回目标语言文件
4. 生成跨语言导航链接

## 注意事项
- 代码块内容不翻译
- YAML frontmatter 保留原字段名
```

---

## 总结

| 主题 | 关键点 |
|------|--------|
| **CNN** | 局部感受野 + 权值共享，图像任务首选 |
| **RNN / LSTM** | 时序建模，但难并行 |
| **Transformer** | Self-Attention + 并行化，LLM 基石 |
| **Fine-Tuning** | 全参数微调，效果最好但成本高 |
| **RLHF** | 人类反馈对齐，让 LLM 更符合人类价值观 |
| **Prompt Engineering** | 零训练成本，CoT / ReAct / Few-Shot |
| **LoRA / QLoRA** | 参数高效微调，消费级 GPU 可训练大模型 |
| **Instruction Tuning** | 让 base model 学会遵循指令 |
| **Prompt Template** | 参数化、模块化的 Prompt 复用 |
| **Tool** | 原子级外部函数调用（Function Calling） |
| **Skills** | 高阶抽象，Prompt + Tool + 流程的封装 |

---

**语言导航：** [中] | [[日]](03_ai_model_ja.md) | [[英]](03_ai_model_en.md)
