# 能力雷达 · Capability Radar

**什么能力正在升值？企业正在为什么 AI 能力付钱？**
每周自动回答这两个问题。

![Capability Radar](.github/social-preview.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/MoonHuang0325/capability-radar?style=social)](https://github.com/MoonHuang0325/capability-radar/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/MoonHuang0325/capability-radar?style=social)](https://github.com/MoonHuang0325/capability-radar/network/members)
![Last commit](https://img.shields.io/github/last-commit/MoonHuang0325/capability-radar)
[![radar-watchdog](https://github.com/MoonHuang0325/capability-radar/actions/workflows/radar-watchdog.yml/badge.svg)](https://github.com/MoonHuang0325/capability-radar/actions/workflows/radar-watchdog.yml)

> 🌍 English intro: [README.en.md](README.en.md)（完整内容为中文，本项目数据聚焦中国招聘与采购市场）

## 本周信号（2026-08-13）

| 信号 | 动量 | 证据 |
|---|---|---|
| Agent 搭建 / 工作流自动化 | ↑ 连续两期最强 | [B 类应用开发岗占新发 AI 岗位 43.8%](data/signals/2026-08-13-maimai-b-class-jobs-share.yml) |
| AI 评估与可观测性 | ↑ 雇主最大供给缺口 | [报告](reports/2026-08-13.md) |
| 大模型安全采购（金融/政务） | ↑ 进入集采目录 | [北京银行中标公告 · A 级](data/signals/2026-08-13-bank-of-beijing-llm-security-gateway.yml) |

**▶ [阅读最新一期](LATEST.md)　🚀 [创建我的雷达](https://github.com/MoonHuang0325/capability-radar/generate)　📊 [结构化信号数据](data/)**

## 拿到信号之后怎么行动

[playbooks/](playbooks/) 是按角色写的**有证据的转型路线图**——运营、销售、开发者三条路径，每个行动节点都挂到仓库里的真实信号并标注证据等级，没证据的节点诚实标注"待补"：

- [🎯 运营 / 市场岗 → AI 应用操盘手](playbooks/README.md#-运营--市场岗--ai-应用操盘手)
- [💼 销售 / 商务岗 → AI 解决方案顾问](playbooks/README.md#-销售--商务岗--ai-解决方案顾问)
- [🛠 开发者 → Agent 工程师](playbooks/README.md#-开发者--agent-工程师)

---

## 它监控两个市场

AI 落地有两个最真实的市场信号：

- **招聘市场（talent）**：企业准备为谁付工资——什么技能在涨价，什么在贬值
- **采购市场（procurement）**：企业正在为什么付钱——中标公告是最诚实的转型数据

Newsletters 回答"发生了什么"，能力雷达回答"**什么正在变得更重要**"。每期与上期逐信号对比，标注新增 / 强化 / 消退，你看到的是趋势的动量，不是孤立的快照。

## 创建我的雷达

本仓库是**模板仓库（Template Repository）**——不用 Fork，点一下生成你自己的：

1. **[创建我的雷达](https://github.com/MoonHuang0325/capability-radar/generate)** → 修改 [radar.yml](radar.yml) 选择你关心的方向（或直接选用 [packs/](packs/) 里的预设：AI 产品经理 / 开发者 / 金融 / 制造）
2. 复制 [prompts/weekly-agent-prompt.md](prompts/weekly-agent-prompt.md) 到**你自己的 AI Agent**（具备联网搜索与定时任务能力即可，如 Kimi / ChatGPT / Claude）
3. 设定每周运行，报告与结构化信号会自动累积

**分工说明**：仓库提供的是协议、配置、数据结构、校验与看门狗；每周的调研执行由你自己的 AI Agent 完成。内置 watchdog 每周检查报告是否按时更新，漏跑自动开 issue 提醒（见 `.github/workflows/`）。

## 三条设计原则

1. **证据分层**：每条信号带 A/B/C 证据等级（定义见[方法论](docs/methodology.md)）。数据可以拿去开会。
2. **失败与成功同权**：企业侧同时收录落地案例与烂尾教训，避坑信息不比成功案例便宜。
3. **人机分工**：人类定框架、选题、判断信号重要性；AI Agent 执行每周调研、撰写、对比。这个项目本身就是一次公开的"AI 时代工作方式"实验。

## 目录结构

```
├── LATEST.md           # 最新一期完整报告（永久有效链接）
├── reports/            # 每周情报快照（按日期归档）
├── data/               # 结构化信号（YAML）与采购记录（CSV），A/B/C 证据分层
│   ├── signals/
│   └── procurement/
├── schemas/
│   └── signal.schema.json  # 信号数据格式定义
├── radar.yml           # 雷达配置：生成后改这一个文件
├── packs/              # 预设监控视角（AI 产品经理 / 开发者 / 金融 / 制造）
├── playbooks/          # 有证据的 AI 转型路线图（按角色）
├── prompts/
│   └── weekly-agent-prompt.md  # 可复用的每周监控提示词
├── docs/
│   └── methodology.md  # 完整方法论：信源分层、证据层、对比机制
├── ROADMAP.md          # 项目路线图：什么在做、什么不做
├── CONTRIBUTING.md     # 如何提交信号、纠错、改进方法论
└── LICENSE
```

## 数据与版权

代码以 [MIT](LICENSE) 授权；第三方原始资料版权归原发布者所有，本项目仅做索引、事实提取与核验存档。详见 [DATA_NOTICE.md](DATA_NOTICE.md)。

## 参与

- 路线图与"不打算做什么"见 [ROADMAP.md](ROADMAP.md)
- 提交信号、纠错、改进方法论见 [CONTRIBUTING.md](CONTRIBUTING.md)

## 作者

[@MoonHuang0325](https://github.com/MoonHuang0325) — 本项目由人类策划方向、AI Agent 执行调研与撰写，每周持续维护。

## License

[MIT](LICENSE)
