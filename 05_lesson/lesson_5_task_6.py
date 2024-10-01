from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
sleep(1)

username = driver.find_element(
    By.ID, 'username').send_keys("tomsmith")
sleep(1)

password = driver.find_element(
    By.ID, 'password').send_keys("SuperSecretPassword!")
sleep(1)

button_login = driver.find_element(By.CSS_SELECTOR, "i").click()
sleep(1)

driver.quit()
