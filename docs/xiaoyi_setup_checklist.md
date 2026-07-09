# 小艺开放平台接入清单

## 本地 POC

- 跑通 `GET /healthz`。
- 跑通 `initialize`、`notifications/initialized`。
- 跑通 `message/stream` SSE 输出。
- 跑通 `tasks/cancel` 和 `clearContext`。
- 准备不少于 120 条评测问题并记录结果。

## 公网部署前

- 准备公网 HTTPS 域名。
- 设置 `A2A_ENFORCE_SIGNATURE=true`。
- 在环境变量配置 `A2A_ACCESS_KEY`、`A2A_SECRET_KEY`，不要写入代码。
- 增加限流、访问日志、错误告警、模型成本监控。
- 准备隐私协议、服务说明、内容合规说明。

## 小艺平台配置

- 创建云 A2A 智能体。
- 配置基础信息、角色指令、隐私协议、内容合规。
- 配置快捷指令：制定学习路线、统计方法选择、解释一个概念、出一道练习题。
- 配置卡片：方法选择卡、学习路线卡、每日一题卡。
- 使用小艺调试台联调，再提交上架审核。

