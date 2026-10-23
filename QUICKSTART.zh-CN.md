# MacLean Quick Start

MacLean 帮你找出 Mac 上可以清理的应用缓存、普通诊断日志、AI 工具缓存，以及你指定的开发项目缓存。先查看报告、选择目标，再由你确认删除。

**第一次使用：下载技能包 → 安装 → 让 Agent 扫描 → 查看报告 → 确认清理。**

当前版本为 **3.0.0-rc.2（候选版）**。本地执行和 Mac MCP Gateway 命令流程已经验证；ChatGPT 网页端完整交互尚未验证。部分目录仍只提供发现与说明，不开放删除。

## 1. 准备环境

- 一台 Mac，使用普通用户账户，不使用 `sudo`。
- Python **3.10 或更新版本**。终端运行 `python3 --version` 检查；如果显示 3.9，请改用已安装的新版 Python 的完整路径。
- 支持本地技能及命令执行的 Agent；也可以直接使用下方终端命令。

MacLean 核心无需安装 pip 依赖，无需新增模型服务或 API Key。安装技能不会自动授予 Agent 访问 Mac 的权限。

## 2. 下载与安装

从项目提供的下载位置取得以下两个文件，放在同一个文件夹中：

- [`maclean-3.0.0-rc.2.zip`](dist/maclean-3.0.0-rc.2.zip)：普通用户安装这个包。
- [`maclean-3.0.0-rc.2.zip.sha256`](dist/maclean-3.0.0-rc.2.zip.sha256)：用于检查下载是否完整。

`-source.zip` 是开发者源码包，日常使用不需要下载。本文不假定项目已经有公开发布页；请使用维护者实际提供的文件。

假设文件位于“下载”文件夹，在终端检查：

```sh
cd ~/Downloads
shasum -a 256 -c maclean-3.0.0-rc.2.zip.sha256
```

看到 `maclean-3.0.0-rc.2.zip: OK` 后再解压。如果校验失败，重新获取文件。

**以 Codex 为例：**

1. 解压 ZIP，得到 `macos-disk-auditor` 文件夹。
2. 在 Finder 按 `⌘⇧G`，输入 `~/.codex/skills/`；若目录不存在，先在终端运行 `mkdir -p ~/.codex/skills`。
3. 把整个 `macos-disk-auditor` 文件夹放进去。最终应存在 `~/.codex/skills/macos-disk-auditor/SKILL.md`。
4. 新建会话并检查技能是否被加载；若未显示，按客户端的技能刷新方式重新加载。

如果已存在同名文件夹，请先保留旧版，不要直接合并覆盖。其他 Agent 使用其支持的技能安装入口，加载同一个 `SKILL.md`；各客户端的安装方式并不通用。

安装后检查能力：

```sh
python3 "$HOME/.codex/skills/macos-disk-auditor/scripts/maclean.py" capabilities
```

确认返回 `software_version: "3.0.0-rc.2"`、`mac_access: true` 和 `python_supported: true`。如需改用其他 Python，后续所有命令都使用同一个解释器路径。

## 3. 让 Agent 帮你使用

把下面这段话发给已加载技能的 Agent：

> 使用 macos-disk-auditor（MacLean）检查这台 Mac 的清理能力，然后扫描支持的缓存和普通诊断日志，生成本地 HTML 报告。先解释扫描范围、可以清理的目标及没有完成的检查，等我选择后再生成清理计划。

想清理开发项目时，明确给出项目的绝对路径，例如：

> 使用 MacLean 扫描 `/Users/你的用户名/Developer/你的项目` 的开发缓存，并生成报告。保留源码、配置和项目状态。

接下来按这个流程操作：

1. **查看报告。** 报告区分“现在可处理、等待处理、保留、待调查”。已验证的真缓存默认选中；可以取消不想处理的目标。
2. **导出选择。** 点击“导出选择的目标 ID”，保存 `selection.json`，把文件路径交给 Agent。
3. **查看计划。** 请 Agent 根据选择生成并展示计划，核对路径、作用域和影响。下载缓存或构建缓存清理后可能需要重新下载或编译。
4. **亲自确认。** 请 Agent 执行该计划，在 Mac 弹出的原生对话框中亲自选择批准或取消。在聊天里说“同意”不会替代这一步。
5. **查看收据。** 请 Agent 展示完成、等待、失败和跳过的结果，以及实际卷空闲空间变化。

