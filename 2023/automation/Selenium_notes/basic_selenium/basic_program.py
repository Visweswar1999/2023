# xpath --> //input[@type='text']

import selenium

import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# driver.get("https://accounts.google.com/signup/v2/webcreateaccount?biz=false&cc=IN&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue%26pli%3D1&dsh=S-1878701436%3A1675079489964027&flowEntry=SignUp&flowName=GlifWebSignIn&hl=en&service=accountsettings&authuser=0")
#
# driver.find_element(By.ID,'firstName').send_keys("bhanu")
#
#
# driver.find_element(By.ID,'lastName').send_keys("prakash")

# driver.find_element(By.XPATH,"//input[@name='Passwd']").send_keys("name")
#
#
#
# driver.find_element(By.NAME,'ConfirmPasswd').send_keys('name')
#
# driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
#
# time.sleep(5)
#
# driver.find_element(By.XPATH,"//span[@jsname='V67aGc' and @class='c']").click()
#
# time.sleep(10)



driver.get("https://www.instagram.com/")

time.sleep(2)

driver.find_element(By.XPATH,"//input[@name='username']").send_keys("visweswar")

time.sleep(5)

driver.find_element(By.XPATH,"//input[@name='password']").send_keys("123")
time.sleep(5)

driver.find_element(By.XPATH,"//div[@class='_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p _abcm']").click()

time.sleep(10)











