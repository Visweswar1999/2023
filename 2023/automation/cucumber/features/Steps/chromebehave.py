import behave

import selenium

from selenium import webdriver

from behave import *

@given('lauch the chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()




