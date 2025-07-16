#!/bin/bash

echo "========================================"
echo "网页自动化定时截屏工具"
echo "========================================"
echo

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    echo "错误：未找到Python3，请先安装Python3"
    exit 1
fi

# 检查依赖是否安装
echo "检查依赖包..."
if ! python3 -c "import selenium" &> /dev/null; then
    echo "正在安装依赖包..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "错误：依赖包安装失败"
        exit 1
    fi
fi

echo
echo "启动定时执行器..."
echo "注意：请确保在 config.py 中启用了定时执行功能"
echo
python3 scheduler.py

echo
echo "定时执行器已停止"
echo "按回车键退出..."
read 