import time

import selenium

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.wikipedia.org/")

driver.execute_script("window.ScroollTo(0,y)")

time.sleep(10)