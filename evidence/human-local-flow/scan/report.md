# MacLean 报告

记录类型：scan
完整扫描：True

## app

### 现在可处理

- 用户标准应用缓存：/private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/Library/Caches/Fixture；逻辑 28672 B，分配 28672 B；ID 5645e9e31b90f193d120
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

## ai

### 现在可处理

### 等待处理

### 保留

### 待调查

## development

### 现在可处理

### 等待处理

### 保留

### 待调查


## 扫描覆盖

- macos\-user\-cache /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home：matched
- macos\-user\-log /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home：absent
- sandbox\-cache /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home：absent
- sandbox\-log /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home：absent
- group\-cache /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home：absent
- group\-log /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home：absent
- app\-render\-cache /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/Library/Application Support：absent
- ai\-render\-cache /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/Library/Application Support：absent
- editor\-code\-cache /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/Library/Application Support：absent
- editor\-vsix\-download /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/Library/Application Support：absent
- ai\-editor\-extra\-cache /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/Library/Application Support：absent
- editor\-log /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/Library/Application Support：absent
- ai\-support\-log /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/Library/Application Support：absent
- browser\-profile\-cache /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/Library/Application Support：absent
- browser\-root\-shader /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/Library/Application Support：absent
- firefox\-support\-cache /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/Library/Application Support：absent
- design\-media\-cache /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/Library/Application Support：absent
- support\-unreviewed\-leaf /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/Library/Application Support：absent
- codex\-legacy\-tui\-log /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/\.codex：absent
- codex\-other\-log /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/\.codex：absent
- codex\-model\-catalog /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/\.codex：absent
- codex\-shell\-snapshots /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/\.codex：absent
- codex\-arg0 /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/\.codex：absent
- codex\-daemon\-releases /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/\.codex：absent
- codex\-standalone\-releases /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/\.codex：absent
- codex\-daemon\-staging /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/\.codex：absent
- codex\-desktop\-runtime\-staging /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home：absent
- claude\-debug\-log /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/\.claude：absent
- claude\-old\-native /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/\.local/share/claude/versions：absent
- cursor\-worker\-versions /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/Library/Application Support：absent
- cursor\-cli\-versions /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home：absent
- next\-build\-cache None：not\_requested
- cargo\-incremental None：not\_requested
- python\-bytecode None：not\_requested
- pytest\-core\-cache None：not\_requested
- pytest\-plugin\-cache None：not\_requested
- ruff\-cache None：not\_requested
- npm\-content\-cache /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/\.npm：absent
- npm\-npx\-cache /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/\.npm：absent
- npm\-diagnostic\-log /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/\.npm：absent
- uv\-native\-cache /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/\.cache/uv：absent
- playwright\-download /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/Library/Caches/ms\-playwright：absent
- puppeteer\-download /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/\.cache/puppeteer：absent
- preserve\-codex\-state /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/\.codex：absent
- preserve\-claude\-state /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/\.claude：absent
- preserve\-primary\-runtime /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home：absent
- preserve\-editor\-state /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home/Library/Application Support：absent
- preserve\-home\-state /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home：absent
- preserve\-project\-inputs None：not\_requested
- preserve\-next\-data\-cache None：not\_requested
- preserve\-audit /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home：absent
- preserve\-sync\-state /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home：absent
- preserve\-service\-state /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home：absent
- preserve\-model\-bundles /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home：absent
- preserve\-environment\-caches /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home：absent
- reserve\-native\-and\-runtime /private/var/folders/qp/\_qdh0v5x2t7djzt2589d64jc0000gp/T/maclean\-acceptance\-00ilwrou/home：absent