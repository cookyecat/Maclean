# MacLean 报告

记录类型：scan
完整扫描：True

目标发现：完整；目录计量：完整。文件数与时间限制是扫描工作量限制，与费用和 Token 无关。

每目标最多 250000 次元数据访问、45 秒；整轮最多 180 秒。目录大小来自文件元数据累加，不读取文件正文。

## macOS 应用

### 现在可处理

- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.appleaccountd；逻辑 353808 B，分配 368640 B；ID c10664efc592f2e3a8d9
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.helpd；逻辑 14052 B，分配 16384 B；ID 671ac2ac819f836d2b81
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/SentryCrash；逻辑 248 B，分配 4096 B；ID da674b166348ed681c2e
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/GeoServices；逻辑 51505043 B，分配 51851264 B；ID 88fd2233128995daa4f5
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.managedappdistributionagent；逻辑 265160 B，分配 331776 B；ID 0a208762b68398484dd0
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/dev\.macmcpgateway\.ownerapp；逻辑 81920 B，分配 81920 B；ID 7887ae2b1fc3ae554029
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.storekitagent；逻辑 343355 B，分配 372736 B；ID d33af38e649832d4fb39
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.HomeKit；逻辑 42230 B，分配 49152 B；ID 703e42cf35199c4c6618
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.proactive\.eventtracker；逻辑 320150 B，分配 331776 B；ID ce6b2ece5cc079c7af25
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.FeatureAccessAgent；逻辑 226152 B，分配 282624 B；ID bbbd1b89b71a4f3f2f54
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/copilot；逻辑 3160 B，分配 4096 B；ID 11fb3851405f3bc80289
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.Safari；逻辑 8 B，分配 4096 B；ID 932191f958f207e646ea
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.termius\-dmg\.mac；逻辑 81920 B，分配 81920 B；ID d92c915fd8a1a53e6a8b
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/GameKit；逻辑 47499 B，分配 49152 B；ID d56349b7151aacecbc8a
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.microsoft\.autoupdate\.fba；逻辑 1029552 B，分配 1069056 B；ID 0fbf8e472e2b1ba8d05f
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/Google；逻辑 708725979 B，分配 756768768 B；ID 58f557f4304396415537
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/Homebrew；逻辑 41716028 B，分配 44224512 B；ID a27a4b8be1693c4f01cb
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.gamed；逻辑 288 B，分配 4096 B；ID 9385a20bc0ea6af48518
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.appstoreagent；逻辑 635407 B，分配 741376 B；ID a1e2f4d5df5b74a4b5f8
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.CloudTelemetry；逻辑 1288052 B，分配 1368064 B；ID 7597cc94e7089d3903e9
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.geoanalyticsd；逻辑 131656 B，分配 172032 B；ID 68d7593c410c6c22feef
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.todesktop\.230313mzl4w4u92\.ShipIt；逻辑 7280 B，分配 12288 B；ID 8c37c28a0a662254c9b8
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.nbagent；逻辑 374472 B，分配 376832 B；ID 5738484d81c2550a6698
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.tipsd；逻辑 378592 B，分配 380928 B；ID 6da731c0b2b316223663
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.itunescloudd；逻辑 1265120 B，分配 1339392 B；ID 869b21c4238e39305aa5
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.icloudwebd；逻辑 139568 B，分配 147456 B；ID a1e366fb5449c25710fb
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.tw93\.MoleApp；逻辑 9760960 B，分配 10559488 B；ID 065faeacadbf724e7855
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.openai\.sky\.CUAService；逻辑 81920 B，分配 81920 B；ID 10efc6b9415a11b5b4a9
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.sogou\.inputmethod\.sogou；逻辑 3081272 B，分配 3244032 B；ID 4931f91568db0122b17a
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.termius\-dmg\.mac\.ShipIt；逻辑 3697 B，分配 8192 B；ID 2ca0ee484212f8a8794a
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.AppleMediaServices；逻辑 1997686 B，分配 2314240 B；ID 2a2347c2f678041efc23
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.remindd；逻辑 147283 B，分配 176128 B；ID ce1fd3d8d3a7b9e904e9
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.dataaccess\.dataaccessd；逻辑 144016 B，分配 172032 B；ID 00592bcf0d30c1455ea3
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.python；逻辑 1367198 B，分配 1544192 B；ID 7b9edf01f018783d785f
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.macpaw\.CleanMyMac5；逻辑 882327 B，分配 921600 B；ID 24a194758c40574c1c94
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.parsecd；逻辑 253395 B，分配 258048 B；ID f194b3b3517c2c54ff81
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.Family\-Settings\.extension；逻辑 175662 B，分配 229376 B；ID 9f384018e7a71ed4fb7c
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.colliderli\.iina；逻辑 178794 B，分配 192512 B；ID e2be7702c38e7883383c
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.microsoft\.VSCode；逻辑 81920 B，分配 81920 B；ID 74dd8efcdeb3bae60ba2
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.amsaccountsd；逻辑 1002407 B，分配 1044480 B；ID 34c4b7bd13bdb4d09b1f
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/FamilyCircle；逻辑 40895 B，分配 53248 B；ID a5f6db40dd34e380174a
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.AMPLibraryAgent；逻辑 673443 B，分配 716800 B；ID 9aa91ded53aaf433386a
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/115Browser；逻辑 5127559 B，分配 5767168 B；ID e0006c39191c8ce093d6
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.feedbacklogger；逻辑 151848 B，分配 217088 B；ID bbdab9adba5e33733be0
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.duetexpertd；逻辑 173712 B，分配 196608 B；ID a305996a3d8d4de5f6fa
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.iTunes；逻辑 644095 B，分配 647168 B；ID 56ae642d6ca37c046ce5
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/cursor\-compile\-cache；逻辑 1557192 B，分配 1634304 B；ID 0b55ae91c65a85df81d5
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/org\.115browser\.115Browser；逻辑 123152 B，分配 126976 B；ID b822d60c73b34479cbec
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/io\.sentry；逻辑 596 B，分配 4096 B；ID fde7d36a5f73c4d6b006
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.translationd；逻辑 203049 B，分配 258048 B；ID 2df7e31bb7e02d5e6350
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.ctcategories\.service；逻辑 3065540 B，分配 3608576 B；ID 715484e8fe72075ad977
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.AuthenticationServicesCore\.AuthenticationServicesAgent；逻辑 131392 B，分配 135168 B；ID 0615e39a5d5e71affeb8
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.iCloudNotificationAgent；逻辑 290750 B，分配 331776 B；ID 50c8a76f8a1dd0fd2d88
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.cache\_delete；逻辑 46703 B，分配 57344 B；ID 1fda014fffc89ec77eb9
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.AMPDevicesAgent；逻辑 206 B，分配 4096 B；ID f3f76f88d49ac5ba5079
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.amsengagementd；逻辑 1686509 B，分配 1765376 B；ID 43616085cb2ee5c45b7f
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.apple\.ap\.adprivacyd；逻辑 1030366 B，分配 1089536 B；ID 3172bd5b7cc8b5643828
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.netease\.uuremote；逻辑 6897741 B，分配 7495680 B；ID 612150f8ca1817e9218c
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/ai\.home\.mac\-mcp\-private\-pilot\.out\.log；逻辑 3980 B，分配 4096 B；ID f5e30cfbe6aa480291c1
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/LemonMonitor\.log；逻辑 10038 B，分配 12288 B；ID 51f8cbe65578e02456c9
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/ai\.home\.mac\-mcp\-tunnel\.out\.log；逻辑 702478 B，分配 761856 B；ID 75d925070a6349499fdf
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/ai\.home\.alidns\-ddns\.out\.log；逻辑 151856 B，分配 217088 B；ID 816010aa1bc80b3cb10c
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/\.DS\_Store；逻辑 12292 B，分配 16384 B；ID 16cb7e77c9f902992be2
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/PhotosSearch\.aapbz；逻辑 4068 B，分配 4096 B；ID 43cea48903478cfaa3ea
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/ai\.home\.mac\-mcp\-project\-workspace\.out\.log；逻辑 78233 B，分配 81920 B；ID 3d703c81976ee44d4f74
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/NGL；逻辑 8086 B，分配 45056 B；ID ef868b90e685a73273fc
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/PhotosLegacyUpgrade\.aapbz；逻辑 1281 B，分配 4096 B；ID 86c41486f5174dda941e
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/DiagnosticReports；逻辑 86354 B，分配 155648 B；ID bda3fe928aea502f2f77
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/Homebrew；逻辑 26 B，分配 4096 B；ID 7e50cba59a9f7340c96a
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/CrashReporter；逻辑 12530 B，分配 16384 B；ID 8c2c23e415772925533b
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/ai\.home\.mac\-mcp\-dc\-bridge\.out\.log；逻辑 3415 B，分配 4096 B；ID 608867c69a84b881faa6
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/Adobe；逻辑 2243 B，分配 36864 B；ID 89f0ecdb7e8bdc08e8ae
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/CSXS；逻辑 57 B，分配 4096 B；ID 8086473eb8576e30141c
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/com\.bageshuo；逻辑 59037 B，分配 61440 B；ID dbaa0da408cd58240e2d
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/RAOS；逻辑 1985899 B，分配 2191360 B；ID 3aff6c36cd9c7ac3897f
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/com\.apple\.AMPLibraryAgent；逻辑 557 B，分配 4096 B；ID ea7868a4696ffc6d35e4
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/ToDesk；逻辑 16507 B，分配 20480 B；ID 21bb23a1c6ab53a117ea
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/Sync；逻辑 738 B，分配 4096 B；ID cd58e19b2fced4563c42
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/Antigravity；逻辑 9275913 B，分配 9281536 B；ID e8f99a5230491dfa2a9e
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/zspace；逻辑 13786795 B，分配 13791232 B；ID d06c499e72f55f705a8c
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 沙盒/应用组标准缓存：/Users/liyang/Library/Containers/com\.apple\.photolibraryd/Data/Library/Caches；逻辑 3932056 B，分配 3936256 B；ID c8361cc5d0dd024a53a1
  规则：sandbox\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 沙盒/应用组标准缓存：/Users/liyang/Library/Containers/com\.apple\.mediastream\.mstreamd/Data/Library/Caches；逻辑 81920 B，分配 81920 B；ID c5a1b2c742946639b034
  规则：sandbox\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 沙盒/应用组标准缓存：/Users/liyang/Library/Containers/com\.apple\.systempreferences\.AppleIDSettings/Data/Library/Caches；逻辑 409361 B，分配 409600 B；ID 2c12504dff43cc5f0bb8
  规则：sandbox\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 沙盒/应用组标准缓存：/Users/liyang/Library/Containers/com\.tencent\.xinWeChat/Data/Library/Caches；逻辑 6995202 B，分配 7507968 B；ID e4ca735f6f05b9f6a9b1
  规则：sandbox\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 沙盒/应用组标准缓存：/Users/liyang/Library/Containers/com\.apple\.wallpaper\.agent/Data/Library/Caches；逻辑 17280108 B，分配 17285120 B；ID 4eddfe9d94bb6eb34f96
  规则：sandbox\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 沙盒/应用组标准缓存：/Users/liyang/Library/Containers/com\.microsoft\.Word/Data/Library/Caches；逻辑 502687 B，分配 512000 B；ID 293aeb72dc4691e873a3
  规则：sandbox\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 沙盒/应用组标准缓存：/Users/liyang/Library/Containers/com\.apple\.photoanalysisd/Data/Library/Caches；逻辑 1298216 B，分配 1302528 B；ID 42465c82ae027cd89e98
  规则：sandbox\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 沙盒/应用组标准缓存：/Users/liyang/Library/Containers/com\.apple\.Notes/Data/Library/Caches；逻辑 139568 B，分配 147456 B；ID 1c3bfdb7b0f77dc8544d
  规则：sandbox\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 沙盒/应用组标准缓存：/Users/liyang/Library/Containers/com\.apple\.geod/Data/Library/Caches；逻辑 2351986 B，分配 3264512 B；ID a51082e21d2434e89733
  规则：sandbox\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 沙盒/应用组标准缓存：/Users/liyang/Library/Containers/com\.tencent\.qq/Data/Library/Caches；逻辑 715474 B，分配 733184 B；ID 11b3d8ece4241f8c2f60
  规则：sandbox\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 沙盒/应用组标准缓存：/Users/liyang/Library/Containers/com\.apple\.mediaanalysisd/Data/Library/Caches；逻辑 284154358 B，分配 284184576 B；ID f0c5bcbd3f1882075791
  规则：sandbox\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 沙盒/应用组诊断日志：/Users/liyang/Library/Containers/com\.microsoft\.Word/Data/Library/Logs；逻辑 6706802 B，分配 6709248 B；ID a767f6c4ca2eb2b720b2
  规则：sandbox\-log
  删除影响：历史诊断不可恢复
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 沙盒/应用组诊断日志：/Users/liyang/Library/Containers/com\.adobe\.acc\.anc\.AdobeCreativeCloud\.AdobeContextMenuExtension/Data/Library/Logs；逻辑 504800 B，分配 507904 B；ID 147eea1cec9daa9517f9
  规则：sandbox\-log
  删除影响：历史诊断不可恢复
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 沙盒/应用组诊断日志：/Users/liyang/Library/Containers/com\.tencent\.tenvideo/Data/Library/Logs；逻辑 96221607 B，分配 96342016 B；ID 3f8e2c50c07ec15739fe
  规则：sandbox\-log
  删除影响：历史诊断不可恢复
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 沙盒/应用组标准缓存：/Users/liyang/Library/Group Containers/group\.com\.apple\.stocks/Library/Caches；逻辑 78096 B，分配 81920 B；ID 058819095cb02c062bb6
  规则：group\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 沙盒/应用组标准缓存：/Users/liyang/Library/Group Containers/group\.com\.apple\.appstoreagent/Library/Caches；逻辑 3106088 B，分配 4009984 B；ID 785ca415da6ab0a31780
  规则：group\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 沙盒/应用组标准缓存：/Users/liyang/Library/Group Containers/group\.com\.apple\.tips/Library/Caches；逻辑 2191529 B，分配 2256896 B；ID a17cb4a731a93f4eb79f
  规则：group\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 沙盒/应用组标准缓存：/Users/liyang/Library/Group Containers/group\.com\.apple\.storekit/Library/Caches；逻辑 1366720 B，分配 2334720 B；ID e481cb37ba04d0d71969
  规则：group\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 沙盒/应用组标准缓存：/Users/liyang/Library/Group Containers/group\.com\.apple\.weather/Library/Caches；逻辑 13417 B，分配 16384 B；ID a090d280d176f8b2d031
  规则：group\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 沙盒/应用组诊断日志：/Users/liyang/Library/Group Containers/S8EX82NJP6\.com\.macpaw\.CleanMyMac5/Library/Logs；逻辑 74510894 B，分配 75522048 B；ID 6428164cf91d655b0172
  规则：group\-log
  删除影响：历史诊断不可恢复
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 沙盒/应用组诊断日志：/Users/liyang/Library/Group Containers/UBF8T346G9\.com\.microsoft\.to\-do\-mac/Library/Logs；逻辑 2243107 B，分配 2248704 B；ID e4e42a178cb3b26c50bf
  规则：group\-log
  删除影响：历史诊断不可恢复
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 已登记应用的 Chromium 渲染缓存叶目录：/Users/liyang/Library/Application Support/Code/Cache；逻辑 51392320 B，分配 51965952 B；ID 040a43093b279de3a7ad
  规则：app\-render\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['electron\-paths', 'mole\-caches'\]
