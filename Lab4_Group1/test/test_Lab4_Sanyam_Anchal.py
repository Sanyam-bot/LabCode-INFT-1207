# Name: Sanyam Singh Sachdeva (100963204) and Anchalpreet Kaur (100960062)
# Name of the program: Body Fat Calculator test
# Date: Mar 11, 2025
# Description: Automated test cases for Body Fat Calculator

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDefaultSuite:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()