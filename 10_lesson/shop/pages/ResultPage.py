import allure
from selenium.webdriver.common.by import By


class ResultPage:

    def __init__(self, driver):
        self._driver = driver

    @allure.step("Запись стоимости товара в переменную, для"
                 "сравнения с итоговой стоимостью")
    def result(self):
        # Нажатие continue
        self._driver.find_element(By.ID, 'continue').click()

        # Прочитайте со страницы итоговую стоимость Total
        price_total = self._driver.find_element(
            By.CSS_SELECTOR, 'div.summary_total_label').text

        return (price_total)

    @allure.step("Закрытие браузера")
    def finish(self):
        # Закройте браузер
        self._driver.find_element(By.ID, "finish").click()