- 已登记应用的 Chromium 渲染缓存叶目录：/Users/liyang/Library/Application Support/Code/Code Cache；逻辑 11656 B，分配 32768 B；ID 5f08a73d4b828bb3f58b
  规则：app\-render\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['electron\-paths', 'mole\-caches'\]
- 已登记应用的 Chromium 渲染缓存叶目录：/Users/liyang/Library/Application Support/Code/GPUCache；逻辑 5837168 B，分配 5840896 B；ID 50e73e899957ff0db487
  规则：app\-render\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['electron\-paths', 'mole\-caches'\]
- 已登记应用的 Chromium 渲染缓存叶目录：/Users/liyang/Library/Application Support/Code/DawnGraphiteCache；逻辑 557424 B，分配 561152 B；ID 55082f40416a70040bf4
  规则：app\-render\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['electron\-paths', 'mole\-caches'\]
- 已登记应用的 Chromium 渲染缓存叶目录：/Users/liyang/Library/Application Support/Code/DawnWebGPUCache；逻辑 557424 B，分配 561152 B；ID 25797c180d7d507d82a9
  规则：app\-render\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['electron\-paths', 'mole\-caches'\]
- 编辑器生成的代码缓存：/Users/liyang/Library/Application Support/Code/CachedData；逻辑 73321697 B，分配 73691136 B；ID 6730bebf5b93afc12b62
  规则：editor\-code\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['vscode\-code\-cache'\]
