# 规则覆盖与研究缺口

规则版本 1.1.0。ready 是契约就绪，执行还必须通过本机探针及人工批准。

| 规则 | 成熟度 | 执行协议 | 验证／缺口 |
|---|---|---|---|
| macos-user-cache | ready | online_inventory | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| macos-user-log | ready | online_inventory | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| sandbox-cache | ready | online_inventory | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| sandbox-log | ready | online_inventory | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| group-cache | ready | online_inventory | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| group-log | ready | online_inventory | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| app-render-cache | ready | online_inventory | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| ai-render-cache | ready | online_inventory | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| editor-code-cache | ready | online_inventory | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| editor-vsix-download | ready | online_inventory | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| ai-editor-extra-cache | research | none | 补齐具体产品的目录用途/版本验证，不能仅因继承 VS Code 就认定所有缓存语义相同。 |
| editor-log | ready | online_inventory | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| ai-support-log | research | none | 逐产品确认日志用途；不要将会话/审计/模型结果存储按名字判为日志。 |
| browser-profile-cache | ready | online_inventory | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| browser-root-shader | ready | online_inventory | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| firefox-support-cache | research | none | 补充 Mozilla 的具体 profile/local-profile 路径与 cache2 验证。Library/Caches 下的标准域由通用规则覆盖。 |
| design-media-cache | research | none | 补充产品官方用途、原始媒体仍可获取及恢复语义；不借其他清理工具的选择自动启用。 |
| support-unreviewed-leaf | research | none | 需应用级依据；只发现和计量，不递归按关键词删除。 |
| codex-legacy-tui-log | ready | online_inventory | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| codex-other-log | research | none | 本次源码仅证明特定旧 TUI 文件；其余日志需补充对应写入者。 |
| codex-model-catalog | research | none | 刷新不是推理，但元数据可能改变后续请求；费用约束未查清前不默认选中。 |
| codex-shell-snapshots | research | none | 需要实现与源码一致的生命周期识别，避免活动命令失败后引发模型重试。 |
| codex-arg0 | research | none | 已定位锁协议，但 Python/macOS 锁兼容和退休动作尚未做 fixture 验证；禁止删 tmp 整体。 |
| codex-daemon-releases | research | none | 需匹配 current 与 selection-history、两类锁、当前/前次选择和运行可执行文件身份；不能仅按版本号排序。 |
| codex-standalone-releases | research | none | 独立 CLI 与 daemon 保留职责不等同；需查启动器/后台运行关系和原生退休协议。 |
| codex-daemon-staging | research | none | 确认不在发布事务中，并实现同一安装/生命周期锁；禁止仅靠目录年龄。 |
| codex-desktop-runtime-staging | research | none | 含 payload/ 和 node-runtime.tar.xz；公开 CLI 源码未找到对应安装器，需验证完成/中断判据。 |
| claude-debug-log | ready | online_inventory | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| claude-old-native | ready | claude_retirement | 生命周期 fixture；厂商签名/卷探针模拟，真实版本未验证 |
| cursor-worker-versions | research | none | 实测没有 current；需识别 worker 实际使用版本及回退职责，不能清空 globalStorage。 |
| cursor-cli-versions | research | none | 官方安装器确认 agent/cursor-agent 两个 launcher 指向版本内 cursor-agent；仍缺少升级期间的保留/回退协议及具体运行引用的版本集成验证，保持只读。 |
| next-build-cache | ready | project_cache | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| cargo-incremental | ready | project_cache | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| python-bytecode | ready | project_cache | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| pytest-core-cache | ready | project_cache | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| pytest-plugin-cache | research | none | 插件可能缓存付费 API/模型结果；未确认键用途时不得清空整个 .pytest_cache。 |
| ruff-cache | ready | project_cache | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| npm-content-cache | ready | native_npm | npm 12.2.0 独立临时 cache 集成通过 |
| npm-npx-cache | ready | native_npx | npm 12.2.0 独立临时 cache 集成通过 |
| npm-diagnostic-log | ready | online_inventory | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| uv-native-cache | ready | native_uv | uv 0.12.5 独立缓存、锁和30秒等待集成通过 |
| playwright-download | ready | download_runtime | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| puppeteer-download | ready | puppeteer_runtime | 生产路径契约＋真实文件系统 fixture；具体应用版本见验收记录 |
| preserve-codex-state | protected | none | 保护域，无删除动作 |
| preserve-claude-state | protected | none | 保护域，无删除动作 |
| preserve-primary-runtime | protected | none | 保护域，无删除动作 |
| preserve-editor-state | protected | none | 保护域，无删除动作 |
| preserve-home-state | protected | none | 保护域，无删除动作 |
| preserve-project-inputs | protected | none | 保护域，无删除动作 |
| preserve-next-data-cache | protected | none | 保护域，无删除动作 |
| preserve-audit | protected | none | 保护域，无删除动作 |
| preserve-sync-state | protected | none | 保护域，无删除动作 |
| preserve-service-state | protected | none | 保护域，无删除动作 |
| preserve-model-bundles | protected | none | 保护域，无删除动作 |
| preserve-environment-caches | protected | none | 保护域，无删除动作 |
| reserve-native-and-runtime | research | none | 禁止通用 Library 规则兜底；只有更具体且验证通过的原生/下载规则能接管。 |
