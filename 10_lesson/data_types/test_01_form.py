import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from data_types.pages.MainPage import MainPage
from data_types.pages.DataColor import DataColor


@allure.id("DataTyps")
@allure.epic("Персональные данные")
@allure.severity("blocker")
@allure.suite("Тест заполнения всех полей формы данных")
@allure.story("Заполнение данных")
@allure.title("Заполнить не все поля данных")
@allure.feature("CREATE")
def test_form():
    with allure.step("Открыть страницу формы Chrome"):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Создать переменную, экземпляр класса MainPage"):
        main_page = MainPage(driver)
        main_page.form()

    with allure.step("Создать переменную, экземпляр класса DataColor"):
        data_color = DataColor(driver)
        red_color = data_color.color_red()
        alert_danger = "rgba(248, 215, 218, 1)"

    with allure.step("Убедиться,что цвет не заполненного поля красный"):
        assert red_color == alert_danger

        grin_color = data_color.color_grin()
        alert_succes = "rgba(209, 231, 221, 1)"

    with allure.step("Убедиться,что цвет заполненных полей зеленый"):
        assert grin_color == alert_succes

    with allure.step("Закрыть драйвер"):
        driver.quit()
