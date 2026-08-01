# LangChain 入门介绍

## 1. 什么是 LangChain

LangChain 是一个用于开发由大语言模型（LLM）驱动的应用程序的开源框架。它提供了一系列工具和抽象，帮助开发者将 LLM 与外部数据源、工具链、记忆机制等集成起来，从而构建更复杂的 AI 应用。

LangChain 最初由 Harrison Chase 于 2022 年 10 月发布，现已成为构建 LLM 应用最流行的框架之一。

## 2. 为什么需要 LangChain

直接使用 LLM API 虽然简单，但在构建实际应用时会遇到以下挑战：

- **上下文管理**：LLM 本身没有长期记忆，需要手动维护对话历史。
- **外部数据集成**：如何让模型访问私有数据、数据库、文档等。
- **工具调用**：如何让模型决定调用外部工具（如搜索、计算、API）。
- **提示工程**：如何有效组织和管理提示词模板。
- **链式调用**：如何将多个步骤组合成完整的工作流。

LangChain 正是为了解决这些问题而设计的。

## 3. 核心概念

### 3.1 Model（模型）

LangChain 支持多种模型类型：

- **LLM**：文本补全模型，如 OpenAI 的 `gpt-3.5-turbo-instruct`。
- **Chat Model**：对话模型，如 `gpt-4`、`Claude`。
- **Embedding Model**：嵌入模型，用于将文本转换为向量，如 `text-embedding-3-small`。

### 3.2 Prompt（提示词）

LangChain 提供了 `PromptTemplate` 来管理提示词模板，支持：

- 变量替换
- 少样本示例（Few-shot）
- 聊天消息模板（ChatPromptTemplate）

示例：

```python
from langchain.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["product"],
    template="请为{product}写一段吸引人的广告语。"
)

prompt = template.format(product="智能手表")
```

### 3.3 Chain（链）

Chain 是 LangChain 的核心概念，表示一系列有序的操作步骤。一个 Chain 可以包含：

- 提示词模板
- 模型调用
- 输出解析器

示例：

```python
from langchain.chains import LLMChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(temperature=0.7)
prompt = PromptTemplate.from_template("请用一句话介绍{topic}。")
chain = LLMChain(llm=llm, prompt=prompt)

result = chain.run(topic="LangChain")
```

### 3.4 Memory（记忆）

Memory 用于在对话中保存上下文信息，使模型能够"记住"之前的对话内容。

常见类型：

- `ConversationBufferMemory`：保存完整对话历史。
- `ConversationBufferWindowMemory`：只保存最近几轮对话。
- `ConversationSummaryMemory`：对历史对话进行摘要，节省 token。

### 3.5 Retriever（检索器）

Retriever 用于从外部数据源中检索相关文档，是构建 RAG（Retrieval-Augmented Generation）应用的关键组件。

典型流程：

1. 文档加载（Document Loaders）
2. 文本分割（Text Splitters）
3. 向量化（Embeddings）
4. 向量存储（Vector Stores）
5. 相似度检索（Similarity Search）

### 3.6 Agent（代理）

Agent 让 LLM 能够自主决定使用哪些工具来完成任务。它不再依赖固定的链式流程，而是根据输入动态选择行动。

示例工具：

- 搜索引擎
- 计算器
- 数据库查询
- 自定义 API

## 4. LangChain 的架构层次

```
┌─────────────────────────────────────────┐
│           LangChain Expression          │
│              Language (LCEL)            │
├─────────────────────────────────────────┤
│  Chains  │  Agents  │  Retrieval (RAG) │
├─────────────────────────────────────────┤
│  Models  │ Prompts  │ Memory │ Output   │
│          │          │        │ Parsers  │
├─────────────────────────────────────────┤
│  Document Loaders │ Embeddings │ Vector  │
│                   │            │ Stores  │
└─────────────────────────────────────────┘
```

## 5. 简单示例：构建一个问答机器人

