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

> **注意**：从GitHub下载仓库后，由于GitHub对大文件的限制，可能需要在本地重新打包应用。详见[常见问题](#⚠️-常见问题)部分。

### 方法二：使用独立虚拟环境（推荐）

为确保依赖不冲突，推荐使用项目自带的脚本在独立环境中运行：

```bash
# 一次性设置（创建虚拟环境并安装依赖）
./setup_env.sh

# 运行应用
./run_dev.sh

# 打包应用（可选）
./build_app.sh
```

### 方法三：通过脚本启动

```bash
# 在终端中执行
./start.sh
```

### 方法四：从源码运行

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

- **问题**: 从GitHub下载后无法运行打包好的应用
  **解决**: 
  1. 使用虚拟环境脚本（推荐）：
     ```bash
     ./setup_env.sh  # 设置环境
     ./run_dev.sh    # 运行应用
     ```
  2. 直接运行Python脚本：
     ```bash
     pip install PyQt5 requests
     python3 bilibili_title_extractor.py
     ```
  3. 手动重新打包应用：
     ```bash
     pip install pyinstaller
     pyinstaller bilibili_app.spec
     # 然后运行 dist/B站标题提取器.app
     ```

## 🛠️ 开发相关

### 项目结构

```
Bilibili/
├── bilibili_title_extractor.py  # 主程序
├── title_parser.py              # 标题解析模块
├── bilibili_app.spec            # PyInstaller打包配置
├── setup_env.sh                 # 环境设置脚本
├── run_dev.sh                   # 开发环境运行脚本
├── build_app.sh                 # 应用打包脚本
├── start.sh                     # 快速启动脚本
└── venv/                        # 虚拟环境（由setup_env.sh创建）
```

### 重新打包应用

```bash
# 方法1：使用虚拟环境（推荐）
./build_app.sh

# 方法2：手动打包
pip install pyinstaller
pyinstaller bilibili_app.spec
```

打包后的应用位于 `dist/B站标题提取器.app` 目录。 