- 已下载扩展安装包副本：/Users/liyang/Library/Application Support/Code/CachedExtensionVSIXs；逻辑 164001813 B，分配 164020224 B；ID 5deb23d00eca6b7306da
  规则：editor\-vsix\-download
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：需要时重新下载扩展包；不卸载扩展
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['vscode\-vsix', 'vscode\-environment'\]
- 编辑器诊断日志：/Users/liyang/Library/Application Support/Code/logs；逻辑 849579 B，分配 1241088 B；ID 9a17d97fee1420b63dad
  规则：editor\-log
  删除影响：历史诊断不可恢复
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['vscode\-environment'\]
- 浏览器 profile 内的渲染/HTTP 缓存叶目录：/Users/liyang/Library/Application Support/Google/Chrome/Default/GPUCache；逻辑 7449248 B，分配 5013504 B；ID a2b1def7cf95f21463d9
  规则：browser\-profile\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths', 'mole\-caches'\]
- 浏览器 profile 内的渲染/HTTP 缓存叶目录：/Users/liyang/Library/Application Support/Google/Chrome/Default/DawnGraphiteCache；逻辑 557424 B，分配 307200 B；ID 0052f6af98f5cd627ce5
  规则：browser\-profile\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths', 'mole\-caches'\]
- 浏览器 profile 内的渲染/HTTP 缓存叶目录：/Users/liyang/Library/Application Support/Google/Chrome/Default/DawnWebGPUCache；逻辑 1642864 B，分配 1380352 B；ID 90b66c0447139720d777
  规则：browser\-profile\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths', 'mole\-caches'\]
- 浏览器 profile 内的渲染/HTTP 缓存叶目录：/Users/liyang/Library/Application Support/Google/Chrome/Profile 7/GPUCache；逻辑 557424 B，分配 561152 B；ID f1df0a3ee8e137cbca17
  规则：browser\-profile\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths', 'mole\-caches'\]
- 浏览器 profile 内的渲染/HTTP 缓存叶目录：/Users/liyang/Library/Application Support/Google/Chrome/Profile 9/GPUCache；逻辑 557424 B，分配 307200 B；ID efd030c96275e97a9543
  规则：browser\-profile\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths', 'mole\-caches'\]
- 浏览器 profile 内的渲染/HTTP 缓存叶目录：/Users/liyang/Library/Application Support/Google/Chrome/Profile 8/GPUCache；逻辑 5837168 B，分配 5586944 B；ID f01f80301192370522ba
  规则：browser\-profile\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths', 'mole\-caches'\]
- 浏览器 profile 内的渲染/HTTP 缓存叶目录：/Users/liyang/Library/Application Support/Google/Chrome/Profile 6/GPUCache；逻辑 4805512 B，分配 4812800 B；ID dea889cf82966f3693ee
  规则：browser\-profile\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths', 'mole\-caches'\]
- 浏览器 profile 内的渲染/HTTP 缓存叶目录：/Users/liyang/Library/Application Support/Google/Chrome/Profile 1/GPUCache；逻辑 557424 B，分配 561152 B；ID 630d892497dc37209348
  规则：browser\-profile\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths', 'mole\-caches'\]
- 浏览器 profile 内的渲染/HTTP 缓存叶目录：/Users/liyang/Library/Application Support/Google/Chrome/Profile 2/GPUCache；逻辑 557424 B，分配 561152 B；ID 14fb3391b6a25c3dfefd
  规则：browser\-profile\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths', 'mole\-caches'\]
- 浏览器 profile 内的渲染/HTTP 缓存叶目录：/Users/liyang/Library/Application Support/Google/Chrome/Profile 7/DawnGraphiteCache；逻辑 557424 B，分配 561152 B；ID a98ac911b5c5c222cfbe
  规则：browser\-profile\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths', 'mole\-caches'\]
- 浏览器 profile 内的渲染/HTTP 缓存叶目录：/Users/liyang/Library/Application Support/Google/Chrome/Profile 9/DawnGraphiteCache；逻辑 557424 B，分配 307200 B；ID c7802d7cac7810204d8c
  规则：browser\-profile\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths', 'mole\-caches'\]
- 浏览器 profile 内的渲染/HTTP 缓存叶目录：/Users/liyang/Library/Application Support/Google/Chrome/Profile 8/DawnGraphiteCache；逻辑 557424 B，分配 307200 B；ID 804aa7e97f0fe4ac71aa
  规则：browser\-profile\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths', 'mole\-caches'\]
- 浏览器 profile 内的渲染/HTTP 缓存叶目录：/Users/liyang/Library/Application Support/Google/Chrome/Profile 6/DawnGraphiteCache；逻辑 557424 B，分配 561152 B；ID 5dc8ea076c351f3d852d
  规则：browser\-profile\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths', 'mole\-caches'\]
- 浏览器 profile 内的渲染/HTTP 缓存叶目录：/Users/liyang/Library/Application Support/Google/Chrome/Profile 1/DawnGraphiteCache；逻辑 557424 B，分配 561152 B；ID 26e250c9050ac36b030d
  规则：browser\-profile\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths', 'mole\-caches'\]
- 浏览器 profile 内的渲染/HTTP 缓存叶目录：/Users/liyang/Library/Application Support/Google/Chrome/Profile 2/DawnGraphiteCache；逻辑 557424 B，分配 561152 B；ID a58163277705760f0151
  规则：browser\-profile\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths', 'mole\-caches'\]
- 浏览器 profile 内的渲染/HTTP 缓存叶目录：/Users/liyang/Library/Application Support/Google/Chrome/Profile 7/DawnWebGPUCache；逻辑 557424 B，分配 561152 B；ID 1d20ca5396aab58b3b9e
  规则：browser\-profile\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths', 'mole\-caches'\]
- 浏览器 profile 内的渲染/HTTP 缓存叶目录：/Users/liyang/Library/Application Support/Google/Chrome/Profile 9/DawnWebGPUCache；逻辑 557424 B，分配 307200 B；ID 0e93ba7e4b17b7d75fb7
  规则：browser\-profile\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths', 'mole\-caches'\]
