

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('./chromedriver.exe')
browser.get('https://naver.com')

tag_a_login = browser.find_element(By.CSS_SELECTOR, '#account > a')
tag_a_login.click()

tag_input_id = browser.find_element(By.CSS_SELECTOR, '#id')
tag_input_pw = browser.find_element(By.CSS_SELECTOR, '#pw')

tag_input_id.send_keys('abcd')
tag_input_pw.send_keys('1234')

tag_input_login = browser.find_element(By.CSS_SELECTOR, '#log\.login')
tag_input_login.click()

