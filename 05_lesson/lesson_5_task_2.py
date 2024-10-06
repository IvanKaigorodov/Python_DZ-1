from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uitestingplayground.com/dynamicid")
sleep(10)
button = driver.find_element(
    By.XPATH, "//button[text()='Button with Dynamic ID']").click()

sleep(5)
