# Common Interview Questions and Answers on Agile Software Project Management (50 Questions)

> Interview preparation document — Agile / Scrum / Kanban / User Stories / Estimation / Metrics / Scaled Agile

**Language Navigation:** [[中]](04_agile_modle.md) | [[日]](04_agile_modle_ja.md) | [英]

---

## Table of Contents

- [I. Agile Fundamentals and Mindset (Q1–Q10)](#sec1)
- [II. The Scrum Framework (Q11–Q22)](#sec2)
- [III. Kanban and the Kanban Method (Q23–Q28)](#sec3)
- [IV. User Stories and Requirements Management (Q29–Q34)](#sec4)
- [V. Agile Estimation and Planning (Q35–Q40)](#sec5)
- [VI. Agile Metrics and Continuous Improvement (Q41–Q45)](#sec6)
- [VII. Scaled Agile and Engineering Practices (Q46–Q50)](#sec7)

---

<a id="sec1"></a>

## I. Agile Fundamentals and Mindset

<a id="q1"></a>
1. **Q: What is Agile? What are its core ideas?**
   [[中]](04_agile_modle.md#q1) | [[日]](04_agile_modle_ja.md#q1) | [英](#q1)

   **A:** Agile is a software development philosophy centered on **iterative and incremental delivery, rapid feedback, and embracing change**. It emphasizes delivering working software in small batches over short cycles, and copes with uncertainty through continuous customer collaboration and self-organizing teams. Agile is not a specific method but a set of values and principles; Scrum, Kanban, and XP are concrete practices that implement it.

<a id="q2"></a>
2. **Q: State the four values of the Agile Manifesto.**
   [[中]](04_agile_modle.md#q2) | [[日]](04_agile_modle_ja.md#q2) | [英](#q2)

   **A:** The Agile Manifesto (2001) proposes four value pairs (the left is valued over the right):
   1. **Individuals and interactions** over processes and tools
   2. **Working software** over comprehensive documentation
   3. **Customer collaboration** over contract negotiation
   4. **Responding to change** over following a plan

   The items on the right still have value, but the items on the left are valued more.

<a id="q3"></a>
3. **Q: What are the key points among the 12 principles of the Agile Manifesto?**
   [[中]](04_agile_modle.md#q3) | [[日]](04_agile_modle_ja.md#q3) | [英](#q3)

   **A:** Key points include: **early and continuous delivery of value**, **welcoming change** (even late in development), **frequent delivery of working software** (weeks to months), **daily collaboration between business and developers**, **trust and motivation of the team**, **face-to-face communication as most effective**, **working software as the primary measure of progress**, **sustainable pace**, **technical excellence and good design**, **simplicity** (the art of maximizing work not done), **self-organizing teams**, and **regular reflection and adjustment**.

<a id="q4"></a>
4. **Q: What is the core difference between Agile and the Waterfall model?**
   [[中]](04_agile_modle.md#q4) | [[日]](04_agile_modle_ja.md#q4) | [英](#q4)

   **A:** Waterfall is **sequential, gated, and large-batch** (requirements → design → development → testing → release), locking in requirements up front; Agile is **iterative, incremental, and small-batch**, allowing requirements to evolve continuously. Waterfall suits projects where requirements are clear and change is costly (aerospace, construction); Agile suits software products where requirements are uncertain and evolve quickly. The core difference lies in the **assumption about the cost of change**: Waterfall assumes change is expensive and therefore locks it down early; Agile assumes change is inevitable and therefore reduces the cost of each individual change.

<a id="q5"></a>
5. **Q: What are Iterations and Increments?**
   [[中]](04_agile_modle.md#q5) | [[日]](04_agile_modle_ja.md#q5) | [英](#q5)

   **A:** An **iteration** refers to a full cycle of "planning → development → testing → review" completed within a fixed short period (1–4 weeks); an **increment** refers to the working, deliverable slice of software functionality produced by each iteration. Multiple iterations accumulate to form the complete product. The iteration is the **process**, while the increment is the **product**. Classic analogy: to paint the Mona Lisa, Waterfall paints from the top-left to the bottom-right cell by cell; Agile sketches the whole picture first and then adds detail round by round.

<a id="q6"></a>
6. **Q: What are the common Agile methods/frameworks?**
   [[中]](04_agile_modle.md#q6) | [[日]](04_agile_modle_ja.md#q6) | [英](#q6)

   **A:** Mainstream Agile methods include:
   - **Scrum**: the most popular team-level Agile framework, based on Sprint iterations
   - **Kanban**: a flow-based method built on visualization and WIP limits
   - **XP (Extreme Programming)**: emphasizes engineering practices (TDD, pair programming, continuous integration)
   - **Lean**: originated from the Toyota Production System, focused on eliminating waste
   - **Crystal**, **FDD (Feature-Driven Development)**, **DSDM**
   - Scaling frameworks: **SAFe**, **LeSS**, **Nexus**, **Scrum@Scale**

<a id="q7"></a>
7. **Q: Is Agile suitable for all types of projects?**
   [[中]](04_agile_modle.md#q7) | [[日]](04_agile_modle_ja.md#q7) | [英](#q7)

   **A:** No. Agile is best suited to scenarios with **uncertain requirements, technical complexity, and a need for rapid feedback** (such as internet products and innovative R&D). It is less suitable when requirements are completely clear and stable (production-line replication), in safety-critical systems (aerospace and medical devices require rigorous documentation), on fixed-price contracts with strong contractual constraints, or in situations where frequent customer interaction is not possible. A **hybrid** approach can be used: Waterfall overall with Agile locally.

<a id="q8"></a>
8. **Q: What are Definition of Ready (DoR) and Definition of Done (DoD)?**
   [[中]](04_agile_modle.md#q8) | [[日]](04_agile_modle_ja.md#q8) | [英](#q8)

   **A:**
   - **DoR (Definition of Ready)**: the conditions a User Story must satisfy before entering a Sprint (clear requirements, defined acceptance criteria, resolved dependencies, estimable, etc.).
   - **DoD (Definition of Done)**: the criteria under which a Story/Increment is considered "done" (code complete, unit tests passing, code reviewed, integration tests passing, deployed to a test environment, documentation updated, etc.).

   Both are a **quality contract** agreed upon by the team, avoiding the fuzzy statement "we're 90% done."

<a id="q9"></a>
9. **Q: What is a Minimum Viable Product (MVP)?**
   [[中]](04_agile_modle.md#q9) | [[日]](04_agile_modle_ja.md#q9) | [英](#q9)

   **A:** An MVP (Minimum Viable Product) is **the simplest version of a product that can validate the core value hypothesis**. It is not a feature-incomplete product but rather one that **focuses on the smallest useful feature set** so it can be shipped quickly to gather feedback from real users, thereby reducing the biggest risk at the lowest cost. The MVP is then iteratively expanded. Classic examples: Dropbox validated demand with a demo video, and the Zappos founder manually shipped shoes from local stores to validate the online shoe-selling model.

<a id="q10"></a>
10. **Q: What is the "Agile Mindset"?**
   [[中]](04_agile_modle.md#q10) | [[日]](04_agile_modle_ja.md#q10) | [英](#q10)

   **A:** The Agile mindset emphasizes **a growth mindset, embracing uncertainty, focusing on customer value, continuous learning and experimentation, psychological safety, and treating failure as learning**. True Agile transformation is not "implementing Scrum" but a shift in organizational culture and ways of thinking—from command-and-control to empowerment and collaboration, from plan-driven to value-driven. Without an Agile mindset, any framework will degrade into "Zombie Scrum."

---

<a id="sec2"></a>

## II. The Scrum Framework

<a id="q11"></a>
11. **Q: What is Scrum? What are its three pillars?**
   [[中]](04_agile_modle.md#q11) | [[日]](04_agile_modle_ja.md#q11) | [英](#q11)

   **A:** Scrum is the most popular Agile framework, grounded in **empiricism**—making decisions through observation and experimentation. Its three pillars are:
   1. **Transparency**: all information is visible to the relevant parties
   2. **Inspection**: artifacts and progress are inspected regularly
   3. **Adaptation**: adjustments are made based on inspection results

   Scrum forms a closed loop through 3 roles, 5 events, and 3 artifacts.

<a id="q12"></a>
12. **Q: What are the three roles in Scrum, and what are their responsibilities?**
   [[中]](04_agile_modle.md#q12) | [[日]](04_agile_modle_ja.md#q12) | [英](#q12)

   **A:**
   - **Product Owner (PO)**: accountable for product value, manages and orders the Product Backlog, and makes "what to do / what not to do" decisions.
   - **Scrum Master (SM)**: a servant leader who champions Scrum, removes impediments, and coaches the team; not a project manager or team lead.
   - **Developers**: a cross-functional team of 3–9 people responsible for delivering the Increment, self-organizing to decide "how to do it."

   The Scrum Team consists of all three, jointly accountable for the product.

<a id="q13"></a>
13. **Q: What are the five events (meetings) in Scrum?**
   [[中]](04_agile_modle.md#q13) | [[日]](04_agile_modle_ja.md#q13) | [英](#q13)

   **A:**
   1. **Sprint**: the entire iteration (1–4 weeks); a container for all other events
   2. **Sprint Planning**: at the start of a Sprint, sets the Sprint Goal and Sprint Backlog (time-boxed to ≤ 8h for a 1-month Sprint)
   3. **Daily Scrum**: 15 minutes, to sync progress and impediments
   4. **Sprint Review**: at the end of the Sprint, demos the Increment to stakeholders and collects feedback (≤ 4h/month)
   5. **Sprint Retrospective**: the team reflects on process improvements (≤ 3h/month)

<a id="q14"></a>
14. **Q: What are the three artifacts in Scrum?**
   [[中]](04_agile_modle.md#q14) | [[日]](04_agile_modle_ja.md#q14) | [英](#q14)

   **A:**
   1. **Product Backlog**: the product-level requirements list, managed by the PO, dynamically ordered
   2. **Sprint Backlog**: the subset of the Backlog committed for the current Sprint plus the delivery plan
   3. **Increment**: the deliverable product outcome at the end of the Sprint

   Each artifact has a corresponding **commitment** (added in the 2020 Scrum Guide):
   - Product Backlog → **Product Goal**
   - Sprint Backlog → **Sprint Goal**
   - Increment → **Definition of Done**

<a id="q15"></a>
15. **Q: How long is a Sprint typically? Why is it fixed?**
   [[中]](04_agile_modle.md#q15) | [[日]](04_agile_modle_ja.md#q15) | [英](#q15)

   **A:** Typically **1–4 weeks**, most commonly 2 weeks. Sprint length **should stay fixed within a product**, because:
   - A stable cadence helps the team build habits and reduces coordination overhead
   - It supports trend analysis by making velocity comparable
   - It gives stakeholders a predictable feedback rhythm

   Once started, a Sprint cannot be extended; if the goal is clearly unachievable, the PO may **cancel the Sprint (Sprint Cancellation)**, but this is a rare last resort.

<a id="q16"></a>
16. **Q: What happens in Sprint Planning, and what does it produce?**
   [[中]](04_agile_modle.md#q16) | [[日]](04_agile_modle_ja.md#q16) | [英](#q16)

   **A:** Sprint Planning answers three questions:
   - **Why**: what value do we want to create this Sprint? → **Sprint Goal**
   - **What**: which Backlog Items can we complete? → select Stories into the Sprint Backlog
   - **How**: how will we deliver? → break items into tasks and do initial design

   Output: the **Sprint Goal + Sprint Backlog**. The entire Scrum Team participates; the PO clarifies priorities and requirements, and the Developers decide on the commitment level.

<a id="q17"></a>
17. **Q: What is the purpose of the Daily Scrum, and what are common pitfalls?**
   [[中]](04_agile_modle.md#q17) | [[日]](04_agile_modle_ja.md#q17) | [英](#q17)

   **A:** **Purpose**: Developers meet for 15 minutes each day to sync progress, surface impediments, and adjust the day's plan to advance the Sprint Goal. It is **not** a status report to the Scrum Master or a manager. The classic three questions (optional): What did I do yesterday? What will I do today? Any impediments?

   **Common pitfalls**:
   - Turning it into a status report (speaking to the SM rather than to peers)
   - Diving into deep technical discussion (should be taken offline)
   - Overrunning the timebox (strictly hold to 15 minutes)
   - The PO or manager interrogating individuals, breaking psychological safety

<a id="q18"></a>
18. **Q: What is the difference between the Sprint Review and the Sprint Retrospective?**
   [[中]](04_agile_modle.md#q18) | [[日]](04_agile_modle_ja.md#q18) | [英](#q18)

   **A:**
   | Dimension | Sprint Review | Sprint Retrospective |
   |-----------|---------------|----------------------|
   | Focus | **Product**: Increment + feedback | **Process**: team collaboration and improvement |
   | Participants | Scrum Team + stakeholders | Scrum Team only |
   | Output | Updated Product Backlog | Concrete improvement action items |
   | Keywords | Demo, feedback, direction adjustment | Reflection, psychological safety, continuous improvement |

   In one sentence: **the Review is about "what we did," the Retrospective is about "how to do it better."**

<a id="q19"></a>
19. **Q: What is the difference between a Scrum Master and a Project Manager?**
   [[中]](04_agile_modle.md#q19) | [[日]](04_agile_modle_ja.md#q19) | [英](#q19)

   **A:**
   | Dimension | Scrum Master | Project Manager |
   |-----------|--------------|-----------------|
   | Positioning | Servant leader, coach | Command-and-control, accountable owner |
   | Authority | No formal management authority | Has authority over resource allocation and decisions |
   | Focus | Process effectiveness, team empowerment | The scope/schedule/cost triangle |
   | Scope | One Scrum Team | All stakeholders of the entire project |
   | Metrics | Team health, delivery capability | Plan completion, KPIs |

   The Scrum Master does not assign tasks, chase progress, or evaluate performance.

<a id="q20"></a>
20. **Q: What is the most important capability for a Product Owner?**
   [[中]](04_agile_modle.md#q20) | [[日]](04_agile_modle_ja.md#q20) | [英](#q20)

   **A:** Core capabilities:
   1. **Value judgment**: identifying what will create the most user/business value
   2. **Prioritization**: strong ordering of the Backlog (not "everything is top priority")
   3. **Requirements expression**: writing clear User Stories and acceptance criteria
   4. **Stakeholder management**: aligning with business, users, and developers
   5. **The courage to say "no"**: rejecting low-value requests to stay focused

   Common failure modes: a part-time PO, a PO without decision authority, or a PO who turns the Backlog into a growing pile of to-dos.

<a id="q21"></a>
21. **Q: What is Product Backlog Refinement?**
   [[中]](04_agile_modle.md#q21) | [[日]](04_agile_modle_ja.md#q21) | [英](#q21)

   **A:** Backlog Refinement (also called Grooming) is an **ongoing** activity (not a formal Scrum event), led by the PO with participation from the whole team, aimed at keeping the Backlog in a **DEEP** state:
   - **D**etailed appropriately: near-term items detailed, far-term items coarse
   - **E**stimated
   - **E**mergent: continuously evolving
   - **P**rioritized

   Typically 5–10% of Sprint time is spent on refinement, including splitting large Stories, adding acceptance criteria, estimating, and ordering.

<a id="q22"></a>
22. **Q: Can new requirements be added mid-Sprint?**
   [[中]](04_agile_modle.md#q22) | [[日]](04_agile_modle_ja.md#q22) | [英](#q22)

   **A:** **In principle, no.** Once the Sprint Goal is set, the Sprint Backlog is "protected" for the development team. Injecting requirements mid-Sprint disrupts the cadence and undermines commitments. **How to handle it**:
   - Urgent and mandatory → the PO negotiates with the team to swap out an equivalent amount of work
   - Not urgent → add it to the Product Backlog for consideration next Sprint
   - Frequent injections → indicate poor PO planning or too-long Sprints, and require retrospective improvement

   Exception: if the Sprint Goal is clearly no longer achievable, the PO may **cancel the Sprint** and replan.

---

<a id="sec3"></a>

## III. Kanban and the Kanban Method

<a id="q23"></a>
23. **Q: What is Kanban? How does it differ from Scrum?**
   [[中]](04_agile_modle.md#q23) | [[日]](04_agile_modle_ja.md#q23) | [英](#q23)

   **A:** Kanban originated from the Toyota Production System and is a **flow-based, visual, pull-driven method**. It does not prescribe roles, events, or iterations, only that you: **visualize the workflow, limit WIP, manage flow, make policies explicit, implement feedback loops, and improve collaboratively**.

   | Dimension | Scrum | Kanban |
   |-----------|-------|--------|
   | Cadence | Fixed Sprints | Continuous flow |
   | Roles | PO/SM/Dev | Not prescribed |
   | Change | Locked within a Sprint | Adjustable at any time |
   | Metrics | Velocity | Lead Time / Throughput |
   | Fit | Product development | Operations, support, diverse tasks |

<a id="q24"></a>
24. **Q: What are the six core practices of Kanban?**
   [[中]](04_agile_modle.md#q24) | [[日]](04_agile_modle_ja.md#q24) | [英](#q24)

   **A:**
   1. **Visualize the workflow** (Kanban board, cards, swimlanes)
   2. **Limit Work in Progress (WIP)** — the most important practice
   3. **Manage flow** (focus on Lead Time and bottlenecks)
   4. **Make policies explicit** (Definition of Ready/Done, prioritization policy)
   5. **Implement feedback loops** (daily standups, replenishment meetings, delivery meetings)
   6. **Improve collaboratively, evolve experimentally** (Kaizen)

<a id="q25"></a>
25. **Q: What is a WIP (Work In Progress) limit? Why is it important?**
   [[中]](04_agile_modle.md#q25) | [[日]](04_agile_modle_ja.md#q25) | [英](#q25)

   **A:** A WIP limit is the **maximum number of items simultaneously in a given workflow state**. Its benefits:
   - **Expose bottlenecks**: when a column hits its limit, upstream must stop, making problems visible
   - **Reduce context switching**: parallelizing many tasks slows every one of them
   - **Speed up delivery**: per **Little's Law**: `Lead Time = WIP / Throughput`, reducing WIP directly shortens delivery time
   - **Improve quality**: focus increases

   Rule of thumb: start with a WIP of 1–1.5× team size, then gradually lower it.

<a id="q26"></a>
26. **Q: What is a Cumulative Flow Diagram (CFD)?**
   [[中]](04_agile_modle.md#q26) | [[日]](04_agile_modle_ja.md#q26) | [英](#q26)

   **A:** The CFD is a core Kanban visualization: the x-axis is time and the y-axis is cumulative item count, with each state stacked in a different color. From it you can read:
   - **WIP**: the vertical thickness of a state at any moment
   - **Lead Time**: the horizontal distance from when an item enters to when it completes
   - **Throughput**: the slope of the completion curve
   - **Bottlenecks**: a band that keeps growing thicker = a queue is piling up in that state

   A healthy CFD has bands rising in parallel; a bulging band signals a bottleneck or blockage.

<a id="q27"></a>
27. **Q: What are Lead Time, Cycle Time, and Throughput?**
   [[中]](04_agile_modle.md#q27) | [[日]](04_agile_modle_ja.md#q27) | [英](#q27)

   **A:**
   - **Lead Time**: total time from **customer request** to **delivery**, viewed from the customer's perspective
   - **Cycle Time**: time from **starting work** to **completion**, viewed from the team's perspective (a subset of Lead Time)
   - **Throughput**: number of items completed per unit time (e.g., 5 stories/week)

   Classic analogy: Lead Time = from ordering to receiving your pizza; Cycle Time = from starting to make the pizza to it coming out of the oven; Throughput = how many pizzas come out per hour.

<a id="q28"></a>
28. **Q: What is Scrumban?**
   [[中]](04_agile_modle.md#q28) | [[日]](04_agile_modle_ja.md#q28) | [英](#q28)

   **A:** Scrumban is a **hybrid of Scrum and Kanban**: it retains Scrum's roles, Sprint cadence, and Review/Retro, while introducing Kanban's visualization and WIP limits. It is commonly used when:
   - A Scrum team wants to improve flow efficiency
   - A team is transitioning from Scrum to Kanban or vice versa
   - A team handles both product development and operations/support

   A typical setup: keep 2-week iterations for the planning cadence, but add WIP limits on the board and allow urgent injections via a swap-out mechanism.

---

<a id="sec4"></a>

## IV. User Stories and Requirements Management

<a id="q29"></a>
29. **Q: What is a User Story? What is the standard format?**
   [[中]](04_agile_modle.md#q29) | [[日]](04_agile_modle_ja.md#q29) | [英](#q29)

   **A:** A User Story is a short expression of a requirement **from the user's perspective**. The classic template:

   > **As** a 〈type of user〉, **I want** 〈some capability〉, **so that** 〈some value〉.
   > As a 〈role〉, I want 〈feature〉, so that 〈benefit〉.

   Example: As an online shopper, I want to save items to a wishlist so that I can quickly order them later.

   A User Story is not an exhaustive requirements document but **a starting point for a conversation** — the details are filled in through discussion.

<a id="q30"></a>
30. **Q: What is the INVEST principle?**
   [[中]](04_agile_modle.md#q30) | [[日]](04_agile_modle_ja.md#q30) | [英](#q30)

   **A:** INVEST is a set of six criteria for evaluating the quality of a User Story:
   - **I**ndependent: minimize dependencies between stories
   - **N**egotiable: details are open to discussion and adjustment
   - **V**aluable: meaningful to the user or business
   - **E**stimable: enough information to estimate effort
   - **S**mall: small enough to complete within a single Sprint
   - **T**estable: has clear acceptance criteria

<a id="q31"></a>
31. **Q: What are the 3Cs of a User Story?**
   [[中]](04_agile_modle.md#q31) | [[日]](04_agile_modle_ja.md#q31) | [英](#q31)

   **A:** The 3Cs are the three elements of a User Story proposed by Ron Jeffries:
   1. **Card**: a short written description of the Story (can be written on a physical or electronic card)
   2. **Conversation**: ongoing discussion with the PO, users, and team about the details
   3. **Confirmation**: acceptance criteria used to verify that the Story is complete

   Core idea: **the card is a token that promises a conversation, not the full text of the requirement**.

<a id="q32"></a>
32. **Q: What is the hierarchical relationship between Epic, Feature, User Story, and Task?**
   [[中]](04_agile_modle.md#q32) | [[日]](04_agile_modle_ja.md#q32) | [英](#q32)

   **A:** From largest to smallest requirement granularity:
   - **Epic**: a large chunk of functionality spanning multiple Sprints or even quarters, e.g., "user account system"
   - **Feature**: a subset of an Epic, e.g., "password recovery"
   - **User Story**: the smallest unit of value that can be completed within a single Sprint, e.g., "recover password via email"
   - **Task**: technical breakdown of a Story, e.g., "implement email-sending API" or "write unit tests"

   Tasks are internal to the team and are usually not visible to the PO; the PO mainly manages down to the Story level.

<a id="q33"></a>
33. **Q: What are Acceptance Criteria? What are common formats?**
   [[中]](04_agile_modle.md#q33) | [[日]](04_agile_modle_ja.md#q33) | [英](#q33)

   **A:** Acceptance criteria describe the specific, verifiable conditions under which **a Story is considered done**, defined jointly by the PO and the team. Common formats:

   **1. Checklist style:**
   ```
   - Entering a valid email results in a reset email being received
   - The email link is valid for 24 hours
   - Invalid emails return a clear error message
   ```

   **2. Gherkin BDD format (Given-When-Then):**
   ```
   Given the user is registered
   When the user clicks "Forgot Password" on the login page and enters their registered email
   Then the system sends a reset email to that address within 1 minute
   ```

<a id="q34"></a>
34. **Q: How do you split a large User Story?**
   [[中]](04_agile_modle.md#q34) | [[日]](04_agile_modle_ja.md#q34) | [英](#q34)

   **A:** Common splitting techniques (SPIDR and similar patterns):
   1. **By workflow steps**: split the sign-up flow into "fill form / verify / activate email"
   2. **By data variations**: support credit cards first → then Alipay → then WeChat Pay
   3. **By business rules**: handle the main scenario first → then edge cases
   4. **By interface/endpoint**: ship Web first → then iOS → then Android
   5. **By acceptance criteria**: a Story with 10 ACs → split into several stories with 2–3 each
   6. **CRUD split**: ship "Create" first → then add "Edit/Delete"
   7. **Performance/quality attributes**: get functionality working first → then optimize to <200ms

   Goal: each Story can be **completed within one Sprint in a few person-days**.

---

<a id="sec5"></a>

## V. Agile Estimation and Planning

<a id="q35"></a>
35. **Q: What are Story Points? Why not use hours?**
   [[中]](04_agile_modle.md#q35) | [[日]](04_agile_modle_ja.md#q35) | [英](#q35)

   **A:** Story Points are a **relative estimation unit** that jointly considers **complexity, effort, and uncertainty**. Reasons to use them instead of hours:
   - Humans are far more accurate at judging **relative size** than **absolute time**
   - It sidesteps individual differences (the same task takes different people different amounts of time)
   - It removes the political pressure of "commitment = hours"
   - Team-level metrics (Velocity) are more stable than individual hours

   Story Points typically use the **Fibonacci sequence** (1, 2, 3, 5, 8, 13, 21, ...), since the growing spacing reflects the increased estimation uncertainty of larger stories.

<a id="q36"></a>
36. **Q: What is Planning Poker?**
   [[中]](04_agile_modle.md#q36) | [[日]](04_agile_modle_ja.md#q36) | [英](#q36)

   **A:** Planning Poker is a collaborative team estimation technique:
   1. The PO briefly describes the Story
   2. The team discusses to clarify
   3. Everyone **reveals a card simultaneously** (a Fibonacci number)
   4. If estimates diverge widely (e.g., 3 vs. 13) → the highest and lowest estimators explain their reasoning
   5. Discuss and revote until estimates converge

   Advantages: **avoids anchoring bias** (in sequential estimation, later voters are influenced by earlier ones), leverages collective wisdom, and surfaces hidden risks and knowledge gaps.

<a id="q37"></a>
37. **Q: What is Velocity, and how do you use it?**
   [[中]](04_agile_modle.md#q37) | [[日]](04_agile_modle_ja.md#q37) | [英](#q37)

   **A:** Velocity is the **average number of Story Points a team completes per Sprint**. Uses:
   - **Forecasting**: with 100 points left in the Backlog and Velocity = 20, ~5 more Sprints are needed
   - **Planning**: the commitment for a new Sprint references the average of the last 3 Sprints' Velocity
   - **Improvement feedback**: the Velocity trend reflects team maturity

   **Caveats**:
   - Velocity is **not** a KPI and cannot be compared across teams (estimation units differ)
   - Do not use it to evaluate individual performance (it induces estimate inflation)
   - For newly formed teams, Velocity fluctuates significantly during the first 3 Sprints, which is normal

<a id="q38"></a>
38. **Q: What is Release Planning?**
   [[中]](04_agile_modle.md#q38) | [[日]](04_agile_modle_ja.md#q38) | [英](#q38)

   **A:** Release Planning is **mid-range planning across multiple Sprints**, answering "when can we release which features?" Steps:
   1. Define the Release Goal and target date
   2. Refine the Backlog and identify Stories that belong to this Release
   3. Estimate the total Story Points P
   4. Estimate the number of Sprints from Velocity V: `N = P / V`
   5. Draft an initial Sprint allocation and milestones
   6. **Continuously update**: adjust after each Sprint based on actuals

   Key idea: **scope, time, and resources — pick two**. Agile typically fixes time and resources and lets scope flex.

<a id="q39"></a>
39. **Q: What are Burndown and Burnup Charts?**
   [[中]](04_agile_modle.md#q39) | [[日]](04_agile_modle_ja.md#q39) | [英](#q39)

   **A:**
   - **Burndown**: the y-axis shows remaining work, "burning down" toward 0, giving a direct view of progress
   - **Burnup**: the y-axis shows cumulative completed work growing upward, while a "total scope line" is also plotted

   **Advantage of the Burnup**: it can show **scope changes** — if the total scope line rises, requirements were added mid-flight, whereas a Burndown may misleadingly suggest the team is not making progress. For that reason, Burnups are better suited to release-level tracking.

<a id="q40"></a>
40. **Q: How do you address the problem of over-committing and missing the Sprint goal?**
   [[中]](04_agile_modle.md#q40) | [[日]](04_agile_modle_ja.md#q40) | [英](#q40)

   **A:** Strategies:
   - **Reference historical Velocity** instead of optimistic estimates
   - **Leave a buffer**: don't fill to 100%; reserve 10–20% for the unexpected
   - **Order by priority**: even if not everything ships, the highest-value Stories are delivered
   - **Split Stories smaller**: small Stories are easier to predict and complete
   - **Retrospective root-cause analysis**: inaccurate estimates? external dependencies? technical debt?
   - **Culture building**: don't punish missed commitments; encourage honest estimation
   - **Show reality in Sprint Review**, without hiding unfinished items

---

<a id="sec6"></a>

## VI. Agile Metrics and Continuous Improvement

<a id="q41"></a>
41. **Q: What metrics are commonly used in Agile projects?**
   [[中]](04_agile_modle.md#q41) | [[日]](04_agile_modle_ja.md#q41) | [英](#q41)

   **A:** They fall into four broad categories:
   - **Delivery efficiency**: Velocity, Throughput, Lead Time, Cycle Time
   - **Quality**: defect density, defect escape rate, code coverage, production incident count
   - **Value/outcomes**: NPS, user activation rate, business KPIs, feature usage rate
   - **Team health**: Sprint Goal achievement rate, Retrospective action completion rate, team happiness

   **Principle**: **measure outcomes over outputs**. Shipping a feature does not equal realizing value.

<a id="q42"></a>
42. **Q: What are the four key DORA metrics?**
   [[中]](04_agile_modle.md#q42) | [[日]](04_agile_modle_ja.md#q42) | [英](#q42)

   **A:** The four DevOps high-performance metrics proposed by DORA (DevOps Research and Assessment):
   1. **Deployment Frequency**: how often deployments to production occur
   2. **Lead Time for Changes**: time from code commit to production
   3. **Change Failure Rate**: percentage of changes that require rollback or hotfix after release
   4. **Mean Time to Restore (MTTR)**: how long it takes to recover from an incident

   Elite team benchmarks (per Google's reports): multiple deployments per day, <1 day lead time, <15% failure rate, <1 hour recovery time.

<a id="q43"></a>
43. **Q: How do you make a Sprint Retrospective effective?**
   [[中]](04_agile_modle.md#q43) | [[日]](04_agile_modle_ja.md#q43) | [英](#q43)

   **A:** Keys to an effective Retro:
   - **Psychological safety**: a blame-free atmosphere (Norm Kerth's Prime Directive)
   - **Vary the format to avoid ritualization**: Start/Stop/Continue, 4Ls (Liked/Learned/Lacked/Longed for), Sailboat, Mad-Sad-Glad
   - **Focus on a few actionable items**: rather than listing 10, pick 1–2 concrete improvements
   - **Track previous actions**: begin each Retro by reviewing whether last time's improvements landed
   - **Data-driven**: combine metrics with subjective impressions, not gut feel alone
   - **Rotate facilitators**: prevents the meeting from becoming stale ritual

   The heart of the practice is a **culture of continuous improvement**, not the meeting itself.

<a id="q44"></a>
44. **Q: What is "Zombie Scrum," and how do you recognize it?**
   [[中]](04_agile_modle.md#q44) | [[日]](04_agile_modle_ja.md#q44) | [英](#q44)

   **A:** Zombie Scrum refers to a state where a team **does Scrum in form but has lost its Agile essence**. Typical symptoms:
   - Sprints exist, but every Sprint slips or has its scope cut
   - Issues raised in Retros are never resolved
   - The Daily is just a status report to the manager
   - No usable Increment at the end of a Sprint
   - The PO is just a requirements messenger with no decision authority
   - Low team morale, lack of psychological safety
   - No interaction with real users, ever

   The cure: return to Agile values and principles, focus on "delivering real value," and rebuild psychological safety and a culture of experimentation.

<a id="q45"></a>
45. **Q: What is Technical Debt, and how do you manage it?**
   [[中]](04_agile_modle.md#q45) | [[日]](04_agile_modle_ja.md#q45) | [英](#q45)

   **A:** Ward Cunningham's metaphor: **suboptimal technical decisions** made in order to ship quickly, which accrue "interest" over time (maintenance cost, difficulty changing). Classifications:
   - **Intentional vs. unintentional**, **prudent vs. reckless** (Martin Fowler's four quadrants)

   **Management strategies**:
   - **Make it visible**: track it as dedicated items in the Backlog
   - **Pay it down regularly**: allocate 15–20% of each Sprint's capacity to refactoring and technical improvements
   - **Quantify the impact**: use production incidents and slowdown in development speed to make the case to the business
   - **Add quality gates to the DoD**: new code doesn't introduce new debt
   - **Boy Scout Rule**: leave the code cleaner than you found it every time you touch it

---

<a id="sec7"></a>

## VII. Scaled Agile and Engineering Practices

<a id="q46"></a>
46. **Q: What are the common scaled Agile frameworks, and what are their characteristics?**
   [[中]](04_agile_modle.md#q46) | [[日]](04_agile_modle_ja.md#q46) | [英](#q46)

   **A:**
   - **SAFe (Scaled Agile Framework)**: the most complete and heaviest framework, spanning Portfolio/Program/Team layers, introducing the ART (Agile Release Train), PI Planning, and SPC certification. Well-suited to large enterprises.
   - **LeSS (Large-Scale Scrum)**: a minimalist scale-up of Scrum, with a single PO and a single Backlog for multiple teams (2–8), emphasizing agility at the organizational level.
   - **Nexus**: from Scrum.org, coordinates 3–9 Scrum teams and introduces a Nexus Integration Team to handle integration.
   - **Scrum@Scale**: proposed by Jeff Sutherland, extending Scrum recursively as a "Scrum of Scrums."
   - **Spotify Model**: Squad/Tribe/Chapter/Guild organizational structure, valuing culture over framework.

<a id="q47"></a>
47. **Q: What is PI Planning in SAFe?**
   [[中]](04_agile_modle.md#q47) | [[日]](04_agile_modle_ja.md#q47) | [英](#q47)

   **A:** PI (Program Increment) Planning is the core event in SAFe, typically held **once every 8–12 weeks over 2 days**, with the entire ART (50–125 people) attending. Purposes:
   - Align business objectives with team plans
   - Identify cross-team dependencies
   - Commit to PI Objectives and assess confidence (a 1–5 vote)
   - Produce a Program Board that visualizes dependencies and milestones

   PI Planning is the heartbeat of SAFe's organizational cadence — expensive to run once, but greatly improves cross-team coordination.

<a id="q48"></a>
48. **Q: What are Continuous Integration (CI), Continuous Delivery (CD), and Continuous Deployment?**
   [[中]](04_agile_modle.md#q48) | [[日]](04_agile_modle_ja.md#q48) | [英](#q48)

   **A:**
   - **CI (Continuous Integration)**: developers merge into mainline frequently (many times per day), and each merge triggers an automated build and test
   - **CD (Continuous Delivery)**: builds on CI so that production release **can happen** at any time with a single click (manual trigger)
   - **Continuous Deployment**: goes further — after passing tests, changes are **automatically** deployed to production

   Relationship: **CI ⊂ CD ⊂ Continuous Deployment**. Netflix and Facebook release hundreds of times per day, powered by a full Continuous Deployment pipeline, robust test automation, and progressive/canary releases.

<a id="q49"></a>
49. **Q: What are the core engineering practices of XP (Extreme Programming)?**
   [[中]](04_agile_modle.md#q49) | [[日]](04_agile_modle_ja.md#q49) | [英](#q49)

   **A:** XP (Kent Beck) focuses on engineering practices and often complements Scrum:
   - **TDD (Test-Driven Development)**: the Red → Green → Refactor cycle
   - **Pair Programming**: two people on one machine for real-time code review
   - **Continuous Integration** (a precursor to modern CI)
   - **Refactoring**: improving code structure in small steps
   - **Simple Design (YAGNI)**: don't build things you don't need yet
   - **Collective Code Ownership**: anyone can modify any code
   - **Small Releases**
   - **On-site Customer**
   - **Sustainable Pace** (no-overtime culture)

   Scrum tells you **what to do and when**; XP tells you **how to do it well**.

<a id="q50"></a>
50. **Q: What are the most common challenges in transitioning from Waterfall to Agile, and how do you address them?**
   [[中]](04_agile_modle.md#q50) | [[日]](04_agile_modle_ja.md#q50) | [英](#q50)

   **A:** **Common challenges**:
   1. **Cultural resistance**: shifting from command-and-control to empowered collaboration; middle managers resist the most
   2. **Contract/budget models**: fixed-price contracts don't fit flexible scope
   3. **Organizational structure**: functional silos (front-end/back-end/QA separated) hinder cross-functional teams
   4. **Metric misuse**: treating Velocity as a KPI, which distorts team behavior
   5. **Zombie Scrum**: adopting the form without changing the mindset
   6. **Weak engineering foundations**: without automated tests and CI/CD, frequent delivery is impossible
   7. **PO absent or without authority**

   **Response strategies**:
   - **Executive commitment + external coaching**
   - **Start with a pilot team**, then expand once successful
   - **Invest in engineering practices** (CI/CD, test automation, DevOps)
   - **Adjust performance systems**: reward teams rather than individual heroes
   - **Ongoing training**: Scrum Masters, POs, and developers all need a mindset upgrade
   - **Patience**: cultural transformation takes 1–3 years — don't expect results in 3 months

---

## Summary

| Category | Core Concepts |
|----------|---------------|
| **Fundamentals** | Agile Manifesto — 4 values + 12 principles, iterative and incremental delivery, MVP, DoR/DoD |
| **Scrum** | 3 roles + 5 events + 3 artifacts, the three pillars (transparency/inspection/adaptation) |
| **Kanban** | Visualization + WIP limits + flow management, Little's Law, CFD |
| **Requirements** | User Story, INVEST, 3Cs, Epic-Feature-Story-Task |
| **Estimation** | Story Points, Planning Poker, Velocity, Burnup/Burndown |
| **Metrics** | DORA four metrics, Lead Time, Throughput, outcome orientation |
| **Scaling** | SAFe / LeSS / Nexus / Spotify, PI Planning |
| **Engineering** | CI/CD, TDD, pair programming, refactoring, DevOps |

---

**Language Navigation:** [[中]](04_agile_modle.md) | [[日]](04_agile_modle_ja.md) | [英]