- 浏览器 profile 内的渲染/HTTP 缓存叶目录：/Users/liyang/Library/Application Support/Google/Chrome/Profile 8/DawnWebGPUCache；逻辑 557424 B，分配 307200 B；ID 87d81d9cc61b507f0c91
  规则：browser\-profile\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths', 'mole\-caches'\]
- 浏览器 profile 内的渲染/HTTP 缓存叶目录：/Users/liyang/Library/Application Support/Google/Chrome/Profile 6/DawnWebGPUCache；逻辑 557424 B，分配 561152 B；ID 3c3d751b579dd96c25dc
  规则：browser\-profile\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths', 'mole\-caches'\]
- 浏览器 profile 内的渲染/HTTP 缓存叶目录：/Users/liyang/Library/Application Support/Google/Chrome/Profile 1/DawnWebGPUCache；逻辑 557424 B，分配 561152 B；ID c944ab18a6e333bfda1d
  规则：browser\-profile\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths', 'mole\-caches'\]
- 浏览器 profile 内的渲染/HTTP 缓存叶目录：/Users/liyang/Library/Application Support/Google/Chrome/Profile 2/DawnWebGPUCache；逻辑 557424 B，分配 561152 B；ID ba51df65c59613e9d401
  规则：browser\-profile\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths', 'mole\-caches'\]
- 浏览器根下 shader/code 缓存：/Users/liyang/Library/Application Support/Google/Chrome/ShaderCache；逻辑 557424 B，分配 561152 B；ID 2fce1ea647c4dad1468e
  规则：browser\-root\-shader
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths'\]
- 浏览器根下 shader/code 缓存：/Users/liyang/Library/Application Support/Google/Chrome/GrShaderCache；逻辑 5933212 B，分配 6332416 B；ID 629e2c354456ecd2a1c6
  规则：browser\-root\-shader
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths'\]
- 浏览器根下 shader/code 缓存：/Users/liyang/Library/Application Support/Google/Chrome/GraphiteDawnCache；逻辑 13151873 B，分配 13348864 B；ID 906ad40a2ef4b9e21378
  规则：browser\-root\-shader
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['chromium\-paths', 'electron\-paths'\]
### 等待处理

### 保留

### 待调查

- 已登记应用的 Chromium 渲染缓存叶目录：/Users/liyang/Library/Application Support/Termius/Cache；逻辑 15756 B，分配 28672 B；ID bf092a3dab52f6325c2e
  规则：app\-render\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['electron\-paths', 'mole\-caches'\]
  未处理原因：\[\{'reason': 'chromium\_layout'\}\]
- 未登记应用的浅层缓存/日志候选：/Users/liyang/Library/Application Support/BambuStudio/Cache；逻辑 5180 B，分配 8192 B；ID d163278499cae0f39576
  规则：support\-unreviewed\-leaf
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['product\-boundary'\]
  研究缺口：需应用级依据；只发现和计量，不递归按关键词删除。
  未处理原因：\[\{'reason': 'research'\}\]
- 未登记应用的浅层缓存/日志候选：/Users/liyang/Library/Application Support/com\.hetao101\.mac\.ScratchMac/Cache；逻辑 1415192 B，分配 1425408 B；ID b5dba46bc2232636244b
  规则：support\-unreviewed\-leaf
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['product\-boundary'\]
  研究缺口：需应用级依据；只发现和计量，不递归按关键词删除。
  未处理原因：\[\{'reason': 'research'\}\]
- 未登记应用的浅层缓存/日志候选：/Users/liyang/Library/Application Support/com\.netease\.163music/Caches；逻辑 124928495 B，分配 128872448 B；ID 4fc848c757ddb392506a
  规则：support\-unreviewed\-leaf
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['product\-boundary'\]
  研究缺口：需应用级依据；只发现和计量，不递归按关键词删除。
  未处理原因：\[\{'reason': 'research'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_956\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_4897\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_81524\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_81471\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_77063\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_48270\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_48653\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_83175\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_15392\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_70840\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_48271\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_77066\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_55971\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_77065\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_70842\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_48655\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_15390\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_4897\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_81524\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_33190\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_83173\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_48652\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_956\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_70839\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_1168\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_70842\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_83169\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_15391\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_48258\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_77016\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_77017\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_15390\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_77064\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_48654\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_15391\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_4900\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_33191\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_15393\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_70839\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_70841\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_77066\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_962\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_48258\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_77063\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_77014\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_55974\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_15393\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_962\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_33188\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_48653\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_70840\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_83176\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_1168\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_77014\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_81471\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_55973\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_48269\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_4899\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_70841\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_48652\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_938\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_33189\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_15392\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_48270\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_77015\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_83169\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_81474\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_33190\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_959\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_959\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_55971\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_81473\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_33189\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_77016\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_938\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_55972\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_48655\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_81474\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_55974\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_4899\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_83175\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_81473\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_77065\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_77064\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_81472\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_33191\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_77017\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_4898\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_83176\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_33188\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_81472\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_4898\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_83173\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_55972\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_48269\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_4900\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_77015\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_48271\_write', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_48654\_read', 'reason': 'special\_or\_symlink'\}, \{'path': '/Users/liyang/Library/Application Support/com\.netease\.163music/Caches/ipc/ipc\_55973\_read', 'reason': 'special\_or\_symlink'\}\]
- 未登记应用的浅层缓存/日志候选：/Users/liyang/Library/Application Support/com\.apple\.NewDeviceOutreach/Caches；逻辑 1165 B，分配 12288 B；ID 12037d77c2129393b427
  规则：support\-unreviewed\-leaf
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['product\-boundary'\]
  研究缺口：需应用级依据；只发现和计量，不递归按关键词删除。
  未处理原因：\[\{'reason': 'research'\}\]
- 未登记应用的浅层缓存/日志候选：/Users/liyang/Library/Application Support/obs\-studio/logs；逻辑 181360 B，分配 204800 B；ID 1f36f3913e9f443de629
  规则：support\-unreviewed\-leaf
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['product\-boundary'\]
  研究缺口：需应用级依据；只发现和计量，不递归按关键词删除。
  未处理原因：\[\{'reason': 'research'\}\]
- 未登记应用的浅层缓存/日志候选：/Users/liyang/Library/Application Support/io\.github\.clash\-verge\-rev\.clash\-verge\-rev/logs；逻辑 1134214 B，分配 1187840 B；ID a8622d006faa89c5f1ad
  规则：support\-unreviewed\-leaf
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['product\-boundary'\]
  研究缺口：需应用级依据；只发现和计量，不递归按关键词删除。
  未处理原因：\[\{'reason': 'research'\}\]
- 未登记应用的浅层缓存/日志候选：/Users/liyang/Library/Application Support/GitHub Desktop/logs；逻辑 162153 B，分配 200704 B；ID 0c63aa9bc769d698725c
  规则：support\-unreviewed\-leaf
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['product\-boundary'\]
  研究缺口：需应用级依据；只发现和计量，不递归按关键词删除。
  未处理原因：\[\{'reason': 'research'\}\]
- 未登记应用的浅层缓存/日志候选：/Users/liyang/Library/Application Support/SlayTheSpire2/logs；逻辑 370836 B，分配 380928 B；ID 41a17f73b3924fa0e8c3
  规则：support\-unreviewed\-leaf
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['product\-boundary'\]
  研究缺口：需应用级依据；只发现和计量，不递归按关键词删除。
  未处理原因：\[\{'reason': 'research'\}\]
