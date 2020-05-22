from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pdb


def main():
    # pdb.set_trace()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('window-size=1200,1100')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36")
    browser = webdriver.Chrome(chrome_options = chrome_options,executable_path = '/mnt/c/Users/mytjx/Desktop/chromedriver')
    browser.get("https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F")

    try:
        username_element = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.ID,"loginName")))

    except Exception as e:
        print(e)
        print("try again")

    
    username_element = browser.find_element_by_id("loginName")
    username_element.send_keys("aaa")

    userpwd_element = browser.find_element_by_id("loginPassword")
    userpwd_element.send_keys("aaa")


    login_element = browser.find_element_by_id("loginAction")
    login_element.click()

    print(browser.page_source)

    time.sleep(30)



if __name__ == "__main__":
    main()