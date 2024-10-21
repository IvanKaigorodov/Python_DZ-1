import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from slow_calculator.pages.CalculatorPage import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_calc(driver):
    calc_page = CalculatorPage(driver)
    calc_page.time(45)  # Время расчета
    calc_page.sum()
    calc_page.time_out(46)  # Время ожтдания > time
    as_is = calc_page.result()

    assert as_is == "15"
