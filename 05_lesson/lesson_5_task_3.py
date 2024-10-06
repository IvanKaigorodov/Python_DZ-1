from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

click_button_blue = driver.find_element(
    By.CSS_SELECTOR, 'button.btn-primary').click()

sleep(2)
