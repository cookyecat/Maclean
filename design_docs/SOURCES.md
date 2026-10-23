# 规则来源与研究边界

审阅日期：2026-10-19。来源用于说明路径和用途，不代替版本适配测试。

证据类型：official-doc / official-source 为原始文档或写入端源码；maintainer-test-plan 为维护者测试记录；cross-check 仅作交叉线索；local-observation 仅证明本机出现过该布局；product-policy 是本产品明确边界。

固定提交链接可以复核同一份 Codex/Mole 源码；main/canary/HEAD 和在线文档会变化，应在适配器发布时补充实际版本或内容摘要。

本次没有对这些应用的全部版本作运行兼容性保证；catalog 中 application_versions_tested 留空，避免把资料审阅冒充实机验收。

## apple-library

类型：`official-doc`；审阅：2026-10-19。

[原始来源](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/MacOSXDirectories/MacOSXDirectories.html)

Caches 可再生成；Logs 是日志；Application Support 可以包含用户数据。

## electron-paths

类型：`official-doc`；审阅：2026-10-19。

[原始来源](https://www.electronjs.org/docs/latest/api/app#appgetpathname)

sessionData 混合缓存与持久状态，不能清空整个 profile。

## chromium-paths

类型：`official-source`；审阅：2026-10-19。

[原始来源](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/user_data_dir.md)

macOS profile 与用户缓存目录的对应关系；HEAD 链接仅表示本次审阅内容。

## vscode-vsix

类型：`maintainer-test-plan`；审阅：2026-10-19。

[原始来源](https://github.com/microsoft/vscode/issues/99873)

维护者验证 CachedExtensionVSIXs 下载副本；不是已安装扩展目录。

## vscode-environment

类型：`official-source`；审阅：2026-10-19。

[原始来源](https://github.com/microsoft/vscode/blob/main/src/vs/platform/environment/common/environmentService.ts)

logs 与 CachedExtensionVSIXs 位于 userdata；User/globalStorage 为持久状态。本次审阅 main。

## vscode-code-cache

类型：`official-source`；审阅：2026-10-19。

[原始来源](https://github.com/microsoft/vscode/blob/main/src/mainImpl.ts)

getCodeCachePath 返回 userdata/CachedData/commit。本次审阅 main。

## mole-caches

类型：`cross-check`；审阅：2026-10-19。

[原始来源](https://github.com/tw93/Mole/blob/7f83db8a97f4ab754887176b6f7d22c14e955fba/lib/clean/app_caches.sh)

交叉核对具体叶目录；不是所有第三方软件的数据语义保证。

## mole-exceptions

类型：`cross-check`；审阅：2026-10-19。

[原始来源](https://github.com/tw93/Mole/blob/7f83db8a97f4ab754887176b6f7d22c14e955fba/lib/core/base.sh)

辅助发现特殊缓存域；例外归为产品边界，不声称全部有 Apple 的删除禁止规定。

## codex-log

类型：`official-source`；审阅：2026-10-19。

[原始来源](https://github.com/openai/codex/blob/8c076942cb70fba8e5c4732c23f1faabc4aed484/codex-rs/tui/src/lib.rs)

remove_legacy_tui_log_file 删除 log/codex-tui.log，考虑已有打开句柄。

## codex-models

类型：`official-source`；审阅：2026-10-19。

[原始来源](https://github.com/openai/codex/blob/8c076942cb70fba8e5c4732c23f1faabc4aed484/codex-rs/models-manager/src/manager.rs)

models_cache.json 是模型目录缓存；不等于服务端 KV 缓存。

## codex-client

类型：`official-source`；审阅：2026-10-19。

[原始来源](https://github.com/openai/codex/blob/8c076942cb70fba8e5c4732c23f1faabc4aed484/codex-rs/core/src/client.rs)

prompt_cache_key 和会话元数据参与请求；不能将普通本地文件与服务端缓存混同。

## codex-arg0

类型：`official-source`；审阅：2026-10-19。

[原始来源](https://github.com/openai/codex/blob/8c076942cb70fba8e5c4732c23f1faabc4aed484/codex-rs/arg0/src/lib.rs)

tmp/arg0-macos；持有 .lock 的命令入口；清理先加锁再退休目录。

## codex-snapshot

类型：`official-source`；审阅：2026-10-19。

[原始来源](https://github.com/openai/codex/blob/8c076942cb70fba8e5c4732c23f1faabc4aed484/codex-rs/core/src/shell_snapshot.rs)

shell_snapshots 的生成与清理生命周期；当前会话不在原生过期清理范围内。

## codex-install

类型：`official-source`；审阅：2026-10-19。

[原始来源](https://github.com/openai/codex/blob/8c076942cb70fba8e5c4732c23f1faabc4aed484/scripts/install/install.sh)

packages/standalone、app-server-daemon、releases、current 与安装锁。

## codex-pruning

类型：`official-source`；审阅：2026-10-19。

[原始来源](https://github.com/openai/codex/blob/8c076942cb70fba8e5c4732c23f1faabc4aed484/codex-rs/app-server-daemon/src/release_pruning.rs)

daemon 退休依赖选择历史、运行实例和生命周期/安装锁。

## codex-stage

类型：`official-source`；审阅：2026-10-19。

[原始来源](https://github.com/openai/codex/blob/8c076942cb70fba8e5c4732c23f1faabc4aed484/codex-rs/app-server-daemon/src/prepare_install.rs)

daemon releases/.staging.* 是发布前安装区。

## claude-env

类型：`official-doc`；审阅：2026-10-19。

[原始来源](https://code.claude.com/docs/en/env-vars)

配置根可调整；调试日志默认 ~/.claude/debug/<session-id>.txt；debug 日志覆盖变量实际是文件路径。

## claude-install

类型：`official-doc`；审阅：2026-10-19。

[原始来源](https://code.claude.com/docs/en/setup)

原生 launcher 指向 versions；保留当前、正在运行及最新两版，自定义 launcher 不自动推断。

## next-cache

类型：`official-doc`；审阅：2026-10-19。

[原始来源](https://nextjs.org/docs/app/guides/ci-build-caching)

默认 .next/cache 为构建缓存。

## next-fetch-cache

类型：`official-source`；审阅：2026-10-19。

[原始来源](https://github.com/vercel/next.js/blob/canary/packages/next/src/server/lib/incremental-cache/file-system-cache.ts)

fetch 响应持久化到 .next/cache/fetch-cache；可能包含业务/API 结果，不与编译缓存一并清理。本次审阅 canary。

## cargo-cache

类型：`official-doc`；审阅：2026-10-19。

[原始来源](https://doc.rust-lang.org/cargo/reference/build-cache.html)

incremental 在 build-dir；build-dir/target-dir 可配置，内部布局可变化。

## python-bytecode

类型：`official-doc`；审阅：2026-10-19。

[原始来源](https://docs.python.org/3/library/py_compile.html)

编译缓存的 __pycache__ 路径；源文件关系必须保留。

## pytest-cache

类型：`official-doc`；审阅：2026-10-19。

[原始来源](https://docs.pytest.org/en/stable/how-to/cache.html)

cacheprovider 同时支持内置结果和插件自定义 cache，因此只清内置键，未知插件键需调查费用。

## ruff-cache

类型：`official-doc`；审阅：2026-10-19。

[原始来源](https://docs.astral.sh/ruff/settings/#cache-dir)

默认 .ruff_cache；配置及环境可改变位置。

## npm-cache

类型：`official-doc`；审阅：2026-10-19。

[原始来源](https://docs.npmjs.com/cli/v11/commands/npm-cache/)

npm 内容缓存和 npx 维护接口；能力需以本机版本核实。

## uv-cache

类型：`official-doc`；审阅：2026-10-19。

[原始来源](https://docs.astral.sh/uv/concepts/cache/)

必须采用 uv cache clean 协调，不直接改内部桶。

## playwright

类型：`official-doc`；审阅：2026-10-19。

[原始来源](https://playwright.dev/docs/browsers)

macOS 浏览器下载目录及覆盖设置；下载产物不是个人浏览器 profile。

## puppeteer

类型：`official-doc`；审阅：2026-10-19。

[原始来源](https://pptr.dev/guides/configuration)

默认 ~/.cache/puppeteer，可配置。

## puppeteer-cache-source

类型：`official-source`；审阅：2026-10-19。

[原始来源](https://github.com/puppeteer/puppeteer/blob/main/packages/browsers/src/Cache.ts)

目录为 browser/platform-buildId；uninstall 同步更新 .metadata 中的别名和 executablePaths。本次审阅 main。

## puppeteer-chrome-source

类型：`official-source`；审阅：2026-10-19。

[原始来源](https://github.com/puppeteer/puppeteer/blob/main/packages/browsers/src/browser-data/chrome.ts)

Mac Chrome for Testing 可执行文件布局。本次审阅 main。

## puppeteer-shell-source

类型：`official-source`；审阅：2026-10-19。

[原始来源](https://github.com/puppeteer/puppeteer/blob/main/packages/browsers/src/browser-data/chrome-headless-shell.ts)

Mac headless shell 可执行文件布局。本次审阅 main。

## puppeteer-firefox-source

类型：`official-source`；审阅：2026-10-19。

[原始来源](https://github.com/puppeteer/puppeteer/blob/main/packages/browsers/src/browser-data/firefox.ts)

Firefox.app / Firefox Nightly.app 可执行文件布局。本次审阅 main。

## live-layouts

类型：`local-observation`；审阅：2026-10-19。

2026-10-18 本机只读测试：Codex runtime install 目录含 payload/ 和 node-runtime.tar.xz；Cursor agent-worker versions 父级没有 current 链接。观察不证明可删。

## product-boundary

类型：`product-policy`；审阅：2026-10-19。

用户约定：不删唯一内容、工具安装或产生额外模型费用的数据；本地下载/编译成本可接受。
