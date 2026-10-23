# MacLean 报告

记录类型：scan
完整扫描：True

## macOS 应用

### 现在可处理

- 用户标准应用缓存：/Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/Library/Caches/Fixture；逻辑 28672 B，分配 28672 B；ID 73fdfd859d88d8b2eaa4
  rule：macos\-user\-cache
  impact：下次访问可能重建；打开句柄可能延迟释放空间
  recovery：应用或工具在本地重新生成或下载
  inference_cost_effect：no\_expected\_increase
  sources：\['apple\-library'\]
  gap：
  issues：\[\]
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

- macos\-user\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home：matched
- macos\-user\-log /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home：absent
- sandbox\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home：absent
- sandbox\-log /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home：absent
- group\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home：absent
- group\-log /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home：absent
- app\-render\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/Library/Application Support：absent
- ai\-render\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/Library/Application Support：absent
- editor\-code\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/Library/Application Support：absent
- editor\-vsix\-download /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/Library/Application Support：absent
- ai\-editor\-extra\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/Library/Application Support：absent
- editor\-log /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/Library/Application Support：absent
- ai\-support\-log /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/Library/Application Support：absent
- browser\-profile\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/Library/Application Support：absent
- browser\-root\-shader /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/Library/Application Support：absent
- firefox\-support\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/Library/Application Support：absent
- design\-media\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/Library/Application Support：absent
- support\-unreviewed\-leaf /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/Library/Application Support：absent
- codex\-legacy\-tui\-log /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/\.codex：absent
- codex\-other\-log /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/\.codex：absent
- codex\-model\-catalog /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/\.codex：absent
- codex\-shell\-snapshots /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/\.codex：absent
- codex\-arg0 /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/\.codex：absent
- codex\-daemon\-releases /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/\.codex：absent
- codex\-standalone\-releases /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/\.codex：absent
- codex\-daemon\-staging /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/\.codex：absent
- codex\-desktop\-runtime\-staging /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home：absent
- claude\-debug\-log /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/\.claude：absent
- claude\-old\-native /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/\.local/share/claude/versions：absent
- cursor\-worker\-versions /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/Library/Application Support：absent
- cursor\-cli\-versions /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home：absent
- next\-build\-cache None：not\_requested
- cargo\-incremental None：not\_requested
- python\-bytecode None：not\_requested
- pytest\-core\-cache None：not\_requested
- pytest\-plugin\-cache None：not\_requested
- ruff\-cache None：not\_requested
- npm\-content\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/\.npm：absent
- npm\-npx\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/\.npm：absent
- npm\-diagnostic\-log /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/\.npm：absent
- uv\-native\-cache /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/\.cache/uv：absent
- playwright\-download /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/Library/Caches/ms\-playwright：absent
- puppeteer\-download /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/\.cache/puppeteer：absent
- preserve\-codex\-state /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/\.codex：absent
- preserve\-claude\-state /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/\.claude：absent
- preserve\-primary\-runtime /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home：absent
- preserve\-editor\-state /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home/Library/Application Support：absent
- preserve\-home\-state /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home：absent
- preserve\-project\-inputs None：not\_requested
- preserve\-next\-data\-cache None：not\_requested
- preserve\-audit /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home：absent
- preserve\-sync\-state /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home：absent
- preserve\-service\-state /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home：absent
- preserve\-model\-bundles /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home：absent
- preserve\-environment\-caches /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home：absent
- reserve\-native\-and\-runtime /Users/liyang/Applications/Mac MCP Gateway\.app/Contents/Resources/runtime/core/maclean\-acceptance\-ks12yz75/home：absent