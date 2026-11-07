---
name: de-ai-tone
description: 清理中文增长长文中的套路化表达时使用。按本套件自己的禁用写法检查，复核语境与误报，做最小改写，再按「改了不走样」原则逐项对照数字、否定、条件、时间、归因和因果。引语、逐字稿、专名、代码和锁定标题不改；不删事实追求清零；风格检查不等于 AI 身份检测。Use when de-templating Chinese growth articles with minimal edits while preserving every fact and qualifier.
---

# 去 AI 味 / De-AI Tone

用白话和自然节奏表达，清理套路，不改变信息。

## 输入

- 正文
- 锁定标题（只读）
- 事实核验表
- 保护范围：引语、逐字稿、专名、代码、锁定标题
- 取舍库：[../../shared/templates/decision-library.md](../../shared/templates/decision-library.md) 的「三、改稿取舍」（特别是归类为「误报」的行）

## 输出

按 [templates/revision-report.md](templates/revision-report.md)：

- 问题与改法清单
- 最小改写稿
- 前后对照
- 语义复核结果

## 步骤

1. **标出保护范围**：引语、逐字稿、专名、代码、锁定标题，整段跳过。
2. **按禁用写法检查**：见 [references/banned-patterns.md](references/banned-patterns.md)。
3. **复核语境与误报**：每个命中回到上下文，问一句「这里真的空泛、重复或误导吗」。取舍库里作者拒绝过的同类改法，默认算误报。
4. **最小改写**：只改有问题的句子。通顺的段落原样保留。
5. **语义复核**：按 [references/meaning-preservation.md](references/meaning-preservation.md) 逐项对照。任何一项走样，撤回该处改写。
6. **重读整稿**：检查衔接，确认没有为了改而改。
7. **交作者审定**：正文仍由作者定稿。作者接受或拒绝的改法记进取舍库。

## 规矩

- 不为「清零」删事实、删限定、删归因。
- 风格偏好不冒充 AI 身份检测，不输出「AI 概率」。
- 不替作者补情绪、经历或态度。
- 数字不加形容词，结尾不拔高。
- 锁定标题一字不改。

## 可选外部工具

- **lieflat-less-ai-tone**：如果本地已经安装，可以调用；本仓库不包含、不复制它的任何规则。是否适用其许可由使用者自行确认。
- **Humanizer-zh**：如果本地已经安装，可以调用做补充检查；本套件已在 [references/meaning-preservation.md](references/meaning-preservation.md) 中按其 MIT 许可归纳了「改了不走样」原则。

外部工具的检查结果只作线索，最终以本文件的步骤和作者审定为准。

## 参考

- [references/banned-patterns.md](references/banned-patterns.md)：本套件自己的禁用写法（自写）
- [references/meaning-preservation.md](references/meaning-preservation.md)：改了不走样（归纳自 Humanizer-zh，MIT）
