from selenium import webdriver
from selenium.webdriver.common.by import By

# dont forget about waits

chrome_browser = webdriver.Chrome()  # ./chrome_driver

chrome_browser.maximize_window()

button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
