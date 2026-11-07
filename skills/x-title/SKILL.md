---
name: x-title
description: 为增长长文拟标题、比较候选或检查已有标题时使用。优先调用本地已安装的 X-title-skill；未安装时按本文件的简版流程执行：读正文，抓一个业务问题和真实反差，出 3–5 个不同角度的候选并写兑现位置，核对数字口径和手机显示，交作者选定后逐字锁定。不预测点击率，不改事实，不自动发布。Use when drafting or checking titles for X long posts / X Articles; delegates to X-title-skill if installed.
---

# 标题 / Title

让读者看懂这篇解决什么问题，并且正文确实兑现。

## 先复用 X-title-skill

本入口复用作者的独立仓库 [X-title-skill](https://github.com/huaxialucaicaizi/X-title-skill)，不另造一套标题理论。

- **本地已安装 X-title-skill**：直接调用它，把本套件的正文、证据表和取舍库「二、标题取舍」作为输入传给它。
- **未安装**：按下面的简版流程执行。

> 说明：X-title-skill 的完整方法目前在该仓库的 PR #1 中，尚未合并到主分支，因此这里只链接仓库主页。合并后以该仓库主分支为准。

## 输入

- 选题、已批大纲
- 正文草稿与证据表（事实锚点）
- 取舍库：[../../shared/templates/decision-library.md](../../shared/templates/decision-library.md) 的「二、标题取舍」「四、已确认偏好」
- 平台与输出模式：X 长帖首句 / X Article 标题

## 输出

按 [templates/title-output.md](templates/title-output.md)：3–5 个不同角度的候选及兑现说明；作者选定后，写入 `title.txt` 并在审批记录里锁定。

## 简版流程

1. **读正文**：没有正文只有主题时，产出标「方向草案」，不能当可发布候选。
2. **找业务问题与真实反差**：一句话写「谁，遇到什么问题，这篇给出哪个答案」，再写一句「不承诺什么」。
3. **出候选**：3–5 个，每个是不同的读者问题或解释重点，不是同义改写。
4. **核对**：按 [references/title-rules.md](references/title-rules.md) 的五条和禁区逐条过；数字核口径；看手机显示。
5. **交作者选**：写推荐和取舍，停在确认点。
6. **锁定**：作者选定后逐字锁定。下游（去 AI 味、配图、发布）一字不改，配图时只能换行。

## 规矩

- 标题不比正文更劲爆，不加正文没有的事实、数字、身份或「独家」。
- 不预测点击率、打开率，不打伪精确总分。
- 正式候选不超过 5 个，不堆量。
- 作者选完后，把选中和否掉的候选及原因记进取舍库。

## 参考

- [references/title-rules.md](references/title-rules.md)：五条基本面、禁区、检查项（简版）
- 上游：[X-title-skill](https://github.com/huaxialucaicaizi/X-title-skill)（作者本人仓库）
