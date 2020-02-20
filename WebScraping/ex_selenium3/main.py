from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time

chromedriver = "C:\\Download\\chromedriver\\chromedriver.exe"  # ex. C:/downloads/chromedriver.exe
driver = webdriver.Chrome(chromedriver)
driver.get('https://news.v.daum.net/v/20200220232918379')

loop, count = True, 0

while loop and count < 10:
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#alex-area > div > div > div > div.cmt_box > div.alex_more > a'))
        )
        more_button = driver.find_element_by_css_selector('#alex-area > div > div > div > div.cmt_box > div.alex_more > a')
        webdriver.ActionChains(driver).click(more_button).perform()
        count += 1
        time.sleep(2)
    except TimeoutException:
        loop = False

comment_box = driver.find_element_by_css_selector('#alex-area > div > div > div > div.cmt_box > ul.list_comment')
comment_list = comment_box.find_elements_by_tag_name('li')

for num, comment_item in enumerate(comment_list):
    print("[" , str(num+1), "]", comment_item.find_element_by_css_selector('div p').text)


driver.quit()