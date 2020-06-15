"""

上海期货交易所

"""
from selenium import webdriver

# IEdriver(忽略安全提示)
def IEbrowserdriver():
    capabilities = webdriver.DesiredCapabilities().INTERNETEXPLORER
    capabilities['acceptSslCerts'] = True
    driver = webdriver.Ie(capabilities=capabilities)
    return driver


# 登录
def login():
    pass


if __name__ == "__main__":
    driver = IEbrowserdriver()