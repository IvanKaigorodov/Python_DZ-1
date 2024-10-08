from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

for _ in range(5):
    click_button = driver.find_element(
        By.XPATH, "//button[text()='Add Element']").click()
    sleep(0.5)

    list_button = driver.find_elements(
        By.XPATH, "//button[text()='Delete']")

print(f'Количество кнопок "Delete": {len(list_button)}')

sleep(1)
