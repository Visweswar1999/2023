import selenium

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com/")

driver.find_element(By.XPATH,"//input[@class='gLFyf']").send_keys("tata")



