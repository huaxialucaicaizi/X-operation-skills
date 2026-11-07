---
name: publish-engage
description: 准备次日发布预览和互动回复草稿时使用。展示账号、标题、全文、图片与版本，筛选相关热门帖并拟回复草稿，等作者对展示过的单条明确说「发」后，才在允许的浏览器界面操作并回读确认。只出预览和草稿，不自动发布、不自动点赞评论私信，不用付费 API、不取 Cookie、不绕过失败。Use when preparing a publish preview and reply drafts for explicit per-item author approval; never auto-posts.
---

# 发布预览与互动 / Publish and Engage

把确认过的内容稳妥交付到指定渠道，不让运营变成自动发布。

## 输入

- 终稿与图片（审批记录中的版本号）
- 目标账号与渠道
- 相关热门原帖及上下文（作者提供或作者允许浏览时可见）
- 已有回复草稿（如有）

## 输出

- 次日预览包：[templates/preview-pack.md](templates/preview-pack.md)
- 逐条互动草稿：[templates/reply-drafts.md](templates/reply-drafts.md)
- 获授权并发布后：真实回执（链接、时间、回读结果）

预览准备时间由作者设定（默认值待补充）。本入口不创建定时任务，不改变已有排程。

## 步骤

1. **组预览包**：账号、平台、标题、全文、图片、各自版本号，原样展示。
2. **筛热门帖**：只挑和本篇增长主题相关、我们有增量观点可补的帖子。分诊见 [references/reply-triage.md](references/reply-triage.md)。
3. **拟回复草稿**：每条写原帖上下文、我们的增量观点、草稿正文。
4. **等授权**：按 [references/authorization-rules.md](references/authorization-rules.md)。
5. **授权后操作**：只在作者允许的浏览器界面操作，只做被授权的那一条。
6. **回读**：发布后打开实际页面，比对标题、正文、图片数量和顺序，记录链接和时间。
7. **失败即停**：遇到登录、验证、拒绝或报错，停下报告，不换工具绕过。

## 规矩

- 作者对展示过的单条明确说「发」才发。版本变了重新确认。
- 互动只出草稿，不默认点赞、评论、转发、私信。
- 不用付费 X API，不取 Cookie，不保存密码或会话到文件。
- 公众号等其他渠道：存草稿、外部归档、跨平台同步、定时发布分别单独授权；公众号不自动发布。
- 授权不写进 Skill 作为永久授权。

## 参考

- [references/authorization-rules.md](references/authorization-rules.md)：授权规则
- [references/reply-triage.md](references/reply-triage.md)：回复分诊
- 思路借鉴：[baoyu-skills](https://github.com/JimLiu/baoyu-skills)（MIT）的图片位置清单、清除占位符、发布前预览检查；[x-agent-skill](https://github.com/Jakeschincariol/x-agent-skill)（MIT）的回复分诊。未采用其自动重试、会话复用、自动排程等做法。未复制其文本。