```python
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

# 初始化模型
llm = ChatOpenAI(model="gpt-4", temperature=0)

# 构建提示词模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一位专业的技术文档助手，请用中文简洁地回答用户问题。"),
    ("human", "{question}")
])

# 使用 LCEL 构建链
chain = prompt | llm | StrOutputParser()

# 调用
response = chain.invoke({"question": "什么是 LangChain？"})
print(response)
```

## 6. 典型应用场景

- **智能客服**：结合企业知识库回答用户问题。
- **文档问答**：对 PDF、Word、网页等文档进行检索和问答。
- **代码助手**：辅助代码生成、解释、重构。
- **数据分析**：让模型查询数据库并生成分析结论。
- **自动化工作流**：通过 Agent 调用多种工具完成复杂任务。

## 7. LangChain 的四大支柱

LangChain 生态由四个核心框架 / 平台组成，分别覆盖应用开发、复杂工作流编排、深度智能代理和企业级运维观测四个层面。

### 7.1 LangChain — 应用开发框架

LangChain 是生态的核心基础框架，提供了一整套开发 LLM 应用所需的能力和抽象，包括：

- 统一接口接入各种 LLM、Chat Model 和 Embedding Model。
- `PromptTemplate`、Few-shot 等提示词管理工具。
- Chain 与 LCEL（LangChain Expression Language）链式调用。
- Memory、Retriever、Agent、Tool 等扩展组件。

它的作用是帮助开发者快速将大模型能力整合到应用中，解决模型调用、上下文管理、外部数据接入、工具调用等常见问题。

### 7.2 LangGraph — 复杂工作流与多代理编排框架

LangGraph 是基于图结构（Graph）的框架，用于构建有状态、可循环、可分支的复杂工作流和多代理（Multi-Agent）系统。

主要特点：

- 以节点（Node）和边（Edge）建模任务流程。
- 支持循环、条件分支、并行执行等人机 / 机机协作模式。
- 内置持久化状态（State Persistence），可恢复和检查工作流执行过程。

LangGraph 适合需要精确控制执行路径、长期运行、多轮交互或复杂 Agent 协作的场景。

### 7.3 DeepAgent — 深度推理与自主执行代理框架

DeepAgent 是面向复杂任务执行和深度研究的代理框架，强调让 LLM 具备更深层次的推理、规划和自主执行能力。

核心能力：

- 多步骤任务分解与规划（Planning）。
- 结合搜索引擎、数据库、API 等工具进行深度信息收集。
- 长周期执行与自我反思（Reflection），持续迭代直到任务完成。

DeepAgent 适用于需要深度调研、复杂报告生成、自动化研究、多步骤决策等高级 Agent 场景。

### 7.4 LangSmith — LLM 应用可观测性与评估平台

LangSmith 是面向 LLM 应用全生命周期的可观测性平台，提供追踪、调试、测试、评估和提示词管理等功能。

核心功能：

- **Tracing**：记录每一次调用链的执行过程，查看输入、输出、延迟和 Token 消耗。
- **Debugging**：快速定位链或 Agent 中的错误和异常行为。
- **Evaluation**：使用数据集对应用进行系统化评估，比较不同版本效果。
- **Prompt Management**：集中管理提示词模板，支持版本控制。

LangSmith 帮助开发团队在生产环境中监控、优化和运维 LLM 应用，提升可靠性和性能。

## 8. 学习建议

1. 先掌握 Prompt Engineering 基础。
2. 熟悉 OpenAI API 或其他 LLM API 的使用。
3. 从简单的 Chain 开始，逐步学习 Memory、Retriever、Agent。
4. 动手实现一个 RAG 或 Agent 项目。
5. 使用 LangSmith 监控和优化应用。

## 9. 参考资源

- 官方文档：https://python.langchain.com/
- GitHub：https://github.com/langchain-ai/langchain
- LangSmith：https://smith.langchain.com/

---

> 本文档为 LangChain 入门介绍，后续可以结合实际项目深入探讨各个组件的高级用法。