- 未登记应用的浅层缓存/日志候选：/Users/liyang/Library/Application Support/com\.netease\.uuremote\.helper/logs；逻辑 153600 B，分配 155648 B；ID 822651dfafaabecd834c
  规则：support\-unreviewed\-leaf
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['product\-boundary'\]
  研究缺口：需应用级依据；只发现和计量，不递归按关键词删除。
  未处理原因：\[\{'reason': 'research'\}\]
- 未登记应用的浅层缓存/日志候选：/Users/liyang/Library/Application Support/com\.hetao101\.mac\.ScratchMac/logs；逻辑 32145099 B，分配 32157696 B；ID cda116a4786fbe032b7d
  规则：support\-unreviewed\-leaf
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['product\-boundary'\]
  研究缺口：需应用级依据；只发现和计量，不递归按关键词删除。
  未处理原因：\[\{'reason': 'research'\}\]
- 未登记应用的浅层缓存/日志候选：/Users/liyang/Library/Application Support/zspace/logs；逻辑 25966626 B，分配 25968640 B；ID ebffc659d1a03f134952
  规则：support\-unreviewed\-leaf
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['product\-boundary'\]
  研究缺口：需应用级依据；只发现和计量，不递归按关键词删除。
  未处理原因：\[\{'reason': 'research'\}\]
- 未登记应用的浅层缓存/日志候选：/Users/liyang/Library/Application Support/com\.netease\.uuremote/logs；逻辑 42365509 B，分配 42467328 B；ID a2e4e14a93b7d3a62831
  规则：support\-unreviewed\-leaf
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['product\-boundary'\]
  研究缺口：需应用级依据；只发现和计量，不递归按关键词删除。
  未处理原因：\[\{'reason': 'research'\}\]
- 未登记应用的浅层缓存/日志候选：/Users/liyang/Library/Application Support/hmcl/logs；逻辑 834516 B，分配 966656 B；ID 3a94bf42f2c0bcf38ca0
  规则：support\-unreviewed\-leaf
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['product\-boundary'\]
  研究缺口：需应用级依据；只发现和计量，不递归按关键词删除。
  未处理原因：\[\{'reason': 'research'\}\]
## AI 客户端

### 现在可处理

- 用户标准应用缓存：/Users/liyang/Library/Caches/Codex；逻辑 5243495 B，分配 5931008 B；ID e847070bbdcdb7f9863b
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.openai\.codex；逻辑 371205 B，分配 405504 B；ID 5231570920ba0029bef3
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户标准应用缓存：/Users/liyang/Library/Caches/com\.todesktop\.230313mzl4w4u92；逻辑 180832 B，分配 184320 B；ID 7b0fc5b39c31ff311320
  规则：macos\-user\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- 用户诊断日志：/Users/liyang/Library/Logs/com\.openai\.codex；逻辑 132536315 B，分配 128200704 B；ID 61e34914173728dcc3ea
  规则：macos\-user\-log
  删除影响：历史诊断不可恢复；打开句柄可能延迟释放
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['apple\-library'\]
- AI 客户端渲染缓存；不含对话/推理状态：/Users/liyang/Library/Application Support/Codex/Cache；逻辑 18067995 B，分配 22102016 B；ID 6b929ffd6bdc932cba7d
  规则：ai\-render\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['electron\-paths', 'mole\-caches'\]
- AI 客户端渲染缓存；不含对话/推理状态：/Users/liyang/Library/Application Support/Codex/Code Cache；逻辑 144 B，分配 16384 B；ID 649dd3d5b46e96dc53a5
  规则：ai\-render\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['electron\-paths', 'mole\-caches'\]
- AI 客户端渲染缓存；不含对话/推理状态：/Users/liyang/Library/Application Support/Codex/GPUCache；逻辑 557424 B，分配 561152 B；ID e60a7c40b682b860c523
  规则：ai\-render\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['electron\-paths', 'mole\-caches'\]
- AI 客户端渲染缓存；不含对话/推理状态：/Users/liyang/Library/Application Support/Codex/ShaderCache；逻辑 557424 B，分配 561152 B；ID b99994d8dcff3dd0c0a3
  规则：ai\-render\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['electron\-paths', 'mole\-caches'\]
- AI 客户端渲染缓存；不含对话/推理状态：/Users/liyang/Library/Application Support/Codex/GrShaderCache；逻辑 557424 B，分配 561152 B；ID 79c8fc172a0e4ff4dcae
  规则：ai\-render\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['electron\-paths', 'mole\-caches'\]
- AI 客户端渲染缓存；不含对话/推理状态：/Users/liyang/Library/Application Support/Codex/GraphiteDawnCache；逻辑 12589316 B，分配 12709888 B；ID ab357dd6961d8714ddc6
  规则：ai\-render\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['electron\-paths', 'mole\-caches'\]
- AI 客户端渲染缓存；不含对话/推理状态：/Users/liyang/Library/Application Support/Codex/DawnGraphiteCache；逻辑 557424 B，分配 561152 B；ID 80799192ba3ba2b5ce16
  规则：ai\-render\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['electron\-paths', 'mole\-caches'\]
- AI 客户端渲染缓存；不含对话/推理状态：/Users/liyang/Library/Application Support/Codex/DawnWebGPUCache；逻辑 557424 B，分配 561152 B；ID 40c27ee24aa7487758ef
  规则：ai\-render\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['electron\-paths', 'mole\-caches'\]
- AI 客户端渲染缓存；不含对话/推理状态：/Users/liyang/Library/Application Support/Cursor/Cache；逻辑 2873457 B，分配 2957312 B；ID ac933b8eecdca51b8015
  规则：ai\-render\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['electron\-paths', 'mole\-caches'\]
- AI 客户端渲染缓存；不含对话/推理状态：/Users/liyang/Library/Application Support/Cursor/Code Cache；逻辑 15348 B，分配 36864 B；ID 67e5eec0a0443bb2fa56
  规则：ai\-render\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['electron\-paths', 'mole\-caches'\]
- AI 客户端渲染缓存；不含对话/推理状态：/Users/liyang/Library/Application Support/Cursor/GPUCache；逻辑 5893876 B，分配 5902336 B；ID 731681e99181d12bba03
  规则：ai\-render\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['electron\-paths', 'mole\-caches'\]
- AI 客户端渲染缓存；不含对话/推理状态：/Users/liyang/Library/Application Support/Cursor/DawnGraphiteCache；逻辑 557424 B，分配 561152 B；ID ebebce607515682b9ed8
  规则：ai\-render\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['electron\-paths', 'mole\-caches'\]
- AI 客户端渲染缓存；不含对话/推理状态：/Users/liyang/Library/Application Support/Cursor/DawnWebGPUCache；逻辑 557424 B，分配 561152 B；ID ab94a314b55e97d5b010
  规则：ai\-render\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['electron\-paths', 'mole\-caches'\]
### 等待处理

### 保留

- 会话、配置、账本、插件、worktree 及安装控制状态：/Users/liyang/\.codex/auth\.json；逻辑 4199 B，分配 8192 B；ID ecf2e15edebfa34fdb14
  规则：preserve\-codex\-state
  删除影响：保留；不进入普通缓存清理
  恢复方式：不适用
  模型费用判断：not\_assessed\_out\_of\_scope
  依据索引：\['product\-boundary'\]
  未处理原因：\[\{'reason': 'protected'\}\]
- 会话、配置、账本、插件、worktree 及安装控制状态：/Users/liyang/\.codex/config\.toml；逻辑 5414 B，分配 8192 B；ID d39f61395a6c1f8f3ad9
  规则：preserve\-codex\-state
  删除影响：保留；不进入普通缓存清理
  恢复方式：不适用
  模型费用判断：not\_assessed\_out\_of\_scope
  依据索引：\['product\-boundary'\]
  未处理原因：\[\{'reason': 'protected'\}\]
