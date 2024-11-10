import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from slow_calculator.pages.CalculatorPage import CalculatorPage


@allure.id("Calculator")
@allure.epic("Калькулятор")
@allure.severity("blocker")
@allure.suite("Тест медленного калькулятора")
@allure.story("Вычисления на калькуляторе")
@allure.title("Сложение на калькуляторе")
@allure.feature("CREATE")
def test_calc():
    with allure.step("Открыть страницу калькулятор в Chrome"):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Создать переменную, экземпляр класса CalculatorPage"):
        calc_page = CalculatorPage(driver)

    with allure.step("Задать время расчета"):
        calc_page.time(45)

    with allure.step("Выполнить сложение"):
        calc_page.sum()

    with allure.step("Время ожидания расчета"):
        calc_page.time_out(46)

    with allure.step("Запись результата в переменную as_is"):
        as_is = calc_page.result()

    with allure.step("Проверка результата"):
        assert as_is == "15"

    driver.quit()
