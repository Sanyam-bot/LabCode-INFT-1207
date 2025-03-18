# Name: Sanyam Singh Sachdeva
# Date: March 18, 2025
# Description: Learning about selenium locating strategies

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestDefaultSuite():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_register(self):
        self.driver.get("https://demo.guru99.com/test/newtours/")
        self.driver.set_window_size(1360, 765)
        self.driver.find_element(By.LINK_TEXT, "REGISTER").click()
        self.driver.find_element(By.NAME, "firstName").click()
        self.driver.find_element(By.NAME, "firstName").send_keys("plug")
        self.driver.find_element(By.NAME, "lastName").click()
        self.driver.find_element(By.NAME, "lastName").send_keys("ing")
        self.driver.find_element(By.NAME, "phone").click()
        self.driver.find_element(By.NAME, "phone").send_keys("999999999")
        self.driver.find_element(By.ID, "userName").click()
        self.driver.find_element(By.NAME, "password").send_keys("m>@G%_iJwKg4Q\'f")
        self.driver.find_element(By.ID, "userName").send_keys("captainamerica@marvel.com")
        self.driver.find_element(By.NAME, "address1").click()
        self.driver.find_element(By.NAME, "address1").send_keys("234 marvel road")
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("New York")
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys("New York")
        self.driver.find_element(By.NAME, "postalCode").click()
        self.driver.find_element(By.NAME, "postalCode").send_keys("789456")
        self.driver.find_element(By.NAME, "country").click()
        dropdown = self.driver.find_element(By.NAME, "country")
        dropdown.find_element(By.XPATH, "//option[. = 'UNITED STATES']").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(247)").click()
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("captain")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").click()
        element = self.driver.find_element(By.NAME, "password")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.NAME, "password").send_keys("captain")
        self.driver.find_element(By.NAME, "confirmPassword").click()
        self.driver.find_element(By.NAME, "confirmPassword").send_keys("captain")
        self.driver.find_element(By.NAME, "submit").click()

        result = self.driver.find_element(By.XPATH, "//font[contains(text(),'Thank you for registering.')]")

        assert result.text == "Thank you for registering. You may now sign-in using the user name and password you've just entered."
        print('Test Case 1 (Registering an user): Successfully Passed')

    def test_login(self):
        self.driver.get("https://demo.guru99.com/test/newtours/")
        self.driver.set_window_size(1360, 765)
        self.driver.find_element(By.LINK_TEXT, "SIGN-ON").click()
        element = self.driver.find_element(By.LINK_TEXT, "SIGN-ON")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.NAME, "userName").click()
        self.driver.find_element(By.NAME, "userName").send_keys("captain")
        self.driver.find_element(By.NAME, "password").send_keys("captain")
        self.driver.find_element(By.NAME, "submit").click()

        result = self.driver.find_element(By.XPATH, "//b[normalize-space()='Thank you for Loggin.']")

        assert result.text == 'Thank you for Loggin.'
        print('Test Case 1 (Logging in an user): Successfully Passed')