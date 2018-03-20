# -*- encoding:utf-8 -*-
import time
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

BAG_URL = 'https://pet-chain.baidu.com/chain/personal'
IGNORE_DOGS = ['11064331', '17484745']

if __name__ == "__main__":
    browser = webdriver.Chrome()  # 打开浏览器
    # browser.set_page_load_timeout(10)  # 页面加载时的超时时间
    # browser.set_script_timeout(10)  # 异步脚本的超时时间
    browser.implicitly_wait(3)  # 隐性等待时间

    # browser.get('https://pet-chain.baidu.com/chain/dogMarket')
    # js = "scrollTo(0,document.body.scrollHeight+10)"
    # browser.execute_script(js)
    # last = browser.find_element_by_css_selector(
    #     ".dog-wrapper > .dog:last-child")
    # last.mouseMoveAt(10, 20)

    browser.get(BAG_URL)    # 跳转仓库页
    # time.sleep(1)

    login_btn = browser.find_element_by_css_selector('.go-login')
    login_btn.click()
    # time.sleep(1)

    pass_link = browser.find_element_by_css_selector(
        '.tang-pass-footerBarULogin')
    pass_link.click()
    # time.sleep(1)

    userName = browser.find_element_by_css_selector(
        '.pass-text-input-userName')
    userName.send_keys("18855951969")
    password = browser.find_element_by_css_selector(
        '.pass-text-input-password')
    password.send_keys("")
    submit = browser.find_element_by_css_selector('.pass-button-submit')
    submit.click()
    # time.sleep(1)

    while True:
        all_dog = browser.find_elements_by_css_selector('.dog-wrapper .dog dl')
        print('当前狗数量' + str(len(all_dog)))
        if len(all_dog) > 0:
            for dog in all_dog:
                num = dog.find_element_by_css_selector(
                    "h3 span:nth-child(2)")
                prices = dog.find_elements_by_css_selector(".price span")
                if num.text not in IGNORE_DOGS and len(prices) == 0:
                    rare = dog.find_element_by_css_selector(".rare")
                    price = 500000
                    # 等级分类: 普通、稀有、卓越、史诗、神话、传说
                    if rare.text == "普通":
                        price = 800
                    elif rare.text == "稀有":
                        price = 1200
                    elif rare.text == "卓越":
                        price = 1800
                    elif rare.text == "史诗":
                        price = 5000
                    elif rare.text == "神话":
                        price = 50000
                    else:
                        price = 500000
                    img = dog.find_element_by_css_selector('img')
                    img.click()
                    # time.sleep(1)

                    sold_btn = browser.find_element_by_css_selector('.button')
                    sold_btn.click()
                    # time.sleep(1)

                    price_input = browser.find_element_by_css_selector(
                        '.mint-msgbox-input > input')
                    price_input.send_keys(price)
                    confirm_btn = browser.find_element_by_css_selector(
                        '.detail-sale-sure')
                    confirm_btn.click()
                    # time.sleep(1)
                    break
        time.sleep(3)
