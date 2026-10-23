# 本轮研究记录

日期：2026-10-19。原始来源快照及摘要：`evidence/research-sources.json`。原始规范的源码／文档依据已随规则包保留。

- **Codex arg0**：固定提交的写入端创建 .lock 并持锁整个命令入口寿命，janitor 先获得同一锁，退休目录后再删除。尚无对应版本 Rust 客户端交叉锁集成与真实安装运行验证，仍为 research，不能把目录中的外部可执行文件链接当成普通缓存树跟随删除。
- **Codex daemon**：固定源码读取选择历史、当前发布和运行身份，涉及生命周期／安装锁与迁移职责。按最新两个 semver 保留会丢失该语义；本版未改写其生命周期。
- **Codex 桌面安装暂存**：资料中的 payload/ 布局已纳入保留回归。公开 CLI daemon 的 .staging.* 不是桌面 codex-runtime-install-* 的安装完成证据，两者继续分开。
- **Cursor**：本次取得的官方安装器使用版本化 FINAL_DIR，并建立 agent/cursor-agent 两个 launcher 链接。此证据收窄了 CLI 路径缺口，但没有说明桌面 worker 消费者、回退和并发更新退休协议；没有因此启用删除。
- **Claude Code**：官方文档说明 launcher、当前版本、运行中版本和最新两个版本的保留关系。实现按数值 semver 排序，仅将通过 Mach-O／厂商签名检查的版本纳入有效集合；测试中的签名和本地卷输出模拟有明确标记，未声称真实版本验证。
- **npm 12.2.0**：本机对应 cache.js 的 npxRm 在整域操作时要求 --force。实际独立 fixture 复现了无该参数失败、添加后成功；已更新规则 1.1.0、规则版本及原生 argv。未运行下载型 npx 命令。
- **uv 0.12.5**：独立缓存与外部共享锁实际测试通过。完整默认等待约30.07秒后返回 pending；未使用 --force、未删锁。
- **Puppeteer**：写入端的 uninstall 同时删除指向 buildId 的 aliases 和平台版本 executablePaths。本版封存元数据前态，在删除前复核；并发变更等待，部分失败保留修复提示。没有将元数据事务 fixture 当成官方浏览器下载/恢复验收。

17 条 research 均保留原成熟度。它们的完整路径、用途和未补齐条件仍由 catalog.json 统一生成 RULES.md／SOURCES.md／覆盖表，不能由用户选择或模型判断临时升级。
