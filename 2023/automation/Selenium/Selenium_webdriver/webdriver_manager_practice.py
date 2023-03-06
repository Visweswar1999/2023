import selenium

from selenium import webdriver

import webdriver_manager

from webdriver_manager.chrome import ChromeDriverManager

from webdriver_manager.firefox import GeckoDriverManager

#to import the chrome driver

driver = webdriver.Chrome(ChromeDriverManager().install())

#to import the firefox browser

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())




