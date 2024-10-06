from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

element = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "div#image-container.col-12.py-2 img#landscape")))

src_three_element = driver.find_element(
    By.CSS_SELECTOR, "#award").get_attribute("src")

print(src_three_element)

driver.quit