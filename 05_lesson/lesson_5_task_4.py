from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")

mod_win = driver.find_element(By.CSS_SELECTOR, '.modal')
sleep(5)

close_mod_win = driver.find_element(By.CSS_SELECTOR, ".modal-footer").click()
sleep(2)

driver.quit()
