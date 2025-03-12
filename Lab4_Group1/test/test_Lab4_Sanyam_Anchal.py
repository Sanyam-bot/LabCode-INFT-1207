# Name: Sanyam Singh Sachdeva (100963204) and Anchalpreet Kaur (100960062)
# Name of the program: Body Fat Calculator test
# Date: Mar 11, 2025
# Description: Automated test cases for Body Fat Calculator

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

GENDER = "male"

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


    def test_with_valid_inputs(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs

        if GENDER == "female":
            self.driver.find_element(By.CSS_SELECTOR,".cbcontainer:nth-child(2) > .rbmark").click()  # Select the female radio button
        else:
            self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()  # Select the male radio button

        self._fill_common_fields("24", "70", "170", "50", "100")

        if GENDER == "female":
            self._fill_female_specific_fields("98")

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        result_text = self.driver.find_element(By.CSS_SELECTOR, "font > b").text
        if GENDER == "female":
            assert result_text == "Body Fat: 31.0%"
        else:
            assert result_text == "Body Fat: 20.1%"
        print(f"{GENDER.capitalize()} Test Case Result: {result_text}")

    def test_with_all_invalid_inputs(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs
        if GENDER == "female":
            self.driver.find_element(By.CSS_SELECTOR,".cbcontainer:nth-child(2) > .rbmark").click()  # Select the female radio button
        else:
            self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()  # Select the male radio button

        self._fill_common_fields("twenty four", "seventy", "hundred", "ninety", "sixty")

        if GENDER == "female":
            self._fill_female_specific_fields("fifty")

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        age_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Please provide a positive age.')]")
        weight_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Please provide a positive weight.')]")
        height_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Height need to be positive.')]")
        neck_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Neck need to be numeric.')]")
        waist_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Waist need to be numeric.')]")
        if GENDER == "female":
            hip_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Hip need to be numeric.')]")

        assert age_error_message.text == "Please provide a positive age."
        print(f"{GENDER.capitalize()} Test Case Result Age Error: {age_error_message.text}")
        assert weight_error_message.text == "Please provide a positive weight."
        print(f"{GENDER.capitalize()} Test Case Result Weight Error: {weight_error_message.text}")
        assert height_error_message.text == "Height need to be positive."
        print(f"{GENDER.capitalize()} Test Case Result Height Error: {height_error_message.text}")
        assert neck_error_message.text == "Neck need to be numeric."
        print(f"{GENDER.capitalize()} Test Case Result Neck Error: {neck_error_message.text}")
        assert waist_error_message.text == "Waist need to be numeric."
        print(f"{GENDER.capitalize()} Test Case Result Waist Error: {waist_error_message.text}")
        if GENDER == "female":
            assert hip_error_message.text == "Hip need to be numeric."
            print(f"{GENDER.capitalize()} Test Case Result Waist Error: {waist_error_message.text}")

    def test_with_empty_age(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs

        if GENDER == "female":
            self.driver.find_element(By.CSS_SELECTOR,".cbcontainer:nth-child(2) > .rbmark").click()  # Select the female radio button
        else:
            self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()  # Select the male radio button

        self._fill_common_fields("", "70", "170", "50", "100")

        if GENDER == "female":
            self._fill_female_specific_fields("98")

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        age_error_message = self.driver.find_element(By.XPATH,"//font[contains(text(), 'Please provide a positive age.')]")

        assert age_error_message.text == "Please provide a positive age."
        print(f"{GENDER.capitalize()} Test Case With Empty Age Error: {age_error_message.text}")

    def test_with_empty_weight(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs

        if GENDER == "female":
            self.driver.find_element(By.CSS_SELECTOR,".cbcontainer:nth-child(2) > .rbmark").click()  # Select the female radio button
        else:
            self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()  # Select the male radio button

        self._fill_common_fields("50", "", "170", "50", "100")

        if GENDER == "female":
            self._fill_female_specific_fields("98")

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        weight_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Please provide a positive weight.')]")

        assert weight_error_message.text == "Please provide a positive weight."
        print(f"{GENDER.capitalize()} Test Case Result Weight Error: {weight_error_message.text}")

    def test_with_empty_height(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs

        if GENDER == "female":
            self.driver.find_element(By.CSS_SELECTOR,".cbcontainer:nth-child(2) > .rbmark").click()  # Select the female radio button
        else:
            self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()  # Select the male radio button

        self._fill_common_fields("50", "70", "", "50", "100")

        if GENDER == "female":
            self._fill_female_specific_fields("98")

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        height_error_message = self.driver.find_element(By.XPATH,"//font[contains(text(), 'Height need to be positive.')]")

        assert height_error_message.text == "Height need to be positive."
        print(f"{GENDER.capitalize()} Test Case With Empty Height Error: {height_error_message.text}")

    def test_with_empty_neck(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs

        if GENDER == "female":
            self.driver.find_element(By.CSS_SELECTOR,".cbcontainer:nth-child(2) > .rbmark").click()  # Select the female radio button
        else:
            self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()  # Select the male radio button

        self._fill_common_fields("50", "70", "170", "", "100")

        if GENDER == "female":
            self._fill_female_specific_fields("98")

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        neck_error_message = self.driver.find_element(By.XPATH,"//font[contains(text(), 'Neck need to be numeric.')]")

        assert neck_error_message.text == "Neck need to be numeric."
        print(f"{GENDER.capitalize()} Test Case With Empty Neck Error: {neck_error_message.text}")

    def test_with_empty_waist(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs

        if GENDER == "female":
            self.driver.find_element(By.CSS_SELECTOR,".cbcontainer:nth-child(2) > .rbmark").click()  # Select the female radio button
        else:
            self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()  # Select the male radio button

        self._fill_common_fields("50", "70", "170", "50", "")

        if GENDER == "female":
            self._fill_female_specific_fields("98")


        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        waist_error_message = self.driver.find_element(By.XPATH,"//font[contains(text(), 'Waist need to be numeric.')]")

        assert waist_error_message.text == "Waist need to be numeric."
        print(f"{GENDER.capitalize()} Test Case With Empty Waist Error: {waist_error_message.text}")

    @pytest.mark.skipif(GENDER != "female", reason="Test Case only applicable for female.")
    def test_with_empty_hip(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs

        self.driver.find_element(By.CSS_SELECTOR,".cbcontainer:nth-child(2) > .rbmark").click()  # Select the female radio button

        self._fill_common_fields("50", "70", "170", "50", "100")
        self._fill_female_specific_fields("")

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        hip_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Hip need to be numeric.')]")

        assert hip_error_message.text == "Hip need to be numeric."
        print(f"Female Test Case Result Hip Error: {hip_error_message.text}")