- 会话、配置、账本、插件、worktree 及安装控制状态：/Users/liyang/\.codex/history\.jsonl；逻辑 340 B，分配 4096 B；ID 2eee39c8f1989fc628bd
  规则：preserve\-codex\-state
  删除影响：保留；不进入普通缓存清理
  恢复方式：不适用
  模型费用判断：not\_assessed\_out\_of\_scope
  依据索引：\['product\-boundary'\]
  未处理原因：\[\{'reason': 'protected'\}\]
- 会话、配置、账本、插件、worktree 及安装控制状态：/Users/liyang/\.codex/session\_index\.jsonl；逻辑 6618 B，分配 8192 B；ID a343729bdc0258cd4c47
  规则：preserve\-codex\-state
  删除影响：保留；不进入普通缓存清理
  恢复方式：不适用
  模型费用判断：not\_assessed\_out\_of\_scope
  依据索引：\['product\-boundary'\]
  未处理原因：\[\{'reason': 'protected'\}\]
- 会话、配置、账本、插件、worktree 及安装控制状态：/Users/liyang/\.codex/state\_5\.sqlite；逻辑 3055616 B，分配 3932160 B；ID fb62533d99eef9e36017
  规则：preserve\-codex\-state
  删除影响：保留；不进入普通缓存清理
  恢复方式：不适用
  模型费用判断：not\_assessed\_out\_of\_scope
  依据索引：\['product\-boundary'\]
  未处理原因：\[\{'reason': 'protected'\}\]
- 会话、配置、账本、插件、worktree 及安装控制状态：/Users/liyang/\.codex/state\_5\.sqlite\-wal；逻辑 4140632 B，分配 4198400 B；ID 4326e502f106f3e33670
  规则：preserve\-codex\-state
  删除影响：保留；不进入普通缓存清理
  恢复方式：不适用
  模型费用判断：not\_assessed\_out\_of\_scope
  依据索引：\['product\-boundary'\]
  未处理原因：\[\{'reason': 'protected'\}\]
- 会话、配置、账本、插件、worktree 及安装控制状态：/Users/liyang/\.codex/state\_5\.sqlite\-shm；逻辑 32768 B，分配 32768 B；ID c26c01acb1172fdc62b3
  规则：preserve\-codex\-state
  删除影响：保留；不进入普通缓存清理
  恢复方式：不适用
  模型费用判断：not\_assessed\_out\_of\_scope
  依据索引：\['product\-boundary'\]
  未处理原因：\[\{'reason': 'protected'\}\]
- 会话、配置、账本、插件、worktree 及安装控制状态：/Users/liyang/\.codex/logs\_2\.sqlite\-wal；逻辑 4700952 B，分配 5279744 B；ID 8894e3921f7f6291abd2
  规则：preserve\-codex\-state
  删除影响：保留；不进入普通缓存清理
  恢复方式：不适用
  模型费用判断：not\_assessed\_out\_of\_scope
  依据索引：\['product\-boundary'\]
  未处理原因：\[\{'reason': 'protected'\}\]
- 会话、配置、账本、插件、worktree 及安装控制状态：/Users/liyang/\.codex/logs\_2\.sqlite\-shm；逻辑 32768 B，分配 32768 B；ID c0cc769e1b13e3ec0489
  规则：preserve\-codex\-state
  删除影响：保留；不进入普通缓存清理
  恢复方式：不适用
  模型费用判断：not\_assessed\_out\_of\_scope
  依据索引：\['product\-boundary'\]
  未处理原因：\[\{'reason': 'protected'\}\]
- 会话、配置、账本、插件、worktree 及安装控制状态：/Users/liyang/\.codex/logs\_2\.sqlite；逻辑 91525120 B，分配 91525120 B；ID 3e33291d5a408d02380d
  规则：preserve\-codex\-state
  删除影响：保留；不进入普通缓存清理
  恢复方式：不适用
  模型费用判断：not\_assessed\_out\_of\_scope
  依据索引：\['product\-boundary'\]
  未处理原因：\[\{'reason': 'protected'\}\]
- Claude 会话、环境、插件与用户状态：/Users/liyang/\.claude/history\.jsonl；逻辑 13487 B，分配 16384 B；ID e7a3e75ed9f936e48369
  规则：preserve\-claude\-state
  删除影响：保留；不进入普通缓存清理
  恢复方式：不适用
  模型费用判断：not\_assessed\_out\_of\_scope
  依据索引：\['product\-boundary'\]
  未处理原因：\[\{'reason': 'protected'\}\]
- Claude 会话、环境、插件与用户状态：/Users/liyang/\.claude/settings\.json；逻辑 815 B，分配 4096 B；ID 1e29447be51784730f29
  规则：preserve\-claude\-state
  删除影响：保留；不进入普通缓存清理
  恢复方式：不适用
  模型费用判断：not\_assessed\_out\_of\_scope
  依据索引：\['product\-boundary'\]
  未处理原因：\[\{'reason': 'protected'\}\]
- 应用/编辑器状态；不从通用缓存规则清除：/Users/liyang/Library/Application Support/Code/Cookies；逻辑 20480 B，分配 20480 B；ID f5ede22923d5641860c1
  规则：preserve\-editor\-state
  删除影响：保留；不进入普通缓存清理
  恢复方式：不适用
  模型费用判断：not\_assessed\_out\_of\_scope
  依据索引：\['product\-boundary'\]
  未处理原因：\[\{'reason': 'protected'\}\]
- 应用/编辑器状态；不从通用缓存规则清除：/Users/liyang/Library/Application Support/Termius/Cookies；逻辑 20480 B，分配 20480 B；ID 407161cc4b5ecd6741d8
  规则：preserve\-editor\-state
  删除影响：保留；不进入普通缓存清理
  恢复方式：不适用
  模型费用判断：not\_assessed\_out\_of\_scope
  依据索引：\['product\-boundary'\]
  未处理原因：\[\{'reason': 'protected'\}\]
- 应用/编辑器状态；不从通用缓存规则清除：/Users/liyang/Library/Application Support/Codex/Cookies；逻辑 20480 B，分配 20480 B；ID 7b52c024faa60a72b901
  规则：preserve\-editor\-state
  删除影响：保留；不进入普通缓存清理
  恢复方式：不适用
  模型费用判断：not\_assessed\_out\_of\_scope
  依据索引：\['product\-boundary'\]
  未处理原因：\[\{'reason': 'protected'\}\]
- 应用/编辑器状态；不从通用缓存规则清除：/Users/liyang/Library/Application Support/Claude/Cookies；逻辑 28672 B，分配 28672 B；ID b02e116883b9c2cab94a
  规则：preserve\-editor\-state
  删除影响：保留；不进入普通缓存清理
  恢复方式：不适用
  模型费用判断：not\_assessed\_out\_of\_scope
  依据索引：\['product\-boundary'\]
  未处理原因：\[\{'reason': 'protected'\}\]
- 应用/编辑器状态；不从通用缓存规则清除：/Users/liyang/Library/Application Support/Cursor/Cookies；逻辑 20480 B，分配 20480 B；ID 5958fde86473b20ed1d6
  规则：preserve\-editor\-state
  删除影响：保留；不进入普通缓存清理
  恢复方式：不适用
  模型费用判断：not\_assessed\_out\_of\_scope
  依据索引：\['product\-boundary'\]
  未处理原因：\[\{'reason': 'protected'\}\]
### 待调查

- AI 编辑器的继承布局：/Users/liyang/Library/Application Support/Cursor/CachedData；逻辑 124137474 B，分配 124493824 B；ID 1238061adee815bcf51d
  规则：ai\-editor\-extra\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['vscode\-vsix', 'live\-layouts'\]
  研究缺口：补齐具体产品的目录用途/版本验证，不能仅因继承 VS Code 就认定所有缓存语义相同。
  未处理原因：\[\{'reason': 'research'\}\]
