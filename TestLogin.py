import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://practicetestautomation.com/practice-test-login/")
username_field = browser.find_element(By.ID,"username")
time.sleep(3)
username_field.send_keys("student")
password_field = browser.find_element(By.ID,"password")
time.sleep(3)
password_field.send_keys("Password123")
login_button = browser.find_element(By.ID,"submit")
time.sleep(3)
login_button.click()
time.sleep(3)
browser.quit()
