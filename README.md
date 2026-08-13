# 能力雷达 · Capability Radar

**什么能力正在升值？企业正在为什么 AI 能力付钱？**
每周自动回答这两个问题。

**Track what companies hire for — and what companies pay for.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/MoonHuang0325/capability-radar?style=social)](https://github.com/MoonHuang0325/capability-radar/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/MoonHuang0325/capability-radar?style=social)](https://github.com/MoonHuang0325/capability-radar/network/members)
![Last commit](https://img.shields.io/github/last-commit/MoonHuang0325/capability-radar)
[![radar-watchdog](https://github.com/MoonHuang0325/capability-radar/actions/workflows/radar-watchdog.yml/badge.svg)](https://github.com/MoonHuang0325/capability-radar/actions/workflows/radar-watchdog.yml)

## 本周信号（2026-08-13）

| 信号 | 动量 | 证据 |
|---|---|---|
| Agent 搭建 / 工作流自动化 | ↑ 连续两期最强 | [B 类应用开发岗占新发 AI 岗位 43.8%](data/signals/2026-08-13-maimai-b-class-jobs-share.yml) |
| AI 评估与可观测性 | ↑ 雇主最大供给缺口 | [报告](reports/2026-08-13.md) |
| 大模型安全采购（金融/政务） | ↑ 进入集采目录 | [北京银行中标公告 · A 级](data/signals/2026-08-13-bank-of-beijing-llm-security-gateway.yml) |

**▶ [阅读最新一期](LATEST.md)　🚀 [部署你自己的雷达](prompts/weekly-agent-prompt.md)　📊 [结构化信号数据](data/)**

---

## 它监控两个市场

AI 落地有两个最真实的市场信号：

- **招聘市场（talent）**：企业准备为谁付工资——什么技能在涨价，什么在贬值
- **采购市场（procurement）**：企业正在为什么付钱——中标公告是最诚实的转型数据

 newsletters 回答"发生了什么"，能力雷达回答"**什么正在变得更重要**"。每期与上期逐信号对比，标注新增 / 强化 / 消退，你看到的是趋势的动量，不是孤立的快照。

## 三条设计原则

1. **证据分层**：每条信号带 A/B/C 证据等级。A=一手来源可点击核验，B=权威二手，C=待核实。数据可以拿去开会。
2. **失败与成功同权**：企业侧同时收录落地案例与烂尾教训，避坑信息不比成功案例便宜。
3. **人机分工**：人类定框架、选题、判断信号重要性；AI Agent 执行每周调研、撰写、对比。这个项目本身就是一次公开的"AI 时代工作方式"实验。

## 部署你自己的雷达

1. Fork 本仓库，修改 [radar.yml](radar.yml) 选择你关心的方向（或直接选用 [packs/](packs/) 里的预设：AI 产品经理 / 开发者 / 金融 / 制造）
2. 复制 [prompts/weekly-agent-prompt.md](prompts/weekly-agent-prompt.md) 到你使用的 AI Agent（具备联网搜索与定时任务能力即可）
3. 设定每周运行，报告与结构化信号会自动累积

内置 watchdog：每周自动检查报告是否按时更新，漏跑会自动开 issue 提醒（见 [ROADMAP](ROADMAP.md) 与 `.github/workflows/`）。

## 目录结构

```
├── LATEST.md           # 最新一期完整报告
├── reports/            # 每周情报快照（按日期归档）
├── data/               # 结构化信号（YAML）与采购记录（CSV），A/B/C 证据分层
│   ├── signals/
│   └── procurement/
├── schemas/
│   └── signal.schema.json  # 信号数据格式定义
├── radar.yml           # 雷达配置：Fork 后改这一个文件
├── packs/              # 预设监控视角（AI 产品经理 / 开发者 / 金融 / 制造）
├── prompts/
│   └── weekly-agent-prompt.md  # 可复用的每周监控提示词
├── docs/
│   └── methodology.md  # 完整方法论：信源分层、证据层、对比机制
├── ROADMAP.md          # 路线图：什么在做、什么不做
├── CONTRIBUTING.md     # 如何提交信号、纠错、改进方法论
└── LICENSE
```

## 参与

- 路线图与"不打算做什么"见 [ROADMAP.md](ROADMAP.md)
- 提交信号、纠错、改进方法论见 [CONTRIBUTING.md](CONTRIBUTING.md)

## 作者

[@MoonHuang0325](https://github.com/MoonHuang0325) — 本项目由人类策划方向、AI Agent 执行调研与撰写，每周持续维护。

## License

[MIT](LICENSE)
