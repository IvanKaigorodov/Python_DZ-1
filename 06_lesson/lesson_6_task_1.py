from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(20)  # Ждать 20 секунд

driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, "[id='ajaxButton']").click()

element = driver.find_element(By.CSS_SELECTOR, "[id='content']")
txt = element.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(txt)

driver.quit()
