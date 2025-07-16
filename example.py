#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用示例：网页自动化截屏工具

这个脚本展示了如何使用WebScreenshot类来自动化网页截屏流程。
"""

from web_screenshot import WebScreenshot
from config import TARGET_URL


def example_basic_usage():
    """基本使用示例"""
    print("=== 基本使用示例 ===")

    # 创建自动化实例
    automation = WebScreenshot()

    # 运行自动化流程
    result = automation.run_automation(TARGET_URL)

    if result:
        print(f"✅ 截图成功保存到: {result}")
    else:
        print("❌ 截图失败")


def example_custom_url():
    """自定义URL示例"""
    print("\n=== 自定义URL示例 ===")

    # 自定义网页地址
    custom_url = "https://www.google.com"

    automation = WebScreenshot()
    result = automation.run_automation(custom_url)

    if result:
        print(f"✅ 自定义URL截图成功: {result}")
    else:
        print("❌ 自定义URL截图失败")


def example_multiple_screenshots():
    """多次截图示例"""
    print("\n=== 多次截图示例 ===")

    urls = [
        "https://www.baidu.com",
        "https://www.google.com",
        "https://www.bing.com"
    ]

    automation = WebScreenshot()

    for i, url in enumerate(urls, 1):
        print(f"\n正在处理第 {i} 个网页: {url}")
        result = automation.run_automation(url)

        if result:
            print(f"✅ 第 {i} 个网页截图成功: {result}")
        else:
            print(f"❌ 第 {i} 个网页截图失败")


if __name__ == "__main__":
    # 运行基本示例
    example_basic_usage()

    # 运行自定义URL示例
    # example_custom_url()

    # 运行多次截图示例
    # example_multiple_screenshots()