- AI 应用专用日志路径：/Users/liyang/Library/Application Support/Cursor/logs；逻辑 24047436 B，分配 26308608 B；ID 1ace6b50c9aa0eba1c0e
  规则：ai\-support\-log
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['mole\-caches'\]
  研究缺口：逐产品确认日志用途；不要将会话/审计/模型结果存储按名字判为日志。
  未处理原因：\[\{'reason': 'research'\}\]
- 模型列表和元数据缓存：/Users/liyang/\.codex/models\_cache\.json；逻辑 399712 B，分配 401408 B；ID 0698a69bd00873c0a945
  规则：codex\-model\-catalog
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['codex\-models', 'codex\-client'\]
  研究缺口：刷新不是推理，但元数据可能改变后续请求；费用约束未查清前不默认选中。
  未处理原因：\[\{'reason': 'research'\}\]
- 本地 Shell 初始化快照：/Users/liyang/\.codex/shell\_snapshots；逻辑 783186 B，分配 786432 B；ID 284b7fe1746e86924f71
  规则：codex\-shell\-snapshots
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['codex\-snapshot'\]
  研究缺口：需要实现与源码一致的生命周期识别，避免活动命令失败后引发模型重试。
  未处理原因：\[\{'reason': 'research'\}\]
- daemon 旧运行时：/Users/liyang/\.codex/packages/app\-server\-daemon/releases/0\.160\.1\-aarch64\-apple\-darwin；逻辑 332936515 B，分配 333037568 B；ID ec733ec19c4cdf14aa87
  规则：codex\-daemon\-releases
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['codex\-pruning', 'codex\-install'\]
  研究缺口：需匹配 current 与 selection\-history、两类锁、当前/前次选择和运行可执行文件身份；不能仅按版本号排序。
  未处理原因：\[\{'reason': 'research'\}, \{'path': '/Users/liyang/\.codex/packages/app\-server\-daemon/releases/0\.160\.1\-aarch64\-apple\-darwin/codex', 'reason': 'special\_or\_symlink'\}\]
- 独立 CLI 版本目录：/Users/liyang/\.codex/packages/standalone/releases/0\.162\.1\-aarch64\-apple\-darwin；逻辑 338133795 B，分配 338235392 B；ID c171b09ec632196238da
  规则：codex\-standalone\-releases
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['codex\-install'\]
  研究缺口：独立 CLI 与 daemon 保留职责不等同；需查启动器/后台运行关系和原生退休协议。
  未处理原因：\[\{'reason': 'research'\}, \{'path': '/Users/liyang/\.codex/packages/standalone/releases/0\.162\.1\-aarch64\-apple\-darwin/codex', 'reason': 'special\_or\_symlink'\}\]
- 实际观察的桌面运行时安装暂存：/Users/liyang/\.cache/codex\-runtimes/codex\-runtime\-install\-k8aHVt；逻辑 272289418 B，分配 272289792 B；ID 4c2af7db4f038ac51759
  规则：codex\-desktop\-runtime\-staging
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['live\-layouts'\]
  研究缺口：含 payload/ 和 node\-runtime\.tar\.xz；公开 CLI 源码未找到对应安装器，需验证完成/中断判据。
  未处理原因：\[\{'reason': 'research'\}\]
- 实际观察的桌面运行时安装暂存：/Users/liyang/\.cache/codex\-runtimes/codex\-runtime\-install\-0Vr0lD；逻辑 353330184 B，分配 353333248 B；ID f0aa8dea62b5bbac4e97
  规则：codex\-desktop\-runtime\-staging
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['live\-layouts'\]
  研究缺口：含 payload/ 和 node\-runtime\.tar\.xz；公开 CLI 源码未找到对应安装器，需验证完成/中断判据。
  未处理原因：\[\{'reason': 'research'\}\]
- 实际观察的桌面运行时安装暂存：/Users/liyang/\.cache/codex\-runtimes/codex\-runtime\-install\-Sgwm9z；逻辑 223681208 B，分配 223682560 B；ID 7a9f3a3adfee0ea4dd4c
  规则：codex\-desktop\-runtime\-staging
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['live\-layouts'\]
  研究缺口：含 payload/ 和 node\-runtime\.tar\.xz；公开 CLI 源码未找到对应安装器，需验证完成/中断判据。
  未处理原因：\[\{'reason': 'research'\}\]
- Cursor CLI 独立安装候选：/Users/liyang/\.local/share/cursor\-agent/versions/2026\.05\.05\-84a231c；逻辑 167137467 B，分配 167297024 B；ID 2a629f37e18054dc5f3c
  规则：cursor\-cli\-versions
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['product\-boundary', 'cursor\-install\-20261019'\]
  研究缺口：官方安装器确认 agent/cursor\-agent 两个 launcher 指向版本内 cursor\-agent；仍缺少升级期间的保留/回退协议及具体运行引用的版本集成验证，保持只读。
  未处理原因：\[\{'reason': 'research'\}\]
## 开发项目与工具

### 现在可处理

- npm 内容寻址下载缓存：/Users/liyang/\.npm/\_cacache；逻辑 208564408 B，分配 214745088 B；ID ae2c34a8348675032cbc
  规则：npm\-content\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['npm\-cache'\]
