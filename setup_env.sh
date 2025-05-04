#!/bin/bash

# 获取脚本所在目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# 检查是否安装了Python
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到Python。请先安装Python 3.6+再运行此脚本。"
    exit 1
fi

# 创建虚拟环境
echo "正在创建虚拟环境..."
python3 -m venv "$SCRIPT_DIR/venv"

# 激活虚拟环境
source "$SCRIPT_DIR/venv/bin/activate"

# 安装依赖
echo "正在安装依赖..."
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org PyQt5 requests pyinstaller

echo "环境设置完成！现在您可以运行:"
echo "  ./run_dev.sh    - 运行应用程序"
echo "  ./build_app.sh  - 打包应用程序" 