HTML 报告本身不会删除文件。遇到等待或失败项，先处理冲突并重新扫描，再生成新计划。

## 4. 不用 Agent，也能在终端完成

以下示例沿用上面的 Codex 安装位置。在同一个终端中执行；将 `SCAN_ID`、`PLAN_ID`、`RECEIPT_ID` 替换为对应命令输出中的实际值。

```sh
MACLEAN_CLI="$HOME/.codex/skills/macos-disk-auditor/scripts/maclean.py"

# 扫描；记录输出中的 scan_id
python3 "$MACLEAN_CLI" scan

# 生成并打开扫描报告
python3 "$MACLEAN_CLI" report --record SCAN_ID --output "$HOME/Downloads/MacLean-scan"
open "$HOME/Downloads/MacLean-scan/report.html"
```

在报告中选择目标，导出 `selection.json`。假设它保存在“下载”文件夹：

```sh
# 生成计划；记录输出中的 plan_id
python3 "$MACLEAN_CLI" plan --scan SCAN_ID --selection "$HOME/Downloads/selection.json"
python3 "$MACLEAN_CLI" report --record PLAN_ID --output "$HOME/Downloads/MacLean-plan"
open "$HOME/Downloads/MacLean-plan/report.html"

# 核对计划后执行；此命令会请求真人批准
python3 "$MACLEAN_CLI" apply --plan PLAN_ID

# 执行后用返回的 receipt_id 生成收据报告
python3 "$MACLEAN_CLI" report --record RECEIPT_ID --output "$HOME/Downloads/MacLean-receipt"
open "$HOME/Downloads/MacLean-receipt/report.html"
```

若取消批准，命令会返回预览状态，不会生成本次执行收据。浏览器下载的选择文件若被重命名，请在命令中使用实际文件名。

常用扫描方式（任选其一）：

```sh
# 只扫描 AI 类别中已有规则支持的对象
python3 "$MACLEAN_CLI" scan --category ai

# 加入你明确选定的开发项目
python3 "$MACLEAN_CLI" scan --project "/绝对路径/你的项目"

# 明确保留一个目录
python3 "$MACLEAN_CLI" scan --keep "/绝对路径/需要保留的目录"
```

## 常见问题

**ChatGPT 网页端能直接清理我的 Mac 吗？** 需要既有 Mac 连接器具备文件传输、命令执行和结果读取权限，并在 Mac 上运行同一份包。仅上传 SKILL 不会获得这些能力。本版已验证 Mac MCP Gateway 命令流程，尚未验证 ChatGPT 网页端完整使用流程；接入方法见安装说明。

**为什么某个目录显示“待调查”或“保留”？** 当前证据不足、布局不支持或命中了保护规则。不会仅凭目录名或文件年龄删除，也不会绕过专用规则改用更宽泛的删除方式。

**为什么没有扫描完？** 报告会分别显示目标发现和大小计量是否完成，并列出权限不足、条目数上限或时间上限等原因。这里的限制与费用和 Token 无关。Agent 可以按具体未完成路径调整扫描限额再扫；不要把部分扫描当作全盘检查完成。

**清理的字节数为什么不等于新增空闲空间？** 文件占用与卷空闲变化是不同指标，报告会分别展示。

**记录保存在哪里？** 默认在当前用户的 `~/Library/Logs/MacLean`。HTML 和 Markdown 报告保存在你指定的输出目录。

更多信息：[完整安装说明](macos-disk-auditor/INSTALL.zh-CN.md) · [规则覆盖](macos-disk-auditor/COVERAGE.zh-CN.md) · [实际验收与未验证范围](macos-disk-auditor/ACCEPTANCE.zh-CN.md)
