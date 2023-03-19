# ID
import time

# Name

# class

# class name

# by tag name

# by link text

# by partial link text

# import selenium
#
# from selenium import webdriver
#
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()

# driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_6b31gegj9g_e&adgrpid=60612964962&hvpone=&hvptwo=&hvadid=486380734071&hvpos=&hvnetw=g&hvrand=17942702572563435787&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007768&hvtargid=kwd-49491430&hydadcr=14454_2154375&gclid=EAIaIQobChMIn-DvhN--_QIVR-R3Ch0FjAb0EAAYASAAEgLrXfD_BwE")
#
# time.sleep(3)
# #contains
# driver.find_element(By.PARTIAL_LINK_TEXT,"Sell").click()
#
# print(driver.title)
#
# # time.sleep(10)
#
# driver.get("https://login.mailchimp.com/signup/")
#
# time.sleep(3)
#
# driver.find_element(By.CLASS_NAME,"fs-exclude rounded-corners-4  av-text invalid").send_keys("kiran")
#
# time.sleep(5)



import selenium

import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://accounts.google.com/signup/v2/webcreateaccount?biz=false&cc=IN&dsh=S2031083605%3A1678155897431537&flowEntry=SignUp&flowName=GlifWebSignIn&ifkv=AWnogHcKDDkwH0WvnHOjhVLIYzj3NExaBTWJCIhUj1VCpxbH0tcca0DjM40FjU9Rm7sIK9zJMNi_")

driver.maximize_window()

driver.find_element(By.NAME,'firstName').send_keys("kiran")

time.sleep(100)

















