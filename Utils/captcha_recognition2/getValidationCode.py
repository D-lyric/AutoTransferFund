# coding=utf-8
import test
import os
import time
from selenium import webdriver
from PIL import Image
from Utils.captcha_recognition2 import test
from INE import IEdriverbrowser




def getCodeStr(driver):
    # driver = IEdriverbrowser()
    '''
    读取验证码文件，生成验证码
    :param picPath:
    :return:
    '''
    picDir = os.path.abspath('.') + r'\Utils\captcha_recognition2\data'
    screenPicPath = picDir + r'\screen.png'              #屏幕截图路径
    codePicPath = picDir + r'\CSCA.png'     #验证码截图路径
    print(screenPicPath)
    print(codePicPath)
    #driver.maximize_window()
    isget = driver.get_screenshot_as_file(screenPicPath)

    if isget:
        locationStr = 'image'
        element = driver.find_element_by_id(locationStr)

        pagePic = Image.open(screenPicPath)  # 读取图片
        elementLocation = element.location  # 元素位置
        elementSize = element.size  # 元素尺寸
        x_start = elementLocation['x']
        y_start = elementLocation['y']
        x_end = x_start + elementSize['width']
        y_end = y_start + elementSize['height']
        elementPic = pagePic.crop((x_start, y_start, x_end, y_end))  # 截取元素图片
        if os.path.exists(codePicPath):
            os.remove(codePicPath)
        elementPic.save(codePicPath) #重写验证码图片

        if os.path.exists(screenPicPath):  #清除屏幕截图
            os.remove(screenPicPath)

        # 生成验证码字符串
        codeStr = test.test_model(use_gpu=False, verification=True, extend_format='png', folder=codePicPath)
        return codeStr
    else:
        print('未获取到屏幕截图')


