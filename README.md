# 网页自动化截屏工具

这是一个简单的Python工具，可以自动打开指定网页、刷新页面并截取屏幕截图。

## 功能特点

- 自动打开指定网页
- 自动刷新页面
- 自动截取屏幕截图
- 截图自动保存到 `screenshots` 目录
- 支持自定义网页地址

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 方法1：调试元素选择器（推荐先运行）
如果你的网页有特定的元素需要点击，建议先运行调试脚本：

```bash
python debug_elements.py
```

这个脚本会列出页面上所有可点击的元素，帮助你找到正确的选择器。

### 方法2：直接运行自动化脚本
1. 安装依赖包：
```bash
pip install -r requirements.txt
```

2. 修改 `config.py` 中的配置：
   - `TARGET_URL` - 目标网页地址
   - `FIRST_ELEMENT_SELECTOR` - 第一个要点击的元素选择器
   - `SECOND_ELEMENT_SELECTOR` - 第二个要点击的元素选择器

3. 运行脚本：
```bash
python web_screenshot.py
```

### 方法2：使用示例脚本
```bash
python example.py
```

### 方法3：自定义使用
```python
from web_screenshot import WebScreenshot

# 创建实例
automation = WebScreenshot()

# 运行自动化流程
result = automation.run_automation("https://www.example.com")

if result:
    print(f"截图保存到: {result}")
```

## 配置说明

在 `config.py` 文件中，你可以修改以下配置：

```python
# 目标网页地址
TARGET_URL = "http://restapi.k8s-mars.gyt.glb.cmos:30088/#/manage/serviceDetail/Deployment/rhgz-engine-ly//ly-app-prd-dualstack-4th3-respool/"

# 截图保存目录
SCREENSHOT_DIR = "screenshots"

# 浏览器窗口大小
WINDOW_SIZE = "1920,1080"

# 页面加载等待时间（秒）
PAGE_LOAD_WAIT = 5

# 第一个元素点击后等待时间（秒）
FIRST_CLICK_WAIT = 30

# 第二个元素点击后等待时间（秒）
SECOND_CLICK_WAIT = 10

# 是否使用无头模式（不显示浏览器窗口）
HEADLESS_MODE = True

# 第一个要点击的元素选择器（运行状态选项卡）
FIRST_ELEMENT_SELECTOR = "li.tab-head-item[ng-click*='switchTab']:contains('运行状态')"

# 第二个要点击的元素选择器
SECOND_ELEMENT_SELECTOR = "li.tab-head-item[ng-click*='switchTab']:nth-child(2)"
```

## 输出

- 截图文件保存在 `screenshots/` 目录下
- 文件名格式：`screenshot_YYYYMMDD_HHMMSS.png`
- 控制台会显示执行进度和结果

## 注意事项

1. 确保你的系统已安装Chrome浏览器
2. 脚本会自动下载ChromeDriver，需要网络连接
3. 如果不需要显示浏览器窗口，可以取消注释代码中的 `--headless` 选项

## 自定义刷新方式

如果网页有特定的刷新按钮，你可以修改 `click_refresh()` 方法：

```python
# 取消注释并修改选择器来点击页面上的刷新按钮
refresh_button = WebDriverWait(self.driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "你的刷新按钮选择器"))
)
refresh_button.click()
``` 