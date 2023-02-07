# import time
#
# import selenium
#
# from selenium import webdriver
#
# from selenium.webdriver.common.by import By
#
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
#
# # we can select the options through
#
# #b.select_by_visible_text("Performance Testing")
#
# # b.select_by_index(1)
#
# # capture all the options and print them in console
#
# abc = b.options
#
# for i in abc:
#     print(i.text)
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
# driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
#
# a = driver.find_element(By.XPATH,"//select[@id='first']")
#
# abc = Select(a)
#
# abc.select_by_index(3)
#
# time.sleep(3)
import time

import  selenium

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")

abc = driver.find_element(By.XPATH,"//select[@class = 'col-lg-3' and @id ='first']")

a = Select(abc)

#a.select_by_index(3)

a.select_by_value("Yahoo")

print(driver.title)

time.sleep(3)


















