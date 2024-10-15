import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_calculator(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay = driver.find_element(By.ID, "delay")
    delay.clear()
    # 45 секунд из условия
    delay.send_keys(45)

    driver.find_element(
        By.XPATH, "//span[text() = '7']").click()
    driver.find_element(
        By.XPATH, "//span[text() = '+']").click()
    driver.find_element(
        By.XPATH, "//span[text() = '8']").click()
    driver.find_element(
        By.XPATH, "//span[text() = '=']").click()

    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "div.screen"), "15"))

    result = driver.find_element(
        By.CSS_SELECTOR, "div.screen").text.strip()
    print(f"Screen text is: {result}")

    assert result == "15"
