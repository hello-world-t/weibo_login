from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def main():
    browser = webdriver.Chrome('C:/Users/mytjx/Desktop/chromedriver.exe')

    browser.get("https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F")

    try:
        username_element = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.ID,"loginName")))

    except Exception as e:
        print(e)
        print("try again")


    username_element = browser.find_element_by_id("loginName")
    username_element.send_keys("aaa")

    userpwd_element = browser.find_element_by_id("loginPassword")
    userpwd_element.send_keys("bbb")


    login_element = browser.find_element_by_id("loginAction")
    login_element.click()

    time.sleep(30)



if __name__ == "__main__":
    main()