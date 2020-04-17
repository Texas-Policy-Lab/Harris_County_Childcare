from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

"""
Launch driver
"""
def launch_driver(pth = "driver/chromedriver.exe"):
    return webdriver.Chrome(executable_path=pth)

"""
Navigate page
"""
def navigate_page(pth):
    driver.get(pth)

"""
Selenium webdriver class
"""
class swebdriver():
    def __init__(self):
        self.driver = launch_driver()