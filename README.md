# B站标题提取器

一个简洁易用的工具，帮你一键提取B站视频/合集中的所有标题。

## ✨ 功能特点

- 支持输入B站视频链接或BV号
- 自动获取视频所有分P或合集中的标题
- 清晰展示标题列表
- 界面简洁直观，操作便捷

## 📥 安装方法

### 方法一：直接使用打包好的应用

1. 下载本仓库
2. 双击 `dist/B站标题提取器.app` 直接运行

### 方法二：通过脚本启动

```bash
# 在终端中执行
./start.sh
```

### 方法三：从源码运行

```bash
# 安装依赖
pip install PyQt5 requests

# 运行程序
python bilibili_title_extractor.py
```

## 🚀 使用示例

1. 启动应用
2. 复制B站视频链接，如: `https://www.bilibili.com/video/BV1JV411t7ow`
3. 粘贴到输入框中
4. 点击【获取标题】按钮
5. 几秒钟后，所有视频标题将显示在下方

### 应用界面预览

![B站标题提取器界面](resources/Screenshot%202025-05-04%20at%2015.15.12.png)

## 🔧 环境要求

- Python 3.6 或更高版本
- 依赖包：
  - PyQt5 (GUI界面)
  - requests (网络请求)

## ⚠️ 常见问题

- **问题**: 程序无法启动
  **解决**: 确保已安装所需依赖 `pip install PyQt5 requests`

- **问题**: 无法提取标题
  **解决**: 检查网络连接，或尝试更换视频链接测试

## 🛠️ 开发相关

### 重新打包应用

```bash
# 安装打包工具
pip install pyinstaller

# 执行打包命令
pyinstaller bilibili_app.spec
```

打包后的应用位于 `dist/B站标题提取器.app` 目录。 