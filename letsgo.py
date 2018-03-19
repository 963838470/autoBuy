# -*- encoding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from threading import Thread

BAG_URL = 'https://pet-chain.baidu.com/chain/personal'
IGNORE_DOGS = []

if __name__ == "__main__":
    browser = webdriver.Chrome()  # 打开浏览器

    while True:
    time.sleep(3)
    if LOGIN_SUCCESS_CONFIRM == driver.current_url:  # 手动登陆后跳转网页网址正确，退出死循环
        browser.get(BAG_URL)  # 打开背包
        print(user + '登录成功！')
        break

    all_dog = browser.find_elements_by_css_selector('.dog-wrapper .dog dl')
    for dog in all_dog:
        print(dog)
