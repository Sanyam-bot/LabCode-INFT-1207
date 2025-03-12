# Name: Sanyam Singh Sachdeva (100963204) and Anchalpreet Kaur (100960062)
# Name of the program: Body Fat Calculator test
# Date: Mar 11, 2025
# Description: Automated test cases for Body Fat Calculator

from selenium import webdriver
from selenium.webdriver.common.by import By

GENDER = "female"

class TestDefaultSuite:
    @classmethod
    def setup_class(cls):
        """Initializes a firefox web driver, and opens the website once before any test"""
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.vars = {}
        cls.driver.get("https://www.calculator.net/body-fat-calculator.html/body-fat-calculator.html")

    @classmethod
    def teardown_class(cls):
        """Quits the driver after all test ran."""
        cls.driver.quit()

    def _fill_common_fields(self, age, weight, height, neck, waist):
        self.driver.find_element(By.NAME, "cage").click()  # Age
        self.driver.find_element(By.NAME, "cage").send_keys(age)  # Send keys to Age
        self.driver.find_element(By.NAME, "cweightkgs").click()  # Weight
        self.driver.find_element(By.NAME, "cweightkgs").send_keys(weight)  # Send keys to Weight
        self.driver.find_element(By.ID, "cheightmeter").click()  # Height
        self.driver.find_element(By.ID, "cheightmeter").send_keys(height)  # Send keys to Height
        self.driver.find_element(By.ID, "cneckmeter").click()  # Neck
        self.driver.find_element(By.ID, "cneckmeter").send_keys(neck)  # Send keys to Neck
        self.driver.find_element(By.ID, "cwaistmeter").click()  # Waist
        self.driver.find_element(By.ID, "cwaistmeter").send_keys(waist)  # Send keys to Waist

    def _fill_female_specific_fields(self, hip):
        self.driver.find_element(By.ID, "chipmeter").click() # Hip
        self.driver.find_element(By.ID, "chipmeter").send_keys(hip) # Send keys to Hip

    def test_clear_btn(self):
        if GENDER == "female":
            self.driver.find_element(By.CSS_SELECTOR,".cbcontainer:nth-child(2) > .rbmark").click()  # Select the female radio button
        else:
            self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()  # Select the male radio button
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs
        age_value = self.driver.find_element(By.NAME, "cage").get_attribute("value")
        weight_value = self.driver.find_element(By.NAME, "cage").get_attribute("value")
        height_value = self.driver.find_element(By.NAME, "cage").get_attribute("value")
        neck_value = self.driver.find_element(By.NAME, "cage").get_attribute("value")
        waist_value = self.driver.find_element(By.NAME, "cage").get_attribute("value")
        if GENDER == "female":
            hip_value = self.driver.find_element(By.ID, "chipmeter").get_attribute("value")

        # Check If the values are empty
        assert age_value == ""
        assert weight_value == ""
        assert height_value == ""
        assert neck_value == ""
        assert waist_value == ""
        if GENDER == "female":
            assert hip_value == ""

        print(f"Clear Button Result: Clears the text fields.")


        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        waist_error_message = self.driver.find_element(By.XPATH,"//font[contains(text(), 'Waist need to be numeric.')]")

        assert waist_error_message.text == "Waist need to be numeric."
        print(f"Male Test Case With Empty Age Error: {waist_error_message.text}")

