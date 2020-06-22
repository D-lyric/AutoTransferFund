"""
Chromedriver的两种启动方式------->无浏览器启动和有浏览器启动无需入参，返回driver对象
chromebrowser_debug------->通过cmd命令打开端口号为9992的Chrome浏览器（需要设置Chromedriver环境变量）
chromedriver_debug------->使用selenium接管端口号为9992的Chrome浏览器，返回driver对象

常用的Options如下：
chrome_options.add_argument('--user-agent=""')   设置请求头的User-Agent
chrome_options.add_argument('--window-size=1280x1024')   设置浏览器分辨率（窗口大小）
chrome_options.add_argument('--start-maximized')   最大化运行（全屏窗口）,不设置，取元素会报错
chrome_options.add_argument('--disable-infobars')   禁用浏览器正在被自动化程序控制的提示
chrome_options.add_argument('--incognito')   隐身模式（无痕模式）
chrome_options.add_argument('--hide-scrollbars')   隐藏滚动条, 应对一些特殊页面
chrome_options.add_argument('--disable-javascript')   禁用javascript
chrome_options.add_argument('--blink-settings=imagesEnabled=false')   不加载图片, 提升速度
chrome_options.add_argument('--headless')   浏览器不提供可视化页面
chrome_options.add_argument('--ignore-certificate-errors')   禁用扩展插件并实现窗口最大化
chrome_options.add_argument('--disable-gpu')   禁用GPU加速
chrome_options.add_argument('–disable-software-rasterizer')
chrome_options.add_argument('--disable-extensions') 禁用扩展插件
chrome_options.add_argument('--start-maximized')  浏览器启动后窗口最大化

"""
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions


# 无头启动
def chromedrivernobrowser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    # 规避检测
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(chrome_options=chrome_options, options=option)
    return driver


# 正常启动
def chromedriverbrowser():
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(options=option)
    return driver


# 用于打开可直接被selenium接管的Chrome浏览器
def chromebrowser_debug():
    cmd_command = 'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"'
    os.system(cmd_command)


# 接管通过cmd命令打开的Chrome浏览器
def chromedriver_debug():
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    return driver

# if __name__ == "__main__":
#     chromebrowser_debug()
