from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = "C:\\Download\\chromedriver\\chromedriver.exe"  # ex. C:/downloads/chromedriver.exe

# 조금만 기다리면 selenium으로 제어할 수 있는 브라우저 새창이 뜬다
# driver = webdriver.Chrome(path)


headless_options = webdriver.ChromeOptions()
headless_options.add_argument('headless')
headless_options.add_argument('window-size=1920x1080')
headless_options.add_argument('disable-gpu') # 그래픽카드를 쓰지 않겠다
headless_options.add_argument('lang=ko_KR')
driver = webdriver.Chrome(path, options=headless_options)

driver.get('http://www.python.org')

assert "Python" in driver.title         ## Titile에 Python 단어가 없으면 에러처리
print(driver.title)
print(driver.current_url)


elem = driver.find_element_by_name("q")

elem.clear()

elem.send_keys("python")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

time.sleep(3)

# h3s = driver.find_elements_by_tag_name("h3")
# for h3 in h3s:
#     print(h3.text)

data = driver.find_elements_by_css_selector("#content > div > section > form > ul > li > h3 > a")
for item in data:
    print(item.text)
# driver.quit()