# MCP 基础概念

## 目录

1. [简介](#简介)
2. [核心概念](#核心概念)
3. [工作原理](#工作原理)
4. [通信机制](#通信机制)
5. [使用场景](#使用场景)
6. [简单示例](#简单示例)
7. [参考资源](#参考资源)

## 简介

MCP（Model Context Protocol，模型上下文协议）是由 Anthropic 提出的一种开放协议，用于在 AI 模型与外部工具、数据源之间建立标准化连接。

简单来说，MCP 让 Claude 等 AI 模型能够像访问 USB 设备一样，统一地调用外部服务。

## 核心概念

| 概念 | 说明 |
|------|------|
| **MCP Client** | 使用 MCP 协议的客户端，例如 Claude Code、Claude Desktop 等 |
| **MCP Server** | 提供具体功能的服务端，例如文件系统、数据库、GitHub、Slack 等 |
| **Tools** | 工具，模型可以调用的函数或能力 |
| **Resources** | 资源，模型可以读取的上下文数据 |
| **Prompts** | 提示模板，预定义的可复用任务模板 |

## 工作原理

```
┌──────────────┐         MCP 协议          ┌──────────────┐
│  MCP Client  │  <--------------------->  │  MCP Server  │
│  (Claude)    │    JSON-RPC / stdio / SSE │  (工具/数据)  │
└──────────────┘                           └──────────────┘
```

基本流程：

1. MCP Client 启动时连接到已配置的 MCP Server。
2. 模型根据用户请求判断是否需要调用外部工具。
3. 通过 MCP 协议发送调用请求给 Server。
4. Server 执行操作并返回结果。
5. 模型将结果整合进回答中。

## 通信机制

MCP Client 与 MCP Server 之间通过标准化的传输层和消息格式进行通信。

### 传输方式

| 传输方式 | 说明 | 适用场景 |
|----------|------|----------|
| **stdio** | 标准输入输出，Client 作为父进程启动 Server 子进程 | 本地工具，如文件系统、Shell 命令 |
| **SSE** | Server-Sent Events，基于 HTTP 的服务端推送 | 远程服务，需要服务器主动推送 |
| **HTTP** | 基于 HTTP 的请求响应 | Web 服务、REST API 封装 |

### 消息格式

MCP 使用 **JSON-RPC 2.0** 作为消息格式，主要包含以下几类消息：

| 消息类型 | 说明 |
|----------|------|
| **Request** | 客户端发送的请求，要求服务端执行某个操作 |
| **Response** | 服务端对请求返回的结果 |
| **Notification** | 单向通知，不需要回复 |
| **Error** | 请求失败时返回的错误信息 |

### 通信生命周期

```
Client                      Server
  |                            |
  |---- initialize ----------->|   初始化连接、交换能力
  |<--- initializeResult ------|
  |                            |
  |---- tools/list ----------->|   发现可用工具
  |<--- tools/listResult ------|
  |                            |
  |---- tools/call ----------->|   调用工具
  |<--- tools/callResult ------|
  |                            |
  |---- shutdown ------------->|   关闭连接
```

### 能力协商

连接建立时，Client 和 Server 会交换各自支持的能力（capabilities），例如：

- `tools`：是否支持工具调用
- `resources`：是否支持资源读取
- `prompts`：是否支持提示模板
- `logging`：是否支持日志上报

只有双方都声明支持的能力，才能在后续通信中使用。

- **文件操作**：读取、搜索、编辑本地文件
- **数据库查询**：连接数据库执行 SQL
- **代码仓库**：与 Git、GitHub 交互
- **项目管理**：读写 Notion、Trello、Jira 等
- **浏览器/搜索**：获取实时网络信息

## 简单示例

一个 MCP Server 可能提供一个 `read_file` 工具：

```json
{
  "name": "read_file",
  "description": "读取指定文件内容",
  "parameters": {
    "path": {
      "type": "string",
      "description": "文件路径"
    }
  }
}
```

Claude 在需要时即可调用该工具读取文件，而无需用户手动复制粘贴。

## 参考资源

- [MCP 官方文档](https://modelcontextprotocol.io/)
- [MCP GitHub 仓库](https://github.com/modelcontextprotocol)
