#!/bin/bash

# 获取脚本所在目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# 打开应用
open "$SCRIPT_DIR/dist/B站标题提取器.app"

echo "正在启动B站标题提取器..." 