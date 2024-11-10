import allure
from selenium.webdriver.common.by import By


class FormPage:

    def __init__(self, driver):
        self._driver = driver

    @allure.step("Ввод имя покупателя")
    def form_first_name(self, var):  # Заполнить имя
        first_name = self._driver.find_element(By.ID, "first-name")
        first_name.clear()
        first_name.send_keys(var)

    @allure.step("Ввод фамилии покупателя")
    def form_last_name(self, var):  # Заполнить фамилию
        last_name = self._driver.find_element(By.ID, "last-name")
        last_name.clear()
        last_name.send_keys(var)

    @allure.step("Ввод индекса покупателя")
    def form_index(self, var):  # Заполнить индекс
        postal_code = self._driver.find_element(By.ID, "postal-code")
        postal_code.clear()
        postal_code.send_keys(var)
