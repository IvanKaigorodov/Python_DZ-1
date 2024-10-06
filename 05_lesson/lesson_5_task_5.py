from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

input_namber = driver.find_element(By.CSS_SELECTOR, "input[type ='number']")

input_namber.send_keys(1000)
sleep(1)

input_namber.clear()

input_namber.send_keys(999)
sleep(1)

driver.quit()
