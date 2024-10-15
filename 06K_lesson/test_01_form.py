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
    alert_success = "rgba(209, 231, 221, 1)"

    color_first_name = (driver.find_element(
        By.ID, "first-name").value_of_css_property("background-color"))
    assert color_first_name == alert_success, f"Expected {
        alert_success}, but got {color_first_name}"

    color_last_name = (driver.find_element(
        By.ID, "last-name").value_of_css_property("background-color"))
    assert color_last_name == alert_success, f"Expected {
        alert_success}, but got {color_last_name}"

    color_address = (driver.find_element(
        By.ID, "address").value_of_css_property("background-color"))
    assert color_address == alert_success, f"Expected {
        alert_success}, but got {color_address}"

    color_e_mail = (driver.find_element(
        By.ID, "e-mail").value_of_css_property("background-color"))
    assert color_e_mail == alert_success, f"Expected {
        alert_success}, but got {color_e_mail}"

    color_phone = (driver.find_element(
        By.ID, "phone").value_of_css_property("background-color"))
    assert color_phone == alert_success, f"Expected {
        alert_success}, but got {color_phone}"

    color_city = (driver.find_element(
        By.ID, "city").value_of_css_property("background-color"))
    assert color_city == alert_success, f"Expected {
        alert_success}, but got {color_city}"

    color_country = (driver.find_element(
        By.ID, "country").value_of_css_property("background-color"))
    assert color_country == alert_success, f"Expected {
        alert_success}, but got {color_country}"

    color_job_position = (driver.find_element(
        By.ID, "job-position").value_of_css_property("background-color"))
    assert color_job_position == alert_success, f"Expected {
        alert_success}, but got {color_job_position}"

    color_company = (driver.find_element(
        By.ID, "company").value_of_css_property("background-color"))
    assert color_company == alert_success, f"Expected {
        alert_success}, but got {color_company}"
