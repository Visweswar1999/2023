import time

import selenium

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

# driver.implicitly_wait(10)

driver.get(
    "https://accounts.google.com/signup/v2/webcreateaccount?biz=false&cc=IN&continue=https%3A%2F%2Fmail.google.com&dsh=S-66111987%3A1675688435387778&flowEntry=SignUp&flowName=GlifWebSignIn&hl=en&service=mail&authuser=0")

# a = driver.find_element(By.XPATH,"//input[@id = 'male']")

time.sleep(10)

