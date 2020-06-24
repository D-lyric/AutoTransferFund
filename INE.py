"""
能源中心

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
def login(driver, username, passwd):
    # 页面定位元素
    locator1 = 'input#formUserName'  # 用户名
    locator2 = 'input#formPassword'  # 密码
    locator3 = 'input#imageCheck'  # 验证码输入框
    # locator4 = 'img[alt="看不清，换一张"]'  # 验证码刷新按钮
    locator5 = '//td[./img[@src="images/login.gif"]]'  # 登陆按钮
    locator6 = '//td[text()="电子出入金"]'  # 电子出入金

    # 开始登陆
    islogin = False
    try:
        # 打开能源中心网站
        driver.get('https://42.24.1.245/')
        driver.maximize_window()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a#overridelink')))
        element = Find_Element(driver, 4, 'a#overridelink').click()
        element = Find_Element(driver, 4, 'a#overridelink').click()
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator1)))
        print('999921||能源中心会服系统登陆||已打开能源中心会服系统登陆界面，开始执行登陆操作')
    except BaseException as err:
        print('999931||能源中心会服系统登陆||能源中心会服系统连接服务器超时>>' + str(err) + '\n请人工介入！')

    i = 0
    while i < 10:
        # 输入用户名、密码
        element = Find_Element(driver, 4, locator1).send_keys(username)
        element = Find_Element(driver, 4, locator2).send_keys(passwd)
        # 输入图片验证码
        # element = Find_Element(driver, 4, locator4).click()
        vercode = getValidationCode.getCodeStr(driver)
        element = Find_Element(driver, 4, locator3)
        element.clear()
        element.send_keys(vercode)
        # time.sleep(5)
        element = Find_Element(driver, 5, locator5).click()
        # 验证是否登录成功
        try:
            WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, locator6)))
            print('999921||能源中心会服系统登陆||能源中心会服系统登陆成功！')
            islogin = True
            break
        except BaseException as err:
            print('999921||能源中心会服系统登陆||能源中心回复系统登陆失败，将在3秒后进行第{}次重试'.format(i + 1))
            i += 1
            time.sleep(3)
    else:
        print('999931||能源中心会服系统登陆||能源中心回复系统登陆失败，请人工介入')

    return islogin


# 资金划拨
def transferfund(driver, bank, fund, bank_card):
    # 页面定位元素
    locator1 = '//td[text()="电子出入金"]'  # 电子出入金
    locator2 = '//td[text()="出入金申请"]'  # 出入金申请
    locator3 = '//td[text()="出入金申请制单"]'  # 出入金申请制单
    locator4 = 'button#btnAddDW'  # 新建
    locator5 = 'input#dwForm_editor_certNo'  # 单据号
    locator6 = 'input#dwForm_editor_accountID'  # 资金账户下拉框
    locator7 = 'div[title="{}"]'.format("82590101(CNY)")  # 02590101(CNY)选项
    locator8 = 'input#dwForm_editor_bankID'  # 银行名称下拉框
    locator9 = 'input#dwForm_editor_zjTypeID'  # 资金用途下拉框
    locator10 = 'div[title="{}"]'.format("批准划转款")  # 批准划转款选项,暂不需要
    locator11 = 'input#dwForm_editor_DWDirection'  # 方向下拉框
    locator12 = 'div[title="{}"]'.format("入金")  # 入金选项
    locator13 = 'input#dwForm_editor_applyAmt'  # 金额
    locator14 = 'input#isAgree'  # 勾选框
    locator15 = 'button#btnConfirm'  # 确定
    locator16 = ''  # 入金成功确认
    locator17 = 'input#dwForm_editor_bankAccount' # 银行账号下拉框

    isIn = False
    try:
        # 进入出入金申请制单界面
        element = Find_Element(driver, 5, locator1).click()
        time.sleep(1)
        element = Find_Element(driver, 5, locator2).click()
        time.sleep(1)
        element = Find_Element(driver, 5, locator3).click()
        time.sleep(3)
        driver.switch_to.frame("mainframe")
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator4)))
        isIn = True
        print('999921||能源中心会服入金||已进入能源中心出入金申请制单界面')
    except BaseException as err:
        print('999921||能源中心会服入金||进入能源中心出入金申请制单界面失败>>' + str(err))
        # driver.quit()

    # 开始入金操作
    if isIn:
        try:
            print('999921||能源中心会服入金||开始能源中心入金操作')
            element = Find_Element(driver, 4, locator4).click()
            WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator5)))
            docno = ''  # 需确认docno（单据号）的获取方式
            element = Find_Element(driver, 4, locator5).send_keys(docno)
            element = Find_Element(driver, 4, locator6).click()
            element = Find_Element(driver, 4, locator7).click()
            element = Find_Element(driver, 4, locator8).click()
            element = Find_Element(driver, 4, 'div[title="{}"]'.format(bank)).click()
            element = Find_Element(driver, 4, locator17).click()
            element = Find_Element(driver, 4, 'div[title="{}"]'.format(bank_card[bank])).click()
            element = Find_Element(driver, 4, locator9).click()
            element = Find_Element(driver, 4, locator10).click()
            element = Find_Element(driver, 4, locator11).click()
            element = Find_Element(driver, 4, locator12).click()
            element = Find_Element(driver, 4, locator13).send_keys(fund)
            element = Find_Element(driver, 4, locator14).click()
            # element = Find_Element(driver, 4, locator15).click()
            # WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, locator16)))
            print('999921||能源中心会服入金||能源中心入金操作成功')
            # driver.quit()
        except BaseException as err:
            print('999931||能源中心会服系统登陆||能源中心入金操作失败>>' + str(err) + '\n请人工介入！')
    else:
        print('999931||能源中心会服入金||请人工介入！')
        # driver.quit()


import os

if __name__ == "__main__":
    """
    :param username: 用户名
    :param passwd: 密码
    :param bank: 银行
    :param bank_card: 银行和卡号对应字典
    :param fund: 入金金额
    """
    bank_card = {'工商银行': '1001190709004666310(CNY)',
                 '交通银行': '310899991010008485318(CNY)',
                 '建设银行': '31001559100059010259(CNY)',
                 '中国银行': '458540782597(CNY)',
                 '农业银行': '03427900046682597(CNY)',
                 '民生银行': '609836188(CNY)'}

    username = 'm8259'
    passwd = '111111'
    bank = '工商银行'
    fund = '123456'
    driver = IEdriverbrowser()
    islogin = login(driver, username, passwd)
    print(islogin)
    # if islogin:
    #     transferfund(driver, bank, fund, bank_card)

    # driver.get('https://42.24.1.245/')
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a#overridelink')))
    # element = Find_Element(driver, 4, 'a#overridelink').click()
    # element = Find_Element(driver, 4, 'a#overridelink').click()
    # element = Find_Element(driver, 4, 'img[alt="看不清，换一张"]').click()
    # element = Find_Element(driver, 5, '//td[./img[@src="images/login.gif"]]').click()
