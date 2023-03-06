#webdriver manager
import time

import selenium

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

time.sleep(2)

driver = webdriver.Chrome(ChromeDriverManager().install())

time.sleep(5)

print(driver.title)

time.sleep(3)


