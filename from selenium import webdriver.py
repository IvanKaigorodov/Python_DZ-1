from selenium import webdriver
from selenium.webdriver.chrome.service import Service as CromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=CromeService(ChromeDriverManager(). install()))
