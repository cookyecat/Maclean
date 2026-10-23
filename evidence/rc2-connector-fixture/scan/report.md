# MacLean 报告

记录类型：scan
完整扫描：True

目标发现：完整；目录计量：完整。文件数与时间限制是扫描工作量限制，与费用和 Token 无关。

每目标最多 250000 次元数据访问、120 秒；整轮最多 600 秒。目录大小来自文件元数据累加，不读取文件正文。

## macOS 应用

### 现在可处理

- 用户标准应用缓存：/Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/Library/Caches/Fixture；逻辑 28672 B，分配 28672 B；ID 2a6302251260f45eb360
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
### 等待处理

### 保留

### 待调查

## AI 客户端

### 现在可处理

### 等待处理

### 保留

### 待调查

## 开发项目与工具

### 现在可处理

### 等待处理

### 保留

### 待调查


## 扫描覆盖

- macos\-user\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home：measurement · matched
- macos\-user\-log /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home：discovery · absent
- sandbox\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home：discovery · absent
- sandbox\-log /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home：discovery · absent
- group\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home：discovery · absent
- group\-log /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home：discovery · absent
- app\-render\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/Library/Application Support：discovery · absent
- ai\-render\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/Library/Application Support：discovery · absent
- editor\-code\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/Library/Application Support：discovery · absent
- editor\-vsix\-download /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/Library/Application Support：discovery · absent
- ai\-editor\-extra\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/Library/Application Support：discovery · absent
- editor\-log /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/Library/Application Support：discovery · absent
- ai\-support\-log /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/Library/Application Support：discovery · absent
- browser\-profile\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/Library/Application Support：discovery · absent
- browser\-root\-shader /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/Library/Application Support：discovery · absent
- firefox\-support\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/Library/Application Support：discovery · absent
- design\-media\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/Library/Application Support：discovery · absent
- support\-unreviewed\-leaf /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/Library/Application Support：discovery · absent
- codex\-legacy\-tui\-log /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/\.codex：discovery · absent
- codex\-other\-log /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/\.codex：discovery · absent
- codex\-model\-catalog /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/\.codex：discovery · absent
- codex\-shell\-snapshots /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/\.codex：discovery · absent
- codex\-arg0 /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/\.codex：discovery · absent
- codex\-daemon\-releases /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/\.codex：discovery · absent
- codex\-standalone\-releases /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/\.codex：discovery · absent
- codex\-daemon\-staging /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/\.codex：discovery · absent
- codex\-desktop\-runtime\-staging /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home：discovery · absent
- claude\-debug\-log /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/\.claude：discovery · absent
- claude\-old\-native /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/\.local/share/claude/versions：discovery · absent
- cursor\-worker\-versions /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/Library/Application Support：discovery · absent
- cursor\-cli\-versions /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home：discovery · absent
- next\-build\-cache None：discovery · not\_requested
- cargo\-incremental None：discovery · not\_requested
- python\-bytecode None：discovery · not\_requested
- pytest\-core\-cache None：discovery · not\_requested
- pytest\-plugin\-cache None：discovery · not\_requested
- ruff\-cache None：discovery · not\_requested
- npm\-content\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/\.npm：discovery · absent
- npm\-npx\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/\.npm：discovery · absent
- npm\-diagnostic\-log /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/\.npm：discovery · absent
- uv\-native\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/\.cache/uv：discovery · absent
- playwright\-download /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/Library/Caches/ms\-playwright：discovery · absent
- puppeteer\-download /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/\.cache/puppeteer：discovery · absent
- preserve\-codex\-state /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/\.codex：discovery · absent
- preserve\-claude\-state /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/\.claude：discovery · absent
- preserve\-primary\-runtime /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home：discovery · absent
- preserve\-editor\-state /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home/Library/Application Support：discovery · absent
- preserve\-home\-state /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home：discovery · absent
- preserve\-project\-inputs None：discovery · not\_requested
- preserve\-next\-data\-cache None：discovery · not\_requested
- preserve\-audit /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home：discovery · absent
- preserve\-sync\-state /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home：discovery · absent
- preserve\-service\-state /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home：discovery · absent
- preserve\-model\-bundles /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home：discovery · absent
- preserve\-environment\-caches /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home：discovery · absent
- reserve\-native\-and\-runtime /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-hh13an67/home：discovery · absent