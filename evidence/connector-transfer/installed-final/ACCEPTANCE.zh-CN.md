# MacLean 3.0.0-rc.1 验收记录

日期：2026-10-19；规则库：1.1.0；基线：用户提供的开发基准 1.0 与资料包 1.0.0。

这是可安装、可执行的候选版本。**不声称已完成所有正式发布验收。** 未验证的产品版本和网页宿主组合列在下方。没有删除用户真实缓存；破坏性测试只在新建临时 fixture 中执行。真实目录仅用于指定范围的只读覆盖检查。

## 已执行

| 检查 | 结果与证据 |
|---|---|
| 原始资料校验器 | 56 条规则、125 个合成决策用例通过；`validation/baseline.json` |
| 生产路径所有权匹配 | 将全部 125 个原始案例接入生产 RuleBook，比较具体所有权与保护关系；不把案例 facts 当运行证据 |
| 生产核心测试 | 62 个 unittest 测试方法通过，详见 `validation/tests.log`；包含真实文件系统、原生工具与明确标记的模拟签名探针 |
| 本地真人批准 | 原生 macOS 对话框确认→临时 28 KiB 缓存执行→收据通过；`validation/human-local-result.json` |
| 连接器真人批准 | Mac MCP Gateway 发起相同核心，原生对话框确认→独立临时 fixture 执行→收据通过；`validation/human-connector-result.json` |
| 本地／连接器模拟批准流程 | 均通过；证据明确写 simulated_fixture_only，不替代上面的人工作业 |
| uv 原生维护 | uv 0.12.5 独立缓存清理、内部链接、外部链接拒绝、外部共享锁、取消；使用 `uv cache clean`，无 --force |
| 完整等待时限 | 外部锁占用约 30.07 秒后 pending，缓存保留；`validation/native-wait-limit.json` |
| npm 原生维护 | npm 12.2.0 的内容缓存与整个 npx 缓存清理通过；npx 原生命令要求 --force；未安装或执行任何 npx 包 |
| 实机只读覆盖 | 指定 Codex log 与 Cursor Cache/GPUCache；发现 2 个 Cursor 已验证缓存目标，扫描完整；未生成真实删除批准 |
| UI | 本地浏览器检查桌面与 320px 明／暗，键盘空格选择、Tab/回车展开；无外链资源；截图 `validation/report-320-light-dark.png` |
| SKILL 格式 | skill-creator quick_validate 通过；验证工具使用已有 conda Python，核心仍无第三方依赖 |
| 安装校验 | ZIP 字节／版本／逐文件校验、缺块、错误哈希、路径穿越、未列出文件、拒绝覆盖既有目录测试通过 |

## 适用验收矩阵

