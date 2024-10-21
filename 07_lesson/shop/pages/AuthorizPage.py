from selenium.webdriver.common.by import By


class AuthorizPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)

    def user_name(self, var):
        user_name = self._driver.find_element(By.ID, "user-name")
        user_name.clear()
        user_name.send_keys(var)

    def password(self, var):
        passwword = self._driver.find_element(By.ID, "password")
        passwword.clear()
        passwword.send_keys(var)

        self._driver.find_element(By.ID, "login-button").click()
