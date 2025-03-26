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

    # Apply filters for style, size, price, color, and material
    def test_02_apply_filters(self):
        driver = self.driver

        # Click on Style, but wait till it's clickable
        style = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.filter-options-item:nth-child(1) > div:nth-child(1)")))
        driver.execute_script("arguments[0].click();", style) # Using javascript to force open the dropdown for style
        # Select pullover, from the drop menu
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.filter-options-item:nth-child(1) > div:nth-child(2) > ol:nth-child(1) > li:nth-child(3) > a:nth-child(1)"))).click()

        # Click on size, but wait till it's clickable
        size = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.filter-options-item:nth-child(1) > div:nth-child(1)")))
        driver.execute_script("arguments[0].click();", size) # Using javascript to force open the dropdown for size
        # Select medium, from the drop menu
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.filter-options-item:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(3) > div:nth-child(1)"))).click()

        # Click on price, but wait till it's clickable
        price = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.filter-options-item:nth-child(9) > div:nth-child(1)")))
        driver.execute_script("arguments[0].click();", price) # Using javascript to force open the dropdown for price
        # Select $50.00 - $59.99, from the drop menu
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.filter-options-item:nth-child(9) > div:nth-child(2) > ol:nth-child(1) > li:nth-child(3) > a:nth-child(1)"))).click()
        # Click on color, but wait till it's clickable
        color = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.filter-options-item:nth-child(2) > div:nth-child(1)")))
        driver.execute_script("arguments[0].click();", color) # Using javascript to force open the dropdown for color
        # Select purple, from the drop menu
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.swatch-option-link-layered:nth-child(4) > div:nth-child(1)"))).click()

        # Click on material, but wait till it's clickable
        material = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.filter-options-item:nth-child(4) > div:nth-child(1)")))
        driver.execute_script("arguments[0].click();", material) # Using material to force open the dropdown for color
        # Select purple, from the drop menu
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.filter-options-item:nth-child(4) > div:nth-child(2) > ol:nth-child(1) > li:nth-child(3) > a:nth-child(1)"))).click()
