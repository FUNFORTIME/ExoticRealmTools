# 快速入门千星奇域 · AI知识库

## 项目简介

**千星奇域AI知识库**是一个专为《原神》UGC（用户生成内容）设计的免费AI工具集，旨在帮助玩家轻松学习和使用节点图编辑技术。即使是派蒙也能快速上手！

## 作者信息

- 📧 在线平台：[点我](https://ugc.070077.xyz)
- 👥 QQ群：`1007538100`
- 💻 GitHub：[点击这里](https://github.com/1475505/Miliastra-toolbox)
- Bilibili：[神奇嘟嘟可](https://space.bilibili.com/233587917)

## 文档编者提示

建议使用时配置自己的API，教程（以DeepSeek API为例子）如下：

### 第一步：获取API密钥

1. [点击访问API密钥创建平台](https://platform.deepseek.com/api_keys)
2. 登录后，进入 **API密钥管理** 页面，点击 **创建新的API密钥** 按钮
3. 妥善保存生成的API Key（只有创建时可见可复制）
4. [DeepSeek额度充值](https://platform.deepseek.com/top_up)

## 第二步：配置API参数

在您的项目配置界面中，请按以下设置填写：

### 基础配置

- **API Base URL**：填写 `https://api.deepseek.com/v1`
- **Model**：选择 `deepseek-chat`
- **API Key**：填入第一步中获取的密钥

### 模型说明

- `deepseek-chat`：标准对话模式（推荐日常使用）
- `deepseek-reasoner`：思考模式（适合复杂推理任务）
- 更多信息见 [DeepSeek官方文档](https://api-docs.deepseek.com/zh-cn/)

## 验证配置

保存配置后，建议发送测试消息验证API是否正常工作。如果返回正常响应，说明配置成功！
