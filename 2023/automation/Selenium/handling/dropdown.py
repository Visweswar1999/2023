# import time
#
# import selenium
#
# from selenium import webdriver
#
# from selenium.webdriver.common.by import By
#
# from selenium.webdriver.support.ui import Select
#
# driver = webdriver.Chrome()
#
# driver.get("https://artoftesting.com/samplesiteforselenium")
#
# a = driver.find_element(By.ID,'testingDropdown')
#
# b = Select(a)
# import time
#
# # we can select the options through
#
# #b.select_by_visible_text("Performance Testing")
#
# # b.select_by_index(1)
#
# # capture all the options and print them in console
# #
# # abc = b.options
# #
# # for i in abc:
# #     print(i.text)
# # import time
# #
# # import selenium
# #
# # from selenium import webdriver
# #
# # from selenium.webdriver.common.by import By
# #
# # from selenium.webdriver.support.ui import Select
# #
# # driver = webdriver.Chrome()
# #
# # driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
# #
# # a = driver.find_element(By.XPATH,"//select[@id='first']")
# #
# # abc = Select(a)
# #
# # abc.select_by_index(3)
# #
# # time.sleep(3)
# # import time
# #
# # import  selenium
# #
# # from selenium import webdriver
# #
# # from selenium.webdriver.common.by import By
# #
# # from selenium.webdriver.support.ui import Select
# #
# # driver = webdriver.Chrome()
# #
# # driver.get("https://www.google.com/")
# #
# # print(driver.title)
#
# # abc = driver.find_element(By.XPATH,"//select[@class = 'col-lg-3' and @id ='first']")
#
# # a = Select(abc)
#
# # a.select_by_index(3)
#
# # a.select_by_value("Yahoo")
# #
# # print(driver.title)
# #
# # time.sleep(3)
#
#
# import selenium
#
# from selenium import webdriver
#
# from selenium.webdriver.common.by import By
#
# from selenium.webdriver.support.ui import Select
#
# driver = webdriver.Chrome()
#
# driver.get("https://artoftesting.com/samplesiteforselenium")
#
# driver.maximize_window()
#
# a = driver.find_element(By.ID,"testingDropdown")
#
# b = Select(a)
#
# b.select_by_value("Automation")
#
# time.sleep(5)
import time

import selenium

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(2)

finding_element = driver.find_element(By.XPATH,"//select[@id = 'speed']")

selecting_element = Select(finding_element)

time.sleep(2)

# selecting_element.select_by_index(3)

time.sleep(8)

result = selecting_element.options

for i in result:
    print(i.text)













