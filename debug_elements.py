#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
调试脚本：帮助找到正确的元素选择器

这个脚本会打开网页并列出所有可点击的元素，帮助你找到正确的选择器。
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from config import *


def debug_elements():
    """调试元素查找"""
    print("=== 元素调试工具 ===")
    print(f"目标网页: {TARGET_URL}")

    # 设置浏览器（不使用无头模式，方便查看）
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument(f"--window-size={WINDOW_SIZE}")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # 打开网页
        print("正在打开网页...")
        driver.get(TARGET_URL)
        time.sleep(PAGE_LOAD_WAIT)
        print("网页加载完成")

        # 等待页面元素加载
        print("等待页面元素加载...")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # 查找所有选项卡元素
        print("\n=== 查找选项卡元素 ===")
        tab_elements = driver.find_elements(
            By.CSS_SELECTOR, "li.tab-head-item")
        print(f"找到 {len(tab_elements)} 个选项卡元素:")

        for i, element in enumerate(tab_elements):
            try:
                text = element.text.strip()
                classes = element.get_attribute("class")
                onclick = element.get_attribute("ng-click")
                print(f"  {i+1}. 文本: '{text}' | 类: {classes} | 点击事件: {onclick}")
            except Exception as e:
                print(f"  {i+1}. 获取信息失败: {e}")

        # 查找包含"运行状态"的元素
        print("\n=== 查找包含'运行状态'的元素 ===")
        try:
            # 使用XPath查找
            xpath_elements = driver.find_elements(
                By.XPATH, "//*[contains(text(), '运行状态')]")
            print(f"XPath找到 {len(xpath_elements)} 个包含'运行状态'的元素:")
            for i, element in enumerate(xpath_elements):
                tag = element.tag_name
                text = element.text.strip()
                classes = element.get_attribute("class")
                print(f"  {i+1}. 标签: {tag} | 文本: '{text}' | 类: {classes}")
        except Exception as e:
            print(f"XPath查找失败: {e}")

        # 查找所有可点击的元素
        print("\n=== 查找所有可点击的元素 ===")
        clickable_elements = driver.find_elements(
            By.CSS_SELECTOR, "[ng-click], [onclick], button, a, li[class*='tab'], li[class*='click']")
        print(f"找到 {len(clickable_elements)} 个可点击元素:")

        for i, element in enumerate(clickable_elements[:10]):  # 只显示前10个
            try:
                tag = element.tag_name
                text = element.text.strip()[:50]  # 限制文本长度
                classes = element.get_attribute("class")
                onclick = element.get_attribute(
                    "ng-click") or element.get_attribute("onclick")
                print(
                    f"  {i+1}. 标签: {tag} | 文本: '{text}' | 类: {classes} | 点击: {onclick}")
            except Exception as e:
                print(f"  {i+1}. 获取信息失败: {e}")

        if len(clickable_elements) > 10:
            print(f"  ... 还有 {len(clickable_elements) - 10} 个元素未显示")

        # 查找所有li元素（可能包含选项卡）
        print("\n=== 查找所有li元素 ===")
        li_elements = driver.find_elements(By.TAG_NAME, "li")
        print(f"找到 {len(li_elements)} 个li元素:")

        for i, element in enumerate(li_elements[:15]):  # 只显示前15个
            try:
                text = element.text.strip()[:30]  # 限制文本长度
                classes = element.get_attribute("class")
                onclick = element.get_attribute("ng-click")
                if text:  # 只显示有文本的元素
                    print(
                        f"  {i+1}. 文本: '{text}' | 类: {classes} | 点击: {onclick}")
            except Exception as e:
                pass

        if len(li_elements) > 15:
            print(f"  ... 还有 {len(li_elements) - 15} 个li元素未显示")

        print("\n=== 调试完成 ===")
        print("请根据上面的信息修改 config.py 中的元素选择器")
        print("按回车键关闭浏览器...")
        input()

    except Exception as e:
        print(f"调试过程出错: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    debug_elements()
