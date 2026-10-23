#!/usr/bin/env python3
"""Validate the development catalog and synthetic path/decision examples.

This is NOT a Mac scanner, evidence probe, approval service, or cleanup engine.
It reads only the adjacent catalog and cases JSON. It never executes a tool,
walks a user directory, or modifies a cache. Facts in cases are test inputs;
production facts must be computed by trusted, versioned adapters.
"""
from __future__ import annotations

import fnmatch
import json
import re
from collections import Counter
from pathlib import Path, PurePosixPath


HERE = Path(__file__).resolve().parent
ACTIONS = {
    "none", "clear_files", "native_npm_clean", "native_npx_rm",
    "native_uv_clean", "remove_downloaded_runtime",
    "remove_puppeteer_runtime", "retire_claude_version",
}
ROUTES = {
    "online_inventory": "online", "project_cache": "online",
    "native_npm": "coordinated", "native_npx": "coordinated",
    "native_uv": "coordinated", "download_runtime": "coordinated",
    "puppeteer_runtime": "coordinated", "claude_retirement": "coordinated",
    "none": "unsupported",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical_syntax(path):
    return (isinstance(path, str) and path.startswith("/")
            and "\x00" not in path and "//" not in path
            and all(p not in {".", ".."} for p in path.split("/")[1:])
            and (path == "/" or not path.endswith("/")))


def validate_schema(catalog):
    require(catalog["schema_version"] == 1, "unsupported schema")
    require(catalog["purpose"] == "development_baseline_not_current_runtime_configuration",
            "catalog must be labelled as development material")
    ids = set()
    for rule in catalog["rules"]:
        rid = rule["id"]
        require(bool(re.fullmatch(r"[a-z][a-z0-9-]+", rid)), f"invalid id {rid}")
        require(rid not in ids, f"duplicate id {rid}")
        ids.add(rid)
        require(rule["status"] in {"ready", "research", "protected"}, rid)
        require(rule["category"] in {"app", "ai", "development"}, rid)
        require(rule["action"] in ACTIONS, f"unknown action in {rid}")
        require(rule["execution_protocol"] in catalog["protocols"], rid)
        require(rule["execution_protocol"] in ROUTES, rid)
        require(rule["selection"] in {"contents", "target", "native_domain"}, rid)
        require(type(rule["priority"]) is int and rule["priority"] > 0, rid)
        require(type(rule["version"]) is int and rule["version"] > 0, rid)
        ready = rule["status"] == "ready"
        require(rule["default_selected"] is ready, f"invalid selection default: {rid}")
        require((rule["action"] != "none") == ready, f"invalid action: {rid}")
        require((rule["execution_protocol"] != "none") == ready, rid)
        expected = {"ready": "disposable", "research": "investigate", "protected": "retain"}
        require(rule["disposition"] == expected[rule["status"]], rid)
        if rule["status"] == "research":
            require(bool(rule["gap"]), f"research needs explicit gap: {rid}")
        require(bool(rule["evidence_sources"]), f"missing evidence: {rid}")
        require(all(s in catalog["sources"] for s in rule["evidence_sources"]), rid)
        require(all(f in catalog["facts"] for f in rule["identity_checks"]), rid)
        for selector in rule["selectors"]:
            require(selector["root"] in catalog["roots"], rid)
            require(selector["kind"] in {"directory", "file", "any"}, rid)
            require(bool(selector["patterns"]), rid)
            for pattern in selector["patterns"]:
                require(isinstance(pattern, str) and bool(pattern), rid)
                if pattern == ".":
                    require(selector["root"] not in {"HOME", "SUPPORT", "PROJECT"}, rid)
                    continue
                require(not pattern.startswith("/") and not pattern.endswith("/"), rid)
                require(all(p not in {"", ".", ".."} for p in pattern.split("/")), rid)
                require(not any(c in pattern for c in ["\x00", "\n", "`", "$", ";", "\\"]), rid)
                if "**" in pattern:
                    require(rid == "python-bytecode" and pattern == "**/__pycache__/*.pyc", rid)
    for sid, source in catalog["sources"].items():
        require(source["reviewed_on"] and source["note"], sid)
        if source["url"] is None:
            require(source["kind"] in {"local-observation", "product-policy"}, sid)
        else:
            require(source["url"].startswith("https://"), sid)


def segment_match(relative, pattern, max_depth):
    """Case-sensitive segment matching; never shell globbing or realpath."""
    parts = () if str(relative) == "." else relative.parts
    wanted = () if pattern == "." else tuple(pattern.split("/"))
    if wanted and wanted[0] == "**":
        prefix_len = len(parts) - (len(wanted) - 1)
        return (0 <= prefix_len <= max_depth
                and all(fnmatch.fnmatchcase(p, w)
                        for p, w in zip(parts[prefix_len:], wanted[1:])))
    return len(parts) == len(wanted) and all(
        fnmatch.fnmatchcase(p, w) for p, w in zip(parts, wanted))


def owners(catalog, roots, path, kind):
    """Find matching anchors, including directory ownership of descendants."""
    results = []
    target = PurePosixPath(path)
    for rule in catalog["rules"]:
        for selector in rule["selectors"]:
            root_text = roots.get(selector["root"])
            if root_text is None:
                continue
            require(canonical_syntax(root_text) and root_text != "/", "invalid fixture root")
            root = PurePosixPath(root_text)
            for anchor in (target, *target.parents):
                try:
                    relative = anchor.relative_to(root)
                except ValueError:
                    continue
                anchor_kind = kind if anchor == target else "directory"
                if selector["kind"] not in {"any", anchor_kind}:
                    continue
                if any(segment_match(relative, p, catalog["global_policy"]["max_project_depth"])
                       for p in selector["patterns"]):
                    score = (rule["status"] == "protected", rule["priority"], len(anchor.parts))
                    results.append((score, rule, str(anchor)))
    return results


def decide(catalog, roots, case):
    """Reference decision on synthetic evidence, NOT a production safety check."""
    output = dict(rule=None, disposition="investigate", selected=False,
                  execution_route="unsupported", planning_state="uncovered", reason="no_rule")
    if not canonical_syntax(case["path"]):
        output.update(disposition="retain", planning_state="retained", reason="unsafe_path")
        return output
    matches = owners(catalog, roots, case["path"], case.get("kind", "directory"))
    if not matches:
        return output
    matches.sort(key=lambda item: item[0], reverse=True)
    score, rule, _ = matches[0]
    if len({r["id"] for s, r, _ in matches if s == score}) > 1:
        output.update(planning_state="preview", reason="ambiguous_owner")
        return output
    output["rule"] = rule["id"]
    context = case.get("context", {})
    for flag in ("out_of_scope", "symlink_ancestor", "is_symlink", "special_file",
                 "user_keep", "unique_content", "paid_model_dependency", "tracked_candidate"):
        if context.get(flag, False):
            output.update(disposition="retain", planning_state="retained", reason=flag)
            return output
    if rule["status"] != "ready":
        output.update(disposition=rule["disposition"], reason=rule["status"],
                      planning_state="retained" if rule["status"] == "protected" else "preview")
        return output
    missing = [f for f in rule["identity_checks"] if case.get("facts", {}).get(f) is not True]
    if missing:
        output.update(planning_state="preview", reason="identity_unverified")
        return output  # IMPORTANT: no fallback to a generic lower-priority owner.
    protocol = rule["execution_protocol"]
    output.update(disposition="disposable", execution_route=ROUTES[protocol])
    if context.get("measurement_partial", False):
        output.update(planning_state="preview", reason="measurement_partial")
        return output
    if case.get("bytes", 1) == 0:
        output.update(planning_state="empty", reason="zero_bytes")
        return output
    if context.get("identity_changed", False):
        output.update(planning_state="preview", reason="identity_changed")
        return output
    output.update(selected=True, planning_state="ready", reason="verified")
    if protocol != "online_inventory" and (
            context.get("target_in_use", False) or context.get("native_lock_busy", False)):
        output.update(execution_route="after_task", planning_state="pending", reason="wait_target")
    return output


def run():
    catalog = json.loads((HERE / "catalog.json").read_text(encoding="utf-8"))
    examples = json.loads((HERE / "cases.json").read_text(encoding="utf-8"))
    validate_schema(catalog)
    seen = set()
    exercised = set()
    for case in examples["cases"]:
        require(case["id"] not in seen, f"duplicate case {case['id']}")
        seen.add(case["id"])
        require(set(case.get("facts", {})) <= set(catalog["facts"]), case["id"])
        roots = {**examples["roots"], **case.get("root_overrides", {})}
        result = decide(catalog, roots, case)
        for field, expected in case["expect"].items():
            require(result.get(field) == expected,
                    f"{case['id']}: {field}: expected {expected!r}; got {result!r}")
        if result["rule"]:
            exercised.add(result["rule"])
        matching_ids = {r["id"] for _, r, _ in owners(
            catalog, roots, case["path"], case.get("kind", "directory"))}
        for rid in case.get("expect_matches", []):
            require(rid in matching_ids, f"{case['id']}: missing discovery match {rid}")
            exercised.add(rid)
    missing = {r["id"] for r in catalog["rules"]} - exercised
    require(not missing, f"rules without a synthetic ownership case: {sorted(missing)}")
    print(json.dumps({
        "catalog_version": catalog["catalog_version"], "rules": len(catalog["rules"]),
        "statuses": dict(Counter(r["status"] for r in catalog["rules"])),
        "synthetic_cases_passed": len(seen), "rules_covered_by_expectations": len(exercised),
        "scope": "schema_and_synthetic_decisions_only",
        "real_scan": False, "real_cleanup": False,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    run()
