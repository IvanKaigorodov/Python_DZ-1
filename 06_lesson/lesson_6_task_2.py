from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

pole_name = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
pole_name.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

txt_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(txt_button)

driver.quit()
