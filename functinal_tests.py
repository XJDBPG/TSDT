import time

from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'Django' in browser.page_source
time.sleep(10)  # 在这里等待10秒钟

browser.quit()  # 手动关闭浏览器