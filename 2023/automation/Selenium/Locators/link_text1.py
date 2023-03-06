import time

import selenium

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/")

driver.find_element(By.PARTIAL_LINK_TEXT,'A/B').click()

print(driver.title)

time.sleep(20)
