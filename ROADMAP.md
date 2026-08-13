# Roadmap

## v0.2 · 进行中 — Fork it. Configure it. It runs itself.

目标：任何人 Fork 一次，就拥有一个会自己工作的 AI 情报雷达。

- [x] 双市场统一叙事：招聘市场（talent）+ 采购市场（procurement）
- [x] 信号结构化：`schemas/signal.schema.json` + `data/signals/`
- [x] 采购数据库起步：`data/procurement/`（CSV，每条带原始公告 URL）
- [x] 证据层：A/B/C 证据分级，写入方法论与提示词
- [x] radar.yml + Radar Packs（AI 产品经理 / 开发者 / 金融 / 制造）
- [x] 漏跑看门狗：GitHub Action 每周检查，漏更自动开 issue
- [ ] 两期历史报告的全面溯源补链接（已补核心条目，剩余逐条核验）
- [ ] 采购记录扩充到 50-100 条（来源：中国政府采购网、招标投标公共服务平台、各行招采官网）
- [ ] 一键运行版：GitHub Actions + 自带采集脚本，Fork 后填 API Key 即可自动周报
- [ ] GitHub Pages：每期产出一张可截图转发的趋势图

## v0.3 · 中期

- [ ] Capability Momentum：按 Hiring / Salary / OSS / Procurement / Persistence / Confidence 六个公开维度给技能打分
- [ ] 「本周能力涨幅榜」「连续 N 周最强能力」等榜单化输出
- [ ] 行业 × 场景转型地图（企业侧素材沉淀的诊断参考框架）
- [ ] Community Radars：社区 PR 自己的 Radar Pack

## 更 later（有意推迟）

- MCP / API / 向量检索：等积累几十周结构化信号后再做，那时数据才有被查询的价值
- 多语言报告：视社区需求

## 不打算做的

- 实时推送。市场信号以周为单位变化才有意义，本项目不追求即时性
- 大而全的 AI 资讯聚合。雷达的价值在对比和动量，不在信息量
- 新闻源/RSS 数量的军备竞赛。我们锁死的赛道是 Information → Signal → Momentum → Decision

路线图会根据每周信号和社区反馈调整，改动记录在本文件的提交历史里。
