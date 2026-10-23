# MacLean SKILL 开发基准 · 第二部分：扫描目录与规则库

版本：1.0.0 · 资料审阅日期：2026-10-19 · 目标：macOS，Python ≥ 3.10

**实施者直接从本部分的 `catalog.json` 取得扫描位置。已确认的缓存由脚本匹配、校验和统计，使用阶段不再逐项请模型判定是否是垃圾。** AI 负责解释报告、处理用户选择，以及调查规则库尚未支持的对象。

本部分与第一部分开发文档一起使用。它是从零实现的规范和数据附件，尚未接入当前 v2.1.0 技能。这里的规则库版本 `1.0.0` 也不是技能发布版本。不要把本目录直接当作已完成、可安装的清理技能。

## 1. 交给实现者的文件

| 文件 | 用途 |
|---|---|
| [catalog.json](catalog.json) | 路径、匹配条件、动作、恢复与费用影响、证据、保留范围的权威数据源 |
| [RULES.md](RULES.md) | 从同一 JSON 生成的完整规则索引；每条列出全部路径表达式 |
| [SOURCES.md](SOURCES.md) | 官方文档、固定提交源码、交叉参考和本机观察的区别 |
| [cases.json](cases.json) | 合成路径与预期决策；实现者可将其映射为临时目录 fixture |
| [validate_catalog.py](validate_catalog.py) | 无第三方依赖的契约校验和参考匹配器；不会扫描或删除用户文件 |
| [ACCEPTANCE.md](ACCEPTANCE.md) | 本次实际验证结果，以及正式技能发布前尚需完成的验收 |

规则共 56 条：27 条 `ready`、17 条 `research`、12 条 `protected`。它们是规则数量，并非某台 Mac 的垃圾数量。

- **ready：** 路径和动作契约足够明确，可以据此开发适配器。适配器取得所需证据后默认选中。它不表示所有应用版本都实机验收过，也不等于删除批准。
- **research：** 知道应当去哪里查看，但用途或维护协议还存在明确缺口。可以显示占用与缺口，不能由普通缓存规则兜底删除。下一次开发研究应从这些位置开始。
- **protected：** 明确保留。包括会话、配置、凭据、依赖环境和特定混合状态域；不纳入普通清理金额/空间统计。

这三个状态属于**规则成熟度**。运行时仍分别记录 `disposition`、`execution_route`、授权和执行结果，不能混为一个“安全等级”。

## 2. 从哪里扫描

`~` 一律指执行清理的 **Mac 当前用户主目录**。网页端云环境的 HOME 不适用。以下是入口，不是可以整棵删除的目录。

### 2.1 macOS 应用缓存与日志

| 精确入口/模式 | 默认动作范围 | 对应规则 |
|---|---|---|
| `~/Library/Caches/*` | 子域内封存的普通缓存文件，排除专用域和保留域 | `macos-user-cache` |
| `~/Library/Logs/*` | 日志文件或子目录内的普通日志文件，保留清理审计记录 | `macos-user-log` |
| `~/Library/Containers/*/Data/Library/Caches` | 沙盒应用标准缓存域中的文件 | `sandbox-cache` |
| `~/Library/Containers/*/Data/Library/Logs` | 沙盒应用标准日志域中的文件 | `sandbox-log` |
| `~/Library/Group Containers/*/Library/Caches` | 实际存在的应用组标准缓存域中的文件 | `group-cache` |
| `~/Library/Group Containers/*/Library/Logs` | 实际存在的应用组标准日志域中的文件 | `group-log` |
| `~/Library/Application Support/<已登记应用>/<缓存叶目录>` | 只处理具体叶目录，通过对应应用布局检查 | `app-render-cache` 等 |
| `~/Library/Application Support/*/{Cache,Caches,cache,log,Log,logs,Logs}` | 未登记应用仅发现并计量；不按关键词递归删除 | `support-unreviewed-leaf` |

Apple 对 `Library/Caches` 的约定支持把可再生成缓存做成固定规则；`Application Support` 则可以保存用户数据，没有“名字包含 cache 就一定可删”的统一承诺。日志也不等于可重建的数据：本基准允许清理普通历史诊断，但报告必须说明历史诊断会丢失。依据见 [Apple 目录文档](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/MacOSXDirectories/MacOSXDirectories.html)。

