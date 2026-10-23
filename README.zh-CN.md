# MacLean

基于提供的两部分基准从零实现的 macOS 清理技能。当前候选版 **3.0.0-rc.2**，规则库 **1.1.0**。核心仅使用 Python 标准库；本地 Agent 和既有 Mac 连接器调用同一代码。

[rc.2 扫描修复与验证结果](macos-disk-auditor/RELEASE.zh-CN.md)

**第一次使用？阅读 [Quick Start：下载安装与首次清理](QUICKSTART.zh-CN.md)。**

- 安装技能：`macos-disk-auditor/`。
- 安装与调用：`macos-disk-auditor/INSTALL.zh-CN.md`。
- 实际验收与未验证范围：`macos-disk-auditor/ACCEPTANCE.zh-CN.md`。
- 全部规则、保护范围与研究缺口：`macos-disk-auditor/COVERAGE.zh-CN.md`、`rules/catalog.json`。
- 自动测试：`tests/`；独立验收入口：`tools/fixture_flow.py`。
- ZIP 与 SHA-256：`dist/`。
- 原始基准和资料包保持在原位置；未改写或冒用其 VALIDATION.json。

```sh
/opt/homebrew/bin/python3 macos-disk-auditor/scripts/maclean.py capabilities
python3 -m unittest discover -s tests -v
```

默认只扫描固定缓存入口。项目必须通过 `--project` 明确选择。扫描不等于删除；删除必须经过封存计划和真人原生批准。测试自动批准仅能用于可丢弃 fixture，不属于安装技能的命令接口。未公开发布，未开启维护，未删除真实缓存。

当前不是“所有宿主、应用版本和验收项均通过”的正式发布：ChatGPT 网页端导入与展示、真实 Claude 签名版本退休、各浏览器官方运行时再安装恢复，以及动态挂载等仍未完整验证，详见验收记录。
