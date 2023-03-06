import time

import selenium

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://phptravels.com/demo/")

driver.find_element(By.XPATH,"//a[contains(text(),'Login') and @class ='jfHeader-menuListLink jfHeader-dynamicLink jfHeader-login-action login btn-outline-white']").click()

time.sleep(3)


