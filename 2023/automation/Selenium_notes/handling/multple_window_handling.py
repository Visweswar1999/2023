import time

import selenium

import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://www.w3schools.com/")

driver.maximize_window()


driver.find_element(By.XPATH,"//a[contains(text(),'Pro')]").click()



