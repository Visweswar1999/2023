import time

import selenium

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()
time.sleep(10)

# driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//button[contains(text(),'Click Me')]").click()
time.sleep(10)

# driver.implicitly_wait(5)

driver.switch_to.alert.dismiss()

time.sleep(15)

