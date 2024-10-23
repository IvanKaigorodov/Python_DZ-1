import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from shop.pages.AuthorizPage import AuthorizPage
from shop.pages.ShopingPage import ShopingPage
from shop.pages.FormPage import FormPage
from shop.pages.ResultPage import ResultPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_shoping(driver):
    # Авторизация
    authoriz_page = AuthorizPage(driver)
    authoriz_page.user_name('standard_user')
    authoriz_page.password('secret_sauce')

    # Покупки
    shop_page = ShopingPage(driver)
    shop_page.shop()

    # Форма покупателя
    form_page = FormPage(driver)
    form_page.form_first_name('Иван')
    form_page.form_last_name('Кайгородов')
    form_page.form_index('650001')

    # Итог
    result_page = ResultPage(driver)
    sum = result_page.result()
    result_page.finish()

    assert sum == "Total: $58.29"
