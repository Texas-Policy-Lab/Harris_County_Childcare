from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

"""
Launch driver
:param: pth string. Default is "driver/chromedriver.exe"
"""
def launch_driver(pth = "driver/chromedriver.exe"):
    return webdriver.Chrome(executable_path=pth)

"""
Navigate page
:param: driver object. Created by the launch_driver function.
:param: url string. Navigates to the given path.
"""
def navigate_page(driver, url):
    driver.get(url)

"""
Accept cookie agreement
:param: driver object. Driver object created by the launch_driver function.
:param: css_selector string. Selector to click to accept cookies. Default is "#hs-eu-confirmation-button"
"""
def accept_cookie(driver, css_selector = "#hs-eu-confirmation-button"):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, css_selector))).click()

"""
Navigate to the home page
:param: driver object. Created by the launch_driver function.
:param: css_selector string. Selector to click to click on image at top-left. Default is ".v-toolbar__content > a"
"""
def nav_home(driver, css_selector = ".v-toolbar__content > a"):
    
    driver.find_element_by_css_selector(css_selector).click()

"""
Selenium webdriver class
"""
class swebdriver(object):
    def __init__(self, url):
        self.url = url
        self.driver = launch_driver()
        navigate_page(self.driver, self.url)
        self.current_url = self.driver.current_url
        accept_cookie(self.driver)
        nav_home(self.driver)
