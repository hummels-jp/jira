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

## 7. LangChain 生态

- **LangChain**：核心框架，提供模型、提示、链、代理等基础能力。
- **LangGraph**：用于构建复杂、有状态的多代理应用。
- **LangServe**：将 LangChain 应用部署为 REST API。
- **LangSmith**：用于监控、调试和评估 LLM 应用的平台。

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
