import allure
from selenium.webdriver.common.by import By


class ShopingPage:

    def __init__(self, driver):
        self._driver = driver

    @allure.step("Добавить товар в корзину")
    def shop(self):  # Покупки
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()

        # Перейти в корзину
        self._driver.find_element(By.ID, "shopping_cart_container").click()

        # Нажатие checkout
        self._driver.find_element(By.ID, "checkout").click()
