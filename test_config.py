#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置测试脚本

这个脚本会测试当前的配置是否正确。
"""

from config import *


def test_config():
    """测试配置"""
    print("=== 配置测试 ===")
    print(f"目标URL: {TARGET_URL}")
    print(f"截图目录: {SCREENSHOT_DIR}")
    print(f"窗口大小: {WINDOW_SIZE}")
    print(f"页面加载等待: {PAGE_LOAD_WAIT} 秒")
    print(f"第一个元素点击后等待: {FIRST_CLICK_WAIT} 秒")
    print(f"第二个元素点击后等待: {SECOND_CLICK_WAIT} 秒")
    print(f"无头模式: {HEADLESS_MODE}")
    print(f"第一个元素选择器: {FIRST_ELEMENT_SELECTOR}")
    print(f"第二个元素选择器: {SECOND_ELEMENT_SELECTOR}")
    print(f"第一个元素备用选择器: {FIRST_ELEMENT_SELECTOR_BACKUP}")
    print(f"第二个元素备用选择器: {SECOND_ELEMENT_SELECTOR_BACKUP}")

    print("\n=== 配置验证 ===")

    # 验证URL格式
    if TARGET_URL.startswith(('http://', 'https://')):
        print("✅ URL格式正确")
    else:
        print("❌ URL格式可能有问题")

    # 验证等待时间
    if FIRST_CLICK_WAIT > 0 and SECOND_CLICK_WAIT > 0:
        print("✅ 等待时间配置正确")
    else:
        print("❌ 等待时间配置有问题")

    # 验证选择器
    if FIRST_ELEMENT_SELECTOR and SECOND_ELEMENT_SELECTOR:
        print("✅ 元素选择器已配置")
    else:
        print("❌ 元素选择器未配置")

    print("\n配置测试完成！")


if __name__ == "__main__":
    test_config()
