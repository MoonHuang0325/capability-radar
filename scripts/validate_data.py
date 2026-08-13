#!/usr/bin/env python3
"""能力雷达数据校验器：CI 中运行，任一检查失败以非零退出。"""
import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

import jsonschema
import yaml
from jsonschema import FormatChecker

ROOT = Path(__file__).resolve().parent.parent
errors = []


def err(msg):
    errors.append(msg)
    print(f"FAIL {msg}")


def ok(msg):
    print(f"  ok {msg}")


signal_schema = json.loads((ROOT / "schemas/signal.schema.json").read_text(encoding="utf-8"))
radar_schema = json.loads((ROOT / "schemas/radar.schema.json").read_text(encoding="utf-8"))

# 1. data/signals/*.yml：schema、id 唯一、文件名日期一致、A 级硬约束、previous 引用完整性、动量可审计
records = {}
for f in sorted((ROOT / "data/signals").glob("*.yml")):
    rec = yaml.safe_load(f.read_text(encoding="utf-8"))
    try:
        jsonschema.validate(rec, signal_schema, format_checker=FormatChecker())
    except jsonschema.ValidationError as e:
        err(f"{f.name}: schema 校验失败: {e.message}")
        continue
    if rec["id"] in records:
        err(f"{f.name}: id 重复 {rec['id']}")
    records[rec["id"]] = rec
    if not f.name.startswith(rec["date"]):
        err(f"{f.name}: 文件名日期与 date 字段不一致")

for rec in records.values():
    rid = rec["id"]
    if rec["confidence"] == "A":
        if not rec["source"].get("url"):
            err(f"{rid}: A 级证据缺少 source.url")
        if not rec.get("archive"):
            err(f"{rid}: A 级证据缺少 archive 存档")
        elif rec["archive"].get("type") == "repo":
            if not (ROOT / rec["archive"]["path"]).exists():
                err(f"{rid}: archive 路径不存在 {rec['archive']['path']}")
        elif rec["archive"].get("type") == "wayback":
            if not re.search(r"/web/\d{14}/", rec["archive"].get("path", "")):
                err(f"{rid}: wayback archive 必须带 14 位时间戳快照地址: {rec['archive'].get('path')}")
    if rec["source"].get("url") is None and rec["confidence"] != "C":
        err(f"{rid}: 无原始链接但 confidence 不是 C")
    if rec["status"] != "new" and not rec.get("status_reason"):
        err(f"{rid}: status 为 {rec['status']} 时必须填写 status_reason（动量必须可审计）")
    prev = rec.get("previous_signal_id")
    if prev is not None:
        if prev not in records:
            err(f"{rid}: previous_signal_id 指向不存在的记录 {prev}")
        else:
            prec = records[prev]
            if prec["series_id"] != rec["series_id"]:
                err(f"{rid}: previous 的 series_id 与本记录不一致（{prec['series_id']} != {rec['series_id']}）")
            if date.fromisoformat(prec["date"]) >= date.fromisoformat(rec["date"]):
                err(f"{rid}: previous 日期必须早于本记录日期")

series_seen = set()
for rec in records.values():
    key = (rec["series_id"], rec["date"])
    if key in series_seen:
        err(f"series_id + date 重复: {key}")
    series_seen.add(key)
ok("signals 校验完成")

# 2. radar.yml 与 packs/*.yml 通过 radar schema
for f in [ROOT / "radar.yml", *sorted((ROOT / "packs").glob("*.yml"))]:
    rec = yaml.safe_load(f.read_text(encoding="utf-8"))
    try:
        jsonschema.validate(rec, radar_schema)
    except jsonschema.ValidationError as e:
        err(f"{f.relative_to(ROOT)}: 配置校验失败: {e.message}")
ok("radar.yml 与 packs 校验完成")

# 3. 采购 CSV：表头一致 + 证据等级合法 + A 级必须有原始链接
expected_header = ["项目名", "采购人", "采购人类型", "行业", "省份", "中标方", "金额(元)", "公告日期", "项目类型", "场景", "原始公告URL", "抓取日期", "证据等级"]
for f in sorted((ROOT / "data/procurement").glob("*.csv")):
    with f.open(encoding="utf-8") as fh:
        reader = csv.reader(fh)
        header = next(reader, None)
        if header != expected_header:
            err(f"{f.name}: 表头与 data/README.md 定义不一致: {header}")
            continue
        for lineno, row in enumerate(reader, start=2):
            if not row:
                continue
            level = row[12].strip()
            url = row[10].strip()
            if level not in ("A", "B", "C"):
                err(f"{f.name}:{lineno}: 证据等级非法 '{level}'")
            if level == "A" and not url:
                err(f"{f.name}:{lineno}: A 级记录缺少原始公告URL")
ok("采购 CSV 校验完成")

# 4. LATEST.md 与最新 reports/*.md 一致
reports = [p for p in (ROOT / "reports").glob("*.md") if re.fullmatch(r"\d{4}-\d{2}-\d{2}\.md", p.name)]
if not reports:
    err("reports/ 下没有符合 YYYY-MM-DD.md 命名的报告")
else:
    latest = sorted(reports)[-1]
    latest_md = ROOT / "LATEST.md"
    if not latest_md.exists():
        err("LATEST.md 不存在")
    elif latest_md.read_text(encoding="utf-8") != latest.read_text(encoding="utf-8"):
        err(f"LATEST.md 与最新报告 {latest.name} 内容不一致")
    else:
        ok(f"LATEST.md 与 {latest.name} 一致")

print()
if errors:
    print(f"共 {len(errors)} 项失败")
    sys.exit(1)
print("全部校验通过")
