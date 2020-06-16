"""

大交所

"""

"""

上海期货交易所

"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver import IeOptions
from selenium.webdriver.ie.options import Options


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
def login(driver, passwd):
    # 页面元素定位
    locator1 = ''  # 登录
    locator2 = ''  # 确认证书
    locator3 = ''  # 密码输入框
    locator4 = ''  # 密码确认
    locator5 = ''  # 继续浏览此网站
    locator6 = ''  # 电子划款业务

    isLogin = False
    try:
        driver.get('https://10.10.36.3')
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(By.XPATH, locator1))
        print('999921||大商所会服入金||已打开大商所登录页面')
    except BaseException as err:
        print('999931||大商所会服登录||大商所会服系统服务器连接超时>>' + str(err) + '\n请人工介入！')

    # 录入登录信息
    try:
        print('999921||大商所会服登录||开始执行登陆操作')
        element = Find_Element(driver, 5, locator1).click()
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(By.XPATH, locator2))
        element = Find_Element(driver, 5, locator2).click()
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(By.XPATH, locator3))
        element = Find_Element(driver, 5, locator3).send_keys(passwd)
        element = Find_Element(driver, 5, locator4).click()
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(By.XPATH, locator5))
        element = Find_Element(driver, 5, locator5).click()
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(By.XPATH, locator6))
        isLogin = True
        print('999921||大商所会服登录||已成功登陆大商所会服系统')
    except BaseException as err:
        print('999931||大商所会服登录||大商所会服系统登陆失败>>' + str(err) + '\n请人工介入！')


# 入金操作
def transferfund(driver, bank, fund):
    # 页面元素定位
    locator1 = ''  # 电子划款业务
    locator2 = ''  # 划款申请录入
    locator3 = ''  # 入金申请录入
    locator4 = ''  # 下一步
    locator5 = ''  # 划款银行下拉框
    locator6 = ''  # 入金金额输入框
    locator7 = ''  # 提交
    locator8 = ''  # 入金成功

    print('999921||大商所会服入金||已进入大商所会服系统，开始执行入金操作')
    isIn = False
    try:
        element = Find_Element(driver, 5, locator1).click()
        element = Find_Element(driver, 5, locator2).click()
        element = Find_Element(driver, 5, locator3).click()
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(By.XPATH, locator4))
        element = Find_Element(driver, 5, locator4).click()
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(By.XPATH, locator5))
        print('999921||大商所会服入金||已进入入金申请录入页面')
        isIn = True
    except BaseException as err:
        print('999931||大商所会服入金||进入入金申请录入页面失败>>' + str(err))

    # 开始入金操作
    if isIn:
        try:
            print('999921||大商所会服入金||开始执行入金操作')
            element = Find_Element(driver, 5, locator5).click()
            element = Find_Element(driver, 5, bank).click()  # 需获取bank定位信息
            element = Find_Element(driver, 5, locator6).send_keys(fund)
            element = Find_Element(driver, 5, locator7).click()
            WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(By.XPATH, locator8))
            print('999921||大商所会服入金||入金操作成功！')
            driver.quit()
        except BaseException as err:
            print('999931||大商所会服入金||入金操作失败，请人工介入！>>' + str(err))

    else:
        print('999931||大商所会服入金||请人工介入！')
        driver.quit()


if __name__ == "__main__":
    """
    :param passwd: UKEY密码
    :param bank 入金银行
    :param fund 入金金额
    """

    passwd = ''
    bank = ''
    fund = ''

    driver = IEdriverbrowser()
    isLogin = login(driver, passwd)
    if isLogin:
        transferfund(driver, bank, fund)
