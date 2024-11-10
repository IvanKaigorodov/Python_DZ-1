import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from shop.pages.AuthorizPage import AuthorizPage
from shop.pages.ShopingPage import ShopingPage
from shop.pages.FormPage import FormPage
from shop.pages.ResultPage import ResultPage


@allure.id("Shop")
@allure.epic("Магазин")
@allure.severity("blocker")
@allure.suite("Тест покупок в магазине")
@allure.story("Покупки")
@allure.title("Авторизация, выбор товаров, оплата покупок")
@allure.feature("CREATE")
def test_shoping():
    with allure.step("Открыть страницу магазин в Chrome"):
        driver = webdriver.Chrome(
            service=ChromeService(
                ChromeDriverManager().install()))

    with allure.step("Создать переменную, экземпляр класса AuthorizPageage"):
        authoriz_page = AuthorizPage(driver)

    with allure.step("Заполнить поле имя"):
        authoriz_page.user_name('standard_user')

    with allure.step("Заполнить поле пароль"):
        authoriz_page.password('secret_sauce')

    with allure.step("Создать переменную, экземпляр класса ShopingPage"):
        shop_page = ShopingPage(driver)

    with allure.step("Сделать покупки"):
        shop_page.shop()

    with allure.step("Создать переменную, экземпляр класса FormPage"):
        form_page = FormPage(driver)

    with allure.step("Заполнить форму покупателя"):
        form_page.form_first_name('Иван')
        form_page.form_last_name('Кайгородов')
        form_page.form_index('650001')

    with allure.step("Создать переменную, экземпляр класса ResultPage"):
        result_page = ResultPage(driver)
        sum = result_page.result()
        result_page.finish()

    with allure.step("Проверить, что полученная сумма равна ожидаемой"):
        assert sum == "Total: $58.29"

    driver.quit()
