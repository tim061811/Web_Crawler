"""
# 取得網頁標籤
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 讓網頁可以按按鍵
import time # 網頁延遲模組


PATH = "D:/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.dcard.tw/f")
search = driver.find_element_by_name("query")
search.send_keys("力積電")
search.send_keys(Keys.RETURN)
time.sleep(10)
titles = driver.find_elements_by_class_name("tgn9uw-3")
for title in titles:
    print(title.text)

time.sleep(5)
driver.quit()
"""
# ------------------------------------------------

# 爬取 IG 關鍵字圖片
from typing import Counter
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
# 讓網頁可以按按鍵

import time

# 下載
import os
import wget

PATH = "D:/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/?hl=zh-tw")

username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

login = driver.find_element('//*[@id="loginForm"]/div/div[3]/button')

username.clear()
password.clear()

username.send_keys()
password.send_keys()
login.click()


search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
    )

keyword = "#dog"
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "KL4Bh"))
    )

img = driver.find_element("KL4Bh")

path = os.path.join(keyword)
os.mkdir(path)
# 未完成
