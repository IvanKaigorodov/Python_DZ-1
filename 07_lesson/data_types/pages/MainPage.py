from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)

    def form(self):
        # Заполнить форму
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='phone']").send_keys("+7985899998787")
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='zip-code']").send_keys("")
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='city']").send_keys("Москва")
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")

        # Нажать на кнопку
        self._driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
