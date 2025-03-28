# Name: Sanyam Singh Sachdeva (100963204) and Anchalpreet Kaur (100960062)
# Date: March 20, 2025
# Description: Using selenium Python API to automate a shopping workflow on the Magento e-commerce platform.

import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
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

    def hover_element(self, element):
        """Performs a hover action on the given element."""
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def test_01_navigate_to_product_page(self):
        """Navigate to Women -> Tops -> Hoodies & Sweatshirts"""
        driver = self.driver

        # Find Women, then hover over it
        women = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ui-id-4")))
        self.hover_element(women)

        # Find tops under women, then hover over it
        tops = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ui-id-9")))
        self.hover_element(tops)

        # Find Hoodies and Sweatshirt under tops, then click on it
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ui-id-12"))).click()

        print("Test Case 1: Successfully navigated to Women -> Tops -> Hoodies & Sweatshirts.")

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
        driver.execute_script("arguments[0].click();", material) # Using javascript to force open the dropdown for material
        # Select polyester, from the drop menu
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.filter-options-item:nth-child(4) > div:nth-child(2) > ol:nth-child(1) > li:nth-child(3) > a:nth-child(1)"))).click()

        print("Test Case 2: Successfully applied filters to the products.")

    def test_03_selected_dress_to_cart(self):
        driver = self.driver

        # Get the first product after applying the filters
        first_product = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "li.product:nth-child(1)")
        ))
        # Hover over the first product
        self.hover_element(first_product)

        # Click on add to cart button, but wait for it to be clickable
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "li.product:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > button:nth-child(4)")
        )).click()

        print("Test Case 3: Successfully added selected dress to the cart.")

    def test_04_proceed_to_checkout(self):
        driver = self.driver

        # Wait until the item is successfully added to the cart
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".message-success > div:nth-child(1)")
        ))

        # Click on the cart button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".showcart")
        )).click()

        # Click on "proceed to checkout" button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#top-cart-btn-checkout")
        )).click()

        print("Test Case 4: Successfully proceeded to checkout.")

    def test_05_assert_order_summary(self):
        driver = self.driver

        # Wait for the checkout-loader element to disappear
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
            (By.ID, "checkout-loader")
        ))

        # Expand the order summary
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.title")
        )).click()

        # Expand item details
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "span.toggle")
        )).click()

        # Assert the order summary
        size_of_dress_cart = driver.find_element(By.CSS_SELECTOR, "dd.values:nth-child(2)")
        color_of_the_dress_cart = driver.find_element(By.CSS_SELECTOR, "dd.values:nth-child(4)")
        qty_of_the_dress_cart = driver.find_element(By.CSS_SELECTOR, ".value")

        assert size_of_dress_cart.text == "M"
        assert color_of_the_dress_cart.text == "Purple"
        assert qty_of_the_dress_cart.text == "1"

        print("Test Case 5: Order Summary has the selected dress.")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestMagnetoWebsite("test_01_navigate_to_product_page"))
    suite.addTest(TestMagnetoWebsite("test_02_apply_filters"))
    suite.addTest(TestMagnetoWebsite("test_03_selected_dress_to_cart"))
    suite.addTest(TestMagnetoWebsite("test_04_proceed_to_checkout"))
    suite.addTest(TestMagnetoWebsite("test_05_assert_order_summary"))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)