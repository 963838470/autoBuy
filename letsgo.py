# -*- encoding:utf-8 -*-
import time
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

BAG_URL = 'https://pet-chain.baidu.com/chain/personal'
IGNORE_DOGS = ['11064331', '17484745']

if __name__ == "__main__":
    browser = webdriver.Chrome()  # 打开浏览器
    browser.get(BAG_URL)    # 跳转仓库页
    time.sleep(1)

    login_btn = browser.find_elements_by_css_selector('.go-login')
    login_btn[0].click()
    time.sleep(1)
    browser.switch_to.frame('iframeResult')

    pass_link = browser.find_elements_by_css_selector('.pass-link')
    pass_link[0].click()
    time.sleep(1)

    userName = browser.find_elements_by_css_selector(
        '.pass-text-input-userName')
    userName[0].send_keys("963838470")
    password = browser.find_elements_by_css_selector(
        '.pass-text-input-password')
    password[0].send_keys("")
    submit = browser.find_elements_by_css_selector(
        '.pass-button pass-button-submit')
    submit[0].click()
    time.sleep(3)
    browser.switch_to.parent_frame()

    while True:
        time.sleep(3)
        all_dog = browser.find_elements_by_css_selector('.dog-wrapper .dog dl')
        if len(all_dog) > 0:
            for dog in all_dog:
                num = dog.find_elements_by_css_selector(
                    "h3 span:nth-child(2)")
                price = dog.find_elements_by_css_selector(".price span")
                if num[0].text not in IGNORE_DOGS and len(price) == 0:
                    rare = dog.find_elements_by_css_selector(".rare")
                    price = 5000
                    if rare[0].text == "稀有":
                        price = 1200
                    img = browser.find_element_by_class_name('img')
                    dog[0].click()
                    img[0].click()
            # break
