---
name: podcast-teardown
description: 把英文产品增长类播客拆成可追溯的增长素材时使用。登记来源并去重，优先复用可靠文字稿，必要时本地转写，校对说话人、专名、数字和引语，按获客/激活/留存/变现/扩张提炼证据卡；大纲获批后才补完整中英逐字稿。不拿摘要冒充全文，不估算时间戳。Use when turning a growth podcast episode into traceable, timestamped evidence cards before topic selection.
---

# 播客拆解 / Podcast Teardown

把一期播客变成可追溯的增长素材，不丢原意。

## 输入

- 单集链接、音频文件或已有文字稿
- 嘉宾、期次
- 目标读者（作者没说就问，不默认）

## 输出

**第一阶段（选题前）**

- 英文转写（原始稿 + 校正稿，分开保存）
- 增长观点证据卡，见 [../../shared/templates/evidence-card.md](../../shared/templates/evidence-card.md)
- 疑点列表

**第二阶段（大纲获批后）**

- 完整中英逐字稿，按 [templates/bilingual-transcript.md](templates/bilingual-transcript.md)
- 术语表，按 [templates/glossary.md](templates/glossary.md)

第一阶段的整体交付格式见 [templates/teardown-output.md](templates/teardown-output.md)。

## 步骤

1. **登记来源并去重**：在来源表里登记，得到 `S-xxx`。已登记过的直接复用。
2. **优先复用可靠稿**：官方文字稿 > 带时间戳的第三方稿 > 自行转写。说明用的是哪种。
3. **必要时本地转写**：可用 faster-whisper 等本地工具。转写工具只负责出字，不负责判断说话人。
4. **校对**：按 [references/transcription-checklist.md](references/transcription-checklist.md) 检查说话人、专名、数字、引语和时间连续性。原始稿不覆盖，校正另存。
5. **提炼证据卡**：只提能落到获客/激活/留存/变现/扩张的具体动作。每张卡写对象、动作、机制、结果、口径、条件、原文摘录。
6. **停下等大纲**：把证据卡交给「增长选题」入口。大纲获批前不做整集翻译。
7. **获批后逐段翻译**：意思一致，不加料，专名按术语表统一。

## 规矩

- 先确认大纲再整集翻译。这是成本闸门。
- 不拿摘要冒充全文。
- 时间戳必须真实。按文字位置估算的时间线不能当原话证据。
- 不能只看最后一个时间戳就认定没有漏段，要检查中间连续性并抽听。
- 原始稿保留，疑点不猜。
- 说话人由人工校对，不声称已自动分离说话人。
- 下载的音频是否删除由作者决定，不默认删除。

## 最低要求（未读取 shared/ 时）

即使没有共用模板，也必须输出：来源链接、原始稿与校正稿位置、每条证据的时间戳和原文摘录、疑点列表。

## 参考

- [references/transcription-checklist.md](references/transcription-checklist.md)：转写与校对清单
- [../../shared/evidence-rules.md](../../shared/evidence-rules.md)：来源与证据规则
- 思路借鉴：[audio-tldr-skill](https://github.com/AugustusW/audio-tldr-skill)（MIT）的转写缓存、校正副本、专名记录；[faster-whisper](https://github.com/SYSTRAN/faster-whisper)（MIT）仅作转写工具。未复制其文本。
