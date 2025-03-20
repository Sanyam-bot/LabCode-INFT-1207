# Name: Sanyam Singh Sachdeva (100963204) and Anchalpreet Kaur (100960062)
# Date: March 20, 2025
# Description: Using selenium Python API to automate a shopping workflow on the Magento e-commerce platform.

import unittest
from selenium import webdriver

class TestMagnetoWebsite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the WebDriver instance before running any tests."""
        cls.driver = webdriver.Firefox() # Creating a firefox driver object
        cls.driver.maximize_window()
        cls.driver.get("https://magento.softwaretestingboard.com/") # Tells the browser to go specific website

    @classmethod
    def tearDownClass(cls):
        """Quit the WebDriver instance after all tests."""
        cls.driver.quit()