**本版登记的应用与叶目录：**

- 普通应用数据根：`Code`、`Code - Insiders`、`VSCodium`、`Slack`、`Discord`、`Notion`、`Figma`、`Termius`。
- AI 应用数据根：`Codex`、`Claude`、`ChatGPT`、`Cursor`、`Windsurf`、`LM Studio`。
- 渲染缓存叶名：`Cache`、`Code Cache`、`GPUCache`、`ShaderCache`、`GrShaderCache`、`DawnCache`、`GraphiteDawnCache`、`DawnGraphiteCache`、`DawnWebGPUCache`。
- VS Code 系列另含 `CachedData`、`CachedExtensionVSIXs`、`logs`。`CachedExtensionVSIXs` 是下载包，不是已安装扩展目录。Cursor/Windsurf 的额外同名目录仍需独立产品验证，当前列为 `research`。
- Chromium 系浏览器根：`Google/Chrome`、`Google/Chrome Canary`、`Microsoft Edge`、`BraveSoftware/Brave-Browser`、`Chromium`、`Vivaldi`、`Arc/User Data`。只展开登记的 shader/code 叶目录及 `Default`、`Guest Profile`、`System Profile`、完整数字形式 `Profile N` 中的缓存叶目录。标准用户缓存位置仍由 Library 规则覆盖。

以上应用相对根都位于 `~/Library/Application Support`。它们是允许检查的位置，不承诺每个产品每个版本一定创建所有叶目录。不存在记 `absent`；布局不符记 `layout_unverified`；不要伪造为已扫描 0 字节。

