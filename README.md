# Capability Radar

**What skills are appreciating? What AI capabilities are companies actually paying for?**
An open-source radar that answers both questions, every week.

![Capability Radar](.github/social-preview.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/MoonHuang0325/capability-radar?style=social)](https://github.com/MoonHuang0325/capability-radar/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/MoonHuang0325/capability-radar?style=social)](https://github.com/MoonHuang0325/capability-radar/network/members)
![Last commit](https://img.shields.io/github/last-commit/MoonHuang0325/capability-radar)
[![radar-watchdog](https://github.com/MoonHuang0325/capability-radar/actions/workflows/radar-watchdog.yml/badge.svg)](https://github.com/MoonHuang0325/capability-radar/actions/workflows/radar-watchdog.yml)

> 🌍 [中文 README](README.zh-CN.md)

## This week's signals (2026-08-13)

| Signal | Momentum | Evidence |
|---|---|---|
| Agent building / workflow automation | ↑ Strongest for 2 consecutive weeks | [B-class applied dev roles = 43.8% of new AI job posts](data/signals/2026-08-13-maimai-b-class-jobs-share.yml) |
| AI evaluation & observability | ↑ Largest employer supply gap | [Report](reports/2026-08-13.md) |
| LLM security procurement (finance/gov) | ↑ Entering centralized procurement catalogs | [Bank of Beijing award notice · Grade A](data/signals/2026-08-13-bank-of-beijing-llm-security-gateway.yml) |

**▶ [Read the latest issue](LATEST.md)　🚀 [Create your own radar](https://github.com/MoonHuang0325/capability-radar/generate)　📊 [Structured signal data](data/)**

---

## It watches two markets

The two most honest market signals of AI adoption:

- **Talent market** — who companies are preparing to pay salaries to: which skills are appreciating, which are depreciating
- **Procurement market** — what companies are paying for right now: award notices are the most honest transformation data

Newsletters tell you *what happened*. Capability Radar tells you **what is becoming more important**. Every issue is compared signal-by-signal against the previous one — marked as new / strengthening / fading — so you see momentum, not isolated snapshots.

## Create My Radar

This is a **template repository** — you don't fork it, you generate your own:

1. **[Create My Radar](https://github.com/MoonHuang0325/capability-radar/generate)** → edit [radar.yml](radar.yml) to pick what you care about (or use a preset from [packs/](packs/): AI Product Manager / Developer / Finance / Manufacturing)
2. Copy [prompts/weekly-agent-prompt.md](prompts/weekly-agent-prompt.md) into your AI agent (any agent with web search + scheduled tasks works)
3. Set it to run weekly — reports and structured signals accumulate automatically

Built-in watchdog: a weekly GitHub Action checks whether the report was updated on time and opens an issue if it wasn't (see [ROADMAP](ROADMAP.md) and `.github/workflows/`).

## Three design principles

1. **Tiered evidence** — every signal carries an A/B/C evidence grade. A = primary source, click-verifiable; B = authoritative secondary; C = unverified. Data you can bring into a meeting.
2. **Failures weigh as much as successes** — the enterprise track collects both adoption cases and abandoned pilots. Avoidance intel isn't cheaper than success stories.
3. **Human/agent division of labor** — the human sets framework, topics, and judges signal importance; the AI agent runs weekly research, writing, and comparison. This project is itself a public experiment in "how work gets done in the AI era."

## Repository structure

```
├── LATEST.md           # Latest full report
├── reports/            # Weekly intelligence snapshots (archived by date)
├── data/               # Structured signals (YAML) & procurement records (CSV), A/B/C graded
│   ├── signals/
│   └── procurement/
├── schemas/
│   └── signal.schema.json  # Signal data format definition
├── radar.yml           # Radar config: the one file you edit after generating
├── packs/              # Preset monitoring lenses (AI PM / Developer / Finance / Manufacturing)
├── prompts/
│   └── weekly-agent-prompt.md  # Reusable weekly monitoring prompt
├── roadmap/            # Evidence-backed AI transition roadmaps per role
├── docs/
│   └── methodology.md  # Full methodology: source tiers, evidence grading, diff mechanism
├── ROADMAP.md          # Project roadmap: what's planned, what's explicitly not
├── CONTRIBUTING.md     # How to submit signals, corrections, methodology improvements
└── LICENSE
```

## Data & licensing

Code is [MIT](LICENSE). Third-party source material remains the property of its original publishers — this project indexes, extracts facts, and archives verification copies. See [DATA_NOTICE.md](DATA_NOTICE.md).

## Contributing

- Roadmap and "what we won't do": [ROADMAP.md](ROADMAP.md)
- Submit signals, corrections, methodology improvements: [CONTRIBUTING.md](CONTRIBUTING.md)

## Author

[@MoonHuang0325](https://github.com/MoonHuang0325) — direction curated by a human, research & writing executed by an AI agent, maintained weekly.
