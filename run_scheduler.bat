@echo off
chcp 65001 >nul
echo ========================================
echo 网页自动化定时截屏工具
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
echo 启动定时执行器...
echo 注意：请确保在 config.py 中启用了定时执行功能
echo.
python scheduler.py

echo.
echo 定时执行器已停止
echo 按任意键退出...
pause >nul 