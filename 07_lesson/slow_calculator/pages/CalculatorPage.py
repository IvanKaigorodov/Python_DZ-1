from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java"
            "/slow-calculator.html")
        self._driver.implicitly_wait(4)

    def time(self, term):
        delay = self._driver.find_element(By.ID, "delay")
        delay.clear()
        delay.send_keys(term)

    def sum(self):
        self._driver.find_element(
            By.XPATH, "//span[text() = '7']").click()
        self._driver.find_element(
            By.XPATH, "//span[text() = '+']").click()
        self._driver.find_element(
            By.XPATH, "//span[text() = '8']").click()
        self._driver.find_element(
            By.XPATH, "//span[text() = '=']").click()

    def time_out(self, term):
        WebDriverWait(self._driver, term).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "div.screen"), "15"))

    def result(self):
        result = self._driver.find_element(
            By.CSS_SELECTOR, "div.screen").text.strip()
        print(f"Screen text is: {result}")
        return (result)