- npm exec/npx 安装缓存：/Users/liyang/\.npm/\_npx；逻辑 191963139 B，分配 263557120 B；ID 3d3d7a5f05de06b70fbc
  规则：npm\-npx\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['npm\-cache', 'npm\-12\-source'\]
  未处理原因：\[\{'path': '/Users/liyang/\.npm/\_npx/31e32ef8478fbf80/node\_modules/\.bin/playwright\-cli', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/31e32ef8478fbf80/node\_modules/\.bin/playwright\-core', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/31e32ef8478fbf80/node\_modules/\.bin/playwright', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/is\-docker', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/is\-inside\-container', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/md2pdf', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/desktop\-commander', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/remove', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/rimraf', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/esvalidate', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/puppeteer', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/node\-which', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/esparse', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/marked', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/setup', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/js\-yaml', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/md\-to\-pdf', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/crc32', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/browsers', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/semver', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/markdown\-it', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/glob', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/uuid', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/pdf2md', 'reason': 'internal\_native\_link'\}, \{'path': '/Users/liyang/\.npm/\_npx/4b4c857f6efdfb61/node\_modules/\.bin/mkdirp', 'reason': 'internal\_native\_link'\}\]
- npm 诊断日志：/Users/liyang/\.npm/\_logs/2026\-10\-18T18\_58\_05\_302Z\-debug\-0\.log；逻辑 101109 B，分配 102400 B；ID 67726ea6613bfd947e1e
  规则：npm\-diagnostic\-log
  删除影响：历史日志不可恢复
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['npm\-cache'\]
- npm 诊断日志：/Users/liyang/\.npm/\_logs/2026\-10\-19T05\_52\_35\_673Z\-debug\-0\.log；逻辑 101020 B，分配 102400 B；ID 2bb70213997d6ca38c77
  规则：npm\-diagnostic\-log
  删除影响：历史日志不可恢复
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['npm\-cache'\]
- npm 诊断日志：/Users/liyang/\.npm/\_logs/2026\-10\-19T05\_58\_28\_924Z\-debug\-0\.log；逻辑 101066 B，分配 102400 B；ID 8dd8f0f2eebcbd0553bf
  规则：npm\-diagnostic\-log
  删除影响：历史日志不可恢复
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['npm\-cache'\]
- npm 诊断日志：/Users/liyang/\.npm/\_logs/2026\-10\-19T10\_13\_42\_081Z\-debug\-0\.log；逻辑 133545 B，分配 135168 B；ID 8912381856f60c21e24f
  规则：npm\-diagnostic\-log
  删除影响：历史日志不可恢复
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['npm\-cache'\]
- npm 诊断日志：/Users/liyang/\.npm/\_logs/2026\-10\-19T05\_54\_50\_792Z\-debug\-0\.log；逻辑 101129 B，分配 102400 B；ID c6d5251c39ac42d61690
  规则：npm\-diagnostic\-log
  删除影响：历史日志不可恢复
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['npm\-cache'\]
- npm 诊断日志：/Users/liyang/\.npm/\_logs/2026\-10\-19T05\_52\_37\_846Z\-debug\-0\.log；逻辑 1089 B，分配 4096 B；ID 821b23606edf77a79327
  规则：npm\-diagnostic\-log
  删除影响：历史日志不可恢复
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['npm\-cache'\]
- npm 诊断日志：/Users/liyang/\.npm/\_logs/2026\-10\-19T05\_53\_43\_139Z\-debug\-0\.log；逻辑 1082 B，分配 4096 B；ID 0d77d312b5bb9728af7b
  规则：npm\-diagnostic\-log
  删除影响：历史日志不可恢复
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['npm\-cache'\]
- npm 诊断日志：/Users/liyang/\.npm/\_logs/2026\-10\-19T05\_58\_30\_982Z\-debug\-0\.log；逻辑 1128 B，分配 4096 B；ID ab89db33a24fcf27d437
  规则：npm\-diagnostic\-log
  删除影响：历史日志不可恢复
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['npm\-cache'\]
- npm 诊断日志：/Users/liyang/\.npm/\_logs/2026\-10\-19T10\_13\_52\_384Z\-debug\-0\.log；逻辑 1054 B，分配 4096 B；ID 78911bc77e02da7180f1
  规则：npm\-diagnostic\-log
  删除影响：历史日志不可恢复
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['npm\-cache'\]
- npm 诊断日志：/Users/liyang/\.npm/\_logs/2026\-10\-19T05\_55\_23\_475Z\-debug\-0\.log；逻辑 1144 B，分配 4096 B；ID 056c7a85d684f4a78e24
  规则：npm\-diagnostic\-log
  删除影响：历史日志不可恢复
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['npm\-cache'\]
- npm 诊断日志：/Users/liyang/\.npm/\_logs/2026\-10\-18T19\_41\_34\_106Z\-debug\-0\.log；逻辑 1012 B，分配 4096 B；ID cd1ab1b264d07a40579c
  规则：npm\-diagnostic\-log
  删除影响：历史日志不可恢复
  恢复方式：只生成今后的日志
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['npm\-cache'\]
- uv 下载/构建缓存域：/Users/liyang/\.cache/uv；逻辑 3139 B，分配 16384 B；ID 31ba60a7090081c15801
  规则：uv\-native\-cache
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：根据已确认用途，不预期增加付费模型计算
  依据索引：\['uv\-cache'\]
### 等待处理

### 保留

### 待调查

- 专用协议拥有的域：/Users/liyang/Library/Caches/ms\-playwright；逻辑 27 B，分配 4096 B；ID 8609b2e08989613a52c5
  规则：reserve\-native\-and\-runtime
  删除影响：下次访问可能重建；打开句柄可能延迟释放空间
  恢复方式：应用或工具在本地重新生成或下载
  模型费用判断：unresolved
  依据索引：\['uv\-cache', 'playwright'\]
  研究缺口：禁止通用 Library 规则兜底；只有更具体且验证通过的原生/下载规则能接管。
  未处理原因：\[\{'reason': 'research'\}\]

## 扫描覆盖

- macos\-user\-cache /Users/liyang：measurement · matched
- macos\-user\-log /Users/liyang：measurement · matched
- sandbox\-cache /Users/liyang：measurement · matched
- sandbox\-log /Users/liyang：measurement · matched
- group\-cache /Users/liyang：measurement · matched
- group\-log /Users/liyang：measurement · matched
- app\-render\-cache /Users/liyang/Library/Application Support：measurement · matched
- ai\-render\-cache /Users/liyang/Library/Application Support：measurement · matched
- editor\-code\-cache /Users/liyang/Library/Application Support：measurement · matched
- editor\-vsix\-download /Users/liyang/Library/Application Support：measurement · matched
- ai\-editor\-extra\-cache /Users/liyang/Library/Application Support：measurement · matched
- editor\-log /Users/liyang/Library/Application Support：measurement · matched
- ai\-support\-log /Users/liyang/Library/Application Support：measurement · matched
- browser\-profile\-cache /Users/liyang/Library/Application Support：measurement · matched
- browser\-root\-shader /Users/liyang/Library/Application Support：measurement · matched
- firefox\-support\-cache /Users/liyang/Library/Application Support：discovery · absent
- design\-media\-cache /Users/liyang/Library/Application Support：discovery · absent
- support\-unreviewed\-leaf /Users/liyang/Library/Application Support：measurement · matched
- codex\-legacy\-tui\-log /Users/liyang/\.codex：discovery · absent
- codex\-other\-log /Users/liyang/\.codex：discovery · absent
- codex\-model\-catalog /Users/liyang/\.codex：measurement · matched
- codex\-shell\-snapshots /Users/liyang/\.codex：measurement · matched
- codex\-arg0 /Users/liyang/\.codex：measurement · matched
- codex\-daemon\-releases /Users/liyang/\.codex：measurement · matched
- codex\-standalone\-releases /Users/liyang/\.codex：measurement · matched
- codex\-daemon\-staging /Users/liyang/\.codex：discovery · absent
- codex\-desktop\-runtime\-staging /Users/liyang：measurement · matched
- claude\-debug\-log /Users/liyang/\.claude：discovery · absent
- claude\-old\-native /Users/liyang/\.local/share/claude/versions：discovery · absent
- cursor\-worker\-versions /Users/liyang/Library/Application Support：measurement · matched
- cursor\-cli\-versions /Users/liyang：measurement · matched
- next\-build\-cache None：discovery · not\_requested
- cargo\-incremental None：discovery · not\_requested
- python\-bytecode None：discovery · not\_requested
- pytest\-core\-cache None：discovery · not\_requested
- pytest\-plugin\-cache None：discovery · not\_requested
- ruff\-cache None：discovery · not\_requested
- npm\-content\-cache /Users/liyang/\.npm：measurement · matched
- npm\-npx\-cache /Users/liyang/\.npm：measurement · matched
- npm\-diagnostic\-log /Users/liyang/\.npm：measurement · matched
- uv\-native\-cache /Users/liyang/\.cache/uv：measurement · matched
- playwright\-download /Users/liyang/Library/Caches/ms\-playwright：discovery · absent
- puppeteer\-download /Users/liyang/\.cache/puppeteer：discovery · absent
- preserve\-codex\-state /Users/liyang/\.codex：measurement · matched
- preserve\-claude\-state /Users/liyang/\.claude：measurement · matched
- preserve\-primary\-runtime /Users/liyang：measurement · matched
- preserve\-editor\-state /Users/liyang/Library/Application Support：measurement · matched
- preserve\-home\-state /Users/liyang：measurement · matched
- preserve\-project\-inputs None：discovery · not\_requested
- preserve\-next\-data\-cache None：discovery · not\_requested
- preserve\-audit /Users/liyang：measurement · matched
- preserve\-sync\-state /Users/liyang：measurement · matched
- preserve\-service\-state /Users/liyang：measurement · matched
- preserve\-model\-bundles /Users/liyang：discovery · absent
- preserve\-environment\-caches /Users/liyang：measurement · matched
- reserve\-native\-and\-runtime /Users/liyang：measurement · matched