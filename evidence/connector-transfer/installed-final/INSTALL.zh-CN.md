# MacLean 安装与使用

软件 `3.0.0-rc.1`，规则 `1.1.0`，安装标识 `macos-disk-auditor`。这是从本次开发基准重新实现的候选版本，不覆盖旧发布包。正式放行范围以 [验收记录](ACCEPTANCE.zh-CN.md) 为准。

## 安装

运行环境：非 root macOS 用户、Python ≥3.10。无需模型服务、API Key、pip 依赖或新增 MCP 服务。缺少 Python 时只报告缺项，不自动安装。

1. 从本地交付目录取得 ZIP 和 `.sha256`，先核对 SHA-256。摘要保证传输完整性，不是来源签名，也不是删除批准。
2. 解压 ZIP 到所用客户端的技能目录，或使用发布包附带的 `scripts/transport.py` 安装到一个尚不存在的新目录。
3. Codex 用户可将 `macos-disk-auditor` 文件夹放到 `~/.codex/skills/`；其他宿主按其技能加载机制登记 `SKILL.md`。不要覆盖现存旧版；先选择独立版本目录验证。
4. 使用明确的 Python 路径执行入口，检查能力和包摘要：

```sh
/opt/homebrew/bin/python3 /绝对技能目录/scripts/maclean.py capabilities
```

`/opt/homebrew/bin/python3` 是本次实测路径，不保证其他 Mac 存在。请使用本机实际 Python ≥3.10 路径。安装技能不会授予磁盘访问或连接器权限。

## 调用

所有记录默认保存在当前 uid 主目录的 `Library/Logs/MacLean`，权限 0700。stdout 为 JSON 摘要，完整清单落盘，不默认输出源码或日志正文。

```sh
python3 /绝对技能目录/scripts/maclean.py scan
python3 /绝对技能目录/scripts/maclean.py scan --project /用户选定项目
python3 /绝对技能目录/scripts/maclean.py inspect --path /用户选定路径
python3 /绝对技能目录/scripts/maclean.py scan --category ai --root-map CODEX_HOME=/自定义根
python3 /绝对技能目录/scripts/maclean.py report --record 扫描ID --output /本地报告目录
python3 /绝对技能目录/scripts/maclean.py plan --scan 扫描ID --selection /选择.json
python3 /绝对技能目录/scripts/maclean.py report --record 计划ID --output /计划报告目录
python3 /绝对技能目录/scripts/maclean.py apply --plan 计划ID
python3 /绝对技能目录/scripts/maclean.py report --record 收据ID --output /结果报告目录
```

选择文件是 JSON 字符串数组，内容仅为目标 ID，可从扫描报告导出。HTML 没有删除能力。`apply` 只接受计划 ID，不接受 `approved`、token 或任意 shell 命令。它在当前进程内调用原生对话框，获得用户确认后才执行。对话框不可用时仅在真人交互终端提供回退；没有批准能力时保留预览。批准最多 30 分钟且绑定完整计划 SHA-256。新增目标需要新计划和新批准。

`--keep /路径` 可多次指定；`--path /路径` 限制扫描范围。权限失败、预算耗尽、布局缺证会留在覆盖报告，使用错误中的 `continue_path` 配合 `--path` 缩小范围再扫；这是新扫描，不复用旧批准。项目发现最多 6 层，排除依赖环境与版本控制树，不执行项目配置脚本。非默认构建目录使用 `NEXT_DIST`、`CARGO_BUILD`、`PYTEST_CACHE`、`RUFF_CACHE` 的显式映射。

若需要不同记录目录，将全局参数放在命令之前：`--state-dir /绝对目录 scan ...`。该状态目录自动加入保留范围。收据不可作为新的批准凭据。中断、pending 或 failed 后先重新扫描，避免重复执行不确定的原生操作。

## 既有 Mac 连接器

连接器需具备文件写入／传输、受控命令执行、长任务查询、报告读取能力。宿主有连接器不等于当前工具权限足够；能力拒绝必须原样报告。

本次实测 Mac MCP Gateway 的工具映射：

| 操作 | 既有工具 |
|---|---|
| 连接检查 | `health_check` |
| 文本／Base64 原始传输 | `write_file`，首次 rewrite，续块 append |
| 执行同一 CLI | `start_process`，建议 `/bin/sh` 和绝对 Python 路径 |
| 等待／取结果 | `read_process_output` |
| 读取报告 | `read_file` |

先将交付 ZIP 的原始字节编码为 Base64，完整传到临时 `.b64` 文件，不让模型重写包内代码。把发布包原样附带的 `transport.py` 传给 Mac，校验其交付摘要后执行：

```sh
/绝对/python3 /已校验/transport.py --archive /临时/包.b64 --base64 \
  --sha256 发布ZIP的SHA256 --version 3.0.0-rc.1 --destination /新技能目录
```

若连接器支持二进制传输则直接传 ZIP，省略 `--base64`。缺块、错误哈希、错误版本、ZIP 路径穿越、符号链接和未列入 manifest 的文件都会拒绝；禁止静默回退。首次 `capabilities` 返回实际软件／规则版本和 manifest 摘要。原生人工批准必须由 Mac 用户完成；聊天中写“批准”不等于可信宿主批准事件。本版尚未接入任何特定宿主的可验证批准事件。

已验证连接器默认 `python3` 可能是 macOS 自带 3.9.6；不能假定与本地终端一致。本次用 `/opt/homebrew/bin/python3`（3.14.7）完成 connector fixture 流程。

## 验收与构建

源码交付根目录：

```sh
python3 '第二部分完整资料包/validate_catalog.py'
python3 -m unittest discover -s tests -v
python3 tools/fixture_flow.py --output evidence/local-fixture-flow
python3 tools/fixture_flow.py --human --output evidence/human-local-flow
python3 macos-disk-auditor/rules/render_reference.py
python3 tools/build_release.py
```

自动测试仅使用新建可丢弃 fixture；`fixture_flow.py` 的默认批准明确标记为模拟，不能作为原生批准验收。`--human` 需要用户亲自确认。测试脚本不随安装技能提供自动批准入口；它们位于源码交付中的 `tools/` 和 `tests/`。不要对真实缓存运行模拟批准。
