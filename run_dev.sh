#!/bin/bash

# 获取脚本所在目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# 激活虚拟环境
source "$SCRIPT_DIR/venv/bin/activate"

# 运行应用程序
python "$SCRIPT_DIR/bilibili_title_extractor.py"

echo "B站标题提取器已启动..." 