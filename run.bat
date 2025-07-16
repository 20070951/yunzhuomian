@echo off
chcp 65001 >nul
echo ========================================
echo 网页自动化截屏工具
echo ========================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误：未找到Python，请先安装Python
    pause
    exit /b 1
)

REM 检查依赖是否安装
echo 检查依赖包...
pip show selenium >nul 2>&1
if errorlevel 1 (
    echo 正在安装依赖包...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo 错误：依赖包安装失败
        pause
        exit /b 1
    )
)

echo.
echo 开始运行自动化截屏...
python web_screenshot.py

echo.
echo 按任意键退出...
pause >nul 