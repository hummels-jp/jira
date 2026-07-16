# 敏捷软件项目管理面试常见问题与解答（50题）

> 面试准备文档 —— Agile / Scrum / Kanban / 用户故事 / 估算 / 度量 / 规模化敏捷

**语言导航：** [中] | [[日]](04_agile_modle_ja.md) | [[英]](04_agile_modle_en.md)

---

## 目录

- [一、敏捷基础与思想（Q1–Q10）](#sec1)
- [二、Scrum 框架（Q11–Q22）](#sec2)
- [三、Kanban 与看板方法（Q23–Q28）](#sec3)
- [四、用户故事与需求管理（Q29–Q34）](#sec4)
- [五、敏捷估算与计划（Q35–Q40）](#sec5)
- [六、敏捷度量与持续改进（Q41–Q45）](#sec6)
- [七、规模化敏捷与工程实践（Q46–Q50）](#sec7)

---

<a id="sec1"></a>

## 一、敏捷基础与思想

<a id="q1"></a>
1. **问：什么是敏捷（Agile）？它的核心思想是什么？**
   [中](#q1) | [[日]](04_agile_modle_ja.md#q1) | [[英]](04_agile_modle_en.md#q1)

   **答：** 敏捷是一种以**迭代增量交付、快速反馈、拥抱变化**为核心的软件开发理念。它强调小批量、短周期地交付可工作的软件，通过持续与客户协作和团队自组织来应对不确定性。敏捷不是具体方法，而是一组价值观和原则，Scrum、Kanban、XP 等都是其具体实践。

<a id="q2"></a>
2. **问：请说出《敏捷宣言》的 4 个价值观。**
   [中](#q2) | [[日]](04_agile_modle_ja.md#q2) | [[英]](04_agile_modle_en.md#q2)

   **答：** 敏捷宣言（Agile Manifesto，2001）提出四对价值观（左项优于右项）：
   1. **个体和互动** 高于 流程和工具
   2. **可工作的软件** 高于 详尽的文档
   3. **客户合作** 高于 合同谈判
   4. **响应变化** 高于 遵循计划

   右项仍有价值，但左项更被重视。

<a id="q3"></a>
3. **问：敏捷宣言的 12 条原则你了解哪些关键点？**
   [中](#q3) | [[日]](04_agile_modle_ja.md#q3) | [[英]](04_agile_modle_en.md#q3)

   **答：** 关键点包括：**尽早持续交付价值**、**欢迎变化**（即使在开发后期）、**频繁交付可工作软件**（几周到几个月）、**业务与开发每日协作**、**信任并激励团队**、**面对面沟通最有效**、**可工作软件是主要进度度量**、**可持续开发节奏**、**技术卓越与良好设计**、**简洁**（不做的艺术）、**自组织团队**、**定期反思与调整**。

<a id="q4"></a>
4. **问：敏捷与瀑布模型的核心区别是什么？**
   [中](#q4) | [[日]](04_agile_modle_ja.md#q4) | [[英]](04_agile_modle_en.md#q4)

   **答：** 瀑布是**顺序、阶段门、大批量**（需求→设计→开发→测试→上线），前期锁定需求；敏捷是**迭代、增量、小批量**，允许需求持续演进。瀑布适合需求明确、变更成本高的项目（航天、建筑）；敏捷适合需求不确定、快速演化的软件产品。核心差别是**变更的成本假设**：瀑布假设变更代价高故前期锁死；敏捷假设变更不可避免故降低单次变更成本。

<a id="q5"></a>
5. **问：什么是迭代（Iteration）和增量（Increment）？**
   [中](#q5) | [[日]](04_agile_modle_ja.md#q5) | [[英]](04_agile_modle_en.md#q5)

   **答：** **迭代**指在固定的短时间（1–4 周）内完成"规划→开发→测试→评审"的完整周期；**增量**指每次迭代产出的可工作、可交付的软件功能片段。多次迭代累积形成完整产品。迭代是**过程**，增量是**产物**。经典比喻：画蒙娜丽莎，瀑布是从左上开始逐格画到右下；敏捷是先画整幅草图，再逐轮加细节。

<a id="q6"></a>
6. **问：常见的敏捷方法/框架有哪些？**
   [中](#q6) | [[日]](04_agile_modle_ja.md#q6) | [[英]](04_agile_modle_en.md#q6)

   **答：** 主流敏捷方法包括：
   - **Scrum**：最流行的团队级敏捷框架，基于 Sprint 迭代
   - **Kanban**：基于看板和 WIP 限制的流式方法
   - **XP（Extreme Programming）**：强调工程实践（TDD、结对编程、持续集成）
   - **Lean**：源自丰田生产系统，消除浪费
   - **Crystal**、**FDD（特性驱动开发）**、**DSDM**
   - 规模化：**SAFe**、**LeSS**、**Nexus**、**Scrum@Scale**

<a id="q7"></a>
7. **问：敏捷适用于所有类型的项目吗？**
   [中](#q7) | [[日]](04_agile_modle_ja.md#q7) | [[英]](04_agile_modle_en.md#q7)

   **答：** 不是。敏捷最适合**需求不确定、技术复杂、需要快速反馈**的场景（如互联网产品、创新研发）。不太适合的场景：需求完全明确且不变（生产线复制）、安全关键系统（航天医疗需严格文档）、强合同约束的固定价项目、无法与客户频繁互动的场景。可以用**混合型（Hybrid）**：整体瀑布 + 局部敏捷。

<a id="q8"></a>
8. **问：什么是 Definition of Ready（DoR）和 Definition of Done（DoD）？**
   [中](#q8) | [[日]](04_agile_modle_ja.md#q8) | [[英]](04_agile_modle_en.md#q8)

   **答：**
   - **DoR（就绪定义）**：一个 User Story 进入 Sprint 前必须满足的条件（需求清晰、验收标准明确、依赖已解决、可估算等）。
   - **DoD（完成定义）**：一个 Story/Increment 被认为"完成"的标准（代码写完、单元测试通过、代码评审、集成测试通过、部署到测试环境、文档更新等）。

   两者是团队共同商定的**质量契约**，避免"完成了 90%"的模糊表述。

<a id="q9"></a>
9. **问：什么是最小可行产品（MVP）？**
   [中](#q9) | [[日]](04_agile_modle_ja.md#q9) | [[英]](04_agile_modle_en.md#q9)

   **答：** MVP（Minimum Viable Product）是**能验证核心价值假设的最简版本产品**。它不是功能残缺的产品，而是**聚焦最小功能集**用于快速上线并从真实用户获取反馈，以最小成本降低最大风险。MVP 之后再迭代扩展。经典例子：Dropbox 用一段演示视频验证需求，Zappos 创始人手动跑腿采购验证在线卖鞋模式。

<a id="q10"></a>
10. **问：什么是"敏捷心态（Agile Mindset）"？**
   [中](#q10) | [[日]](04_agile_modle_ja.md#q10) | [[英]](04_agile_modle_en.md#q10)

   **答：** 敏捷心态强调**成长思维、拥抱不确定性、以客户价值为中心、持续学习与实验、心理安全、失败即学习**。真正的敏捷转型不是"实施 Scrum"，而是组织文化和思维方式的转变——从命令控制到赋能协作，从计划驱动到价值驱动。没有敏捷心态，任何框架都会退化为"僵尸 Scrum（Zombie Scrum）"。

---

<a id="sec2"></a>

## 二、Scrum 框架

<a id="q11"></a>
11. **问：什么是 Scrum？它的三大支柱是什么？**
   [中](#q11) | [[日]](04_agile_modle_ja.md#q11) | [[英]](04_agile_modle_en.md#q11)

   **答：** Scrum 是最流行的敏捷框架，基于**经验主义（Empiricism）**——通过观察和实验做决策。三大支柱：
   1. **透明（Transparency）**：所有信息对相关方可见
   2. **检视（Inspection）**：定期检查产物和进展
   3. **适应（Adaptation）**：根据检视结果调整

   Scrum 通过 3 个角色、5 个事件、3 个工件形成闭环。

<a id="q12"></a>
12. **问：Scrum 有哪三个角色？各自职责是什么？**
   [中](#q12) | [[日]](04_agile_modle_ja.md#q12) | [[英]](04_agile_modle_en.md#q12)

   **答：**
   - **Product Owner（PO，产品负责人）**：对产品价值负责，管理和排序 Product Backlog，做"做什么/不做什么"的决策。
   - **Scrum Master（SM）**：仆人式领导，负责推行 Scrum、扫除障碍、辅导团队，不是项目经理也不是团队长。
   - **Developers（开发团队）**：3–9 人跨职能团队，负责交付增量，自组织决定"如何做"。

   Scrum Team 是这三者的整体，共同对产品负责。

<a id="q13"></a>
13. **问：Scrum 的 5 个事件（会议）是什么？**
   [中](#q13) | [[日]](04_agile_modle_ja.md#q13) | [[英]](04_agile_modle_en.md#q13)

   **答：**
   1. **Sprint**：整个迭代（1–4 周），是其他所有事件的容器
   2. **Sprint Planning（迭代计划会）**：Sprint 开始，制定 Sprint Goal 和 Sprint Backlog（时长 ≤ 8h/月）
   3. **Daily Scrum（每日站会）**：15 分钟，同步进展与障碍
   4. **Sprint Review（迭代评审）**：Sprint 结束，向干系人演示增量，收集反馈（≤ 4h/月）
   5. **Sprint Retrospective（回顾会）**：团队反思过程改进（≤ 3h/月）

<a id="q14"></a>
14. **问：Scrum 的 3 个工件（Artifacts）是什么？**
   [中](#q14) | [[日]](04_agile_modle_ja.md#q14) | [[英]](04_agile_modle_en.md#q14)

   **答：**
   1. **Product Backlog**：产品级需求清单，PO 管理，动态排序
   2. **Sprint Backlog**：本次 Sprint 承诺完成的 Backlog 子集 + 交付计划
   3. **Increment（增量）**：Sprint 结束时可交付的产品成果

   每个工件都有对应的**承诺（Commitment）**（Scrum Guide 2020 新增）：
   - Product Backlog → **Product Goal**
   - Sprint Backlog → **Sprint Goal**
   - Increment → **Definition of Done**

<a id="q15"></a>
15. **问：Sprint 长度一般多久？为什么固定？**
   [中](#q15) | [[日]](04_agile_modle_ja.md#q15) | [[英]](04_agile_modle_en.md#q15)

   **答：** 通常 **1–4 周**，最常见 2 周。Sprint 长度**在一个产品中应保持固定**，因为：
   - 稳定的节奏便于团队养成习惯，降低协调成本
   - 便于对比 velocity 做趋势分析
   - 让干系人形成可预期的反馈节奏

   Sprint 一旦开始不能延长；如果目标已明显不可能达成，PO 可以**中止 Sprint（Sprint Cancellation）**，但这是极少见的最后手段。

<a id="q16"></a>
16. **问：Sprint Planning 会议做什么？输出什么？**
   [中](#q16) | [[日]](04_agile_modle_ja.md#q16) | [[英]](04_agile_modle_en.md#q16)

   **答：** Sprint Planning 回答三个问题：
   - **Why**：本 Sprint 想创造什么价值？→ **Sprint Goal**
   - **What**：能完成哪些 Backlog Item？→ 挑选 Story 进入 Sprint Backlog
   - **How**：如何交付？→ 拆分为任务、初步设计

   输出：**Sprint Goal + Sprint Backlog**。整个 Scrum Team 参与，PO 澄清优先级和需求，Developers 决定承诺量。

<a id="q17"></a>
17. **问：Daily Scrum（每日站会）的目的和常见误区？**
   [中](#q17) | [[日]](04_agile_modle_ja.md#q17) | [[英]](04_agile_modle_en.md#q17)

   **答：** **目的**：Developers 每天 15 分钟同步进展、发现障碍、调整当日计划以推进 Sprint Goal。**不是**向 SM 或经理汇报。经典三问（可选）：昨天做了什么？今天做什么？有什么障碍？

   **常见误区**：
   - 变成状态汇报会（对着 SM 说而非对同伴说）
   - 深入技术讨论（应会后单独讨论）
   - 站会超时（严格控制 15 分钟）
   - PO/经理点名审问，破坏心理安全

<a id="q18"></a>
18. **问：Sprint Review 和 Sprint Retrospective 的区别？**
   [中](#q18) | [[日]](04_agile_modle_ja.md#q18) | [[英]](04_agile_modle_en.md#q18)

   **答：**
   | 维度 | Sprint Review | Sprint Retrospective |
   |------|---------------|----------------------|
   | 焦点 | **产品**：增量+反馈 | **过程**：团队协作与改进 |
   | 参与者 | Scrum Team + 干系人 | 仅 Scrum Team |
   | 输出 | 更新的 Product Backlog | 具体的改进行动项 |
   | 关键词 | Demo、反馈、方向调整 | 反思、心理安全、持续改进 |

   一句话：**Review 谈"做了什么"，Retro 谈"怎么做得更好"**。

<a id="q19"></a>
19. **问：Scrum Master 和 Project Manager 有何区别？**
   [中](#q19) | [[日]](04_agile_modle_ja.md#q19) | [[英]](04_agile_modle_en.md#q19)

   **答：**
   | 维度 | Scrum Master | Project Manager |
   |------|--------------|-----------------|
   | 定位 | 仆人式领导、教练 | 命令控制、负责人 |
   | 权限 | 无正式管理权 | 有资源分配和决策权 |
   | 关注 | 过程有效性、团队赋能 | 范围/进度/成本三角 |
   | 对象 | 一个 Scrum Team | 整个项目干系人 |
   | 度量 | 团队健康、交付能力 | 计划完成度、KPI |

   Scrum Master 不安排任务、不催进度、不评估绩效。

<a id="q20"></a>
20. **问：Product Owner 最重要的能力是什么？**
   [中](#q20) | [[日]](04_agile_modle_ja.md#q20) | [[英]](04_agile_modle_en.md#q20)

   **答：** 核心能力：
   1. **价值判断**：识别什么最能创造用户/业务价值
   2. **优先级决策**：能对 Backlog 强排序（不能"都是最高"）
   3. **需求表达**：写清楚的 User Story 和验收标准
   4. **利益相关方管理**：与业务、用户、开发多方对齐
   5. **说"不"的勇气**：拒绝低价值需求以聚焦

   一个失败的 PO 常见于：兼职、无决策权、把 Backlog 变成待办清单堆积。

<a id="q21"></a>
21. **问：什么是 Product Backlog Refinement（Backlog 梳理）？**
   [中](#q21) | [[日]](04_agile_modle_ja.md#q21) | [[英]](04_agile_modle_en.md#q21)

   **答：** Backlog Refinement（又称 Grooming）是**持续进行**的活动（不是正式 Scrum 事件），由 PO 主导、全团队参与，目的是让 Backlog 保持**DEEP** 状态：
   - **D**etailed appropriately：近期项目细致，远期项目粗略
   - **E**stimated：估算过
   - **E**mergent：持续演进
   - **P**rioritized：已排序

   通常每 Sprint 花 5–10% 时间做 Refinement，包括拆分大 Story、补充验收标准、估算、排序。

<a id="q22"></a>
22. **问：Sprint 中途可以增加新需求吗？**
   [中](#q22) | [[日]](04_agile_modle_ja.md#q22) | [[英]](04_agile_modle_en.md#q22)

   **答：** **原则上不可以**。Sprint Goal 一旦确定，Sprint Backlog 内容对开发团队是"保护"的。中途插入需求会破坏节奏、损害承诺。**处理方式**：
   - 紧急且必须做 → PO 与团队协商换出等价工作量的 Story
   - 不紧急 → 加入 Product Backlog，下 Sprint 再考虑
   - 频繁插入 → 说明 PO 计划不到位或 Sprint 过长，需回顾改进

   例外：Sprint Goal 已明显失效，PO 可**中止 Sprint** 重新规划。

---

<a id="sec3"></a>

## 三、Kanban 与看板方法

<a id="q23"></a>
23. **问：什么是 Kanban？它与 Scrum 有何区别？**
   [中](#q23) | [[日]](04_agile_modle_ja.md#q23) | [[英]](04_agile_modle_en.md#q23)

   **答：** Kanban（看板）源自丰田生产系统，是一种**基于流的可视化拉动方法**。它不规定角色、事件或迭代，只要求：**可视化工作流、限制 WIP、管理流动、显式规则、反馈循环、协作改进**。

   | 维度 | Scrum | Kanban |
   |------|-------|--------|
   | 节奏 | 固定 Sprint | 连续流 |
   | 角色 | PO/SM/Dev | 无规定 |
   | 变更 | Sprint 中锁定 | 随时可调整 |
   | 度量 | Velocity | Lead Time / Throughput |
   | 适用 | 产品开发 | 运维、支持、任务多样 |

<a id="q24"></a>
24. **问：Kanban 的六大核心实践是什么？**
   [中](#q24) | [[日]](04_agile_modle_ja.md#q24) | [[英]](04_agile_modle_en.md#q24)

   **答：**
   1. **可视化工作流**（看板墙、卡片、泳道）
   2. **限制在制品（WIP Limit）**——最重要的实践
   3. **管理流动**（关注 Lead Time、瓶颈）
   4. **显式规则**（Definition of Ready/Done、优先级策略）
   5. **反馈循环**（每日站会、补充会议、交付会议）
   6. **协作改进、实验演化**（Kaizen）

<a id="q25"></a>
25. **问：什么是 WIP（Work In Progress）限制？为什么重要？**
   [中](#q25) | [[日]](04_agile_modle_ja.md#q25) | [[英]](04_agile_modle_en.md#q25)

   **答：** WIP 限制是**每个工作状态列同时进行的任务数上限**。设定 WIP 限制的作用：
   - **暴露瓶颈**：当某列达到上限，上游只能停下，问题显性化
   - **减少上下文切换**：多任务并行让每项都变慢
   - **加快交付**：根据**Little's Law**：`Lead Time = WIP / Throughput`，减少 WIP 直接缩短交付时间
   - **提升质量**：专注度提高

   经验：初始 WIP 设为团队人数的 1–1.5 倍，然后逐步降低。

<a id="q26"></a>
26. **问：什么是 Cumulative Flow Diagram（CFD，累积流图）？**
   [中](#q26) | [[日]](04_agile_modle_ja.md#q26) | [[英]](04_agile_modle_en.md#q26)

   **答：** CFD 是 Kanban 核心可视化工具，横轴时间，纵轴累积任务数，每种状态用不同颜色堆叠。可读出：
   - **WIP**：任意时刻某状态的垂直厚度
   - **Lead Time**：某任务从进入到完成的水平距离
   - **Throughput**：完成曲线的斜率
   - **瓶颈**：某色带持续变厚 = 该状态积压

   健康的 CFD 各色带平行上升；某色带鼓包说明有瓶颈或阻塞。

<a id="q27"></a>
27. **问：Lead Time、Cycle Time、Throughput 分别是什么？**
   [中](#q27) | [[日]](04_agile_modle_ja.md#q27) | [[英]](04_agile_modle_en.md#q27)

   **答：**
   - **Lead Time（前置时间）**：从**客户请求**到**交付完成**的总时间，客户视角
   - **Cycle Time（周期时间）**：从**开始工作**到**完成**的时间，团队视角（Lead Time 的子集）
   - **Throughput（吞吐率）**：单位时间完成的任务数（如 5 stories/week）

   经典类比：Lead Time = 从下单到收到披萨；Cycle Time = 从开始做披萨到出炉；Throughput = 每小时出几个披萨。

<a id="q28"></a>
28. **问：什么是 Scrumban？**
   [中](#q28) | [[日]](04_agile_modle_ja.md#q28) | [[英]](04_agile_modle_en.md#q28)

   **答：** Scrumban 是 **Scrum + Kanban 的混合方法**：保留 Scrum 的角色、Sprint 节奏、评审回顾，同时引入 Kanban 的可视化和 WIP 限制。常用于：
   - Scrum 团队想改善流动效率
   - 从 Scrum 过渡到 Kanban 或反之
   - 兼有产品开发和运维支持的团队

   典型做法：保留 2 周迭代做规划节奏，但看板上加 WIP 限制，允许紧急插入通过换出机制处理。

---

<a id="sec4"></a>

## 四、用户故事与需求管理

<a id="q29"></a>
29. **问：什么是用户故事（User Story）？标准格式是什么？**
   [中](#q29) | [[日]](04_agile_modle_ja.md#q29) | [[英]](04_agile_modle_en.md#q29)

   **答：** User Story 是**从用户视角**描述功能的简短需求表达。经典模板：

   > **作为**〈某类用户〉，**我想要**〈某个功能〉，**以便**〈获得某种价值〉。
   > As a 〈role〉, I want 〈feature〉, so that 〈benefit〉.

   例：作为在线购物者，我想保存商品到收藏夹，以便下次快速下单。

   User Story 不是详尽需求文档，而是**对话的起点**——细节在讨论中补充。

<a id="q30"></a>
30. **问：INVEST 原则是什么？**
   [中](#q30) | [[日]](04_agile_modle_ja.md#q30) | [[英]](04_agile_modle_en.md#q30)

   **答：** INVEST 是评估 User Story 好坏的 6 个标准：
   - **I**ndependent：独立（尽量减少故事间依赖）
   - **N**egotiable：可协商（细节可讨论调整）
   - **V**aluable：有价值（对用户或业务有意义）
   - **E**stimable：可估算（信息足够估工作量）
   - **S**mall：足够小（能在一个 Sprint 内完成）
   - **T**estable：可测试（有明确验收标准）

<a id="q31"></a>
31. **问：User Story 的 3C 是什么？**
   [中](#q31) | [[日]](04_agile_modle_ja.md#q31) | [[英]](04_agile_modle_en.md#q31)

   **答：** 3C 是 Ron Jeffries 提出的 User Story 三要素：
   1. **Card（卡片）**：Story 的简短书面描述（可写在物理/电子卡片上）
   2. **Conversation（对话）**：团队与 PO、用户就细节的持续讨论
   3. **Confirmation（确认）**：验收标准（Acceptance Criteria），用于验证 Story 完成

   核心思想：**卡片是承诺开对话的凭证，不是需求全文**。

<a id="q32"></a>
32. **问：Epic、Feature、User Story、Task 的层级关系？**
   [中](#q32) | [[日]](04_agile_modle_ja.md#q32) | [[英]](04_agile_modle_en.md#q32)

   **答：** 从大到小的需求粒度层级：
   - **Epic（史诗）**：跨多个 Sprint 甚至几个季度的大功能块，如"用户账户体系"
   - **Feature（特性）**：Epic 的子集，如"密码找回"
   - **User Story（用户故事）**：一个 Sprint 内可完成的最小价值单元，如"通过邮箱找回密码"
   - **Task（任务）**：Story 的技术分解，如"实现邮件发送 API"、"写单元测试"

   Task 是团队内部工作，通常不对 PO 可见；PO 主要管理到 Story 层。

<a id="q33"></a>
33. **问：什么是验收标准（Acceptance Criteria）？常见格式？**
   [中](#q33) | [[日]](04_agile_modle_ja.md#q33) | [[英]](04_agile_modle_en.md#q33)

   **答：** 验收标准描述 **Story 何时算完成**的具体、可验证的条件，由 PO 与团队共同定义。常见格式：

   **1. 清单式：**
   ```
   - 输入正确邮箱能收到重置邮件
   - 邮件链接 24 小时内有效
   - 无效邮箱返回明确错误提示
   ```

   **2. Gherkin BDD 格式（Given-When-Then）：**
   ```
   Given 用户已注册
   When 用户在登录页点击"忘记密码"并输入注册邮箱
   Then 系统在 1 分钟内发送重置邮件到该邮箱
   ```

<a id="q34"></a>
34. **问：如何拆分大的 User Story？**
   [中](#q34) | [[日]](04_agile_modle_ja.md#q34) | [[英]](04_agile_modle_en.md#q34)

   **答：** 常用拆分技巧（SPIDR 或类似模式）：
   1. **按工作流步骤**：注册流程拆为"填表单/验证/激活邮箱"
   2. **按数据变体**：先支持信用卡→再支付宝→再微信
   3. **按业务规则**：先处理主流场景→再处理异常
   4. **按接口/端点**：先做 Web→再 iOS→再 Android
   5. **按验收标准**：一个 Story 有 10 个 AC→拆成多个各 2–3 个
   6. **CRUD 拆分**：先"创建"上线→再补"编辑/删除"
   7. **性能/质量属性**：先功能可用→再优化到 <200ms

   目标：每个 Story 能在 **一个 Sprint 内、几人天内完成**。

---

<a id="sec5"></a>

## 五、敏捷估算与计划

<a id="q35"></a>
35. **问：什么是故事点（Story Point）？为什么不用工时？**
   [中](#q35) | [[日]](04_agile_modle_ja.md#q35) | [[英]](04_agile_modle_en.md#q35)

   **答：** Story Point 是**相对估算单位**，综合考虑**复杂度、工作量、不确定性**三个维度。使用它而非工时的原因：
   - 人对**相对大小**的判断远比**绝对时间**准确
   - 避开个体差异（同一任务不同人耗时不同）
   - 摆脱"承诺=工时"的政治压力
   - 团队级度量（Velocity）比个人工时更稳定

   常用 **斐波那契数列**（1, 2, 3, 5, 8, 13, 21, ...），因为间距扩大反映了大 Story 的估算不确定性。

<a id="q36"></a>
36. **问：什么是计划扑克（Planning Poker）？**
   [中](#q36) | [[日]](04_agile_modle_ja.md#q36) | [[英]](04_agile_modle_en.md#q36)

   **答：** Planning Poker 是团队协作估算技巧：
   1. PO 简述 Story
   2. 团队讨论澄清
   3. 每人**同时亮牌**（斐波那契数字）
   4. 差异大的（如 3 和 13）→ 最高和最低者解释思路
   5. 讨论后再次投票，直至收敛

   优势：**避免锚定效应**（若逐个发言，后来者会被前者影响）、集思广益暴露隐藏风险和知识差。

<a id="q37"></a>
37. **问：什么是 Velocity（速率）？如何使用？**
   [中](#q37) | [[日]](04_agile_modle_ja.md#q37) | [[英]](04_agile_modle_en.md#q37)

   **答：** Velocity 是团队**每个 Sprint 平均完成的故事点数**。用途：
   - **预测**：Backlog 剩余 100 点，Velocity=20，则需 5 个 Sprint
   - **计划**：新 Sprint 承诺量参考近 3 次平均 Velocity
   - **改进反馈**：Velocity 趋势反映团队成熟度

   **注意事项**：
   - Velocity **不是** KPI，不能跨团队比较（估算单位不同）
   - 不能用它评估个人绩效（会诱发膨胀估算）
   - 新组建团队 Velocity 前 3 Sprint 波动大，属正常

<a id="q38"></a>
38. **问：什么是发布计划（Release Planning）？**
   [中](#q38) | [[日]](04_agile_modle_ja.md#q38) | [[英]](04_agile_modle_en.md#q38)

   **答：** Release Planning 是**跨多个 Sprint 的中期规划**，回答"何时能发布哪些功能"。步骤：
   1. 确定 Release Goal 和目标日期
   2. 梳理 Backlog，识别属于本 Release 的 Story
   3. 估算总故事点 P
   4. 基于 Velocity V 估算 Sprint 数：`N = P / V`
   5. 制定初步 Sprint 分配和里程碑
   6. **持续更新**：每 Sprint 后根据实际调整

   关键理念：**范围、时间、资源三选二**——敏捷通常固定时间和资源，让范围灵活。

<a id="q39"></a>
39. **问：什么是燃尽图（Burndown Chart）和燃起图（Burnup Chart）？**
   [中](#q39) | [[日]](04_agile_modle_ja.md#q39) | [[英]](04_agile_modle_en.md#q39)

   **答：**
   - **Burndown（燃尽图）**：Y 轴剩余工作量，从上到下"燃尽"到 0，直观显示进度
   - **Burnup（燃起图）**：Y 轴累积完成量向上增长，同时画出"总范围线"

   **Burnup 的优势**：能显示**范围变化**——若总范围线上升说明中途加了需求，而 Burndown 会误以为团队没进展。因此 Burnup 更适合发布级别的跟踪。

<a id="q40"></a>
40. **问：如何应对承诺过多完不成的问题？**
   [中](#q40) | [[日]](04_agile_modle_ja.md#q40) | [[英]](04_agile_modle_en.md#q40)

   **答：** 应对策略：
   - **参考历史 Velocity** 而非乐观估计
   - **留出 buffer**：不要 100% 塞满，预留 10–20% 应对突发
   - **按优先级排序**：即使完不成，最高价值的 Story 已交付
   - **拆细 Story**：小 Story 更易预测和完成
   - **回顾根因**：估算不准？外部依赖？技术债？
   - **文化建设**：承诺不达标不惩罚，鼓励诚实估算
   - **Sprint Review 中如实展示**，不掩盖未完成项

---

<a id="sec6"></a>

## 六、敏捷度量与持续改进

<a id="q41"></a>
41. **问：敏捷项目常用的度量指标有哪些？**
   [中](#q41) | [[日]](04_agile_modle_ja.md#q41) | [[英]](04_agile_modle_en.md#q41)

   **答：** 分四大类：
   - **交付效率**：Velocity、Throughput、Lead Time、Cycle Time
   - **质量**：缺陷密度、缺陷逃逸率、代码覆盖率、生产事故数
   - **价值/结果**：NPS、用户激活率、业务 KPI、Feature 使用率
   - **团队健康**：Sprint Goal 达成率、Retrospective 行动完成率、团队幸福度

   **原则**：**度量结果而非产出**（Outcomes over Outputs）。功能上线不等于价值实现。

<a id="q42"></a>
42. **问：什么是 DORA 四大关键指标？**
   [中](#q42) | [[日]](04_agile_modle_ja.md#q42) | [[英]](04_agile_modle_en.md#q42)

   **答：** DORA（DevOps Research and Assessment）研究提出的 4 个 DevOps 高绩效指标：
   1. **Deployment Frequency（部署频率）**：多久部署一次生产
   2. **Lead Time for Changes（变更前置时间）**：代码提交到上线的时间
   3. **Change Failure Rate（变更失败率）**：上线后需回滚/热修的比例
   4. **Mean Time to Restore（MTTR，平均恢复时间）**：故障后多久恢复

   精英团队标准（Google 报告）：日多次部署、<1 天上线、<15% 失败率、<1 小时恢复。

<a id="q43"></a>
43. **问：Sprint Retrospective 如何做才有效？**
   [中](#q43) | [[日]](04_agile_modle_ja.md#q43) | [[英]](04_agile_modle_en.md#q43)

   **答：** 有效 Retro 的关键：
   - **心理安全**：无指责氛围（Norm Kerth's Prime Directive）
   - **多样格式防僵化**：Start/Stop/Continue、4Ls（Liked/Learned/Lacked/Longed for）、Sailboat、Mad-Sad-Glad
   - **聚焦少数可行动项**：与其列 10 条，不如挑 1–2 条切实改进
   - **跟踪上次行动**：下次 Retro 开始先复盘上次的改进是否落地
   - **数据驱动**：结合度量指标而非纯感受
   - **定期换主持人**：避免仪式化

   核心是**持续改进的文化**，而非会议本身。

<a id="q44"></a>
44. **问：什么是"僵尸敏捷（Zombie Scrum）"？如何识别？**
   [中](#q44) | [[日]](04_agile_modle_ja.md#q44) | [[英]](04_agile_modle_en.md#q44)

   **答：** Zombie Scrum 指**形式上做 Scrum，实质失去敏捷本质**的状态。典型症状：
   - 有 Sprint 但每次都在延期或砍范围
   - Retro 提出的问题从未解决
   - Daily 只是对经理汇报
   - Sprint 结束没有可用增量
   - PO 只是需求传声筒无决策权
   - 团队士气低、缺乏心理安全
   - 从来不与真实用户交互

   治疗：回到敏捷价值观和原则，聚焦"交付真实价值"，重建心理安全和实验文化。

<a id="q45"></a>
45. **问：什么是技术债（Technical Debt）？如何管理？**
   [中](#q45) | [[日]](04_agile_modle_ja.md#q45) | [[英]](04_agile_modle_en.md#q45)

   **答：** Ward Cunningham 提出的比喻：为快速交付而做的**次优技术决策**，会随时间累积"利息"（维护成本、变更困难）。分类：
   - **有意 vs 无意**、**审慎 vs 鲁莽**（Martin Fowler 四象限）

   **管理策略**：
   - **可视化**：在 Backlog 中作为专项条目
   - **定期偿还**：每 Sprint 分配 15–20% 容量给重构/技术改进
   - **量化影响**：用生产事故、开发速度下降说服业务方
   - **DoD 加入质量门槛**：新代码不引入新债
   - **Boy Scout Rule**：每次改代码都留下比之前更干净的版本

---

<a id="sec7"></a>

## 七、规模化敏捷与工程实践

<a id="q46"></a>
46. **问：常见的规模化敏捷框架有哪些？各自特点？**
   [中](#q46) | [[日]](04_agile_modle_ja.md#q46) | [[英]](04_agile_modle_en.md#q46)

   **答：**
   - **SAFe（Scaled Agile Framework）**：最完整最重的框架，含 Portfolio/Program/Team 三层，引入 ART（Agile Release Train）、PI Planning、SPC 认证。适合大型企业。
   - **LeSS（Large-Scale Scrum）**：Scrum 的极简放大，一个 PO 一份 Backlog 管多个团队（2–8 个），强调组织层面的敏捷。
   - **Nexus**：Scrum.org 出品，3–9 个 Scrum 团队协作，引入 Nexus Integration Team 处理集成。
   - **Scrum@Scale**：Jeff Sutherland 提出，"Scrum of Scrums"递归扩展。
   - **Spotify Model**：Squad/Tribe/Chapter/Guild 组织结构，重视文化而非框架。

<a id="q47"></a>
47. **问：什么是 SAFe 中的 PI Planning？**
   [中](#q47) | [[日]](04_agile_modle_ja.md#q47) | [[英]](04_agile_modle_en.md#q47)

   **答：** PI（Program Increment）Planning 是 SAFe 的核心活动，通常**8–12 周一次、2 天**，一个 ART（50–125 人）全体参与。目的：
   - 对齐业务目标与团队计划
   - 识别跨团队依赖
   - 承诺 PI Objectives 并评估信心度（1–5 分投票）
   - 生成 Program Board 可视化依赖和里程碑

   PI Planning 是 SAFe 组织节奏的心跳，一次成本高但显著提升跨团队协同。

<a id="q48"></a>
48. **问：什么是持续集成（CI）、持续交付（CD）、持续部署？**
   [中](#q48) | [[日]](04_agile_modle_ja.md#q48) | [[英]](04_agile_modle_en.md#q48)

   **答：**
   - **CI（Continuous Integration）**：开发者频繁（每天多次）合入主干，每次合入触发自动构建和测试
   - **CD（Continuous Delivery）**：在 CI 基础上，随时**可以**一键部署到生产（手动触发上线）
   - **Continuous Deployment（持续部署）**：更进一步，通过测试后**自动**部署到生产

   关系：**CI ⊂ CD ⊂ Continuous Deployment**。Netflix、Facebook 一天可上线数百次，靠的是完整的 Continuous Deployment 流水线 + 强测试自动化 + 灰度发布。

<a id="q49"></a>
49. **问：XP（极限编程）的核心工程实践有哪些？**
   [中](#q49) | [[日]](04_agile_modle_ja.md#q49) | [[英]](04_agile_modle_en.md#q49)

   **答：** XP（Kent Beck）注重工程实践，与 Scrum 常互补：
   - **TDD（测试驱动开发）**：Red → Green → Refactor 循环
   - **结对编程（Pair Programming）**：两人一机，实时代码评审
   - **持续集成**（前身）
   - **重构（Refactoring）**：小步改进代码结构
   - **简单设计（YAGNI）**：不做未来才需要的功能
   - **集体代码所有权**：任何人可修改任何代码
   - **小步发布**
   - **现场客户（On-site Customer）**
   - **可持续节奏**（不加班文化）

   Scrum 告诉你**做什么/何时做**，XP 告诉你**如何做好**。

<a id="q50"></a>
50. **问：从瀑布向敏捷转型，最常见的挑战和应对策略？**
   [中](#q50) | [[日]](04_agile_modle_ja.md#q50) | [[英]](04_agile_modle_en.md#q50)

   **答：** **常见挑战**：
   1. **文化阻力**：从命令控制到赋能协作，中层管理者最抵触
   2. **合同/预算模式**：固定价合同难以配合范围灵活
   3. **组织结构**：职能孤岛（前端/后端/测试分离）阻碍跨职能团队
   4. **度量误用**：把 Velocity 当 KPI，扭曲团队行为
   5. **僵尸 Scrum**：只学形式，不改思维
   6. **技术基础薄弱**：无自动化测试和 CI/CD，无法频繁交付
   7. **PO 缺位或无授权**

   **应对策略**：
   - **高层承诺 + 引入外部教练**
   - **从试点团队开始**，成功后再扩展
   - **投资工程实践**（CI/CD、自动化测试、DevOps）
   - **调整绩效制度**：奖励团队而非个人英雄
   - **持续培训**：Scrum Master、PO、开发者都需要认知升级
   - **耐心**：文化转型需 1–3 年，不要指望 3 个月见效

---

## 总结

| 类别 | 核心概念 |
|------|---------|
| **基础** | 敏捷宣言 4 价值观 + 12 原则、迭代增量、MVP、DoR/DoD |
| **Scrum** | 3 角色 + 5 事件 + 3 工件、三支柱（透明/检视/适应） |
| **Kanban** | 可视化 + WIP 限制 + 流管理、Little's Law、CFD |
| **需求** | User Story、INVEST、3C、Epic-Feature-Story-Task |
| **估算** | Story Point、Planning Poker、Velocity、Burnup/Burndown |
| **度量** | DORA 四指标、Lead Time、Throughput、结果导向 |
| **规模化** | SAFe / LeSS / Nexus / Spotify、PI Planning |
| **工程实践** | CI/CD、TDD、结对编程、重构、DevOps |

---

**语言导航：** [中] | [[日]](04_agile_modle_ja.md) | [[英]](04_agile_modle_en.md)
