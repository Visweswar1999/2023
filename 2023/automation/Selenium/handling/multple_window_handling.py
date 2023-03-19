# import time
#
# import selenium
#
# from selenium import webdriver
#
# from selenium.webdriver.common.by import By
#
# from selenium.webdriver.common.window import WindowTypes
#
# driver = webdriver.Chrome()
#
# driver.get("https://phptravels.com/demo/")
#
# print(driver.current_window_handle)
#
# driver.find_element(By.XPATH,"//a[@class = 'jfHeader-menuListLink jfHeader-dynamicLink jfHeader-login-action login btn-outline-white']").click()
# #
# print(driver.current_window_handle)
import time

# a = driver.window_handles
#
#
# for i in a:
#     driver.switch_to.window(i)
#     print(driver.title)
#     time.sleep(5)

import selenium

import  time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://phptravels.com/demo/")

time.sleep(2)
driver.maximize_window()

locate = driver.find_element(By.XPATH,"//a[@class = 'jfHeader-menuListLink jfHeader-dynamicLink jfHeader-signup-action signup  btn-outline-dark']")

time.sleep(5)

locate.click()

time.sleep(5)

# print(driver.current_window_handle)

time.sleep(5)

multiple = driver.window_handles

#

for i in multiple:
    # driver.switch_to.window(i)
    print(driver.title)
    time.sleep(30)






