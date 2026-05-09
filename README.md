# 智能聊天机器人 (My Chatbot)

## 项目简介
这是一个基于 Python 和 Streamlit 搭建的本地智能聊天机器人，利用 Ollama 调用本地部署的 Qwen 模型实现实时对话。

## 功能演示
![聊天界面截图](./demo.png)

## 技术栈
- **编程语言**：Python 3.10+
- **核心框架**：Streamlit
- **模型部署**：Ollama (Qwen / DeepSeek)

## 快速开始

### 环境要求
- Python 3.10 或更高版本
- Ollama 并已拉取模型

### 安装与运行

1. **克隆仓库**
    ```bash
    git clone https://github.com/linhaicheng2026/chatbot.git
    cd my-chatbot

2. 安装依赖
    ```bash
    pip install -r requirements.txt
 
3. 启动应用
    ```bash
     streamlit run app.py

### 项目结构
    my-chatbot/
    ├── app.py # 主程序入口，聊天界面逻辑
    ├── utils.py # 工具函数，如模型调用封装
    ├── requirements.txt # 项目依赖清单
    ├── .gitignore # Git忽略规则
    └── README.md # 项目说明文档

### 学习笔记
2026-05-08：完成 Streamlit 聊天界面的初步搭建，实现基本问答。

2026-05-09：遇到 .gitignore 规则不生效的问题，最终排查是 Windows 下文件编码（BOM头）导致，已解决。