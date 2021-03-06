"""

上海期货交易所

"""
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver import IeOptions
from selenium.webdriver.ie.options import Options
from Utils.captcha_recognition2 import getValidationCode
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions


def IEdrivernobrowser():
    # 无头启动
    IE_options = Options()
    IE_options.add_argument("--headless")
    IE_options.add_argument("--disable-gpu")
    # 规避检测
    option = IeOptions()
    option.add_additional_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Ie(ie_options=IE_options, options=option)
    return driver


def IEdriverbrowser():
    # 正常启动
    # 规避检测
    option = IeOptions()
    option.add_additional_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Ie(options=option)
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
    chrome_driver = r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    return driver


# def IEbrowserdriver():
#     capabilities = webdriver.DesiredCapabilities().INTERNETEXPLORER
#     capabilities['acceptSslCerts'] = True
#     driver = webdriver.Ie(capabilities=capabilities)
#     return driver

def Find_Element(driver, mode, locator):
    try:
        if mode == 1:
            element = driver.find_element_by_name(locator)
            return element
        if mode == 2:
            element = driver.find_element_by_id(locator)
            return element
        if mode == 3:
            element = driver.find_element_by_class(locator)
            return element
        if mode == 4:
            element = driver.find_element_by_css_selector(locator)
            return element
        if mode == 5:
            element = driver.find_element_by_xpath(locator)
            return element
        if mode == 6:
            element = driver.find_element_by_link_text(locator)
            return element
        else:
            errmsg = '该类型未定义：{}'.format(mode)
    except BaseException as err:
        print(err)


# 登录
def login(driver, username, passwd):
    # 页面定位元素
    locator1 = ''  # 用户名
    locator2 = ''  # 密码
    locator3 = ''  # 验证码输入框
    locator4 = ''  # 验证码刷新按钮
    locator5 = ''  # 登陆按钮
    locator6 = ''  # 电子出入金

    # 开始登陆
    islogin = False
    try:
        # 打开上交所网站
        driver.get('https://192.168.9.113')
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(By.XPATH, locator1))
        print('999921||上交所会服系统登陆||已打开上交所会服系统登陆界面，开始执行登陆操作')
    except BaseException as err:
        print('999931||上交所会服系统登陆||上交所会服系统连接服务器超时>>' + str(err) + '\n请人工介入！')
    # 输入用户名、密码
    element = Find_Element(driver, 5, locator1).send_keys(username)
    element = Find_Element(driver, 5, locator2).send_keys(passwd)
    i = 0
    while i < 10:
        # 输入图片验证码
        element = Find_Element(driver, 5, locator4).click()
        vercode = getValidationCode.getCodeStr(driver)
        element = Find_Element(driver, 5, locator3)
        element.clear()
        element.send_keys(vercode)
        element = Find_Element(driver, 5, locator5)
        # 验证是否登录成功
        try:
            WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(By.XPATH, locator6))
            print('999921||上交所会服系统登陆||上交所会服系统登陆成功！')
            islogin = True
            break
        except BaseException as err:
            print('999921||上交所会服系统登陆||上交所回复系统登陆失败，将在3秒后进行第{}次重试'.format(i + 1))
            i += 1
            time.sleep(3)
    else:
        print('999931||上交所会服系统登陆||上交所回复系统登陆失败，请人工介入')
        driver.quit()

    return islogin


# 资金划拨
def transferfund(driver, bank, fund):
    # 页面定位元素
    locator1 = '//td[text()="电子出入金"]'  # 电子出入金
    locator2 = '//td[text()="出入金申请"]'  # 出入金申请
    locator3 = '//td[text()="出入金申请制单"]'  # 出入金申请制单
    locator4 = ''  # 新建
    locator5 = ''  # 单据号
    locator6 = ''  # 资金账户下拉框
    locator7 = ''  # 02590101(CNY)选项
    locator8 = ''  # 银行名称下拉框
    locator9 = ''  # 资金用途下拉框
    locator10 = ''  # 批准划转款选项
    locator11 = ''  # 方向下拉框
    locator12 = ''  # 入金选项
    locator13 = ''  # 金额
    locator14 = ''  # 勾选框
    locator15 = ''  # 确定
    locator16 = ''  # 入金成功确认

    isIn = False
    try:
        # 进入出入金申请制单界面
        element = Find_Element(driver, 5, locator1).click()
        element = Find_Element(driver, 5, locator2).click()
        element = Find_Element(driver, 5, locator3).click()
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(By.XPATH, locator4))
        isIn = True
        print('999921||上交所会服入金||已进入上交所出入金申请制单界面')
    except BaseException as err:
        print('999921||上交所会服入金||进入上交所出入金申请制单界面失败>>' + str(err))

    # 开始入金操作
    if isIn:
        try:
            print('999921||上交所会服入金||开始上交所入金操作')
            element = Find_Element(driver, 5, locator4).click()
            WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(By.XPATH, locator5))
            docno = ''  # 需确认docno（单据号）的获取方式
            element = Find_Element(driver, 5, locator5).send_keys(docno)
            element = Find_Element(driver, 5, locator6).click()
            element = Find_Element(driver, 5, locator7).click()
            element = Find_Element(driver, 5, locator8).click()
            element = Find_Element(driver, 5, bank).click()
            element = Find_Element(driver, 5, locator9).click()
            element = Find_Element(driver, 5, locator10).click()
            element = Find_Element(driver, 5, locator11).click()
            element = Find_Element(driver, 5, locator12).click()
            element = Find_Element(driver, 5, locator13).send_keys(fund)
            element = Find_Element(driver, 5, locator14).click()
            element = Find_Element(driver, 5, locator15).click()
            WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(By.XPATH, locator16))
            print('999921||上交所会服入金||上交所入金操作成功')
            driver.quit()
        except BaseException as err:
            print('999931||上交所会服系统登陆||上交所入金操作失败>>' + str(err) + '\n请人工介入！')
    else:
        print('999931||上交所会服入金||请人工介入！')
        driver.quit()


# if __name__ == "__main__":
#     """
#     :param username: 用户名
#     :param passwd: 密码
#     :param bank: 银行
#     :param fund: 入金金额
#     """
#     username = ''
#     passwd = ''
#     bank = ''
#     fund = ''
#     driver = IEdriverbrowser()
#     islogin = login(driver, username, passwd)
#     if islogin:
#         transferfund(driver, bank, fund)

if __name__ == "__main__":
    driver = chromedriver_debug()


