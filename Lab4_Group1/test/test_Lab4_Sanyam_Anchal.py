# Name: Sanyam Singh Sachdeva (100963204) and Anchalpreet Kaur (100960062)
# Name of the program: Body Fat Calculator test
# Date: Mar 11, 2025
# Description: Automated test cases for Body Fat Calculator

from selenium import webdriver
from selenium.webdriver.common.by import By


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

    def test_clear_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs
        age_value = self.driver.find_element(By.NAME, "cage").get_attribute("value")
        weight_value = self.driver.find_element(By.NAME, "cage").get_attribute("value")
        height_value = self.driver.find_element(By.NAME, "cage").get_attribute("value")
        neck_value = self.driver.find_element(By.NAME, "cage").get_attribute("value")
        waist_value = self.driver.find_element(By.NAME, "cage").get_attribute("value")

        # Check If the values are empty
        assert age_value == ""
        assert weight_value == ""
        assert height_value == ""
        assert neck_value == ""
        assert waist_value == ""

        print(f"Clear Button Result: Clears the text fields.")


    def test_male_valid(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs
        self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()  # Select the male radio button
        self.driver.find_element(By.NAME, "cage").click()  # Age
        self.driver.find_element(By.NAME, "cage").send_keys("24")  # Send keys to Age
        self.driver.find_element(By.NAME, "cweightkgs").click()  # Weight
        self.driver.find_element(By.NAME, "cweightkgs").send_keys("70")  # Send keys to Weight
        self.driver.find_element(By.ID, "cheightmeter").click()  # Height
        self.driver.find_element(By.ID, "cheightmeter").send_keys("170")  # Send keys to Height
        self.driver.find_element(By.ID, "cneckmeter").click()  # Neck
        self.driver.find_element(By.ID, "cneckmeter").send_keys("50")  # Send keys to Neck
        self.driver.find_element(By.ID, "cwaistmeter").click()  # Waist
        self.driver.find_element(By.ID, "cwaistmeter").send_keys("100")  # Send keys to Waist

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        result_text = self.driver.find_element(By.CSS_SELECTOR, "font > b").text
        assert result_text == "Body Fat: 20.1%"
        print(f"Male Test Case Result: {result_text}")

    def test_male_all_invalid_type(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs
        self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()  # Select the male radio button
        self.driver.find_element(By.NAME, "cage").click()  # Age
        self.driver.find_element(By.NAME, "cage").send_keys("twenty four")  # Send keys to Age
        self.driver.find_element(By.NAME, "cweightkgs").click()  # Weight
        self.driver.find_element(By.NAME, "cweightkgs").send_keys("seventy")  # Send keys to Weight
        self.driver.find_element(By.ID, "cheightmeter").click()  # Height
        self.driver.find_element(By.ID, "cheightmeter").send_keys("one seventy")  # Send keys to Height
        self.driver.find_element(By.ID, "cneckmeter").click()  # Neck
        self.driver.find_element(By.ID, "cneckmeter").send_keys("fifty")  # Send keys to Neck
        self.driver.find_element(By.ID, "cwaistmeter").click()  # Waist
        self.driver.find_element(By.ID, "cwaistmeter").send_keys("hundred")  # Send keys to Waist

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        age_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Please provide a positive age.')]")
        weight_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Please provide a positive weight.')]")
        height_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Height need to be positive.')]")
        neck_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Neck need to be numeric.')]")
        waist_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Waist need to be numeric.')]")

        assert age_error_message.text == "Please provide a positive age."
        assert weight_error_message.text == "Please provide a positive weight."
        assert height_error_message.text == "Height need to be positive."
        assert neck_error_message.text == "Neck need to be numeric."
        assert waist_error_message.text == "Waist need to be numeric."
        print(f"Male Test Case Result Age Error: {age_error_message.text}")
        print(f"Male Test Case Result Weight Error: {weight_error_message.text}")
        print(f"Male Test Case Result Height Error: {height_error_message.text}")
        print(f"Male Test Case Result Neck Error: {neck_error_message.text}")
        print(f"Male Test Case Result Waist Error: {waist_error_message.text}")

    def test_male_empty_age(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs
        self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()  # Select the male radio button
        self.driver.find_element(By.NAME, "cweightkgs").click()  # Weight
        self.driver.find_element(By.NAME, "cweightkgs").send_keys("80")  # Send keys to Weight
        self.driver.find_element(By.ID, "cheightmeter").click()  # Height
        self.driver.find_element(By.ID, "cheightmeter").send_keys("110")  # Send keys to Height
        self.driver.find_element(By.ID, "cneckmeter").click()  # Neck
        self.driver.find_element(By.ID, "cneckmeter").send_keys("60")  # Send keys to Neck
        self.driver.find_element(By.ID, "cwaistmeter").click()  # Waist
        self.driver.find_element(By.ID, "cwaistmeter").send_keys("140")  # Send keys to Waist

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        age_error_message = self.driver.find_element(By.XPATH,"//font[contains(text(), 'Please provide a positive age.')]")

        assert age_error_message.text == "Please provide a positive age."
        print(f"Male Test Case With Empty Age Error: {age_error_message.text}")

    def test_male_empty_weight(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs
        self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()  # Select the male radio button
        self.driver.find_element(By.NAME, "cage").click()  # Age
        self.driver.find_element(By.NAME, "cage").send_keys("24")  # Send keys to Age
        self.driver.find_element(By.ID, "cheightmeter").click()  # Height
        self.driver.find_element(By.ID, "cheightmeter").send_keys("170")  # Send keys to Height
        self.driver.find_element(By.ID, "cneckmeter").click()  # Neck
        self.driver.find_element(By.ID, "cneckmeter").send_keys("50")  # Send keys to Neck
        self.driver.find_element(By.ID, "cwaistmeter").click()  # Waist
        self.driver.find_element(By.ID, "cwaistmeter").send_keys("100")  # Send keys to Waist

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        weight_error_message = self.driver.find_element(By.XPATH,"//font[contains(text(), 'Please provide a positive weight.')]")

        assert weight_error_message.text == "Please provide a positive weight."
        print(f"Male Test Case With Empty Age Error: {weight_error_message.text}")

    def test_male_empty_height(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs
        self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()  # Select the male radio button
        self.driver.find_element(By.NAME, "cage").click()  # Age
        self.driver.find_element(By.NAME, "cage").send_keys("24")  # Send keys to Age
        self.driver.find_element(By.NAME, "cweightkgs").click()  # Weight
        self.driver.find_element(By.NAME, "cweightkgs").send_keys("70")  # Send keys to Weight
        self.driver.find_element(By.ID, "cneckmeter").click()  # Neck
        self.driver.find_element(By.ID, "cneckmeter").send_keys("50")  # Send keys to Neck
        self.driver.find_element(By.ID, "cwaistmeter").click()  # Waist
        self.driver.find_element(By.ID, "cwaistmeter").send_keys("100")  # Send keys to Waist

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        height_error_message = self.driver.find_element(By.XPATH,"//font[contains(text(), 'Height need to be positive.')]")

        assert height_error_message.text == "Height need to be positive."
        print(f"Male Test Case With Empty Age Error: {height_error_message.text}")

    def test_male_empty_neck(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs
        self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()  # Select the male radio button
        self.driver.find_element(By.NAME, "cage").click()  # Age
        self.driver.find_element(By.NAME, "cage").send_keys("24")  # Send keys to Age
        self.driver.find_element(By.NAME, "cweightkgs").click()  # Weight
        self.driver.find_element(By.NAME, "cweightkgs").send_keys("70")  # Send keys to Weight
        self.driver.find_element(By.ID, "cheightmeter").click()  # Height
        self.driver.find_element(By.ID, "cheightmeter").send_keys("170")  # Send keys to Height
        self.driver.find_element(By.ID, "cwaistmeter").click()  # Waist
        self.driver.find_element(By.ID, "cwaistmeter").send_keys("100")  # Send keys to Waist

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        neck_error_message = self.driver.find_element(By.XPATH,"//font[contains(text(), 'Neck need to be numeric.')]")

        assert neck_error_message.text == "Neck need to be numeric."
        print(f"Male Test Case With Empty Age Error: {neck_error_message.text}")

    def test_male_empty_waist(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs
        self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()  # Select the male radio button
        self.driver.find_element(By.NAME, "cage").click()  # Age
        self.driver.find_element(By.NAME, "cage").send_keys("24")  # Send keys to Age
        self.driver.find_element(By.NAME, "cweightkgs").click()  # Weight
        self.driver.find_element(By.NAME, "cweightkgs").send_keys("70")  # Send keys to Weight
        self.driver.find_element(By.ID, "cheightmeter").click()  # Height
        self.driver.find_element(By.ID, "cheightmeter").send_keys("170")  # Send keys to Height
        self.driver.find_element(By.ID, "cneckmeter").click()  # Neck
        self.driver.find_element(By.ID, "cneckmeter").send_keys("50")  # Send keys to Neck


        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        waist_error_message = self.driver.find_element(By.XPATH,"//font[contains(text(), 'Waist need to be numeric.')]")

        assert waist_error_message.text == "Waist need to be numeric."
        print(f"Male Test Case With Empty Age Error: {waist_error_message.text}")

    def test_female_valid(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs
        self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(2) > .rbmark").click()  # Select the female radio button
        self.driver.find_element(By.NAME, "cage").click()  # Age
        self.driver.find_element(By.NAME, "cage").send_keys("24")  # Send keys to Age
        self.driver.find_element(By.NAME, "cweightkgs").click()  # Weight
        self.driver.find_element(By.NAME, "cweightkgs").send_keys("70")  # Send keys to Weight
        self.driver.find_element(By.ID, "cheightmeter").click()  # Height
        self.driver.find_element(By.ID, "cheightmeter").send_keys("170")  # Send keys to Height
        self.driver.find_element(By.ID, "cneckmeter").click()  # Neck
        self.driver.find_element(By.ID, "cneckmeter").send_keys("50")  # Send keys to Neck
        self.driver.find_element(By.ID, "cwaistmeter").click()  # Waist
        self.driver.find_element(By.ID, "cwaistmeter").send_keys("80")  # Send keys to Waist
        self.driver.find_element(By.ID, "chipmeter").click() # Hip
        self.driver.find_element(By.ID, "chipmeter").send_keys("92") # Send keys to Hip

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        result_text = self.driver.find_element(By.CSS_SELECTOR, "font > b").text
        assert result_text == "Body Fat: 17.7%"
        print(f"Female Test Case Result: {result_text}")

    def test_female_all_invalid_type(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs
        self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(2) > .rbmark").click()  # Select the female radio button
        self.driver.find_element(By.NAME, "cage").click()  # Age
        self.driver.find_element(By.NAME, "cage").send_keys("twenty four")  # Send keys to Age
        self.driver.find_element(By.NAME, "cweightkgs").click()  # Weight
        self.driver.find_element(By.NAME, "cweightkgs").send_keys("seventy")  # Send keys to Weight
        self.driver.find_element(By.ID, "cheightmeter").click()  # Height
        self.driver.find_element(By.ID, "cheightmeter").send_keys("one seventy")  # Send keys to Height
        self.driver.find_element(By.ID, "cneckmeter").click()  # Neck
        self.driver.find_element(By.ID, "cneckmeter").send_keys("fifty")  # Send keys to Neck
        self.driver.find_element(By.ID, "cwaistmeter").click()  # Waist
        self.driver.find_element(By.ID, "cwaistmeter").send_keys("hundred")  # Send keys to Waist
        self.driver.find_element(By.ID, "chipmeter").click() # Hip
        self.driver.find_element(By.ID, "chipmeter").send_keys("Ninety") # Send keys to Hip

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        age_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Please provide a positive age.')]")
        weight_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Please provide a positive weight.')]")
        height_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Height need to be positive.')]")
        neck_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Neck need to be numeric.')]")
        waist_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Waist need to be numeric.')]")
        hip_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Hip need to be numeric.')]")

        assert age_error_message.text == "Please provide a positive age."
        assert weight_error_message.text == "Please provide a positive weight."
        assert height_error_message.text == "Height need to be positive."
        assert neck_error_message.text == "Neck need to be numeric."
        assert waist_error_message.text == "Waist need to be numeric."
        assert hip_error_message.text == "Hip need to be numeric."
        print(f"Female Test Case Result Age Error: {age_error_message.text}")
        print(f"Female Test Case Result Weight Error: {weight_error_message.text}")
        print(f"Female Test Case Result Height Error: {height_error_message.text}")
        print(f"Female Test Case Result Neck Error: {neck_error_message.text}")
        print(f"Female Test Case Result Waist Error: {waist_error_message.text}")
        print(f"Female Test Case Result Hip Error: {hip_error_message.text}")

    def test_female_empty_age(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs
        self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(2) > .rbmark").click()  # Select the female radio button
        self.driver.find_element(By.NAME, "cweightkgs").click()  # Weight
        self.driver.find_element(By.NAME, "cweightkgs").send_keys("80")  # Send keys to Weight
        self.driver.find_element(By.ID, "cheightmeter").click()  # Height
        self.driver.find_element(By.ID, "cheightmeter").send_keys("110")  # Send keys to Height
        self.driver.find_element(By.ID, "cneckmeter").click()  # Neck
        self.driver.find_element(By.ID, "cneckmeter").send_keys("60")  # Send keys to Neck
        self.driver.find_element(By.ID, "cwaistmeter").click()  # Waist
        self.driver.find_element(By.ID, "cwaistmeter").send_keys("140")  # Send keys to Waist
        self.driver.find_element(By.ID, "chipmeter").click() # Hip
        self.driver.find_element(By.ID, "chipmeter").send_keys("92") # Send keys to Hip

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        age_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Please provide a positive age.')]")

        assert age_error_message.text == "Please provide a positive age."
        print(f"Female Test Case Result Age Error: {age_error_message.text}")

    def test_female_empty_weight(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs
        self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(2) > .rbmark").click()  # Select the female radio button
        self.driver.find_element(By.NAME, "cage").click()  # Age
        self.driver.find_element(By.NAME, "cage").send_keys("24")  # Send keys to Age
        self.driver.find_element(By.ID, "cheightmeter").click()  # Height
        self.driver.find_element(By.ID, "cheightmeter").send_keys("170")  # Send keys to Height
        self.driver.find_element(By.ID, "cneckmeter").click()  # Neck
        self.driver.find_element(By.ID, "cneckmeter").send_keys("50")  # Send keys to Neck
        self.driver.find_element(By.ID, "cwaistmeter").click()  # Waist
        self.driver.find_element(By.ID, "cwaistmeter").send_keys("80")  # Send keys to Waist
        self.driver.find_element(By.ID, "chipmeter").click() # Hip
        self.driver.find_element(By.ID, "chipmeter").send_keys("92") # Send keys to Hip

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        weight_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Please provide a positive weight.')]")

        assert weight_error_message.text == "Please provide a positive weight."
        print(f"Female Test Case Result Weight Error: {weight_error_message.text}")

    def test_female_empty_height(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs
        self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(2) > .rbmark").click()  # Select the female radio button
        self.driver.find_element(By.NAME, "cage").click()  # Age
        self.driver.find_element(By.NAME, "cage").send_keys("24")  # Send keys to Age
        self.driver.find_element(By.NAME, "cweightkgs").click()  # Weight
        self.driver.find_element(By.NAME, "cweightkgs").send_keys("70")  # Send keys to Weight
        self.driver.find_element(By.ID, "cneckmeter").click()  # Neck
        self.driver.find_element(By.ID, "cneckmeter").send_keys("50")  # Send keys to Neck
        self.driver.find_element(By.ID, "cwaistmeter").click()  # Waist
        self.driver.find_element(By.ID, "cwaistmeter").send_keys("80")  # Send keys to Waist
        self.driver.find_element(By.ID, "chipmeter").click() # Hip
        self.driver.find_element(By.ID, "chipmeter").send_keys("92") # Send keys to Hip

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        height_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Height need to be positive.')]")

        assert height_error_message.text == "Height need to be positive."
        print(f"Female Test Case Result Height Error: {height_error_message.text}")

    def test_female_empty_neck(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs
        self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(2) > .rbmark").click()  # Select the female radio button
        self.driver.find_element(By.NAME, "cage").click()  # Age
        self.driver.find_element(By.NAME, "cage").send_keys("24")  # Send keys to Age
        self.driver.find_element(By.NAME, "cweightkgs").click()  # Weight
        self.driver.find_element(By.NAME, "cweightkgs").send_keys("70")  # Send keys to Weight
        self.driver.find_element(By.ID, "cheightmeter").click()  # Height
        self.driver.find_element(By.ID, "cheightmeter").send_keys("170")  # Send keys to Height
        self.driver.find_element(By.ID, "cwaistmeter").click()  # Waist
        self.driver.find_element(By.ID, "cwaistmeter").send_keys("80")  # Send keys to Waist
        self.driver.find_element(By.ID, "chipmeter").click() # Hip
        self.driver.find_element(By.ID, "chipmeter").send_keys("92") # Send keys to Hip

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        neck_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Neck need to be numeric.')]")

        assert neck_error_message.text == "Neck need to be numeric."
        print(f"Female Test Case Result Neck Error: {neck_error_message.text}")

    def test_female_empty_waist(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs
        self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(2) > .rbmark").click()  # Select the female radio button
        self.driver.find_element(By.NAME, "cage").click()  # Age
        self.driver.find_element(By.NAME, "cage").send_keys("24")  # Send keys to Age
        self.driver.find_element(By.NAME, "cweightkgs").click()  # Weight
        self.driver.find_element(By.NAME, "cweightkgs").send_keys("70")  # Send keys to Weight
        self.driver.find_element(By.ID, "cheightmeter").click()  # Height
        self.driver.find_element(By.ID, "cheightmeter").send_keys("170")  # Send keys to Height
        self.driver.find_element(By.ID, "cneckmeter").click()  # Neck
        self.driver.find_element(By.ID, "cneckmeter").send_keys("50")  # Send keys to Neck
        self.driver.find_element(By.ID, "chipmeter").click() # Hip
        self.driver.find_element(By.ID, "chipmeter").send_keys("92") # Send keys to Hip

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        waist_error_message = self.driver.find_element(By.XPATH, "//font[contains(text(), 'Waist need to be numeric.')]")

        assert waist_error_message.text == "Waist need to be numeric."
        print(f"Female Test Case Result Waist Error: {waist_error_message.text}")

