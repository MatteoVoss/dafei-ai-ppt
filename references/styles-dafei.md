# 大飞新增风格 C / D / E

三种风格都是在风格 A（`assets/template.html`）基础上的"皮肤"：HTML 结构、类名、`data-anim` 动效、演讲者模式完全一致，直接使用 `layouts.md` 的页面骨架。区别只在配色、字体和质感。皮肤源码在 `src-skins/`（common.css + 各风格 css，`build.py` 重新生成模板）。

## 通用规则
- 配色已内置，**不使用 `themes.md` 切换主题，不接受自定义 hex**。
- 深色页（`.slide.hero.dark` / `.dark`）与浅色页交替，避免连续 3 页同色。
- 数据页优先用数据大字报；前后对比用 `.grid-2-6-6` 左右两栏（左=改前，右=改后，右栏自动高亮）；核心结论用大字金句页。
- 所有数字来自用户资料并在页脚注明出处，缺数据写"待补"（模板会以强调色显示）。
- 中文大标题 ≤ 12 字，必要时手动换行；交付前逐页截图检查无溢出、无重叠。

## 风格 C · 商务汇报风 `template-business.html`
- 色：深蓝 #0b1f3a / 白 #ffffff；主色蓝 #2f6bff，辅色金 #f5a524（只用于极少量强调）。
- 字：Noto Sans SC + Inter，全程无衬线。
- 特征：kicker 为蓝底白字小标签；数据卡片为白卡片 + 顶部蓝线 + 轻阴影。
- 适合：工作汇报、述职、季度复盘、客户方案。
- 必查：不出现衬线体；金色每页最多一处。

## 风格 D · 科技发布会风 `template-tech.html`
- 色：纯黑 #05060b，渐变 #00e5ff → #7c5cff → #ff3dcd（标题关键词、大数字）。
- 字：Space Grotesk + Noto Sans SC，元数据 JetBrains Mono。
- 特征：细网格背景、渐变大数字、发光边框卡片。
- 适合：AI 产品发布、技术分享、Demo Day。
- 必查：渐变只用在标题和数字上，正文保持白/灰；每页渐变元素 ≤ 2 处。

## 风格 E · 国潮东方风 `template-guochao.html`
- 色：宣纸 #f2ead9 / 黛青 #2c4a4e；朱红 #c0392b、金 #e9b04f 点缀。
- 字：标题马善政书法体（Ma Shan Zheng，英文数字自动回落 Playfair Display），正文 Noto Serif SC。
- 特征：纸纹噪点质感；hero 页可加印章：`<section class="slide hero dark" data-seal="汇报">`（2-4 字，竖排朱红印章显示在右下）。
- 适合：文化、品牌故事、节日活动、教育培训、传统行业汇报。
- 必查：书法体只用于大标题和金句，正文不能用；印章每份 deck 最多 2 处。
