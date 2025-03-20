# Name: Sanyam Singh Sachdeva (100963204) and Anchalpreet Kaur (100960062)
# Date: March 20, 2025
# Description: Using selenium Python API to automate a shopping workflow on the Magento e-commerce platform.

import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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

    def test_01_navigate_to_product_page(self):
        """Navigate to Women -> Tops -> Hoodies & Sweatshirts"""
        print("Navigating to Women -> Tops -> Hoodies & Sweatshirts")
        driver = self.driver
        # Click on Women, but wait till it's clickable
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Women"))).click()
        # Click on Tops, but wait till it's clickable
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Tops"))).click()
        time.sleep(5) # Implicitly wait for 5 seconds
        # Click on Category, but wait till it's clickable
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Category']"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Hoodies & Sweatshirts')]"))
        ).click()

