# X-operation-skills

X 运营 Skill 套件：把英文产品增长类播客，做成中文增长干货，并在 X 上发布和复盘。

一个仓库，9 个入口 Skill：8 个内容生产入口，加 1 个涨粉策略层。每个入口可以单独用，也可以按顺序串起来；它们共用同一套来源表、证据编号、审批记录和取舍库。

核心是获客、激活、留存、变现、扩张的具体动作、机制、证据和适用条件。传播角度只服务表达，不决定选题。

## 项目地图

| # | 入口 | 做什么 |
|---|---|---|
| ① | **[podcast-teardown](skills/podcast-teardown/SKILL.md) 播客拆解** | 登记来源、转写校对，提炼带时间戳的增长证据卡 |
| ② | **[growth-topics](skills/growth-topics/SKILL.md) 增长选题** | 过增长门槛，给 3 个候选和带证据缺口的大纲 |
| ③ | **[x-title](skills/x-title/SKILL.md) 标题** | 复用 X-title-skill，出 3–5 个不同角度候选，选定后锁定 |
| ④ | **[longform-writing](skills/longform-writing/SKILL.md) 长文写作** | 两种模式：X 长帖 / X Article；附事实核验表 |
| ⑤ | **[de-ai-tone](skills/de-ai-tone/SKILL.md) 去 AI 味** | 按自写禁用写法做最小改写，逐项核对改了不走样 |
| ⑥ | **[cover-and-figures](skills/cover-and-figures/SKILL.md) 头图配图** | 观点先于图型，HTML/CSS 本地渲染，对表目检 |
| ⑦ | **[publish-engage](skills/publish-engage/SKILL.md) 发布互动** | 预览包和回复草稿，逐条授权后才发 |
| ⑧ | **[data-review](skills/data-review/SKILL.md) 数据复盘** | 用账号自己的数据做周复盘，回流选题和标题 |
| ⑨ | **[x-growth](skills/x-growth/SKILL.md) X 涨粉** | 策略层：主页定位、一周计划与分发、互动与合作草稿、周度涨粉复盘；账号与目标只放本地配置 |

共用部分：

- **[shared/workflow.md](shared/workflow.md) 流程与审批闸门**
- **[shared/evidence-rules.md](shared/evidence-rules.md) 来源与证据规则**
- **[shared/templates/decision-library.md](shared/templates/decision-library.md) 取舍库**：记录作者选中/否掉的选题、标题、改稿及原因，供各入口读取
- **[shared/templates/source-register.md](shared/templates/source-register.md) 来源表**、**[shared/templates/evidence-card.md](shared/templates/evidence-card.md) 证据卡**、**[shared/templates/approval-log.md](shared/templates/approval-log.md) 审批记录**

## 流程

```
① 播客拆解 → ② 增长选题与大纲 → 【作者确认大纲】
   → ④ 长文写作（中途调用 ③ 标题）→ ⑤ 去 AI 味 → 【作者审定正文和标题】
   → ⑥ 头图配图 → ⑦ 完整预览与逐条授权 → ⑧ 数据复盘 → 回流 ② ③

⑨ X 涨粉：策略层，读 ⑧ 的数据，给 ② ④ 下本周配比与分发需求，互动和合作草稿交 ⑦ 授权发送
```

三道闸门：大纲确认前不写全文；正文和标题审定前不做图；作者对展示过的单条明确说「发」之前不发布。

## 安装

```bash
git clone https://github.com/huaxialucaicaizi/X-operation-skills.git
cd X-operation-skills
```

把需要的入口复制到你的 Agent 的 skills 目录，并把 `shared/` 放到 skills 目录的上一级（各入口通过 `../../shared/` 引用共用模板）。以 Claude Code 的用户级目录为例：

```bash
mkdir -p ~/.claude/skills
cp -r skills/* ~/.claude/skills/
cp -r shared ~/.claude/shared
```

