#!/bin/bash

# 获取脚本所在目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# 激活虚拟环境
source "$SCRIPT_DIR/venv/bin/activate"

# 打包应用程序
pyinstaller "$SCRIPT_DIR/bilibili_app.spec" --noconfirm

echo "应用程序打包完成，位于 dist/B站标题提取器.app" 