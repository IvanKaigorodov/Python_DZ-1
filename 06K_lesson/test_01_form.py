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


def test_form(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(
        By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")
    driver.find_element(
        By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
    driver.find_element(
        By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(
        By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(
        By.CSS_SELECTOR, "[name='phone']").send_keys("+7985899998787")
    driver.find_element(
        By.CSS_SELECTOR, "[name='zip-code']").send_keys("")
    driver.find_element(
        By.CSS_SELECTOR, "[name='city']").send_keys("Москва")
    driver.find_element(
        By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
    driver.find_element(
        By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")
    driver.find_element(
        By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    # Проверка красного поля
    alert_danger = "rgba(248, 215, 218, 1)"
    color_zip = (driver.find_element(
        By.ID, "zip-code").value_of_css_property("background-color")
        )
    assert color_zip == alert_danger, f"Expected {
        alert_danger}, but got {color_zip}"

    # Проверка зеленого поля
    other_fields = [
        "#first-name",
        "#last-name",
        "#address",
        "#e-mail",
        "#phone",
        "#city",
        "#country",
        "#job-position",
        "#company",
    ]
    for field in other_fields:
        field_color = driver.find_element(
            By.CSS_SELECTOR, field).value_of_css_property(
            "background-color")
    assert field_color == "rgba(209, 231, 221, 1)"
