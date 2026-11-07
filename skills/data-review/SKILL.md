---
name: data-review
description: 用账号自己的真实发帖数据做周复盘时使用。从浏览器可见数据、用户导出或截图中记录逐帖指标，对齐观察窗并复算，按主题/标题/体裁对读 Top 与 Bottom，写观察、其他解释和下周一个低成本实验，回流选题与标题入口。看不到的指标填 NA，不估算，不说因果，不预测曝光，不购买数据服务。Use for weekly post-performance reviews from the account's own visible data; no estimates, no causal claims.
---

# 数据复盘 / Data Review

用自己的真实结果改进选题与标题，而不是追通用算法传说。

## 输入

- 已发清单（链接、发布时间、体裁、主题、标题、增长环节标签）
- 指标来源：浏览器可见数据、作者导出的文件或截图
- 采样时间
- 取舍库：[../../shared/templates/decision-library.md](../../shared/templates/decision-library.md)

## 输出

- 逐帖表：[templates/post-metrics.md](templates/post-metrics.md)
- 周复盘：[templates/weekly-review.md](templates/weekly-review.md)，含 Top/Bottom 对读、证据与局限、下周一个实验建议
- 回流：给「增长选题」和「标题」入口的建议；把真实表现补回取舍库对应行

## 步骤

1. **记录**：按 [references/metrics-definitions.md](references/metrics-definitions.md) 填逐帖表。看不到填 `NA` 并写原因。
2. **对齐观察窗**：如发布后 24 小时、7 天。不同观察窗的数字不混比。
3. **计算并复算**：比例指标（如每千曝光互动）用脚本或表格公式算，再手工抽查一行。
4. **分组对读**：按主题、增长环节、标题角度、体裁（X 长帖 / X Article）分组，Top 与 Bottom 并排看。
5. **写观察**：每条观察写样本数 n、证据、其他可能的解释。
6. **下周一个实验**：只提一个、成本低、能在下周观察的调整。
7. **回流**：建议写给选题和标题入口；只影响未来候选。

## 规矩

- 看不到就填 NA，不估算收藏，不把周净增粉分摊到单帖。
- 公开 views 和后台 impressions 分开列，不混用。
- 小样本只作线索，不说因果，不说「保爆」。
- 不同时间、不同题目的发布不叫严格 A/B。
- 不引用未经验证的「算法权重」或固定阈值。
- 调整只影响未来候选，不改已定稿标题，不改增长定位。
- 周报默认存本地，不购买数据服务，不接付费 API。

## 参考

- [references/metrics-definitions.md](references/metrics-definitions.md)：指标口径
- 思路借鉴：[x-agent-skill](https://github.com/Jakeschincariol/x-agent-skill) 的 x-audit（MIT）与 [marketingskills](https://github.com/coreyhaines31/marketingskills) 的 analytics（MIT）：用账号自身数据、每千曝光指标、统一观察窗、反馈循环。不采用其中的算法权重、倍数阈值或因果结论。未复制其文本。