渲染缓存检查使用固定应用根与多个 Chromium 缓存结构标记，不能只看单一名字。Cookie、IndexedDB、Local Storage、Service Worker、登录信息和整个 profile 不在清理范围。Electron 的 `sessionData` 同时包含持久状态和缓存，因此不能整目录清空。[Electron 路径说明](https://www.electronjs.org/docs/latest/api/app#appgetpathname)

`CloudKit` / FileProvider 同步域、字体/索引服务特定域、e5rt 运行资源、Deno/Poetry/R 的混合域等，使用独立保留规则。这里是本产品尚未建立专用动作的范围边界，不应宣传成“Apple 禁止清理这些路径”。同样，不扫描或删除 `/System`、`/Library`、`/private/var`、系统日志数据库、备份、邮件附件、文稿版本和废纸篓；它们需要另外的产品功能与授权范围。

### 2.2 AI 客户端与 Harness

| 产品 | 固定路径（默认） | 本版处理 |
|---|---|---|
| Codex/ChatGPT/Claude/Cursor/Windsurf/LM Studio 桌面端 | 上节各自 Application Support 根下的渲染缓存；标准 Library 缓存/日志域 | 验证布局后清理；不清空用户数据根 |
| Codex CLI | `~/.codex/log/codex-tui.log` | 固定诊断日志规则；官方启动逻辑也包含旧文件清理 |
| Codex CLI | `~/.codex/models_cache.json` | 已定位为模型目录元数据；暂不清理，不将其称为服务端 prompt cache |
| Codex CLI | `~/.codex/shell_snapshots` | 研究原生会话生命周期后再启用 |
| Codex 命令入口 | `~/.codex/tmp/arg0-macos/codex-arg0*`，兼容候选 `tmp/arg0/codex-arg0*` | 需实现与源码一致的锁与退休协议；不清整个 tmp |
| Codex daemon | `~/.codex/packages/app-server-daemon/releases/*`、其中 `.staging.*` | 需核对 current、selection-history、运行实例和安装/生命周期锁 |
| Codex 独立 CLI | `~/.codex/packages/standalone/releases/*` | 不套用 daemon 或“保留最新两版”的推测规则 |
| Codex 桌面运行时暂存 | `~/.cache/codex-runtimes/codex-runtime-install-*` | 本机观察到；公开 CLI 源码未证明其安装完成判据，保持待研究 |
| Claude Code | `~/.claude/debug/*.txt` | 调试日志，默认选中；不读取正文 |
| Claude Code 原生安装 | `~/.local/share/claude/versions/<semver>` | 按已验证 launcher/版本保留关系清理旧文件；不改当前启动器 |
| Cursor worker | `~/Library/Application Support/Cursor/User/globalStorage/anysphere.cursor-agent-worker/agent-cli/.local/share/cursor-agent/versions/*` | 已观察路径；缺少可靠当前版本映射，不清 globalStorage |
| Cursor CLI | `~/.local/share/cursor-agent/versions/*` | 路径候选，仍需安装器证据和版本引用验证 |

`CODEX_HOME`、`CLAUDE_CONFIG_DIR` 可以改变配置根，规则按下节的绑定方式展开。Claude 原生二进制根不随 `CLAUDE_CONFIG_DIR` 自动改变。Claude 调试日志覆盖变量实际可以指定**文件路径**，不能把它当目录拼接 `*.txt`；本版只支持默认/配置根下的 debug 布局，额外文件覆盖需要显式适配并报告覆盖缺口。[Claude 环境变量文档](https://code.claude.com/docs/en/env-vars)

Claude 原生旧版本：完整解析数字 semver，排除 launcher 目标和最新两版；运行中旧版本仍有保留职责，只能在退出后重新验证退休资格。自定义启动器、签名/布局未知、网络共享卷均不自动判旧。具体保留条件依据其官方安装说明，不能外推到 Codex/Cursor。[Claude 安装与版本保留说明](https://code.claude.com/docs/en/setup)

**Codex 的费用边界：** 本地普通诊断、下载副本与本地编译成本，和服务端 prompt cache 命中是不同机制。本基准不会因“可能影响模型”泛泛保留普通诊断；也不会承诺删除任意 `.codex` 文件都不增加费用。会话、历史、状态数据库及其 WAL、记忆、配置、凭据、工具/插件等明确保留。元数据与临时运行状态若仍可能改变后续请求或触发模型重试，就在开发阶段查清后再发布规则，而非每次使用时让模型猜测。

本次 Codex 证据固定到提交 `8c076942cb70fba8e5c4732c23f1faabc4aed484`。源码确认的 daemon `.staging.*` 和本机观察的桌面 `codex-runtime-install-*` 是两类对象，不得互相代替证据。逐文件来源在 [SOURCES.md](SOURCES.md)。

### 2.3 开发项目与下载缓存

| 目标 | 默认精确路径/域 | 身份与动作 |
|---|---|---|
| Next.js | `<项目>/.next/cache` | package.json 声明 next；排除 `fetch-cache` 业务响应域，其他未提交修改不影响资格 |
| Cargo | `<build-dir>/{debug,release}/incremental`、`<build-dir>/<target-triple>/{debug,release}/incremental` | Cargo.toml；仅 incremental，不清整个 target 或部署产物 |
| Python | `<项目>/**/__pycache__/*.pyc` | 有对应 `.py` 源文件；不导入模块，不清无源码字节码；排除依赖环境 |
| pytest | `<项目>/.pytest_cache/v/cache/{nodeids,lastfailed,stepwise}` | cache tag + Python 项目；只清内置键 |
| Ruff | `<项目>/.ruff_cache` | cache tag 与 Ruff 版本目录布局；未知条目分开报告 |
| npm 内容缓存 | `<npm cache>/_cacache` | `npm cache clean --force --cache <绑定域>`，按本机版本能力适配 |
| npx 安装缓存 | `<npm cache>/_npx` | 已支持版本的 `npm cache npx rm --cache <绑定域>`；等待目标引用结束 |
| npm 诊断日志 | `<npm cache>/_logs/*.log` | 普通日志文件清理 |
| uv 缓存 | `uv cache dir` 返回的域 | `uv cache clean --cache-dir <绑定域>`，不直接删除内部文件 |
| Playwright 下载运行时 | `~/Library/Caches/ms-playwright/{chromium,chromium_headless_shell,firefox,webkit,ffmpeg}-<数字版本>` | 完整下载标记、版本布局；只删除指定下载副本 |
| Puppeteer 下载运行时 | `~/.cache/puppeteer/{chrome,chrome-headless-shell,firefox}/{mac,mac_arm}-<buildId>` | 对应浏览器可执行文件布局；同步维护该版本的下载元数据 |

`node_modules`、虚拟环境、`.git`、整个 `.next` / `target` / `dist` / `build` 不属于本基准默认清理目标。源码目录本身未获删除授权，**不代表** `src/__pycache__/x.pyc` 也必须保留；应按具体叶项判断。项目中被 Git 跟踪的候选文件保留，只查候选范围，不要求整个工作区干净。

pytest 允许插件缓存任意计算结果。因此内置索引可以按规则清理，未知键可能涉及付费 API、模型生成或用户成果，不能清空整个 `.pytest_cache`。[pytest cache 文档](https://docs.pytest.org/en/stable/how-to/cache.html)

Next.js 的 `cache/fetch-cache` 保存 fetch 响应；本产品推断其中可能含业务/API 计算结果，因此单独保留，不把它的大小计入可清编译缓存。这不是断言所有 fetch 请求都收费，而是将业务响应与本地编译产物分开。[Next.js 写入端源码](https://github.com/vercel/next.js/blob/canary/packages/next/src/server/lib/incremental-cache/file-system-cache.ts)

uv 要使用原生维护接口，遵守锁；`prune` 和清空不是一回事。npm 的 `--force` 是其清缓存接口要求，不能被实现为“强制结束进程/删除锁”。只调用已安装工具，不为了获得清理命令运行可能下载执行软件的 `npx <package>`。[uv 缓存文档](https://docs.astral.sh/uv/concepts/cache/)、[npm cache 文档](https://docs.npmjs.com/cli/v11/commands/npm-cache/)

## 3. 根目录绑定与发现预算

全部根解析规范在 `catalog.json.roots`，实施者不能把表中的默认值当作实际运行路径。

1. Mac 端用当前 uid 取得 HOME，拒绝以 root 身份替代用户扫描。`HOME` 和 `SUPPORT` 固定，不接受模型任意改写。
2. 可配置根采用“用户明确指定 > 仅读取被允许的对应环境键 > 默认值”。原生工具缓存优先查询实际安装工具，查询在空工作目录完成；不转储环境、shell 历史或用户配置正文。
3. 每次绑定保存根名、绝对路径、来源、解析状态、设备/文件身份和授权范围。显式路径意味着范围选择，不自动证明内容可删。
4. 非默认 Next distDir、Cargo build-dir、pytest/Ruff cache-dir 使用每项目显式映射。不执行 `next.config.js`、`.puppeteerrc.js`、`setup.py` 或项目 hook 来发现路径。无法解析时显示 `root_unresolved` 与配置入口。
5. `PLAYWRIGHT_BROWSERS_PATH=0` 指包内安装，不是 `/0`，本版不自动处理包内运行时。uv 不可用时可只读探测 `~/.cache/uv` 和 `~/Library/Caches/uv`，不能由通用规则代删。
6. 项目只在用户选定根中发现：最大深度 6、每次 50,000 元数据条目、180 秒。Python `**` 最多跨越 6 层父目录，不跟随链接，不进入 `.git`、node_modules、虚拟环境。
7. 所有枚举共享本轮 50,000 条目/180 秒预算；单目标计量另限 50,000 条目/30 秒且仍受本轮总预算约束。超限保留部分结果和可继续的根/目录游标，不能写成完整扫描。

固定模式中的 `*` 是**单个路径段**，不跨越 `/`，不是传给 shell 的 glob。只有 Python 规则有受预算约束的 `**`；`.` 表示已验证工具缓存根本身。不得使用字符串前缀代替路径归属检查，`Caches-Old` 不属于 `Caches`。

默认按目录项原始大小写精确匹配，不以 `lower()` 合并条目。在大小写不敏感卷上，静态路径探测可能返回同一对象，应按实际文件身份去重。出现别名/链接/大小写冲突要记录，不能扩大为不区分大小写的任意目录删除。

## 4. 规则契约和执行语义

### 4.1 开发规则与运行证据分离

每条 JSON 规则必须包含稳定 `id`、版本、分类、成熟度、优先级、根和路径模式、类型、身份检查、类型化动作、执行协议、默认选择、用途、恢复方式、影响、费用评估和证据来源。

`facts` 是**需要适配器实现的探针规范**，不是运行时可由 AI 填写的布尔批准。案例文件里的 `true` 仅为合成输入。生产端要从元数据、允许的 manifest 字段或固定原生接口取得证据；不接受模型直接声明 `native_supported=true` 或 `approved=true`。

匹配路径后按以下顺序处理：

1. 先应用扫描范围、用户保留项、唯一内容/已知付费重算依赖、链接与特殊文件限制。
2. `protected` 匹配对象及其后代优先保留。例外只能通过新版本规则明确收窄，模型不能覆盖。
3. 从其余匹配中选最高优先级，再选更深的具体匹配根。若仍有不同规则并列，保留预览并报告冲突。
4. `research` 与专用原生域声明占有该路径。身份检查失败时保持待调查，**不回退到较宽的可删规则**。
5. `ready` 所需证据全部通过且计量完整，形成默认选中的候选。近期生成、共享、重建慢、来源创建者未知均不单独降低资格。
6. 活动状态另行决定在线执行、原生协调或待执行。普通在线文件清理不因全局进程名而阻断；具体编译写入/运行引用和原生锁才决定是否等待。

一个缓存域内有独立 FIFO、socket 或链接，不应把所有普通文件一并丢弃：逐叶封存可清文件，特殊项单独显示未处理。下载运行时作为完整副本操作时则使用其专用协议。持久业务数据库/WAL 与普通缓存中的索引要由目录语义/专用例外区分，不能按 `.db` / `-wal` 后缀全盘删除或全盘保留。

### 4.2 父子重叠和原生域

例：`~/Library/Caches/ms-playwright/chromium-1234` 同时落在通用 Library 域和专用下载规则中，只由下载规则拥有。上层通用候选的动作和计量都必须减去整个保留/专用子树，不能父子各报一次，也不能通过选中父目录绕过子规则。

若 uv 实际根是 `~/Library/Caches/uv`，专用适配器验证成功后走原生清理；命令不支持或不可用时显示待处理，通用规则不得接管。自定义 uv 根也必须先登记为原生保留域。

`contents` 指目录内经封存的普通文件，默认保留目录；若目标本身是文件则只作用于该文件。`target` 指有完整身份的单个目标/下载副本；`native_domain` 指原生命令实际可能影响的完整域。原生域不允许伪装成只批准其中几个文件；副作用和诊断文件也应声明。

一个父级原生动作不能排除某个受保护子项时，整个动作不可执行，不能以“原生接口更安全”为由忽略保留规则。报告分别列目标逻辑大小、去重后的已测分配块与卷可用空间变化；硬链接/克隆/APFS/打开句柄等因素使它们可能不同。

### 4.3 执行协议

完整定义在 `catalog.json.protocols`，开发时实现固定枚举分派。路径和 argv 使用独立参数传递，不使用 shell 拼接，不接受规则 JSON 内嵌命令脚本。

- **online_inventory：** 只删封存的普通文件。复核目标及祖先身份，不读取日志正文；新建/变化文件跳过。在线日志打开句柄可能延迟实际释放。
- **project_cache：** 同上，加目标范围的构建协调。其他文件脏或无关程序运行不构成阻断。
- **native_npm / native_npx / native_uv：** 根和可执行文件先绑定；验证命令版本能力与实际影响域；遵守工具锁和原生清理语义。
- **download_runtime：** 完整下载副本与普通浏览器资料严格分离。检查具体运行引用；内部链接只解除、不跟随，指向域外/唯一内容则待调查；不自动关闭应用。
- **puppeteer_runtime：** 另声明该版本在 `.metadata` 中的 aliases/executablePaths 键更新。仅操作批准的键，其他版本保留；并发修改则停止该项，不能留下已删除版本的错误引用。适配器应封存事务前状态，部分失败出具修复收据。
- **claude_retirement：** 再核对 launcher、当前保留集合、签名和运行引用；只移除批准的旧版文件，不改启动器。运行引用消失后仍需重新验证退休资格。

等待上限为 30 秒；超时保留 `pending`，继续独立项。删除资格与时机分开，不能把“等待”显示成永久保留，也不能把待执行空间加到“现在可处理”。

### 4.4 批准、费用与结果

选择清单只含目标 ID；核心重新生成不可变计划。所有新动作都需要绑定当前计划摘要的批量批准：可信宿主事件可直接采用，否则使用 Mac 原生对话框，无图形界面则人工终端。AI 不能代按确认、伪造输入或填写批准字段。

执行前重新验证目标身份、规则版本和批准范围；局部变化只跳过该项，不使所有独立动作一起失败。取消不执行剩余动作。批准时效、摘要检查和准确收据沿用第一部分契约。

费用字段 `no_expected_increase` 表示依据目前确认的用途，不预期触发额外付费模型计算，**不保证任意外部工作流的最终账单**。已知会导致付费推理/嵌入重算的对象保留。下载与编译成本可接受，但恢复应使用明确的本地/原生动作，不通过自动重跑 Agent 任务来恢复文件。

规则发现器不能擅自读取会话、源码正文、环境转储来推测费用；证据缺口在开发阶段解决。用户另外指定保留的诊断/缓存优先保留，不能把默认选中当作强制清理。

## 5. 完整覆盖与新规则研究

报告必须附扫描覆盖表，每个根/规则至少出现一种状态：`matched`、`absent`、`access_denied`、`budget_exceeded`、`layout_unverified`、`root_unresolved`。候选匹配不等于全部量完；权限错误/未完成计量要保留错误和已知部分。

0 字节已验证对象不生成清理动作，不堆在主报告中；可在覆盖表中查看。AI 客户端也可能只命中通用 Library 规则，应按确定的应用归属在报告中归入 AI 类，不需要另加一条重复清理规则。

更新规则采用以下开发流程：

1. 在官方文档/开源写入端找到真实路径、配置覆盖、格式和恢复方式；固定源码提交或记录文档审阅日期。
2. 用 Mole/CleanMyMac 作为覆盖线索与交叉核对，不把两个工具都勾选视为对唯一内容和费用后果的证明。
3. 标出可重建下载/编译数据、不可重建状态、当前工具与回退职责；追踪可能涉及模型付费重算的依赖。
4. 写入精确选择器、身份探针和类型化动作；有原生协议的优先实现该协议。
5. 在可丢弃 fixture 上验证正例、反例、活动/锁、身份替换、部分失败和恢复副作用，再做明确版本的本机集成测试。
6. 增加规则版本和完整性清单；审阅通过才从 `research` 改为 `ready` 并进入技能发布。使用阶段不要求用户重复审阅同一种目录语义。

没有证据的路径不伪造为 `ready`；也不能只列“以后研究”而不说明路径和缺口。17 条待研究项已经逐条填写 `gap`，其中 Codex/Cursor 生命周期适配是优先任务。

## 6. 双宿主实施顺序

先实现规则加载、根绑定、受限枚举、事实探针、去重计量和覆盖表；再实现计划/批准/动作/收据，最后接入 SKILL 和现有 Mac 连接器。两种宿主运行同一份带完整性校验的 Python 核心与规则数据，网页端只负责传输与调用，不重写清理脚本。

任意 AI 客户端要使用本技能，必须具备技能/指令加载能力，以及访问用户 Mac 的受控执行渠道。**安装一个文档文件本身不会让 ChatGPT 网页端获得本机磁盘权限。** 网页端应复用已经连接的 Mac 执行通道，无连接时给出安装/连接指引，不在云环境伪造扫描。

首版工作集中在本规则库覆盖的缓存、诊断和可退休下载副本；worktree 收尾、CLI 归因/卸载、隔离、自动维护等不作为本开发基准的必备交付，避免重新扩大实现范围。

开发者起步检查（只校验文档附件，不执行清理）：

```sh
python3 docs/scan-catalog/validate_catalog.py
```

实现必须复用这些路径和优先级；如需改变，应修改 JSON、案例与来源记录。用户真实目录不是破坏性测试 fixture。正式发布的验收要求见 [ACCEPTANCE.md](ACCEPTANCE.md)。
