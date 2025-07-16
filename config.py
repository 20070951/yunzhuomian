# 配置文件

# 目标网页地址 - 修改这里为你想要截图的网页
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
# 根据图片中的HTML结构，选择包含"运行状态"文本的选项卡
FIRST_ELEMENT_SELECTOR = "li.tab-head-item[ng-click*='switchTab']:contains('运行状态'), li.tab-head-item[ng-bind*='tab.serName']:contains('运行状态')"

# 第二个要点击的元素选择器（根据实际需要修改）
# 这里选择第二个选项卡，你可以根据实际需要修改
SECOND_ELEMENT_SELECTOR = "li.tab-head-item[ng-click*='switchTab']:nth-child(2), li.tab-head-item[ng-bind*='tab.serName']:nth-child(2)"

# 备用选择器（如果上面的选择器不工作）
FIRST_ELEMENT_SELECTOR_BACKUP = "li.tab-head-item.active, li.tab-head-item:first-child"
SECOND_ELEMENT_SELECTOR_BACKUP = "li.tab-head-item:nth-child(2)"

# 自定义刷新按钮选择器（如果网页有特定的刷新按钮）
REFRESH_BUTTON_SELECTOR = None
# 例如：REFRESH_BUTTON_SELECTOR = "button[aria-label='刷新']"

# 定时执行配置
# 是否启用定时执行
ENABLE_SCHEDULER = False

# 执行间隔时间（分钟）
SCHEDULE_INTERVAL_MINUTES = 30

# 最大执行次数（0表示无限执行）
MAX_EXECUTIONS = 0

# 是否在每次执行后显示执行统计
SHOW_STATS = True
