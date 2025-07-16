import time
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from config import *


class WebScreenshot:
    def __init__(self):
        self.driver = None
        self.screenshot_dir = SCREENSHOT_DIR

        # 创建截图保存目录
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def setup_driver(self):
        """设置Chrome浏览器驱动"""
        chrome_options = Options()
        # 可选：无头模式（不显示浏览器窗口）
        if HEADLESS_MODE:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument(f"--window-size={WINDOW_SIZE}")

        # 自动下载并设置ChromeDriver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def open_website(self, url):
        """打开指定网页"""
        try:
            print(f"正在打开网页: {url}")
            self.driver.get(url)
            time.sleep(PAGE_LOAD_WAIT)  # 等待页面加载
            print("网页加载完成")
            return True
        except Exception as e:
            print(f"打开网页失败: {e}")
            return False

    def find_element_by_text(self, text, selector_base="li.tab-head-item"):
        """通过文本内容查找元素"""
        try:
            # 方法1：使用XPath查找包含特定文本的元素
            xpath_selector = f"//{selector_base}[contains(text(), '{text}')]"
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath_selector))
            )
            return element
        except:
            try:
                # 方法2：查找所有匹配的元素，然后筛选
                elements = self.driver.find_elements(
                    By.CSS_SELECTOR, selector_base)
                for element in elements:
                    if text in element.text:
                        return element
            except:
                pass
        return None

    def click_first_element(self):
        """点击第一个元素（运行状态选项卡）"""
        try:
            print("正在查找并点击第一个元素（运行状态选项卡）...")

            # 等待页面完全加载
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "li.tab-head-item"))
            )

            # 尝试多种方法查找元素
            first_element = None

            # 方法1：通过文本内容查找
            first_element = self.find_element_by_text("运行状态")

            # 方法2：如果方法1失败，使用CSS选择器
            if not first_element:
                try:
                    first_element = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(
                            (By.CSS_SELECTOR, FIRST_ELEMENT_SELECTOR))
                    )
                except:
                    pass

            # 方法3：如果方法2失败，使用备用选择器
            if not first_element:
                try:
                    first_element = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(
                            (By.CSS_SELECTOR, FIRST_ELEMENT_SELECTOR_BACKUP))
                    )
                except:
                    pass

            if not first_element:
                raise Exception("无法找到第一个元素")

            # 滚动到元素可见
            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);", first_element)
            time.sleep(1)

            # 点击元素
            first_element.click()
            print(f"第一个元素点击成功，等待 {FIRST_CLICK_WAIT} 秒...")
            time.sleep(FIRST_CLICK_WAIT)
            print("第一个元素等待完成")
            return True

        except Exception as e:
            print(f"点击第一个元素失败: {e}")
            return False

    def click_second_element(self):
        """点击第二个元素"""
        try:
            print("正在查找并点击第二个元素...")

            # 查找第二个元素
            second_element = None

            # 方法1：使用CSS选择器
            try:
                second_element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, SECOND_ELEMENT_SELECTOR))
                )
            except:
                pass

            # 方法2：如果方法1失败，使用备用选择器
            if not second_element:
                try:
                    second_element = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(
                            (By.CSS_SELECTOR, SECOND_ELEMENT_SELECTOR_BACKUP))
                    )
                except:
                    pass

            # 方法3：如果方法2失败，选择第二个选项卡
            if not second_element:
                try:
                    elements = self.driver.find_elements(
                        By.CSS_SELECTOR, "li.tab-head-item")
                    if len(elements) >= 2:
                        second_element = elements[1]
                except:
                    pass

            if not second_element:
                raise Exception("无法找到第二个元素")

            # 滚动到元素可见
            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);", second_element)
            time.sleep(1)

            # 点击元素
            second_element.click()
            print(f"第二个元素点击成功，等待 {SECOND_CLICK_WAIT} 秒...")
            time.sleep(SECOND_CLICK_WAIT)
            print("第二个元素等待完成")
            return True

        except Exception as e:
            print(f"点击第二个元素失败: {e}")
            return False

    def click_refresh(self):
        """点击刷新按钮（保留原有功能）"""
        try:
            if REFRESH_BUTTON_SELECTOR:
                # 方法2：点击页面上的刷新按钮
                print("正在点击页面刷新按钮...")
                refresh_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, REFRESH_BUTTON_SELECTOR))
                )
                refresh_button.click()
                time.sleep(PAGE_LOAD_WAIT)
                print("页面刷新完成")
            else:
                # 方法1：使用浏览器刷新
                print("正在刷新页面...")
                self.driver.refresh()
                time.sleep(PAGE_LOAD_WAIT)  # 等待刷新完成
                print("页面刷新完成")
            return True

        except Exception as e:
            print(f"刷新页面失败: {e}")
            return False

    def take_screenshot(self, filename=None):
        """截取屏幕截图"""
        try:
            if filename is None:
                # 生成带时间戳的文件名
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"screenshot_{timestamp}.png"

            filepath = os.path.join(self.screenshot_dir, filename)

            print(f"正在截取屏幕截图...")
            self.driver.save_screenshot(filepath)
            print(f"截图已保存到: {filepath}")
            return filepath

        except Exception as e:
            print(f"截图失败: {e}")
            return None

    def run_automation(self, url):
        """运行完整的自动化流程"""
        try:
            # 1. 设置浏览器驱动
            self.setup_driver()

            # 2. 打开网页
            if not self.open_website(url):
                return False

            # 3. 点击第一个元素（运行状态选项卡）
            if not self.click_first_element():
                return False

            # 4. 点击第二个元素
            if not self.click_second_element():
                return False

            # 5. 截取屏幕截图
            screenshot_path = self.take_screenshot()
            if screenshot_path:
                print("自动化流程完成！")
                return screenshot_path
            else:
                return False

        except Exception as e:
            print(f"自动化流程出错: {e}")
            return False
        finally:
            # 关闭浏览器
            if self.driver:
                self.driver.quit()
                print("浏览器已关闭")


def main():
    """主函数"""
    print("=== 网页自动化截屏工具 ===")
    print(f"目标网页: {TARGET_URL}")

    # 创建自动化实例
    automation = WebScreenshot()

    # 运行自动化流程
    result = automation.run_automation(TARGET_URL)

    if result:
        print(f"✅ 成功！截图保存在: {result}")
    else:
        print("❌ 失败！请检查网络连接和网页地址")


if __name__ == "__main__":
    main()