| 领域 | 状态 | 具体范围／限制 |
|---|---|---|
| 根绑定 | 已实现、fixture 验证 | 当前 uid HOME；HOME/SUPPORT 不可覆盖；允许环境键及显式映射；原生根查询；拒绝 root／非 Mac 执行 |
| 标准目录 | 已验证 | Library、沙盒、应用组、AI 诊断；`.DS_Store` 不打断通配目录发现；特殊文件不阻断独立普通文件 |
| 路径与身份 | 已验证主要回归 | 文件／父路径替换、链接、穿越、范围边界、硬链接、删除瞬间替换；动态挂载切换／恶意同 uid 任意修改执行代码不作已验证声明 |
| 枚举预算 | 已实现、fixture 验证 | 50,000／180 秒共享预算、单目标 50,000／30 秒、6 层项目发现；取消保存部分记录；continue_path 提供缩小范围的新扫描入口，不是完整快照续传游标 |
| 证据与隐私 | 已验证 | 受限 JSON／plist、43 字节缓存标签、源码配对元数据、Git 候选范围查询；不读取源码／会话／日志正文 |
| 项目缓存 | 已验证 | 脏项目仍可清独立缓存；已跟踪项保留；Next fetch-cache、pytest 未知键、Ruff 未知子树、无源码字节码保留 |
| 活动冲突 | 已验证 | 在线日志不按进程名阻断；具体项目／下载副本引用及 uv 原生锁只影响相关目标；取消不继续后续动作 |
| 原生域边界 | 已验证 | 完整域批准；保护项、用户保留项或不支持布局不能回退直接删除；版本不匹配进入待调查 |
| 浏览器下载副本 | 协议 fixture 通过 | Playwright 完成标记／缺标记、内部／外部链接、打开引用；Puppeteer 布局、别名和 executablePaths、并发元数据变更；未实际下载各官方浏览器版本并做再次安装恢复 |
| Claude 退休 | 契约测试通过，真实版本未验证 | 完整数字 semver；当前＋最新两个签名有效版本；Mach-O、厂商签名、磁盘属性、运行引用；生命周期测试用模拟 codesign/diskutil 输出，不能算真实 Anthropic 二进制验收 |
| 重叠与空间 | 已验证 | 所有权阻止父域绕过子域；硬链接按设备/inode 去重；计划量、处理量、清单残留和卷空闲变化分列；硬链接因本次 unlink 改变身份而跳过的其他别名需要新扫描 |
| 批量批准 | 人工正向＋自动反例通过 | 摘要、到期、篡改、伪造 channel/approved 拒绝；原生真人正向通过；人工取消／无 GUI 真人终端回退尚未人工验收 |
| 收据与中断 | 已验证 | 每项先写 started，完成后 fsync；已完成不重做；不确定动作 pending；局部错误继续；JSONL 末条若因异常硬中断损坏会拒绝读取，需检查原始收据，不能无证重跑 |
| 双宿主 | 本地与连接器命令流程通过 | **ChatGPT 网页端技能导入、展示和完整交互未验证**；不能以连接器 API 结果替代 |
| 发布 | 候选包 | 递归 manifest、ZIP、SHA-256、安装说明及源码交付；未公开发布、未覆盖旧版本、未开启持续维护 |

## 实际环境

- 本地执行：Codex 桌面会话，macOS 26.5.2（25F84）、Apple Silicon、Python 3.14.7。
- 连接器：Mac MCP Gateway，desktop-commander bridge 25 个工具，使用 `/bin/sh` 与 `/opt/homebrew/bin/python3`（3.14.7）。其默认 python3 实测为 3.9.6，低于最低要求；核心 capabilities 会报告不支持，不静默使用。
- 原生工具：uv 0.12.5（210d1f678）、npm 12.2.0。其他版本当前不获原生动作资格。
- Apple osascript、lsof、codesign、diskutil 接口在本机可用；codesign/diskutil 的 Claude 产品验证没有真实样本。
- Chrome／Electron／编辑器／Next／Cargo／pytest／Ruff／Playwright／Puppeteer 的布局 fixture 经过测试；没有据此宣称所有应用版本实测兼容。

## 仍保留的研究项

完整路径与逐条 gap 见 [规则覆盖表](COVERAGE.zh-CN.md) 和 [catalog.json](rules/catalog.json)。共 17 条 research，12 条 protected；无 research 转为可执行。

Codex arg0 的公开写入端确认了持锁和退休协议，但尚未完成对应 Rust 客户端版本与 Python/macOS 的交叉锁集成。daemon 的历史选择、迁移、安装／生命周期锁不能用 semver 排序替代；桌面 `payload/` 暂存没有公开安装器完成判据。Cursor 官方安装器证明了 CLI 的两个 launcher 指向版本目录，但 worker 无 current 的布局、运行消费者和回退职责仍未补齐。上述对象继续只读发现。

## 验收复现

见 [安装与调用](INSTALL.zh-CN.md)。源码 `tests/` 包含全部测试，`tools/fixture_flow.py --human` 可重做人工批准 fixture，`tools/check_wait_limit.py` 验证完整 30 秒锁等待。自动批准测试入口不包含在安装包中，也不得用于用户真实目录。
