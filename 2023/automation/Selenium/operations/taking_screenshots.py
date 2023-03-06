# # import time
# #
# # import os
# #
# # import selenium
# #
# # # To change the cureent running path
# #
# # os.chdir("C:\\Users\\Hp\\Desktop\\vis")
# #
# # from selenium import webdriver
# #
# # driver = webdriver.Chrome()
# #
# # driver.get("https://www.google.com/")
# #
# # driver.save_screenshot("image.png")
# #
# # time.sleep(10)
#
#
#
#
import time

import selenium

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

time.sleep(3)

driver.find_element(By.XPATH,"//button[contains(text(),'Click Me')]")

time.sleep(3)

driver.switch_to.alert

time.sleep(2)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
