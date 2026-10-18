# 修改说明（AGPL-3.0 第5条）

本项目 **大飞AIPPT（dafei-ai-ppt）** 基于歸藏（op7418）的开源项目 guizang-ppt-skill 二次开发：
原仓库 https://github.com/op7418/guizang-ppt-skill ，原作者版权与协议见 LICENSE（AGPL-3.0），本项目同样以 AGPL-3.0 开源。

修改者：大飞
本项目源码地址：https://github.com/MatteoVoss/dafei-ai-ppt

主要修改：
1. SKILL.md：改名为 dafei-ai-ppt / 大飞AIPPT，补充 WorkBuddy 开放平台所需 frontmatter 字段；新增"大飞5步法"工作流；风格选择从 2 种扩展到 5 种。
2. 新增风格 C 商务汇报风、D 科技发布会风、E 国潮东方风：assets/template-business.html、template-tech.html、template-guochao.html（基于原 template.html 生成，皮肤源码见 src-skins/）。
3. 新增 references/styles-dafei.md、assets/previews/ 预览图。
4. 删除原仓库内部规划文档 docs/。
5. v1.1.0：大飞5步法设为唯一澄清流程；风格选择并入第 1 步；新增"直接做"快速模式（可跳过第 1–4 步，防编造检查保留）；删除原"启动前检查更新"步骤；原"7 问澄清"改为第 1 步参考清单。
6. v1.1.1：默认必须走完整 5 步；只上传文档不再视为"直接做"，需用户明确说"直接做"才跳过。
7. v1.2.0：澄清改为"选择题、一次一题"，优先调用环境自带的可点选提问工具；每步确认也用选择题。
8. v1.3.0：5 步法改为每步 1 道选择题（用途/资料处理/思路确认/大纲确认/选风格），受众与时长改为推断后在第 3 步确认。
9. v1.3.1：新增对话规范——全程中文、不对用户提内部步骤编号与术语。
其余文件保持原样。
