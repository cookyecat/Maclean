# 完整扫描规则索引

由 `render_reference.py` 从 `catalog.json` 生成；修改规则应先修改 JSON。

这里列出的路径表达式全部参与规则匹配，不是示例路径。`${ROOT}` 的实际绑定见文末。
`ready` 是开发契约就绪；只有身份探针、适配器和批准均通过才能执行。

| 规则 ID | 分类 | 成熟度 | 用途 |
|---|---|---|---|
| [macos-user-cache](#macos-user-cache) | app | ready | 用户标准应用缓存 |
| [macos-user-log](#macos-user-log) | app | ready | 用户诊断日志 |
| [sandbox-cache](#sandbox-cache) | app | ready | 沙盒/应用组标准缓存 |
| [sandbox-log](#sandbox-log) | app | ready | 沙盒/应用组诊断日志 |
| [group-cache](#group-cache) | app | ready | 沙盒/应用组标准缓存 |
| [group-log](#group-log) | app | ready | 沙盒/应用组诊断日志 |
| [app-render-cache](#app-render-cache) | app | ready | 已登记应用的 Chromium 渲染缓存叶目录 |
| [ai-render-cache](#ai-render-cache) | ai | ready | AI 客户端渲染缓存；不含对话/推理状态 |
| [editor-code-cache](#editor-code-cache) | app | ready | 编辑器生成的代码缓存 |
| [editor-vsix-download](#editor-vsix-download) | app | ready | 已下载扩展安装包副本 |
| [ai-editor-extra-cache](#ai-editor-extra-cache) | ai | research | AI 编辑器的继承布局 |
| [editor-log](#editor-log) | app | ready | 编辑器诊断日志 |
| [ai-support-log](#ai-support-log) | ai | research | AI 应用专用日志路径 |
| [browser-profile-cache](#browser-profile-cache) | app | ready | 浏览器 profile 内的渲染/HTTP 缓存叶目录 |
| [browser-root-shader](#browser-root-shader) | app | ready | 浏览器根下 shader/code 缓存 |
| [firefox-support-cache](#firefox-support-cache) | app | research | Firefox 专用缓存候选 |
| [design-media-cache](#design-media-cache) | app | research | 设计软件专用缓存候选 |
| [support-unreviewed-leaf](#support-unreviewed-leaf) | app | research | 未登记应用的浅层缓存/日志候选 |
| [codex-legacy-tui-log](#codex-legacy-tui-log) | ai | ready | Codex 官方启动逻辑可清的旧诊断日志 |
| [codex-other-log](#codex-other-log) | ai | research | Codex 其他日志候选 |
| [codex-model-catalog](#codex-model-catalog) | ai | research | 模型列表和元数据缓存 |
| [codex-shell-snapshots](#codex-shell-snapshots) | ai | research | 本地 Shell 初始化快照 |
| [codex-arg0](#codex-arg0) | ai | research | 自动生成的命令入口 |
| [codex-daemon-releases](#codex-daemon-releases) | ai | research | daemon 旧运行时 |
| [codex-standalone-releases](#codex-standalone-releases) | ai | research | 独立 CLI 版本目录 |
| [codex-daemon-staging](#codex-daemon-staging) | ai | research | 源码确认的发布前暂存 |
| [codex-desktop-runtime-staging](#codex-desktop-runtime-staging) | ai | research | 实际观察的桌面运行时安装暂存 |
| [claude-debug-log](#claude-debug-log) | ai | ready | Claude Code 调试日志 |
| [claude-old-native](#claude-old-native) | ai | ready | Claude 原生旧版可执行文件 |
| [cursor-worker-versions](#cursor-worker-versions) | ai | research | Cursor agent-worker 版本和临时安装 |
| [cursor-cli-versions](#cursor-cli-versions) | ai | research | Cursor CLI 独立安装候选 |
| [next-build-cache](#next-build-cache) | development | ready | Next.js 构建缓存 |
| [cargo-incremental](#cargo-incremental) | development | ready | Cargo 本地增量编译产物 |
| [python-bytecode](#python-bytecode) | development | ready | 有对应源码的 Python 编译缓存 |
| [pytest-core-cache](#pytest-core-cache) | development | ready | pytest 内置测试索引和失败列表 |
| [pytest-plugin-cache](#pytest-plugin-cache) | development | research | pytest 插件自定义缓存 |
| [ruff-cache](#ruff-cache) | development | ready | Ruff 本地检查结果 |
| [npm-content-cache](#npm-content-cache) | development | ready | npm 内容寻址下载缓存 |
| [npm-npx-cache](#npm-npx-cache) | development | ready | npm exec/npx 安装缓存 |
| [npm-diagnostic-log](#npm-diagnostic-log) | development | ready | npm 诊断日志 |
| [uv-native-cache](#uv-native-cache) | development | ready | uv 下载/构建缓存域 |
| [playwright-download](#playwright-download) | development | ready | Playwright 自动下载副本 |
| [puppeteer-download](#puppeteer-download) | development | ready | Puppeteer 自动下载副本 |
| [preserve-codex-state](#preserve-codex-state) | ai | protected | 会话、配置、账本、插件、worktree 及安装控制状态 |
| [preserve-claude-state](#preserve-claude-state) | ai | protected | Claude 会话、环境、插件与用户状态 |
| [preserve-primary-runtime](#preserve-primary-runtime) | ai | protected | 当前工具运行环境不属于安装暂存 |
| [preserve-editor-state](#preserve-editor-state) | ai | protected | 应用/编辑器状态；不从通用缓存规则清除 |
| [preserve-home-state](#preserve-home-state) | app | protected | 凭据、配置和个人数据 |
| [preserve-project-inputs](#preserve-project-inputs) | development | protected | 有界发现范围内的版本控制、依赖环境和配置不进入普通缓存；src/dist/build 本身未获清理授权，但其中精确匹配的缓存叶项可另行清理 |
| [preserve-next-data-cache](#preserve-next-data-cache) | development | protected | 业务/API 响应缓存可能参与付费计算复用，不与编译缓存一并清理 |
| [preserve-audit](#preserve-audit) | app | protected | 清理收据和审计历史 |
| [preserve-sync-state](#preserve-sync-state) | app | protected | 同步或可能尚未同步的数据 |
| [preserve-service-state](#preserve-service-state) | app | protected | 系统服务专用状态，普通文件清理协议未验证 |
| [preserve-model-bundles](#preserve-model-bundles) | app | protected | 模型/运行时资源不是普通缓存 |
| [preserve-environment-caches](#preserve-environment-caches) | app | protected | 可能包含应用状态或正在链接的依赖环境 |
| [reserve-native-and-runtime](#reserve-native-and-runtime) | development | research | 专用协议拥有的域 |

## macos-user-cache

用户标准应用缓存

- 版本：1；成熟度：`ready`；优先级：100。
- 选择范围：`contents`；判定：`disposable`；默认选中：true。
- 动作：`clear_files`；协议：`online_inventory`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`no_expected_increase`。
- 来源：[apple-library](SOURCES.md#apple-library)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `HOME`；目标类型 `directory`：

```text
${HOME}/Library/Caches/*
```

## macos-user-log

用户诊断日志

- 版本：1；成熟度：`ready`；优先级：100。
- 选择范围：`contents`；判定：`disposable`；默认选中：true。
- 动作：`clear_files`；协议：`online_inventory`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：只生成今后的日志。
- 影响：历史诊断不可恢复；打开句柄可能延迟释放。
- 费用字段：`no_expected_increase`。
- 来源：[apple-library](SOURCES.md#apple-library)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `HOME`；目标类型 `any`：

```text
${HOME}/Library/Logs/*
```

## sandbox-cache

沙盒/应用组标准缓存

- 版本：1；成熟度：`ready`；优先级：100。
- 选择范围：`contents`；判定：`disposable`；默认选中：true。
- 动作：`clear_files`；协议：`online_inventory`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`no_expected_increase`。
- 来源：[apple-library](SOURCES.md#apple-library)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `HOME`；目标类型 `directory`：

```text
${HOME}/Library/Containers/*/Data/Library/Caches
```

## sandbox-log

沙盒/应用组诊断日志

- 版本：1；成熟度：`ready`；优先级：100。
- 选择范围：`contents`；判定：`disposable`；默认选中：true。
- 动作：`clear_files`；协议：`online_inventory`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：只生成今后的日志。
- 影响：历史诊断不可恢复。
- 费用字段：`no_expected_increase`。
- 来源：[apple-library](SOURCES.md#apple-library)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `HOME`；目标类型 `directory`：

```text
${HOME}/Library/Containers/*/Data/Library/Logs
```

## group-cache

沙盒/应用组标准缓存

- 版本：1；成熟度：`ready`；优先级：100。
- 选择范围：`contents`；判定：`disposable`；默认选中：true。
- 动作：`clear_files`；协议：`online_inventory`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`no_expected_increase`。
- 来源：[apple-library](SOURCES.md#apple-library)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `HOME`；目标类型 `directory`：

```text
${HOME}/Library/Group Containers/*/Library/Caches
```

## group-log

沙盒/应用组诊断日志

- 版本：1；成熟度：`ready`；优先级：100。
- 选择范围：`contents`；判定：`disposable`；默认选中：true。
- 动作：`clear_files`；协议：`online_inventory`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：只生成今后的日志。
- 影响：历史诊断不可恢复。
- 费用字段：`no_expected_increase`。
- 来源：[apple-library](SOURCES.md#apple-library)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `HOME`；目标类型 `directory`：

```text
${HOME}/Library/Group Containers/*/Library/Logs
```

## app-render-cache

已登记应用的 Chromium 渲染缓存叶目录

- 版本：1；成熟度：`ready`；优先级：200。
- 选择范围：`contents`；判定：`disposable`；默认选中：true。
- 动作：`clear_files`；协议：`online_inventory`。
- 身份检查：`chromium_layout`。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`no_expected_increase`。
- 来源：[electron-paths](SOURCES.md#electron-paths)、[mole-caches](SOURCES.md#mole-caches)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `SUPPORT`；目标类型 `directory`：

```text
${SUPPORT}/Code/Cache
${SUPPORT}/Code/Code Cache
${SUPPORT}/Code/GPUCache
${SUPPORT}/Code/ShaderCache
${SUPPORT}/Code/GrShaderCache
${SUPPORT}/Code/DawnCache
${SUPPORT}/Code/GraphiteDawnCache
${SUPPORT}/Code/DawnGraphiteCache
${SUPPORT}/Code/DawnWebGPUCache
${SUPPORT}/Code - Insiders/Cache
${SUPPORT}/Code - Insiders/Code Cache
${SUPPORT}/Code - Insiders/GPUCache
${SUPPORT}/Code - Insiders/ShaderCache
${SUPPORT}/Code - Insiders/GrShaderCache
${SUPPORT}/Code - Insiders/DawnCache
${SUPPORT}/Code - Insiders/GraphiteDawnCache
${SUPPORT}/Code - Insiders/DawnGraphiteCache
${SUPPORT}/Code - Insiders/DawnWebGPUCache
${SUPPORT}/VSCodium/Cache
${SUPPORT}/VSCodium/Code Cache
${SUPPORT}/VSCodium/GPUCache
${SUPPORT}/VSCodium/ShaderCache
${SUPPORT}/VSCodium/GrShaderCache
${SUPPORT}/VSCodium/DawnCache
${SUPPORT}/VSCodium/GraphiteDawnCache
${SUPPORT}/VSCodium/DawnGraphiteCache
${SUPPORT}/VSCodium/DawnWebGPUCache
${SUPPORT}/Slack/Cache
${SUPPORT}/Slack/Code Cache
${SUPPORT}/Slack/GPUCache
${SUPPORT}/Slack/ShaderCache
${SUPPORT}/Slack/GrShaderCache
${SUPPORT}/Slack/DawnCache
${SUPPORT}/Slack/GraphiteDawnCache
${SUPPORT}/Slack/DawnGraphiteCache
${SUPPORT}/Slack/DawnWebGPUCache
${SUPPORT}/Discord/Cache
${SUPPORT}/Discord/Code Cache
${SUPPORT}/Discord/GPUCache
${SUPPORT}/Discord/ShaderCache
${SUPPORT}/Discord/GrShaderCache
${SUPPORT}/Discord/DawnCache
${SUPPORT}/Discord/GraphiteDawnCache
${SUPPORT}/Discord/DawnGraphiteCache
${SUPPORT}/Discord/DawnWebGPUCache
${SUPPORT}/Notion/Cache
${SUPPORT}/Notion/Code Cache
${SUPPORT}/Notion/GPUCache
${SUPPORT}/Notion/ShaderCache
${SUPPORT}/Notion/GrShaderCache
${SUPPORT}/Notion/DawnCache
${SUPPORT}/Notion/GraphiteDawnCache
${SUPPORT}/Notion/DawnGraphiteCache
${SUPPORT}/Notion/DawnWebGPUCache
${SUPPORT}/Figma/Cache
${SUPPORT}/Figma/Code Cache
${SUPPORT}/Figma/GPUCache
${SUPPORT}/Figma/ShaderCache
${SUPPORT}/Figma/GrShaderCache
${SUPPORT}/Figma/DawnCache
${SUPPORT}/Figma/GraphiteDawnCache
${SUPPORT}/Figma/DawnGraphiteCache
${SUPPORT}/Figma/DawnWebGPUCache
${SUPPORT}/Termius/Cache
${SUPPORT}/Termius/Code Cache
${SUPPORT}/Termius/GPUCache
${SUPPORT}/Termius/ShaderCache
${SUPPORT}/Termius/GrShaderCache
${SUPPORT}/Termius/DawnCache
${SUPPORT}/Termius/GraphiteDawnCache
${SUPPORT}/Termius/DawnGraphiteCache
${SUPPORT}/Termius/DawnWebGPUCache
```

## ai-render-cache

AI 客户端渲染缓存；不含对话/推理状态

- 版本：1；成熟度：`ready`；优先级：200。
- 选择范围：`contents`；判定：`disposable`；默认选中：true。
- 动作：`clear_files`；协议：`online_inventory`。
- 身份检查：`chromium_layout`。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`no_expected_increase`。
- 来源：[electron-paths](SOURCES.md#electron-paths)、[mole-caches](SOURCES.md#mole-caches)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `SUPPORT`；目标类型 `directory`：

```text
${SUPPORT}/Codex/Cache
${SUPPORT}/Codex/Code Cache
${SUPPORT}/Codex/GPUCache
${SUPPORT}/Codex/ShaderCache
${SUPPORT}/Codex/GrShaderCache
${SUPPORT}/Codex/DawnCache
${SUPPORT}/Codex/GraphiteDawnCache
${SUPPORT}/Codex/DawnGraphiteCache
${SUPPORT}/Codex/DawnWebGPUCache
${SUPPORT}/Claude/Cache
${SUPPORT}/Claude/Code Cache
${SUPPORT}/Claude/GPUCache
${SUPPORT}/Claude/ShaderCache
${SUPPORT}/Claude/GrShaderCache
${SUPPORT}/Claude/DawnCache
${SUPPORT}/Claude/GraphiteDawnCache
${SUPPORT}/Claude/DawnGraphiteCache
${SUPPORT}/Claude/DawnWebGPUCache
${SUPPORT}/ChatGPT/Cache
${SUPPORT}/ChatGPT/Code Cache
${SUPPORT}/ChatGPT/GPUCache
${SUPPORT}/ChatGPT/ShaderCache
${SUPPORT}/ChatGPT/GrShaderCache
${SUPPORT}/ChatGPT/DawnCache
${SUPPORT}/ChatGPT/GraphiteDawnCache
${SUPPORT}/ChatGPT/DawnGraphiteCache
${SUPPORT}/ChatGPT/DawnWebGPUCache
${SUPPORT}/Cursor/Cache
${SUPPORT}/Cursor/Code Cache
${SUPPORT}/Cursor/GPUCache
${SUPPORT}/Cursor/ShaderCache
${SUPPORT}/Cursor/GrShaderCache
${SUPPORT}/Cursor/DawnCache
${SUPPORT}/Cursor/GraphiteDawnCache
${SUPPORT}/Cursor/DawnGraphiteCache
${SUPPORT}/Cursor/DawnWebGPUCache
${SUPPORT}/Windsurf/Cache
${SUPPORT}/Windsurf/Code Cache
${SUPPORT}/Windsurf/GPUCache
${SUPPORT}/Windsurf/ShaderCache
${SUPPORT}/Windsurf/GrShaderCache
${SUPPORT}/Windsurf/DawnCache
${SUPPORT}/Windsurf/GraphiteDawnCache
${SUPPORT}/Windsurf/DawnGraphiteCache
${SUPPORT}/Windsurf/DawnWebGPUCache
${SUPPORT}/LM Studio/Cache
${SUPPORT}/LM Studio/Code Cache
${SUPPORT}/LM Studio/GPUCache
${SUPPORT}/LM Studio/ShaderCache
${SUPPORT}/LM Studio/GrShaderCache
${SUPPORT}/LM Studio/DawnCache
${SUPPORT}/LM Studio/GraphiteDawnCache
${SUPPORT}/LM Studio/DawnGraphiteCache
${SUPPORT}/LM Studio/DawnWebGPUCache
```

## editor-code-cache

编辑器生成的代码缓存

- 版本：1；成熟度：`ready`；优先级：200。
- 选择范围：`contents`；判定：`disposable`；默认选中：true。
- 动作：`clear_files`；协议：`online_inventory`。
- 身份检查：`editor_layout`。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`no_expected_increase`。
- 来源：[vscode-code-cache](SOURCES.md#vscode-code-cache)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `SUPPORT`；目标类型 `directory`：

```text
${SUPPORT}/Code/CachedData
${SUPPORT}/Code - Insiders/CachedData
${SUPPORT}/VSCodium/CachedData
```

## editor-vsix-download

已下载扩展安装包副本

- 版本：1；成熟度：`ready`；优先级：200。
- 选择范围：`contents`；判定：`disposable`；默认选中：true。
- 动作：`clear_files`；协议：`online_inventory`。
- 身份检查：`editor_layout`。
- 恢复：需要时重新下载扩展包；不卸载扩展。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`no_expected_increase`。
- 来源：[vscode-vsix](SOURCES.md#vscode-vsix)、[vscode-environment](SOURCES.md#vscode-environment)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `SUPPORT`；目标类型 `directory`：

```text
${SUPPORT}/Code/CachedExtensionVSIXs
${SUPPORT}/Code - Insiders/CachedExtensionVSIXs
${SUPPORT}/VSCodium/CachedExtensionVSIXs
```

## ai-editor-extra-cache

AI 编辑器的继承布局

- 版本：1；成熟度：`research`；优先级：250。
- 选择范围：`contents`；判定：`investigate`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`unresolved`。
- 来源：[vscode-vsix](SOURCES.md#vscode-vsix)、[live-layouts](SOURCES.md#live-layouts)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。
- 待补证据/实现：补齐具体产品的目录用途/版本验证，不能仅因继承 VS Code 就认定所有缓存语义相同。

根 `SUPPORT`；目标类型 `directory`：

```text
${SUPPORT}/Cursor/CachedData
${SUPPORT}/Cursor/CachedExtensionVSIXs
${SUPPORT}/Windsurf/CachedData
${SUPPORT}/Windsurf/CachedExtensionVSIXs
```

## editor-log

编辑器诊断日志

- 版本：1；成熟度：`ready`；优先级：200。
- 选择范围：`contents`；判定：`disposable`；默认选中：true。
- 动作：`clear_files`；协议：`online_inventory`。
- 身份检查：`editor_layout`。
- 恢复：只生成今后的日志。
- 影响：历史诊断不可恢复。
- 费用字段：`no_expected_increase`。
- 来源：[vscode-environment](SOURCES.md#vscode-environment)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `SUPPORT`；目标类型 `directory`：

```text
${SUPPORT}/Code/logs
${SUPPORT}/Code - Insiders/logs
${SUPPORT}/VSCodium/logs
```

## ai-support-log

AI 应用专用日志路径

- 版本：1；成熟度：`research`；优先级：250。
- 选择范围：`contents`；判定：`investigate`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`unresolved`。
- 来源：[mole-caches](SOURCES.md#mole-caches)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。
- 待补证据/实现：逐产品确认日志用途；不要将会话/审计/模型结果存储按名字判为日志。

根 `SUPPORT`；目标类型 `directory`：

```text
${SUPPORT}/Codex/logs
${SUPPORT}/Codex/Logs
${SUPPORT}/Claude/logs
${SUPPORT}/Claude/Logs
${SUPPORT}/ChatGPT/logs
${SUPPORT}/ChatGPT/Logs
${SUPPORT}/Cursor/logs
${SUPPORT}/Cursor/Logs
${SUPPORT}/Windsurf/logs
${SUPPORT}/Windsurf/Logs
${SUPPORT}/LM Studio/logs
${SUPPORT}/LM Studio/Logs
```

## browser-profile-cache

浏览器 profile 内的渲染/HTTP 缓存叶目录

- 版本：1；成熟度：`ready`；优先级：220。
- 选择范围：`contents`；判定：`disposable`；默认选中：true。
- 动作：`clear_files`；协议：`online_inventory`。
- 身份检查：`browser_profile`。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`no_expected_increase`。
- 来源：[chromium-paths](SOURCES.md#chromium-paths)、[electron-paths](SOURCES.md#electron-paths)、[mole-caches](SOURCES.md#mole-caches)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `SUPPORT`；目标类型 `directory`：

```text
${SUPPORT}/Google/Chrome/Default/Cache
${SUPPORT}/Google/Chrome/Default/Code Cache
${SUPPORT}/Google/Chrome/Default/GPUCache
${SUPPORT}/Google/Chrome/Default/ShaderCache
${SUPPORT}/Google/Chrome/Default/GrShaderCache
${SUPPORT}/Google/Chrome/Default/DawnCache
${SUPPORT}/Google/Chrome/Default/GraphiteDawnCache
${SUPPORT}/Google/Chrome/Default/DawnGraphiteCache
${SUPPORT}/Google/Chrome/Default/DawnWebGPUCache
${SUPPORT}/Google/Chrome/Profile [0-9]*/Cache
${SUPPORT}/Google/Chrome/Profile [0-9]*/Code Cache
${SUPPORT}/Google/Chrome/Profile [0-9]*/GPUCache
${SUPPORT}/Google/Chrome/Profile [0-9]*/ShaderCache
${SUPPORT}/Google/Chrome/Profile [0-9]*/GrShaderCache
${SUPPORT}/Google/Chrome/Profile [0-9]*/DawnCache
${SUPPORT}/Google/Chrome/Profile [0-9]*/GraphiteDawnCache
${SUPPORT}/Google/Chrome/Profile [0-9]*/DawnGraphiteCache
${SUPPORT}/Google/Chrome/Profile [0-9]*/DawnWebGPUCache
${SUPPORT}/Google/Chrome/Guest Profile/Cache
${SUPPORT}/Google/Chrome/Guest Profile/Code Cache
${SUPPORT}/Google/Chrome/Guest Profile/GPUCache
${SUPPORT}/Google/Chrome/Guest Profile/ShaderCache
${SUPPORT}/Google/Chrome/Guest Profile/GrShaderCache
${SUPPORT}/Google/Chrome/Guest Profile/DawnCache
${SUPPORT}/Google/Chrome/Guest Profile/GraphiteDawnCache
${SUPPORT}/Google/Chrome/Guest Profile/DawnGraphiteCache
${SUPPORT}/Google/Chrome/Guest Profile/DawnWebGPUCache
${SUPPORT}/Google/Chrome/System Profile/Cache
${SUPPORT}/Google/Chrome/System Profile/Code Cache
${SUPPORT}/Google/Chrome/System Profile/GPUCache
${SUPPORT}/Google/Chrome/System Profile/ShaderCache
${SUPPORT}/Google/Chrome/System Profile/GrShaderCache
${SUPPORT}/Google/Chrome/System Profile/DawnCache
${SUPPORT}/Google/Chrome/System Profile/GraphiteDawnCache
${SUPPORT}/Google/Chrome/System Profile/DawnGraphiteCache
${SUPPORT}/Google/Chrome/System Profile/DawnWebGPUCache
${SUPPORT}/Google/Chrome Canary/Default/Cache
${SUPPORT}/Google/Chrome Canary/Default/Code Cache
${SUPPORT}/Google/Chrome Canary/Default/GPUCache
${SUPPORT}/Google/Chrome Canary/Default/ShaderCache
${SUPPORT}/Google/Chrome Canary/Default/GrShaderCache
${SUPPORT}/Google/Chrome Canary/Default/DawnCache
${SUPPORT}/Google/Chrome Canary/Default/GraphiteDawnCache
${SUPPORT}/Google/Chrome Canary/Default/DawnGraphiteCache
${SUPPORT}/Google/Chrome Canary/Default/DawnWebGPUCache
${SUPPORT}/Google/Chrome Canary/Profile [0-9]*/Cache
${SUPPORT}/Google/Chrome Canary/Profile [0-9]*/Code Cache
${SUPPORT}/Google/Chrome Canary/Profile [0-9]*/GPUCache
${SUPPORT}/Google/Chrome Canary/Profile [0-9]*/ShaderCache
${SUPPORT}/Google/Chrome Canary/Profile [0-9]*/GrShaderCache
${SUPPORT}/Google/Chrome Canary/Profile [0-9]*/DawnCache
${SUPPORT}/Google/Chrome Canary/Profile [0-9]*/GraphiteDawnCache
${SUPPORT}/Google/Chrome Canary/Profile [0-9]*/DawnGraphiteCache
${SUPPORT}/Google/Chrome Canary/Profile [0-9]*/DawnWebGPUCache
${SUPPORT}/Google/Chrome Canary/Guest Profile/Cache
${SUPPORT}/Google/Chrome Canary/Guest Profile/Code Cache
${SUPPORT}/Google/Chrome Canary/Guest Profile/GPUCache
${SUPPORT}/Google/Chrome Canary/Guest Profile/ShaderCache
${SUPPORT}/Google/Chrome Canary/Guest Profile/GrShaderCache
${SUPPORT}/Google/Chrome Canary/Guest Profile/DawnCache
${SUPPORT}/Google/Chrome Canary/Guest Profile/GraphiteDawnCache
${SUPPORT}/Google/Chrome Canary/Guest Profile/DawnGraphiteCache
${SUPPORT}/Google/Chrome Canary/Guest Profile/DawnWebGPUCache
${SUPPORT}/Google/Chrome Canary/System Profile/Cache
${SUPPORT}/Google/Chrome Canary/System Profile/Code Cache
${SUPPORT}/Google/Chrome Canary/System Profile/GPUCache
${SUPPORT}/Google/Chrome Canary/System Profile/ShaderCache
${SUPPORT}/Google/Chrome Canary/System Profile/GrShaderCache
${SUPPORT}/Google/Chrome Canary/System Profile/DawnCache
${SUPPORT}/Google/Chrome Canary/System Profile/GraphiteDawnCache
${SUPPORT}/Google/Chrome Canary/System Profile/DawnGraphiteCache
${SUPPORT}/Google/Chrome Canary/System Profile/DawnWebGPUCache
${SUPPORT}/Microsoft Edge/Default/Cache
${SUPPORT}/Microsoft Edge/Default/Code Cache
${SUPPORT}/Microsoft Edge/Default/GPUCache
${SUPPORT}/Microsoft Edge/Default/ShaderCache
${SUPPORT}/Microsoft Edge/Default/GrShaderCache
${SUPPORT}/Microsoft Edge/Default/DawnCache
${SUPPORT}/Microsoft Edge/Default/GraphiteDawnCache
${SUPPORT}/Microsoft Edge/Default/DawnGraphiteCache
${SUPPORT}/Microsoft Edge/Default/DawnWebGPUCache
${SUPPORT}/Microsoft Edge/Profile [0-9]*/Cache
${SUPPORT}/Microsoft Edge/Profile [0-9]*/Code Cache
${SUPPORT}/Microsoft Edge/Profile [0-9]*/GPUCache
${SUPPORT}/Microsoft Edge/Profile [0-9]*/ShaderCache
${SUPPORT}/Microsoft Edge/Profile [0-9]*/GrShaderCache
${SUPPORT}/Microsoft Edge/Profile [0-9]*/DawnCache
${SUPPORT}/Microsoft Edge/Profile [0-9]*/GraphiteDawnCache
${SUPPORT}/Microsoft Edge/Profile [0-9]*/DawnGraphiteCache
${SUPPORT}/Microsoft Edge/Profile [0-9]*/DawnWebGPUCache
${SUPPORT}/Microsoft Edge/Guest Profile/Cache
${SUPPORT}/Microsoft Edge/Guest Profile/Code Cache
${SUPPORT}/Microsoft Edge/Guest Profile/GPUCache
${SUPPORT}/Microsoft Edge/Guest Profile/ShaderCache
${SUPPORT}/Microsoft Edge/Guest Profile/GrShaderCache
${SUPPORT}/Microsoft Edge/Guest Profile/DawnCache
${SUPPORT}/Microsoft Edge/Guest Profile/GraphiteDawnCache
${SUPPORT}/Microsoft Edge/Guest Profile/DawnGraphiteCache
${SUPPORT}/Microsoft Edge/Guest Profile/DawnWebGPUCache
${SUPPORT}/Microsoft Edge/System Profile/Cache
${SUPPORT}/Microsoft Edge/System Profile/Code Cache
${SUPPORT}/Microsoft Edge/System Profile/GPUCache
${SUPPORT}/Microsoft Edge/System Profile/ShaderCache
${SUPPORT}/Microsoft Edge/System Profile/GrShaderCache
${SUPPORT}/Microsoft Edge/System Profile/DawnCache
${SUPPORT}/Microsoft Edge/System Profile/GraphiteDawnCache
${SUPPORT}/Microsoft Edge/System Profile/DawnGraphiteCache
${SUPPORT}/Microsoft Edge/System Profile/DawnWebGPUCache
${SUPPORT}/BraveSoftware/Brave-Browser/Default/Cache
${SUPPORT}/BraveSoftware/Brave-Browser/Default/Code Cache
${SUPPORT}/BraveSoftware/Brave-Browser/Default/GPUCache
${SUPPORT}/BraveSoftware/Brave-Browser/Default/ShaderCache
${SUPPORT}/BraveSoftware/Brave-Browser/Default/GrShaderCache
${SUPPORT}/BraveSoftware/Brave-Browser/Default/DawnCache
${SUPPORT}/BraveSoftware/Brave-Browser/Default/GraphiteDawnCache
${SUPPORT}/BraveSoftware/Brave-Browser/Default/DawnGraphiteCache
${SUPPORT}/BraveSoftware/Brave-Browser/Default/DawnWebGPUCache
${SUPPORT}/BraveSoftware/Brave-Browser/Profile [0-9]*/Cache
${SUPPORT}/BraveSoftware/Brave-Browser/Profile [0-9]*/Code Cache
${SUPPORT}/BraveSoftware/Brave-Browser/Profile [0-9]*/GPUCache
${SUPPORT}/BraveSoftware/Brave-Browser/Profile [0-9]*/ShaderCache
${SUPPORT}/BraveSoftware/Brave-Browser/Profile [0-9]*/GrShaderCache
${SUPPORT}/BraveSoftware/Brave-Browser/Profile [0-9]*/DawnCache
${SUPPORT}/BraveSoftware/Brave-Browser/Profile [0-9]*/GraphiteDawnCache
${SUPPORT}/BraveSoftware/Brave-Browser/Profile [0-9]*/DawnGraphiteCache
${SUPPORT}/BraveSoftware/Brave-Browser/Profile [0-9]*/DawnWebGPUCache
${SUPPORT}/BraveSoftware/Brave-Browser/Guest Profile/Cache
${SUPPORT}/BraveSoftware/Brave-Browser/Guest Profile/Code Cache
${SUPPORT}/BraveSoftware/Brave-Browser/Guest Profile/GPUCache
${SUPPORT}/BraveSoftware/Brave-Browser/Guest Profile/ShaderCache
${SUPPORT}/BraveSoftware/Brave-Browser/Guest Profile/GrShaderCache
${SUPPORT}/BraveSoftware/Brave-Browser/Guest Profile/DawnCache
${SUPPORT}/BraveSoftware/Brave-Browser/Guest Profile/GraphiteDawnCache
${SUPPORT}/BraveSoftware/Brave-Browser/Guest Profile/DawnGraphiteCache
${SUPPORT}/BraveSoftware/Brave-Browser/Guest Profile/DawnWebGPUCache
${SUPPORT}/BraveSoftware/Brave-Browser/System Profile/Cache
${SUPPORT}/BraveSoftware/Brave-Browser/System Profile/Code Cache
${SUPPORT}/BraveSoftware/Brave-Browser/System Profile/GPUCache
${SUPPORT}/BraveSoftware/Brave-Browser/System Profile/ShaderCache
${SUPPORT}/BraveSoftware/Brave-Browser/System Profile/GrShaderCache
${SUPPORT}/BraveSoftware/Brave-Browser/System Profile/DawnCache
${SUPPORT}/BraveSoftware/Brave-Browser/System Profile/GraphiteDawnCache
${SUPPORT}/BraveSoftware/Brave-Browser/System Profile/DawnGraphiteCache
${SUPPORT}/BraveSoftware/Brave-Browser/System Profile/DawnWebGPUCache
${SUPPORT}/Chromium/Default/Cache
${SUPPORT}/Chromium/Default/Code Cache
${SUPPORT}/Chromium/Default/GPUCache
${SUPPORT}/Chromium/Default/ShaderCache
${SUPPORT}/Chromium/Default/GrShaderCache
${SUPPORT}/Chromium/Default/DawnCache
${SUPPORT}/Chromium/Default/GraphiteDawnCache
${SUPPORT}/Chromium/Default/DawnGraphiteCache
${SUPPORT}/Chromium/Default/DawnWebGPUCache
${SUPPORT}/Chromium/Profile [0-9]*/Cache
${SUPPORT}/Chromium/Profile [0-9]*/Code Cache
${SUPPORT}/Chromium/Profile [0-9]*/GPUCache
${SUPPORT}/Chromium/Profile [0-9]*/ShaderCache
${SUPPORT}/Chromium/Profile [0-9]*/GrShaderCache
${SUPPORT}/Chromium/Profile [0-9]*/DawnCache
${SUPPORT}/Chromium/Profile [0-9]*/GraphiteDawnCache
${SUPPORT}/Chromium/Profile [0-9]*/DawnGraphiteCache
${SUPPORT}/Chromium/Profile [0-9]*/DawnWebGPUCache
${SUPPORT}/Chromium/Guest Profile/Cache
${SUPPORT}/Chromium/Guest Profile/Code Cache
${SUPPORT}/Chromium/Guest Profile/GPUCache
${SUPPORT}/Chromium/Guest Profile/ShaderCache
${SUPPORT}/Chromium/Guest Profile/GrShaderCache
${SUPPORT}/Chromium/Guest Profile/DawnCache
${SUPPORT}/Chromium/Guest Profile/GraphiteDawnCache
${SUPPORT}/Chromium/Guest Profile/DawnGraphiteCache
${SUPPORT}/Chromium/Guest Profile/DawnWebGPUCache
${SUPPORT}/Chromium/System Profile/Cache
${SUPPORT}/Chromium/System Profile/Code Cache
${SUPPORT}/Chromium/System Profile/GPUCache
${SUPPORT}/Chromium/System Profile/ShaderCache
${SUPPORT}/Chromium/System Profile/GrShaderCache
${SUPPORT}/Chromium/System Profile/DawnCache
${SUPPORT}/Chromium/System Profile/GraphiteDawnCache
${SUPPORT}/Chromium/System Profile/DawnGraphiteCache
${SUPPORT}/Chromium/System Profile/DawnWebGPUCache
${SUPPORT}/Vivaldi/Default/Cache
${SUPPORT}/Vivaldi/Default/Code Cache
${SUPPORT}/Vivaldi/Default/GPUCache
${SUPPORT}/Vivaldi/Default/ShaderCache
${SUPPORT}/Vivaldi/Default/GrShaderCache
${SUPPORT}/Vivaldi/Default/DawnCache
${SUPPORT}/Vivaldi/Default/GraphiteDawnCache
${SUPPORT}/Vivaldi/Default/DawnGraphiteCache
${SUPPORT}/Vivaldi/Default/DawnWebGPUCache
${SUPPORT}/Vivaldi/Profile [0-9]*/Cache
${SUPPORT}/Vivaldi/Profile [0-9]*/Code Cache
${SUPPORT}/Vivaldi/Profile [0-9]*/GPUCache
${SUPPORT}/Vivaldi/Profile [0-9]*/ShaderCache
${SUPPORT}/Vivaldi/Profile [0-9]*/GrShaderCache
${SUPPORT}/Vivaldi/Profile [0-9]*/DawnCache
${SUPPORT}/Vivaldi/Profile [0-9]*/GraphiteDawnCache
${SUPPORT}/Vivaldi/Profile [0-9]*/DawnGraphiteCache
${SUPPORT}/Vivaldi/Profile [0-9]*/DawnWebGPUCache
${SUPPORT}/Vivaldi/Guest Profile/Cache
${SUPPORT}/Vivaldi/Guest Profile/Code Cache
${SUPPORT}/Vivaldi/Guest Profile/GPUCache
${SUPPORT}/Vivaldi/Guest Profile/ShaderCache
${SUPPORT}/Vivaldi/Guest Profile/GrShaderCache
${SUPPORT}/Vivaldi/Guest Profile/DawnCache
${SUPPORT}/Vivaldi/Guest Profile/GraphiteDawnCache
${SUPPORT}/Vivaldi/Guest Profile/DawnGraphiteCache
${SUPPORT}/Vivaldi/Guest Profile/DawnWebGPUCache
${SUPPORT}/Vivaldi/System Profile/Cache
${SUPPORT}/Vivaldi/System Profile/Code Cache
${SUPPORT}/Vivaldi/System Profile/GPUCache
${SUPPORT}/Vivaldi/System Profile/ShaderCache
${SUPPORT}/Vivaldi/System Profile/GrShaderCache
${SUPPORT}/Vivaldi/System Profile/DawnCache
${SUPPORT}/Vivaldi/System Profile/GraphiteDawnCache
${SUPPORT}/Vivaldi/System Profile/DawnGraphiteCache
${SUPPORT}/Vivaldi/System Profile/DawnWebGPUCache
${SUPPORT}/Arc/User Data/Default/Cache
${SUPPORT}/Arc/User Data/Default/Code Cache
${SUPPORT}/Arc/User Data/Default/GPUCache
${SUPPORT}/Arc/User Data/Default/ShaderCache
${SUPPORT}/Arc/User Data/Default/GrShaderCache
${SUPPORT}/Arc/User Data/Default/DawnCache
${SUPPORT}/Arc/User Data/Default/GraphiteDawnCache
${SUPPORT}/Arc/User Data/Default/DawnGraphiteCache
${SUPPORT}/Arc/User Data/Default/DawnWebGPUCache
${SUPPORT}/Arc/User Data/Profile [0-9]*/Cache
${SUPPORT}/Arc/User Data/Profile [0-9]*/Code Cache
${SUPPORT}/Arc/User Data/Profile [0-9]*/GPUCache
${SUPPORT}/Arc/User Data/Profile [0-9]*/ShaderCache
${SUPPORT}/Arc/User Data/Profile [0-9]*/GrShaderCache
${SUPPORT}/Arc/User Data/Profile [0-9]*/DawnCache
${SUPPORT}/Arc/User Data/Profile [0-9]*/GraphiteDawnCache
${SUPPORT}/Arc/User Data/Profile [0-9]*/DawnGraphiteCache
${SUPPORT}/Arc/User Data/Profile [0-9]*/DawnWebGPUCache
${SUPPORT}/Arc/User Data/Guest Profile/Cache
${SUPPORT}/Arc/User Data/Guest Profile/Code Cache
${SUPPORT}/Arc/User Data/Guest Profile/GPUCache
${SUPPORT}/Arc/User Data/Guest Profile/ShaderCache
${SUPPORT}/Arc/User Data/Guest Profile/GrShaderCache
${SUPPORT}/Arc/User Data/Guest Profile/DawnCache
${SUPPORT}/Arc/User Data/Guest Profile/GraphiteDawnCache
${SUPPORT}/Arc/User Data/Guest Profile/DawnGraphiteCache
${SUPPORT}/Arc/User Data/Guest Profile/DawnWebGPUCache
${SUPPORT}/Arc/User Data/System Profile/Cache
${SUPPORT}/Arc/User Data/System Profile/Code Cache
${SUPPORT}/Arc/User Data/System Profile/GPUCache
${SUPPORT}/Arc/User Data/System Profile/ShaderCache
${SUPPORT}/Arc/User Data/System Profile/GrShaderCache
${SUPPORT}/Arc/User Data/System Profile/DawnCache
${SUPPORT}/Arc/User Data/System Profile/GraphiteDawnCache
${SUPPORT}/Arc/User Data/System Profile/DawnGraphiteCache
${SUPPORT}/Arc/User Data/System Profile/DawnWebGPUCache
```

## browser-root-shader

浏览器根下 shader/code 缓存

- 版本：1；成熟度：`ready`；优先级：220。
- 选择范围：`contents`；判定：`disposable`；默认选中：true。
- 动作：`clear_files`；协议：`online_inventory`。
- 身份检查：`chromium_layout`。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`no_expected_increase`。
- 来源：[chromium-paths](SOURCES.md#chromium-paths)、[electron-paths](SOURCES.md#electron-paths)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `SUPPORT`；目标类型 `directory`：

```text
${SUPPORT}/Google/Chrome/Code Cache
${SUPPORT}/Google/Chrome/GPUCache
${SUPPORT}/Google/Chrome/ShaderCache
${SUPPORT}/Google/Chrome/GrShaderCache
${SUPPORT}/Google/Chrome/DawnCache
${SUPPORT}/Google/Chrome/GraphiteDawnCache
${SUPPORT}/Google/Chrome/DawnGraphiteCache
${SUPPORT}/Google/Chrome/DawnWebGPUCache
${SUPPORT}/Google/Chrome Canary/Code Cache
${SUPPORT}/Google/Chrome Canary/GPUCache
${SUPPORT}/Google/Chrome Canary/ShaderCache
${SUPPORT}/Google/Chrome Canary/GrShaderCache
${SUPPORT}/Google/Chrome Canary/DawnCache
${SUPPORT}/Google/Chrome Canary/GraphiteDawnCache
${SUPPORT}/Google/Chrome Canary/DawnGraphiteCache
${SUPPORT}/Google/Chrome Canary/DawnWebGPUCache
${SUPPORT}/Microsoft Edge/Code Cache
${SUPPORT}/Microsoft Edge/GPUCache
${SUPPORT}/Microsoft Edge/ShaderCache
${SUPPORT}/Microsoft Edge/GrShaderCache
${SUPPORT}/Microsoft Edge/DawnCache
${SUPPORT}/Microsoft Edge/GraphiteDawnCache
${SUPPORT}/Microsoft Edge/DawnGraphiteCache
${SUPPORT}/Microsoft Edge/DawnWebGPUCache
${SUPPORT}/BraveSoftware/Brave-Browser/Code Cache
${SUPPORT}/BraveSoftware/Brave-Browser/GPUCache
${SUPPORT}/BraveSoftware/Brave-Browser/ShaderCache
${SUPPORT}/BraveSoftware/Brave-Browser/GrShaderCache
${SUPPORT}/BraveSoftware/Brave-Browser/DawnCache
${SUPPORT}/BraveSoftware/Brave-Browser/GraphiteDawnCache
${SUPPORT}/BraveSoftware/Brave-Browser/DawnGraphiteCache
${SUPPORT}/BraveSoftware/Brave-Browser/DawnWebGPUCache
${SUPPORT}/Chromium/Code Cache
${SUPPORT}/Chromium/GPUCache
${SUPPORT}/Chromium/ShaderCache
${SUPPORT}/Chromium/GrShaderCache
${SUPPORT}/Chromium/DawnCache
${SUPPORT}/Chromium/GraphiteDawnCache
${SUPPORT}/Chromium/DawnGraphiteCache
${SUPPORT}/Chromium/DawnWebGPUCache
${SUPPORT}/Vivaldi/Code Cache
${SUPPORT}/Vivaldi/GPUCache
${SUPPORT}/Vivaldi/ShaderCache
${SUPPORT}/Vivaldi/GrShaderCache
${SUPPORT}/Vivaldi/DawnCache
${SUPPORT}/Vivaldi/GraphiteDawnCache
${SUPPORT}/Vivaldi/DawnGraphiteCache
${SUPPORT}/Vivaldi/DawnWebGPUCache
${SUPPORT}/Arc/User Data/Code Cache
${SUPPORT}/Arc/User Data/GPUCache
${SUPPORT}/Arc/User Data/ShaderCache
${SUPPORT}/Arc/User Data/GrShaderCache
${SUPPORT}/Arc/User Data/DawnCache
${SUPPORT}/Arc/User Data/GraphiteDawnCache
${SUPPORT}/Arc/User Data/DawnGraphiteCache
${SUPPORT}/Arc/User Data/DawnWebGPUCache
```

## firefox-support-cache

Firefox 专用缓存候选

- 版本：1；成熟度：`research`；优先级：400。
- 选择范围：`contents`；判定：`investigate`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`unresolved`。
- 来源：[mole-caches](SOURCES.md#mole-caches)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。
- 待补证据/实现：补充 Mozilla 的具体 profile/local-profile 路径与 cache2 验证。Library/Caches 下的标准域由通用规则覆盖。

根 `SUPPORT`；目标类型 `directory`：

```text
${SUPPORT}/Firefox/Profiles/*/cache2
```

## design-media-cache

设计软件专用缓存候选

- 版本：1；成熟度：`research`；优先级：400。
- 选择范围：`contents`；判定：`investigate`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`unresolved`。
- 来源：[mole-caches](SOURCES.md#mole-caches)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。
- 待补证据/实现：补充产品官方用途、原始媒体仍可获取及恢复语义；不借其他清理工具的选择自动启用。

根 `SUPPORT`；目标类型 `directory`：

```text
${SUPPORT}/Adobe/Common/Media Cache Files
${SUPPORT}/com.bohemiancoding.sketch3/cache
```

## support-unreviewed-leaf

未登记应用的浅层缓存/日志候选

- 版本：1；成熟度：`research`；优先级：10。
- 选择范围：`contents`；判定：`investigate`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`unresolved`。
- 来源：[product-boundary](SOURCES.md#product-boundary)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。
- 待补证据/实现：需应用级依据；只发现和计量，不递归按关键词删除。

根 `SUPPORT`；目标类型 `directory`：

```text
${SUPPORT}/*/Cache
${SUPPORT}/*/Caches
${SUPPORT}/*/cache
${SUPPORT}/*/log
${SUPPORT}/*/Log
${SUPPORT}/*/logs
${SUPPORT}/*/Logs
```

## codex-legacy-tui-log

Codex 官方启动逻辑可清的旧诊断日志

- 版本：1；成熟度：`ready`；优先级：300。
- 选择范围：`contents`；判定：`disposable`；默认选中：true。
- 动作：`clear_files`；协议：`online_inventory`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：只生成今后的诊断。
- 影响：旧诊断不可恢复；不读取正文。
- 费用字段：`no_expected_increase`。
- 来源：[codex-log](SOURCES.md#codex-log)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `CODEX_HOME`；目标类型 `file`：

```text
${CODEX_HOME}/log/codex-tui.log
```

## codex-other-log

Codex 其他日志候选

- 版本：1；成熟度：`research`；优先级：10。
- 选择范围：`contents`；判定：`investigate`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`unresolved`。
- 来源：[codex-log](SOURCES.md#codex-log)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。
- 待补证据/实现：本次源码仅证明特定旧 TUI 文件；其余日志需补充对应写入者。

根 `CODEX_HOME`；目标类型 `any`：

```text
${CODEX_HOME}/log/*
```

## codex-model-catalog

模型列表和元数据缓存

- 版本：1；成熟度：`research`；优先级：400。
- 选择范围：`contents`；判定：`investigate`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`unresolved`。
- 来源：[codex-models](SOURCES.md#codex-models)、[codex-client](SOURCES.md#codex-client)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。
- 待补证据/实现：刷新不是推理，但元数据可能改变后续请求；费用约束未查清前不默认选中。

根 `CODEX_HOME`；目标类型 `file`：

```text
${CODEX_HOME}/models_cache.json
```

## codex-shell-snapshots

本地 Shell 初始化快照

- 版本：1；成熟度：`research`；优先级：400。
- 选择范围：`contents`；判定：`investigate`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`unresolved`。
- 来源：[codex-snapshot](SOURCES.md#codex-snapshot)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。
- 待补证据/实现：需要实现与源码一致的生命周期识别，避免活动命令失败后引发模型重试。

根 `CODEX_HOME`；目标类型 `directory`：

```text
${CODEX_HOME}/shell_snapshots
```

## codex-arg0

自动生成的命令入口

- 版本：1；成熟度：`research`；优先级：400。
- 选择范围：`contents`；判定：`investigate`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`unresolved`。
- 来源：[codex-arg0](SOURCES.md#codex-arg0)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。
- 待补证据/实现：已定位锁协议，但 Python/macOS 锁兼容和退休动作尚未做 fixture 验证；禁止删 tmp 整体。

根 `CODEX_HOME`；目标类型 `directory`：

```text
${CODEX_HOME}/tmp/arg0-macos/codex-arg0*
${CODEX_HOME}/tmp/arg0/codex-arg0*
```

## codex-daemon-releases

daemon 旧运行时

- 版本：1；成熟度：`research`；优先级：400。
- 选择范围：`contents`；判定：`investigate`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`unresolved`。
- 来源：[codex-pruning](SOURCES.md#codex-pruning)、[codex-install](SOURCES.md#codex-install)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。
- 待补证据/实现：需匹配 current 与 selection-history、两类锁、当前/前次选择和运行可执行文件身份；不能仅按版本号排序。

根 `CODEX_HOME`；目标类型 `directory`：

```text
${CODEX_HOME}/packages/app-server-daemon/releases/*
```

## codex-standalone-releases

独立 CLI 版本目录

- 版本：1；成熟度：`research`；优先级：400。
- 选择范围：`contents`；判定：`investigate`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`unresolved`。
- 来源：[codex-install](SOURCES.md#codex-install)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。
- 待补证据/实现：独立 CLI 与 daemon 保留职责不等同；需查启动器/后台运行关系和原生退休协议。

根 `CODEX_HOME`；目标类型 `directory`：

```text
${CODEX_HOME}/packages/standalone/releases/*
```

## codex-daemon-staging

源码确认的发布前暂存

- 版本：1；成熟度：`research`；优先级：500。
- 选择范围：`contents`；判定：`investigate`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`unresolved`。
- 来源：[codex-stage](SOURCES.md#codex-stage)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。
- 待补证据/实现：确认不在发布事务中，并实现同一安装/生命周期锁；禁止仅靠目录年龄。

根 `CODEX_HOME`；目标类型 `directory`：

```text
${CODEX_HOME}/packages/app-server-daemon/releases/.staging.*
```

## codex-desktop-runtime-staging

实际观察的桌面运行时安装暂存

- 版本：1；成熟度：`research`；优先级：400。
- 选择范围：`contents`；判定：`investigate`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`unresolved`。
- 来源：[live-layouts](SOURCES.md#live-layouts)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。
- 待补证据/实现：含 payload/ 和 node-runtime.tar.xz；公开 CLI 源码未找到对应安装器，需验证完成/中断判据。

根 `HOME`；目标类型 `directory`：

```text
${HOME}/.cache/codex-runtimes/codex-runtime-install-*
```

## claude-debug-log

Claude Code 调试日志

- 版本：1；成熟度：`ready`；优先级：300。
- 选择范围：`contents`；判定：`disposable`；默认选中：true。
- 动作：`clear_files`；协议：`online_inventory`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：只生成今后的诊断。
- 影响：删除历史诊断；不读取日志内容。
- 费用字段：`no_expected_increase`。
- 来源：[claude-env](SOURCES.md#claude-env)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `CLAUDE_HOME`；目标类型 `file`：

```text
${CLAUDE_HOME}/debug/*.txt
```

## claude-old-native

Claude 原生旧版可执行文件

- 版本：1；成熟度：`ready`；优先级：300。
- 选择范围：`target`；判定：`disposable`；默认选中：true。
- 动作：`retire_claude_version`；协议：`claude_retirement`。
- 身份检查：`claude_launcher`、`claude_obsolete`、`local_volume`。
- 恢复：原生安装器可重新下载；保留当前及最新两个有效版本。
- 影响：只移除经判定无保留职责的旧版本，运行中的旧版本等待。
- 费用字段：`no_expected_increase`。
- 来源：[claude-install](SOURCES.md#claude-install)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `CLAUDE_VERSIONS`；目标类型 `file`：

```text
${CLAUDE_VERSIONS}/[0-9]*.[0-9]*.[0-9]*
```

## cursor-worker-versions

Cursor agent-worker 版本和临时安装

- 版本：1；成熟度：`research`；优先级：500。
- 选择范围：`contents`；判定：`investigate`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`unresolved`。
- 来源：[live-layouts](SOURCES.md#live-layouts)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。
- 待补证据/实现：实测没有 current；需识别 worker 实际使用版本及回退职责，不能清空 globalStorage。

根 `SUPPORT`；目标类型 `directory`：

```text
${SUPPORT}/Cursor/User/globalStorage/anysphere.cursor-agent-worker/agent-cli/.local/share/cursor-agent/versions/*
```

## cursor-cli-versions

Cursor CLI 独立安装候选

- 版本：1；成熟度：`research`；优先级：400。
- 选择范围：`contents`；判定：`investigate`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`unresolved`。
- 来源：[product-boundary](SOURCES.md#product-boundary)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。
- 待补证据/实现：本机没有对该布局完成验证；需官方安装器依据与 launcher 映射。

根 `HOME`；目标类型 `directory`：

```text
${HOME}/.local/share/cursor-agent/versions/*
```

## next-build-cache

Next.js 构建缓存

- 版本：1；成熟度：`ready`；优先级：100。
- 选择范围：`contents`；判定：`disposable`；默认选中：true。
- 动作：`clear_files`；协议：`project_cache`。
- 身份检查：`next_project`、`project_untracked`。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`no_expected_increase`。
- 来源：[next-cache](SOURCES.md#next-cache)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `NEXT_DIST`；目标类型 `directory`：

```text
${NEXT_DIST}/cache
```

## cargo-incremental

Cargo 本地增量编译产物

- 版本：1；成熟度：`ready`；优先级：100。
- 选择范围：`contents`；判定：`disposable`；默认选中：true。
- 动作：`clear_files`；协议：`project_cache`。
- 身份检查：`rust_project`、`project_untracked`。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：只清 incremental，不清 deps/build/整个 target；活动编译叶项待执行。
- 费用字段：`no_expected_increase`。
- 来源：[cargo-cache](SOURCES.md#cargo-cache)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `CARGO_BUILD`；目标类型 `directory`：

```text
${CARGO_BUILD}/debug/incremental
${CARGO_BUILD}/release/incremental
${CARGO_BUILD}/*/debug/incremental
${CARGO_BUILD}/*/release/incremental
```

## python-bytecode

有对应源码的 Python 编译缓存

- 版本：1；成熟度：`ready`；优先级：100。
- 选择范围：`target`；判定：`disposable`；默认选中：true。
- 动作：`clear_files`；协议：`project_cache`。
- 身份检查：`python_project`、`python_source_pair`、`project_untracked`。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`no_expected_increase`。
- 来源：[python-bytecode](SOURCES.md#python-bytecode)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `PROJECT`；目标类型 `file`：

```text
${PROJECT}/**/__pycache__/*.pyc
```

## pytest-core-cache

pytest 内置测试索引和失败列表

- 版本：1；成熟度：`ready`；优先级：100。
- 选择范围：`target`；判定：`disposable`；默认选中：true。
- 动作：`clear_files`；协议：`project_cache`。
- 身份检查：`python_project`、`cache_tag`、`project_untracked`。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：丢失历史失败/排序信息；不自动重跑测试。
- 费用字段：`no_expected_increase`。
- 来源：[pytest-cache](SOURCES.md#pytest-cache)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `PYTEST_CACHE`；目标类型 `file`：

```text
${PYTEST_CACHE}/v/cache/nodeids
${PYTEST_CACHE}/v/cache/lastfailed
${PYTEST_CACHE}/v/cache/stepwise
```

## pytest-plugin-cache

pytest 插件自定义缓存

- 版本：1；成熟度：`research`；优先级：10。
- 选择范围：`contents`；判定：`investigate`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`unresolved`。
- 来源：[pytest-cache](SOURCES.md#pytest-cache)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。
- 待补证据/实现：插件可能缓存付费 API/模型结果；未确认键用途时不得清空整个 .pytest_cache。

根 `PYTEST_CACHE`；目标类型 `any`：

```text
${PYTEST_CACHE}/v/*
```

## ruff-cache

Ruff 本地检查结果

- 版本：1；成熟度：`ready`；优先级：100。
- 选择范围：`contents`；判定：`disposable`；默认选中：true。
- 动作：`clear_files`；协议：`project_cache`。
- 身份检查：`python_project`、`cache_tag`、`ruff_layout`、`project_untracked`。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`no_expected_increase`。
- 来源：[ruff-cache](SOURCES.md#ruff-cache)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `RUFF_CACHE`；目标类型 `directory`：

```text
${RUFF_CACHE}
```

## npm-content-cache

npm 内容寻址下载缓存

- 版本：1；成熟度：`ready`；优先级：600。
- 选择范围：`native_domain`；判定：`disposable`；默认选中：true。
- 动作：`native_npm_clean`；协议：`native_npm`。
- 身份检查：`native_domain_verified`、`native_supported`。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`no_expected_increase`。
- 来源：[npm-cache](SOURCES.md#npm-cache)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `NPM_CACHE`；目标类型 `directory`：

```text
${NPM_CACHE}/_cacache
```

## npm-npx-cache

npm exec/npx 安装缓存

- 版本：1；成熟度：`ready`；优先级：600。
- 选择范围：`native_domain`；判定：`disposable`；默认选中：true。
- 动作：`native_npx_rm`；协议：`native_npx`。
- 身份检查：`native_domain_verified`、`native_supported`。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`no_expected_increase`。
- 来源：[npm-cache](SOURCES.md#npm-cache)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `NPM_CACHE`；目标类型 `directory`：

```text
${NPM_CACHE}/_npx
```

## npm-diagnostic-log

npm 诊断日志

- 版本：1；成熟度：`ready`；优先级：600。
- 选择范围：`contents`；判定：`disposable`；默认选中：true。
- 动作：`clear_files`；协议：`online_inventory`。
- 身份检查：`native_domain_verified`。
- 恢复：只生成今后的日志。
- 影响：历史日志不可恢复。
- 费用字段：`no_expected_increase`。
- 来源：[npm-cache](SOURCES.md#npm-cache)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `NPM_CACHE`；目标类型 `file`：

```text
${NPM_CACHE}/_logs/*.log
```

## uv-native-cache

uv 下载/构建缓存域

- 版本：1；成熟度：`ready`；优先级：600。
- 选择范围：`native_domain`；判定：`disposable`；默认选中：true。
- 动作：`native_uv_clean`；协议：`native_uv`。
- 身份检查：`native_domain_verified`、`native_supported`。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`no_expected_increase`。
- 来源：[uv-cache](SOURCES.md#uv-cache)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `UV_CACHE`；目标类型 `directory`：

```text
${UV_CACHE}
```

## playwright-download

Playwright 自动下载副本

- 版本：1；成熟度：`ready`；优先级：600。
- 选择范围：`target`；判定：`disposable`；默认选中：true。
- 动作：`remove_downloaded_runtime`；协议：`download_runtime`。
- 身份检查：`playwright_layout`。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：再次使用前可能需要原生安装命令下载；不要通过运行模型任务触发恢复。
- 费用字段：`no_expected_increase`。
- 来源：[playwright](SOURCES.md#playwright)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `PLAYWRIGHT_CACHE`；目标类型 `directory`：

```text
${PLAYWRIGHT_CACHE}/chromium-*
${PLAYWRIGHT_CACHE}/chromium_headless_shell-*
${PLAYWRIGHT_CACHE}/firefox-*
${PLAYWRIGHT_CACHE}/webkit-*
${PLAYWRIGHT_CACHE}/ffmpeg-*
```

## puppeteer-download

Puppeteer 自动下载副本

- 版本：1；成熟度：`ready`；优先级：600。
- 选择范围：`target`；判定：`disposable`；默认选中：true。
- 动作：`remove_puppeteer_runtime`；协议：`puppeteer_runtime`。
- 身份检查：`puppeteer_layout`。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`no_expected_increase`。
- 来源：[puppeteer](SOURCES.md#puppeteer)、[puppeteer-cache-source](SOURCES.md#puppeteer-cache-source)、[puppeteer-chrome-source](SOURCES.md#puppeteer-chrome-source)、[puppeteer-shell-source](SOURCES.md#puppeteer-shell-source)、[puppeteer-firefox-source](SOURCES.md#puppeteer-firefox-source)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `PUPPETEER_CACHE`；目标类型 `directory`：

```text
${PUPPETEER_CACHE}/chrome/mac-*
${PUPPETEER_CACHE}/chrome/mac_arm-*
${PUPPETEER_CACHE}/chrome-headless-shell/mac-*
${PUPPETEER_CACHE}/chrome-headless-shell/mac_arm-*
${PUPPETEER_CACHE}/firefox/mac-*
${PUPPETEER_CACHE}/firefox/mac_arm-*
```

## preserve-codex-state

会话、配置、账本、插件、worktree 及安装控制状态

- 版本：1；成熟度：`protected`；优先级：1000。
- 选择范围：`contents`；判定：`retain`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：不适用。
- 影响：保留；不进入普通缓存清理。
- 费用字段：`not_assessed_out_of_scope`。
- 来源：[product-boundary](SOURCES.md#product-boundary)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `CODEX_HOME`；目标类型 `any`：

```text
${CODEX_HOME}/auth.json
${CODEX_HOME}/config.toml
${CODEX_HOME}/sessions
${CODEX_HOME}/archived_sessions
${CODEX_HOME}/history.jsonl
${CODEX_HOME}/session_index.jsonl
${CODEX_HOME}/state_*.sqlite*
${CODEX_HOME}/logs_*.sqlite*
${CODEX_HOME}/memories
${CODEX_HOME}/worktrees
${CODEX_HOME}/plugins
${CODEX_HOME}/skills
${CODEX_HOME}/packages/*/current
${CODEX_HOME}/packages/*/selection-history
${CODEX_HOME}/packages/*/install.lock*
```

## preserve-claude-state

Claude 会话、环境、插件与用户状态

- 版本：1；成熟度：`protected`；优先级：1000。
- 选择范围：`contents`；判定：`retain`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：不适用。
- 影响：保留；不进入普通缓存清理。
- 费用字段：`not_assessed_out_of_scope`。
- 来源：[product-boundary](SOURCES.md#product-boundary)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `CLAUDE_HOME`；目标类型 `any`：

```text
${CLAUDE_HOME}/projects
${CLAUDE_HOME}/history.jsonl
${CLAUDE_HOME}/settings.json
${CLAUDE_HOME}/settings.local.json
${CLAUDE_HOME}/.credentials.json
${CLAUDE_HOME}/todos
${CLAUDE_HOME}/tasks
${CLAUDE_HOME}/plans
${CLAUDE_HOME}/file-history
${CLAUDE_HOME}/plugins
${CLAUDE_HOME}/skills
${CLAUDE_HOME}/session-env
```

## preserve-primary-runtime

当前工具运行环境不属于安装暂存

- 版本：1；成熟度：`protected`；优先级：1000。
- 选择范围：`contents`；判定：`retain`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：不适用。
- 影响：保留；不进入普通缓存清理。
- 费用字段：`not_assessed_out_of_scope`。
- 来源：[product-boundary](SOURCES.md#product-boundary)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `HOME`；目标类型 `any`：

```text
${HOME}/.cache/codex-runtimes/codex-primary-runtime
```

## preserve-editor-state

应用/编辑器状态；不从通用缓存规则清除

- 版本：1；成熟度：`protected`；优先级：1000。
- 选择范围：`contents`；判定：`retain`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：不适用。
- 影响：保留；不进入普通缓存清理。
- 费用字段：`not_assessed_out_of_scope`。
- 来源：[product-boundary](SOURCES.md#product-boundary)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `SUPPORT`；目标类型 `any`：

```text
${SUPPORT}/Code/User
${SUPPORT}/Code/Backups
${SUPPORT}/Code/Local Storage
${SUPPORT}/Code/IndexedDB
${SUPPORT}/Code/Session Storage
${SUPPORT}/Code/Cookies
${SUPPORT}/Code/Login Data
${SUPPORT}/Code/History
${SUPPORT}/Code/Service Worker
${SUPPORT}/Code - Insiders/User
${SUPPORT}/Code - Insiders/Backups
${SUPPORT}/Code - Insiders/Local Storage
${SUPPORT}/Code - Insiders/IndexedDB
${SUPPORT}/Code - Insiders/Session Storage
${SUPPORT}/Code - Insiders/Cookies
${SUPPORT}/Code - Insiders/Login Data
${SUPPORT}/Code - Insiders/History
${SUPPORT}/Code - Insiders/Service Worker
${SUPPORT}/VSCodium/User
${SUPPORT}/VSCodium/Backups
${SUPPORT}/VSCodium/Local Storage
${SUPPORT}/VSCodium/IndexedDB
${SUPPORT}/VSCodium/Session Storage
${SUPPORT}/VSCodium/Cookies
${SUPPORT}/VSCodium/Login Data
${SUPPORT}/VSCodium/History
${SUPPORT}/VSCodium/Service Worker
${SUPPORT}/Slack/User
${SUPPORT}/Slack/Backups
${SUPPORT}/Slack/Local Storage
${SUPPORT}/Slack/IndexedDB
${SUPPORT}/Slack/Session Storage
${SUPPORT}/Slack/Cookies
${SUPPORT}/Slack/Login Data
${SUPPORT}/Slack/History
${SUPPORT}/Slack/Service Worker
${SUPPORT}/Discord/User
${SUPPORT}/Discord/Backups
${SUPPORT}/Discord/Local Storage
${SUPPORT}/Discord/IndexedDB
${SUPPORT}/Discord/Session Storage
${SUPPORT}/Discord/Cookies
${SUPPORT}/Discord/Login Data
${SUPPORT}/Discord/History
${SUPPORT}/Discord/Service Worker
${SUPPORT}/Notion/User
${SUPPORT}/Notion/Backups
${SUPPORT}/Notion/Local Storage
${SUPPORT}/Notion/IndexedDB
${SUPPORT}/Notion/Session Storage
${SUPPORT}/Notion/Cookies
${SUPPORT}/Notion/Login Data
${SUPPORT}/Notion/History
${SUPPORT}/Notion/Service Worker
${SUPPORT}/Figma/User
${SUPPORT}/Figma/Backups
${SUPPORT}/Figma/Local Storage
${SUPPORT}/Figma/IndexedDB
${SUPPORT}/Figma/Session Storage
${SUPPORT}/Figma/Cookies
${SUPPORT}/Figma/Login Data
${SUPPORT}/Figma/History
${SUPPORT}/Figma/Service Worker
${SUPPORT}/Termius/User
${SUPPORT}/Termius/Backups
${SUPPORT}/Termius/Local Storage
${SUPPORT}/Termius/IndexedDB
${SUPPORT}/Termius/Session Storage
${SUPPORT}/Termius/Cookies
${SUPPORT}/Termius/Login Data
${SUPPORT}/Termius/History
${SUPPORT}/Termius/Service Worker
${SUPPORT}/Codex/User
${SUPPORT}/Codex/Backups
${SUPPORT}/Codex/Local Storage
${SUPPORT}/Codex/IndexedDB
${SUPPORT}/Codex/Session Storage
${SUPPORT}/Codex/Cookies
${SUPPORT}/Codex/Login Data
${SUPPORT}/Codex/History
${SUPPORT}/Codex/Service Worker
${SUPPORT}/Claude/User
${SUPPORT}/Claude/Backups
${SUPPORT}/Claude/Local Storage
${SUPPORT}/Claude/IndexedDB
${SUPPORT}/Claude/Session Storage
${SUPPORT}/Claude/Cookies
${SUPPORT}/Claude/Login Data
${SUPPORT}/Claude/History
${SUPPORT}/Claude/Service Worker
${SUPPORT}/ChatGPT/User
${SUPPORT}/ChatGPT/Backups
${SUPPORT}/ChatGPT/Local Storage
${SUPPORT}/ChatGPT/IndexedDB
${SUPPORT}/ChatGPT/Session Storage
${SUPPORT}/ChatGPT/Cookies
${SUPPORT}/ChatGPT/Login Data
${SUPPORT}/ChatGPT/History
${SUPPORT}/ChatGPT/Service Worker
${SUPPORT}/Cursor/User
${SUPPORT}/Cursor/Backups
${SUPPORT}/Cursor/Local Storage
${SUPPORT}/Cursor/IndexedDB
${SUPPORT}/Cursor/Session Storage
${SUPPORT}/Cursor/Cookies
${SUPPORT}/Cursor/Login Data
${SUPPORT}/Cursor/History
${SUPPORT}/Cursor/Service Worker
${SUPPORT}/Windsurf/User
${SUPPORT}/Windsurf/Backups
${SUPPORT}/Windsurf/Local Storage
${SUPPORT}/Windsurf/IndexedDB
${SUPPORT}/Windsurf/Session Storage
${SUPPORT}/Windsurf/Cookies
${SUPPORT}/Windsurf/Login Data
${SUPPORT}/Windsurf/History
${SUPPORT}/Windsurf/Service Worker
${SUPPORT}/LM Studio/User
${SUPPORT}/LM Studio/Backups
${SUPPORT}/LM Studio/Local Storage
${SUPPORT}/LM Studio/IndexedDB
${SUPPORT}/LM Studio/Session Storage
${SUPPORT}/LM Studio/Cookies
${SUPPORT}/LM Studio/Login Data
${SUPPORT}/LM Studio/History
${SUPPORT}/LM Studio/Service Worker
```

## preserve-home-state

凭据、配置和个人数据

- 版本：1；成熟度：`protected`；优先级：1000。
- 选择范围：`contents`；判定：`retain`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：不适用。
- 影响：保留；不进入普通缓存清理。
- 费用字段：`not_assessed_out_of_scope`。
- 来源：[product-boundary](SOURCES.md#product-boundary)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `HOME`；目标类型 `any`：

```text
${HOME}/.ssh
${HOME}/.gnupg
${HOME}/.aws
${HOME}/Library/Preferences
${HOME}/Library/Mail
${HOME}/Library/Messages
${HOME}/Library/Keychains
```

## preserve-project-inputs

有界发现范围内的版本控制、依赖环境和配置不进入普通缓存；src/dist/build 本身未获清理授权，但其中精确匹配的缓存叶项可另行清理

- 版本：1；成熟度：`protected`；优先级：1000。
- 选择范围：`contents`；判定：`retain`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：不适用。
- 影响：保留；不进入普通缓存清理。
- 费用字段：`not_assessed_out_of_scope`。
- 来源：[product-boundary](SOURCES.md#product-boundary)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `PROJECT`；目标类型 `any`：

```text
${PROJECT}/.git
${PROJECT}/node_modules
${PROJECT}/.venv
${PROJECT}/venv
${PROJECT}/.env
${PROJECT}/*/.git
${PROJECT}/*/node_modules
${PROJECT}/*/.venv
${PROJECT}/*/venv
${PROJECT}/*/.env
${PROJECT}/*/*/.git
${PROJECT}/*/*/node_modules
${PROJECT}/*/*/.venv
${PROJECT}/*/*/venv
${PROJECT}/*/*/.env
${PROJECT}/*/*/*/.git
${PROJECT}/*/*/*/node_modules
${PROJECT}/*/*/*/.venv
${PROJECT}/*/*/*/venv
${PROJECT}/*/*/*/.env
${PROJECT}/*/*/*/*/.git
${PROJECT}/*/*/*/*/node_modules
${PROJECT}/*/*/*/*/.venv
${PROJECT}/*/*/*/*/venv
${PROJECT}/*/*/*/*/.env
${PROJECT}/*/*/*/*/*/.git
${PROJECT}/*/*/*/*/*/node_modules
${PROJECT}/*/*/*/*/*/.venv
${PROJECT}/*/*/*/*/*/venv
${PROJECT}/*/*/*/*/*/.env
${PROJECT}/*/*/*/*/*/*/.git
${PROJECT}/*/*/*/*/*/*/node_modules
${PROJECT}/*/*/*/*/*/*/.venv
${PROJECT}/*/*/*/*/*/*/venv
${PROJECT}/*/*/*/*/*/*/.env
```

## preserve-next-data-cache

业务/API 响应缓存可能参与付费计算复用，不与编译缓存一并清理

- 版本：1；成熟度：`protected`；优先级：1000。
- 选择范围：`contents`；判定：`retain`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：不适用。
- 影响：保留；不进入普通缓存清理。
- 费用字段：`not_assessed_out_of_scope`。
- 来源：[next-fetch-cache](SOURCES.md#next-fetch-cache)、[product-boundary](SOURCES.md#product-boundary)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `NEXT_DIST`；目标类型 `any`：

```text
${NEXT_DIST}/cache/fetch-cache
```

## preserve-audit

清理收据和审计历史

- 版本：1；成熟度：`protected`；优先级：1000。
- 选择范围：`contents`；判定：`retain`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：不适用。
- 影响：保留；不进入普通缓存清理。
- 费用字段：`not_assessed_out_of_scope`。
- 来源：[product-boundary](SOURCES.md#product-boundary)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `HOME`；目标类型 `any`：

```text
${HOME}/Library/Logs/MacLean
${HOME}/Library/Logs/maclean
${HOME}/Library/Logs/macos-disk-auditor
${HOME}/Library/Logs/mole
```

## preserve-sync-state

同步或可能尚未同步的数据

- 版本：1；成熟度：`protected`；优先级：1000。
- 选择范围：`contents`；判定：`retain`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：不适用。
- 影响：保留；不进入普通缓存清理。
- 费用字段：`not_assessed_out_of_scope`。
- 来源：[product-boundary](SOURCES.md#product-boundary)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `HOME`；目标类型 `any`：

```text
${HOME}/Library/Caches/CloudKit*
${HOME}/Library/Caches/*[Ff]ile[Pp]rovider*
```

## preserve-service-state

系统服务专用状态，普通文件清理协议未验证

- 版本：1；成熟度：`protected`；优先级：1000。
- 选择范围：`contents`；判定：`retain`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：不适用。
- 影响：保留；不进入普通缓存清理。
- 费用字段：`not_assessed_out_of_scope`。
- 来源：[product-boundary](SOURCES.md#product-boundary)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `HOME`；目标类型 `any`：

```text
${HOME}/Library/Caches/com.apple.FontRegistry*
${HOME}/Library/Caches/com.apple.[sS]potlight*
```

## preserve-model-bundles

模型/运行时资源不是普通缓存

- 版本：1；成熟度：`protected`；优先级：1000。
- 选择范围：`contents`；判定：`retain`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：不适用。
- 影响：保留；不进入普通缓存清理。
- 费用字段：`not_assessed_out_of_scope`。
- 来源：[product-boundary](SOURCES.md#product-boundary)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `HOME`；目标类型 `any`：

```text
${HOME}/Library/Caches/*com.apple.e5rt*
```

## preserve-environment-caches

可能包含应用状态或正在链接的依赖环境

- 版本：1；成熟度：`protected`；优先级：1000。
- 选择范围：`contents`；判定：`retain`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：不适用。
- 影响：保留；不进入普通缓存清理。
- 费用字段：`not_assessed_out_of_scope`。
- 来源：[product-boundary](SOURCES.md#product-boundary)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。

根 `HOME`；目标类型 `any`：

```text
${HOME}/Library/Caches/deno
${HOME}/Library/Caches/pypoetry
${HOME}/Library/Caches/org.R-project.R
```

## reserve-native-and-runtime

专用协议拥有的域

- 版本：1；成熟度：`research`；优先级：550。
- 选择范围：`contents`；判定：`investigate`；默认选中：false。
- 动作：`none`；协议：`none`。
- 身份检查：标准域语义 + 全局范围/身份/例外检查。
- 恢复：应用或工具在本地重新生成或下载。
- 影响：下次访问可能重建；打开句柄可能延迟释放空间。
- 费用字段：`unresolved`。
- 来源：[uv-cache](SOURCES.md#uv-cache)、[playwright](SOURCES.md#playwright)。
- 验证范围：文档/源码审阅；本目录未执行该适配器的真实删除测试。
- 待补证据/实现：禁止通用 Library 规则兜底；只有更具体且验证通过的原生/下载规则能接管。

根 `HOME`；目标类型 `directory`：

```text
${HOME}/Library/Caches/uv
${HOME}/Library/Caches/ms-playwright
```

## 根绑定

### HOME

默认：`macOS 当前执行用户的主目录`

Mac 端 pwd.getpwuid(os.getuid()).pw_dir；不使用网页云容器 HOME；禁止以 root 代替用户运行。

### SUPPORT

默认：`${HOME}/Library/Application Support`

固定相对于 Mac HOME，不接受整体覆盖；自定义 userdata 需开发时增加 app_id/绝对根绑定及用例，不能把单个应用根误当整个 SUPPORT。

### CODEX_HOME

默认：`${HOME}/.codex`

显式 --root-map > 本次 Mac 进程的 CODEX_HOME（只读取此键）> 默认。

### CLAUDE_HOME

默认：`${HOME}/.claude`

显式 --root-map > CLAUDE_CONFIG_DIR（只读取此键）> 默认。

### CLAUDE_VERSIONS

默认：`${HOME}/.local/share/claude/versions`

默认位置或显式登记；不依据 CLAUDE_CONFIG_DIR 改变二进制位置。

### PROJECT

默认：`必须由用户选定`

用户选定根下发现的项目；最多深度 6、50000 条目、180 秒；排除环境/安装/版本控制目录。多 manifest 同一目录只登记一次。

### NEXT_DIST

默认：`${PROJECT}/.next`

每项目显式 root-map 可覆盖；不执行 next.config.js/ts；默认不存在时报告可能为未构建/自定义路径，不能猜测全盘。

### CARGO_BUILD

默认：`${PROJECT}/target`

每项目显式 root-map 可覆盖实际 build-dir；不将所有 target 当垃圾；workspace 根必须是用户选定范围。

### PYTEST_CACHE

默认：`${PROJECT}/.pytest_cache`

每项目显式 root-map 覆盖 cache_dir，不导入 conftest 或运行测试。

### RUFF_CACHE

默认：`${PROJECT}/.ruff_cache`

每项目显式 root-map 覆盖实际 cache-dir；不猜配置继承，不运行用户 Python。

### NPM_CACHE

默认：`${HOME}/.npm`

由现有 npm 的 npm config get cache 查询，或显式指定 --cache；默认值只作工具不可用时的只读发现。查询在临时空工作目录运行。

### UV_CACHE

默认：`${HOME}/.cache/uv`

由现有 uv cache dir 查询，或显式指定 --cache-dir；默认及 ~/Library/Caches/uv 仅作只读备用入口，不能假定 Mac 一定使用 Library。

### PLAYWRIGHT_CACHE

默认：`${HOME}/Library/Caches/ms-playwright`

显式 root-map > PLAYWRIGHT_BROWSERS_PATH 的绝对路径 > 默认；值 0 表示包内安装，不展开为 /0，首版不清。

### PUPPETEER_CACHE

默认：`${HOME}/.cache/puppeteer`

显式 root-map > PUPPETEER_CACHE_DIR > 默认；不执行 .puppeteerrc.js。

## 身份探针定义

以下是需要开发的探针，不能由模型提供真假值代替。

### chromium_layout

缓存目标的应用 profile 根有至少两个独立非链接目录：Code Cache/GPUCache/ShaderCache/GrShaderCache/DawnCache/GraphiteDawnCache/DawnGraphiteCache/DawnWebGPUCache；只凭名字不通过。

### editor_layout

明确已安装的 Code/Code - Insiders/VSCodium（或已登记同布局产品）；目标在其已登记 userdata 根，User 目录存在且非链接；不得执行该应用。

### browser_profile

profile 名必须为 Default/Guest Profile/System Profile 或完整匹配 Profile [0-9]+；并通过 chromium_layout。

### next_project

同一 PROJECT 的 package.json dependencies/devDependencies 含 next；只读取这些字段，文件上限 1 MiB。

### rust_project

PROJECT/Cargo.toml 是非链接文件；不执行 build.rs。

### python_project

PROJECT 中有 pyproject.toml/setup.cfg/setup.py/requirements.txt 之一；仅判断存在。

### python_source_pair

按 importlib.util.source_from_cache 的命名关系，将每个 .pyc 对应到现存非链接 .py；不存在源码的 bytecode 不入清单。

### project_untracked

仅查询所选叶项的 git ls-files；若被跟踪则保留该项；非 Git 项目通过，Git 查询失败则待调查；项目其他修改无关。

### cache_tag

目标缓存根 CACHEDIR.TAG 为非链接文件且前 43 字节是 Signature: 8a477f597d28d172789f06886806bc55；不读取其他内容。

### ruff_layout

根只含 CACHEDIR.TAG/.gitignore 与数字点分版本目录；未知顶层条目分开报告，不授权未知子树。

### native_domain_verified

原生程序给出的绝对缓存域与封存根一致；安全路径检查通过，根不是 HOME、/、源码/凭据目录。

### native_supported

已安装工具的 --version/--help 确认指定命令与根参数可用；禁止临时下载 npm 包来获得命令。

### playwright_layout

version 名匹配 (chromium|chromium_headless_shell|firefox|webkit|ffmpeg)-[0-9]+；有普通 INSTALLATION_COMPLETE 文件。

### puppeteer_layout

产品 chrome/chrome-headless-shell/firefox，版本目录完整匹配 mac(_arm)?-[A-Za-z0-9._-]+；Chrome 为 chrome-mac-{x64|arm64}/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing，headless shell 为 chrome-headless-shell-mac-{x64|arm64}/chrome-headless-shell，Firefox 为 Firefox.app/Contents/MacOS/firefox 或 Firefox Nightly.app/Contents/MacOS/firefox。架构须与 mac/mac_arm 相符；可执行文件必须在该副本内。产品 .metadata 上限 1 MiB，只接受 aliases/executablePaths 的字符串映射；可执行文件重定向至副本外或未知格式不通过。

### claude_launcher

仅允许 readlink 读取 ~/.local/bin/claude 元数据；目标严格落在 CLAUDE_VERSIONS 下，是签名可验证的普通 Mach-O 文件；自定义 launcher/脚本或无法确认厂商的二进制不通过。

### claude_obsolete

版本名是完整数字 semver；同一根按 semver 排序，排除 launcher 当前目标和最新两个有效版本；非候选版本单独保留。

### local_volume

以目标卷的系统属性确认本地卷；旧运行时若位于网络/未知卷则等待人工指定生命周期，不自动清。

## 执行协议定义

### online_inventory

封存普通文件清单；保持目录；执行时复核文件及祖先身份；新/修改文件不删；不打开日志正文；独立特殊文件跳过。

### project_cache

与 online_inventory 相同；对本次明确活动构建的写入叶项等待结束，其他独立缓存继续；不检查整个项目是否干净。

### native_npm

绝对 npm 路径及固定 argv，cache clean --force --cache ROOT；--force 是 npm 的清缓存必需参数，不是强制解锁；完整原生域批准，记录创建的诊断文件。

### native_npx

绝对 npm 路径及 cache npx rm --cache ROOT；仅在已验证支持的版本执行；按完整 _npx 域批准，目标有运行引用则等待。

### native_uv

绝对 uv 路径及 cache clean --cache-dir ROOT；保留锁，不传 --force；支持时为子进程设置 UV_LOCK_TIMEOUT=30。不能用 prune 冒充 clean。

### download_runtime

完整下载副本为一个动作；明确具体目标无运行引用后删除，不关闭浏览器；内部符号链接只解绑、不跟随，外部/唯一内容则待调查。

### puppeteer_runtime

先按 download_runtime 协议检查；动作还需声明同一产品 .metadata 中指向目标 buildId 的 aliases 和 platform-buildId 对应 executablePaths 键。只删除这些映射，保留其他字段/版本，文件缺失不创建。写入前复核摘要、并发写入则待执行；不执行用户 JS 配置，不静默扩大清空范围。

### claude_retirement

重新检查 launcher、保留集合和目标二进制身份；确认目标无运行引用；不改 launcher；仅删除批准的旧版本文件。

### none

只读展示或保留，不生成执行动作。