其他 Agent 的 skills 目录位置以其文档为准。只装单个入口时，没有 `shared/` 也能运行，但输出会注明「未读取共用来源表/取舍库」。

真实的来源表、取舍库、复盘数据，以及 X 涨粉的账号配置（从 `skills/x-growth/templates/growth-config.example.md` 复制），建议放在本地 `local/` 目录（已在 `.gitignore` 中忽略），默认不公开。

## 这个套件不做什么

- 不编造数据、引语、亲历、测试、来源或算法结论；未知写「待补充」
- 不改事实，不夸大
- 不预测点击率、曝光或「爆款概率」
- 不自动发布，不自动点赞、评论、私信
- 不使用付费 API，不读取 Cookie，不绕过登录或失败

## 校验

```bash
python3 scripts/validate.py
```

检查每个 SKILL.md 的 frontmatter、必需文件、相对链接，以及 README 中是否误加了徽章或旧仓库名。CI 在每个 PR 上自动运行。

## 致谢

本套件的规则和流程由作者自定，以下项目只提供方法上的参考。除特别说明外，均为借鉴思路、用自己的话重写，未复制原文。许可信息来自各仓库的 LICENSE 文件或 GitHub API。

| 项目 | 许可 | 借鉴了什么 | 用在哪里 |
|---|---|---|---|
| [huaxialucaicaizi/X-title-skill](https://github.com/huaxialucaicaizi/X-title-skill) | 作者本人仓库 | 标题方法整体复用 | 标题 |
| [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) | MIT，Copyright (c) 2026 歸藏 | 「改了不走样」：信息与确定程度守恒、作者声音、逐项对照（归纳重述） | 去 AI 味 |
| [AugustusW/audio-tldr-skill](https://github.com/AugustusW/audio-tldr-skill) | MIT | 转写缓存、原稿与校正稿分开、专名记录 | 播客拆解 |
| [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) | MIT | 仅作为可选的本地转写工具 | 播客拆解 |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT | 受众问题、信息增量检查、内容复用；账号自身数据与反馈循环 | 增长选题、数据复盘、X 涨粉 |
| [Gracker/gracker-writing](https://github.com/Gracker/gracker-writing) | MIT | 事实强度、整稿与局部审查分开 | 长文写作 |
| [criccomini/write-like-paul-graham](https://github.com/criccomini/write-like-paul-graham) | MIT | 先论点骨架、前几段给答案 | 长文写作 |
| [codejunkie99/x-article-skills](https://github.com/codejunkie99/x-article-skills) | 未识别 | 只借鉴「早给价值、讲清作者增量」的思路，未复制任何文本 | 长文写作 |
| [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | MIT | 信息结构与视觉风格分开、按信息关系选图型；发布前预览与图片位置检查 | 头图配图、发布互动 |
| [Jakeschincariol/x-agent-skill](https://github.com/Jakeschincariol/x-agent-skill) | MIT | 回复分诊；账号自身数据、每千曝光指标、统一观察窗；x-plan 的周计划统筹内容与互动、主页承诺与置顶一致 | 发布互动、数据复盘、X 涨粉 |

可选外部工具（本仓库未包含、未复制其任何内容）：[larashero3-dotcom/lieflat-less-ai-tone](https://github.com/larashero3-dotcom/lieflat-less-ai-tone)（CC BY-NC 4.0）。去 AI 味入口只写「本地装了就调用」，许可是否适用由使用者自行确认。

## 作者

华夏路菜菜子：前大厂 AI 产品增长，现 AI 创业者

## 许可

非商业许可，见 [LICENSE](LICENSE)。未经作者事先书面许可，不得商用，也不得将本项目上架、收录或分发到第三方 AI 产品、Skill 商店或类似渠道。联系：GitHub [@huaxialucaicaizi](https://github.com/huaxialucaicaizi)。

变更记录见 [CHANGELOG.md](CHANGELOG.md)。
