import re
from selenium import webdriver

url = 'http://www.ncbi.nlm.nih.gov/pubmed/17708774'

driver = webdriver.PhantomJS()
driver.get(url)

html = driver.page_source
matched = re.search(r'Cited by (\d+) PubMed Central articles', html)
if matched:
    print(matched.group(1))
else:
    print('not found')

driver.close()