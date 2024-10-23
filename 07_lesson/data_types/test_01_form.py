import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from data_types.pages.MainPage import MainPage
from data_types.pages.DataColor import DataColor


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_form(driver):

    main_page = MainPage(driver)
    main_page.form()

    data_color = DataColor(driver)
    red_color = data_color.color_red()
    alert_danger = "rgba(248, 215, 218, 1)"  # Красный цвет
    assert red_color == alert_danger

    grin_color = data_color.color_grin()
    alert_succes = "rgba(209, 231, 221, 1)"  # Зеленый цвет
    assert grin_color == alert_succes
