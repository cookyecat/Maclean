#!/usr/bin/env python3
"""Regenerate RULES.md and SOURCES.md from the development catalog only."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def render():
    catalog = json.loads((HERE / "catalog.json").read_text(encoding="utf-8"))
    lines = [
        "# 完整扫描规则索引", "",
        "由 `render_reference.py` 从 `catalog.json` 生成；修改规则应先修改 JSON。", "",
        "这里列出的路径表达式全部参与规则匹配，不是示例路径。`${ROOT}` 的实际绑定见文末。",
        "`ready` 是开发契约就绪；只有身份探针、适配器和批准均通过才能执行。", "",
        "| 规则 ID | 分类 | 成熟度 | 用途 |", "|---|---|---|---|",
    ]
    for rule in catalog["rules"]:
        lines.append(f"| [{rule['id']}](#{rule['id']}) | {rule['category']} | {rule['status']} | {rule['purpose']} |")
    lines += [""]
    for rule in catalog["rules"]:
        lines += [f"## {rule['id']}", "", rule["purpose"], "",
                  f"- 版本：{rule['version']}；成熟度：`{rule['status']}`；优先级：{rule['priority']}。",
                  f"- 选择范围：`{rule['selection']}`；判定：`{rule['disposition']}`；默认选中：{str(rule['default_selected']).lower()}。",
                  f"- 动作：`{rule['action']}`；协议：`{rule['execution_protocol']}`。",
                  "- 身份检查：" + ("、".join(f"`{f}`" for f in rule["identity_checks"]) or "标准域语义 + 全局范围/身份/例外检查") + "。",
                  f"- 恢复：{rule['recovery']}。", f"- 影响：{rule['impact']}。",
                  f"- 费用字段：`{rule['inference_cost_effect']}`。",
                  "- 来源：" + "、".join(f"[{sid}](SOURCES.md#{sid})" for sid in rule["evidence_sources"]) + "。",
                  "- 验证范围：文档/源码审阅；实际执行测试见 ACCEPTANCE.zh-CN.md，不能把 fixture 当应用版本验收。"]
        if rule["gap"]:
            lines.append("- 待补证据/实现：" + rule["gap"])
        for selector in rule["selectors"]:
            lines += ["", f"根 `{selector['root']}`；目标类型 `{selector['kind']}`：", "", "```text"]
            lines += ["${" + selector["root"] + "}" + ("" if p == "." else "/" + p)
                      for p in selector["patterns"]]
            lines += ["```"]
        lines += [""]
    lines += ["## 根绑定", ""]
    for name, root in catalog["roots"].items():
        lines += [f"### {name}", "", f"默认：`{root['default'] or '必须由用户选定'}`", "", root["resolution"], ""]
    lines += ["## 身份探针定义", "", "以下是需要开发的探针，不能由模型提供真假值代替。", ""]
    for name, definition in catalog["facts"].items():
        lines += [f"### {name}", "", definition, ""]
    lines += ["## 执行协议定义", ""]
    for name, definition in catalog["protocols"].items():
        lines += [f"### {name}", "", definition, ""]
    (HERE / "RULES.md").write_text("\n".join(lines), encoding="utf-8")

    sources = ["# 规则来源与研究边界", "",
               f"审阅日期：{catalog['reviewed_on']}。来源用于说明路径和用途，不代替版本适配测试。", "",
               "证据类型：official-doc / official-source 为原始文档或写入端源码；maintainer-test-plan 为维护者测试记录；cross-check 仅作交叉线索；local-observation 仅证明本机出现过该布局；product-policy 是本产品明确边界。", "",
               "固定提交链接可以复核同一份 Codex/Mole 源码；main/canary/HEAD 和在线文档会变化，应在适配器发布时补充实际版本或内容摘要。", "",
               "本次没有对这些应用的全部版本作运行兼容性保证；catalog 中 application_versions_tested 留空，避免把资料审阅冒充实机验收。", ""]
    for sid, source in catalog["sources"].items():
        sources += [f"## {sid}", "", f"类型：`{source['kind']}`；审阅：{source['reviewed_on']}。", ""]
        if source["url"]:
            sources += [f"[原始来源]({source['url']})", ""]
        sources += [source["note"], ""]
    (HERE / "SOURCES.md").write_text("\n".join(sources), encoding="utf-8")


if __name__ == "__main__":
    render()
