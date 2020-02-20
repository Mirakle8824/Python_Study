from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = "C:\\Download\\chromedriver\\chromedriver.exe"  # ex. C:/downloads/chromedriver.exe
# driver = webdriver.Chrome(path)


headless_options = webdriver.ChromeOptions()
headless_options.add_argument('headless')
headless_options.add_argument('window-size=1920x1080')
headless_options.add_argument('disable-gpu') # 그래픽카드를 쓰지 않겠다
headless_options.add_argument('lang=ko_KR')
driver = webdriver.Chrome(path, options=headless_options)

# driver.get('https://news.v.daum.net/v/20170202185812986')

# elem = driver.find_element_by_tag_name('h3')
# print(elem.text)

# elem = driver.find_element_by_class_name('tit_view')
# print(elem.text)

# titles = driver.find_elements_by_tag_name('h3')
# # for title in titles:
# #     print(title.text)

# elem = driver.find_element_by_id('harmonyContainer')

# elem = driver.find_element_by_css_selector('h3.tit_view')
# print(elem.text)

# head_title = driver.find_element_by_css_selector('head > title')
# print(head_title.get_attribute('text'), ":", head_title.text)

#
# driver.get('https://news.v.daum.net/v/20170202180355822')
# head_title = driver.find_element_by_css_selector("div[role='navigation']")
# print(head_title.get_attribute('text'), ":", head_title.text)

######## Twitter 로그인
driver.get('https://twitter.com/')
id_field = driver.find_element_by_name("session[username_or_email]")
id_field.clear()
id_field.send_keys('-')
pw_field = driver.find_element_by_name("session[password]")
pw_field.clear()
pw_field.send_keys('-')
pw_field.send_keys(Keys.RETURN)

time.sleep(2)
#
# data = driver.find_element_by_css_selector('div.content')
# for item in data:
#     print(item.text)


driver.quit()