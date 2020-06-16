"""

郑商所

"""

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver import IeOptions
from selenium.webdriver.ie.options import Options
from Utils.captcha_recognition2 import getValidationCode


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
def login():
    pass

# 入金操作
def transferfund(bank, fund):
    # 页面元素定位
    locator1 = ''  # 入金管理
    locator2 = ''  # 录入
    locator3 = ''  # 资金类型下拉框
    locator4 = ''  # 保证金选项
    locator5 = ''  # 银行下拉框
    locator6 = ''  # 申请金额输入框
    locator7 = ''  # 提交
    locator8 = ''  # 提交成功确认

    # 实例化IE浏览器驱动
    driver = IEdriverbrowser()
    driver.get('https://member.czce.com.cn')

    # 进入录入界面
    isIn = False
    try:
        element = Find_Element(driver, 5, locator1).click()
        element = Find_Element(driver, 5, locator2).click()
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(By.XPATH, locator3))
        print('999921||郑商所会服入金||已进入录入界面')
        isIn = True
    except BaseException as err:
        print('999931||郑商所会服入金||进入录入界面失败>>'+ str(err))

    # 开始入金操作
    if isIn:
        try:
            print('999921||郑商所会服入金||开始执行入金操作')
            element = Find_Element(driver, 5, locator3).click()
            element = Find_Element(driver, 5, locator4).click()
            element = Find_Element(driver, 5, locator5).click()
            element = Find_Element(driver, 5, bank).click()
            element = Find_Element(driver, 5, locator6).send_keys(fund)
            element = Find_Element(driver, 5, locator7).click()
            WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(By.XPATH, locator8))
            print('999921||郑商所会服入金||入金操作成功！')
        except BaseException as err:
            print('999931||郑商所会服入金||入金操作失败>>'+str(err)+'\n请人工介入！')
    else:
        print('999931||郑商所会服入金||请人工介入！')
