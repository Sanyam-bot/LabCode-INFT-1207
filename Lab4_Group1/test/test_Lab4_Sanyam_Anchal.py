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

    def test_male_valid(self):
        self.driver.get("https://www.calculator.net/body-fat-calculator.html/body-fat-calculator.html")
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()  # Clear all the default inputs
        self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()  # Select the male radio button
        self.driver.find_element(By.NAME, "cage").click()  # Age
        self.driver.find_element(By.NAME, "cage").send_keys("24")  # Send keys to Age
        self.driver.find_element(By.NAME, "cweightkgs").click()  # Weight
        self.driver.find_element(By.NAME, "cweightkgs").send_keys("70")  # Send keys to Weight
        self.driver.find_element(By.ID, "cheightmeter").click()  # Weight
        self.driver.find_element(By.ID, "cheightmeter").send_keys("170")  # Send keys to Weight
        self.driver.find_element(By.ID, "cneckmeter").click()  # Weight
        self.driver.find_element(By.ID, "cneckmeter").send_keys("50")  # Send keys to Weight
        self.driver.find_element(By.ID, "cwaistmeter").click()  # Waist
        self.driver.find_element(By.ID, "cwaistmeter").send_keys("100")  # Send keys to Waist

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()  # Click the calculate button
        result_text = self.driver.find_element(By.CSS_SELECTOR, "font > b").text
        assert result_text == "Body Fat: 20.1%"
        print("Male Test Case Result:", result_text)

        self.driver.close()  # Close the driver
