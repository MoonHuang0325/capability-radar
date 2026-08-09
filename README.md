# 能力雷达 · Capability Radar

> 一份每周自动更新的双轨情报系统：**个人侧**追踪 AI 时代最有竞争力的能力信号，**企业侧**追踪各行业 AI 转型信号。
> An open-source, weekly-updated dual-track intelligence radar: personal AI-era capability signals + industry AI-transformation signals.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 解决什么问题

很多人拿着强大的 AI 工具，却不知道用它做什么、往哪个方向投入才有回报。这个问题有两面：

- **个人侧**：什么能力正在升值？什么技能正在贬值？薪酬溢价在哪里？
- **企业侧**：传统行业面对 AI 转型，谁在落地？预算是多少？坑在哪里？

能力雷达用自动化方式持续追踪这两组信号，每周输出一份带对比的情报快照——不是静态报告，而是**有动量方向的趋势追踪**。

## 核心设计

### 能力图谱五层框架（个人侧）

| 层 | 内容 | 典型信号源 |
|---|---|---|
| 基础层 | AI 素养、提示词 | LinkedIn / Coursera / WEF |
| 应用层 | Agent 搭建、工作流自动化、AI+数据分析 | 招聘 JD、脉脉、猎聘、BOSS直聘 |
| 工程层 | Python、部署、云平台 | Stanford AI Index / Lightcast |
| 治理层 | AI 伦理、合规 | EU AI Act、行业监管动态 |
| 人性层 | 批判性思维、AI 输出验证能力 | Microsoft WTI、麦肯锡 |

每层每周标注热度变化（↑↓→），并维护信号级锚点表，逐周对比**新增 / 消退 / 强化**。

### 行业 AI 转型追踪（企业侧）

按行业归档（制造 / 零售 / 医疗 / 金融 / 教育 / 物流…），每周收集：

- **落地案例**：谁做了、用什么方案、投入产出
- **预算与采购信号**：咨询报告、招标动态、AI 预算变化
- **失败教训**：烂尾项目、ROI 不达预期、组织阻力——和成功案例同等重要

### 机会窗口

每期附未来 2–6 周可参与的大会、黑客松、认证与报告发布窗口。

## 目录结构

```
├── reports/            # 每周情报快照（按日期归档）
├── docs/
│   └── methodology.md  # 完整方法论：信号源、分层框架、对比机制
├── prompts/
│   └── weekly-agent-prompt.md  # 可复用的每周监控提示词
└── LICENSE
```

## 如何部署你自己的雷达

本项目的方法论与提示词完全开放。你可以：

1. 阅读 [docs/methodology.md](docs/methodology.md) 理解设计逻辑
2. 复制 [prompts/weekly-agent-prompt.md](prompts/weekly-agent-prompt.md) 到你使用的 AI Agent（任何具备联网搜索与定时任务能力的 Agent 均可）
3. 按你的行业/职业目标修改监控维度，设定每周定时运行

## 最新一期

见 [reports/](reports/) 目录下日期最新的快照。

## 作者

[@MoonHuang0325](https://github.com/MoonHuang0325) — 本项目由人类策划方向、AI Agent 执行调研与撰写，每周持续维护。维护过程本身即是对"AI 时代工作方式"的一次公开实验。

## License

[MIT](LICENSE)
