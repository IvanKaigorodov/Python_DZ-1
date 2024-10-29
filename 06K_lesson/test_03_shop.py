import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_03_shop(driver):
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    user_name = driver.find_element(By.ID, "user-name")
    user_name.clear()
    user_name.send_keys("standard_user")

    passwword = driver.find_element(By.ID, "password")
    passwword.clear()
    passwword.send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    # Покупки
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-onesie").click()

    # Перейти в корзину
    driver.find_element(By.ID, "shopping_cart_container").click()

    # Нажатие checkout
    driver.find_element(By.ID, "checkout").click()

    # Заполни форму
    first_name = driver.find_element(By.ID, "first-name")
    first_name.clear()
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.clear()
    last_name.send_keys("Кайгородов")

    postal_code = driver.find_element(By.ID, "postal-code")
    postal_code.clear()
    postal_code.send_keys("650001")

    # Нажатие continue
    driver.find_element(By.ID, 'continue').click()

    # Прочитайте со страницы итоговую стоимость ( Total )
    price_total = driver.find_element(
        By.CSS_SELECTOR, 'div.summary_total_label').text

    # Закройте браузер
    driver.find_element(By.ID, "finish").click()

    # Проверьте, что итоговая сумма равна $58.29
    assert price_total == "Total: $58.29"
