import selenium

import time

from  selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://www.google.com/")

search_bar =driver.find_element(By.XPATH,"//input[@class = 'gLFyf']")

search_bar.send_keys()

selecting = Select(search_bar)

selecting.select_by_index(1)

time.sleep(2)



