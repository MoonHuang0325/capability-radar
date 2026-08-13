# 参与贡献

能力雷达欢迎五类贡献。所有数据类贡献的唯一硬性要求是**来源与日期**，无法溯源的信息不会被纳入。

## 1. 提交信号或信源

用 [信号提交模板](../../issues/new?template=signal-submission.md) 开 issue。

## 2. 提交采购记录

发现大模型/AI 相关中标公告，用 [采购记录模板](../../issues/new?template=procurement-record.md) 开 issue，或直接 PR 追加到 `data/procurement/` 当月 CSV。字段定义见 [data/README.md](data/README.md)。原始公告链接必填；把公告原件一并存到 `evidence/` 的，直接记 A 级。

## 3. 提交 Radar Pack

想监控一个新职业或新行业？PR 一个 `packs/你的方向.yml`（格式见 [schemas/radar.schema.json](schemas/radar.schema.json)，参考现有 pack）。这是门槛最低的贡献方式，社区视角是本项目最想要的资产。

## 4. 纠错

报告或数据里的错误、过时、口径歧义，用 [纠错模板](../../issues/new?template=correction.md) 开 issue。纠错是对这个项目最有价值的贡献之一，会被优先处理。

## 5. 改进方法论与提示词

`docs/methodology.md` 和 `prompts/weekly-agent-prompt.md` 接受 Pull Request。建议先在 issue 里说明改动想解决的问题，再提 PR。

## 几条原则

- 所有数据必须带来源与日期，这是本项目的地基
- 证据分级定义以 [methodology.md](docs/methodology.md) 为唯一标准
- 失败教训与成功案例同等权重，欢迎补充避坑类信号
- PR 会经过数据校验 CI（schema、CSV 表头、LATEST 一致性），提交前可本地运行 `python scripts/validate_data.py`
- 讨论对事不对人，用中文或英文都可以

## 维护方式说明

本项目由人类维护者（@MoonHuang0325）与 AI Agent 协作维护：周报的调研与撰写由 AI 自动执行，框架、选题与最终发布由人类负责。你提交的 issue 和 PR 也会以同样的人机协作方式处理，人类对每一次合并负责。
