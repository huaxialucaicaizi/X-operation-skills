---
name: x-growth
description: 把增长干货变成持续关注时使用，是前 8 个入口之上的运营策略层。读本地配置和⑧的数据，从可配置来源的当日 AI 热点中挑能讲增长打法的并加上获客/激活/留存/变现视角，给出主页定位优化建议、一周增长计划、长帖/Article 分发清单、互动与合作候选及草稿、周度涨粉复盘和下周一个实验。只出建议和草稿，逐条等作者批准；不自动发布、回复、关注或私信，不做涨粉或曝光预测，不引用未经验证的算法说法。Use when planning weekly X follower growth on top of the content pipeline; drafts only, author approves each action.
---

# X 涨粉 / X Growth

把增长干货变成持续关注。本入口决定「为谁写、本周发什么、怎么触达、怎么转成持续关注」，不再造写作或发布工具。

## 先读配置

账号、目标、起止日期、语言、时间预算等都只放在本地配置里。复制 [templates/growth-config.example.md](templates/growth-config.example.md) 到 `local/growth-config.md` 后填写（`local/` 已在 .gitignore 中忽略）。

- 配置里标「待补充」的项，输出中原样写「待补充」，不猜。
- 粉丝基线必须在启动当天从账号实际页面记录，不用旧数据，不编造。
- 目标粉丝数是目标，不是效果承诺；只算差额和每周所需净增，不预测能否达成。

## 与前 8 个入口的关系

| 环节 | 交给谁 | 本入口做什么 |
|---|---|---|
| 证据 | ① 播客拆解 | 不重复拆解 |
| 选题与大纲 | ② 增长选题 | 提供本周配比和读者问题方向 |
| 标题 | ③ 标题 | 不改锁定标题 |
| 写作 | ④ 长文写作 | 指定 X 长帖 / X Article 模式和导读需求 |
| 去 AI 味、配图 | ⑤ ⑥ | 不介入 |
| 预览、授权、发布、互动发送 | ⑦ 发布互动 | 只出草稿和候选，发送一律走⑦的授权流程 |
| 数据 | ⑧ 数据复盘 | 消费⑧的逐帖数据，补账号层指标，不重复采集 |

## 输入

- 本地配置（见上），含热点来源
- 当日 AI 热点（只取配置中列出的来源）
- 账号主页现状：bio、置顶、横幅、最近帖子
- ⑧ 的逐帖数据与周复盘
- 已批定位、素材库
- 取舍库：[../../shared/templates/decision-library.md](../../shared/templates/decision-library.md)

## 输出（默认存本地）

| 输出 | 模板 |
|---|---|
| 当日热点候选（带增长视角） | [templates/daily-hotspots.md](templates/daily-hotspots.md) |
| 主页优化建议（修改前后对照） | [templates/profile-review.md](templates/profile-review.md) |
| 一周增长计划（含分发清单） | [templates/weekly-growth-plan.md](templates/weekly-growth-plan.md) |
| 互动与合作候选及草稿 | [templates/engagement-candidates.md](templates/engagement-candidates.md) |
| 周度涨粉复盘与下周一个实验 | [templates/weekly-growth-review.md](templates/weekly-growth-review.md) |

## 步骤

1. **定位与主页**：按 [references/positioning-and-profile.md](references/positioning-and-profile.md) 检查读者能否说出「关注后能持续得到什么」，给修改前后对照。
2. **本周节奏与配比**：按 [references/cadence-and-distribution.md](references/cadence-and-distribution.md) 排一周主槽位，给②④下需求。
3. **当日热点联动**：按 [references/hotspot-linkage.md](references/hotspot-linkage.md)，从配置来源挑当日 AI 热点，先过增长门槛，再选一个最站得住的增长环节（获客/激活/留存/变现/扩张）加视角，标明推断；候选交作者选，用于当日选题或互动回复。
4. **分发清单**：每个主作品决定 X 长帖还是 X Article，是否配导读帖，是否拆附加内容，每条单独审批。
5. **互动与合作候选**：按 [references/engagement-and-collab.md](references/engagement-and-collab.md) 列候选和草稿，交⑦走授权。
6. **周度复盘**：按 [references/growth-review.md](references/growth-review.md) 读⑧数据，写「保留什么、停什么、下周试什么」，只定一个实验。
7. **回流**：读者问题回流②，标题结构回流③；选中/否掉的理由记进取舍库。

## 默认值（试行，可在配置中改）

| 项 | 默认值 | 性质 |
|---|---|---|
| 主内容 | 每日一个主槽位 | 默认 |
| 英文内容 | 每周 1–2 条，**占用当日主槽位**，不额外加量 | 默认，可改 |
| 周配比 | 4 条案例/机制拆解 + 2 条操作清单/流程 + 1 条本周方法总结 | **试行值**，不是算法最优比例 |
| 互动回复草稿 | 每日 ≤ 3 条 | **试行值**，是上限不是任务指标 |
| 试行期 | 2 周 | 默认，可改 |

试行值默认先跑 2 周（试行期可在配置中改），再用自己的数据决定是否调整。

## 人工闸门

- 沿用套件闸门：大纲先批；正文和标题定稿后再做图；锁定标题一字不改。见 [../../shared/workflow.md](../../shared/workflow.md)。
- 「发」只针对已展示的单条、账号、渠道、版本；改稿要重新确认。它不代表自动评论、社群发帖、合作邀约、跨平台同步或未来排程的授权。
- 主页的 bio、横幅、链接、置顶，各自单独批准后才改。
- 作者每日审核时间超出配置的预算时，先减预告、互动、英文附加量，不减事实检查。

## 禁区

- 不买粉，不刷曝光、刷量，不诱导虚假互动，不加入互助刷量群。
- 不批量或自动关注、取关、点赞、评论、私信。
- 不冒充亲历，不编头衔或成绩，不抄袭。
- 不做涨粉、曝光、达标概率预测。
- 不引用未经验证的算法说法（例如「外链必限流」「发后必须马上自评」「黄金 15 分钟」）。
- 不用付费 X API，不购买额外工具，不取 Cookie，不绕过权限、失败或风控。
- 不创建定时任务，不修改现有发布时间。

## 参考

- [references/positioning-and-profile.md](references/positioning-and-profile.md)：定位与主页
- [references/hotspot-linkage.md](references/hotspot-linkage.md)：热点联动
- [references/cadence-and-distribution.md](references/cadence-and-distribution.md)：节奏、配比与长帖/Article 分发
- [references/engagement-and-collab.md](references/engagement-and-collab.md)：互动与合作互推
- [references/growth-review.md](references/growth-review.md)：周度涨粉复盘指标
- 思路借鉴：[x-agent-skill](https://github.com/Jakeschincariol/x-agent-skill)（MIT）的 x-plan：用周计划统筹内容和互动对象，主页承诺与置顶一致，按自身基线比较表现。不采用其回复频次、抢发时间、算法权重、固定体裁频率和私信增长路线。[marketingskills](https://github.com/coreyhaines31/marketingskills)（MIT）：受众问题、内容复用、指标服务决策等通用思路。两者均未复制文本；仓库存在和许可明确，不代表其方法已被证明能涨粉。
