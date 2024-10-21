from selenium.webdriver.common.by import By


class DataColor:

    def __init__(self, driver):
        self._driver = driver

    def color_red(self):  # Красное поле

        color_zip = (self._driver.find_element(
            By.ID, "zip-code").value_of_css_property(
                "background-color")
        )
        return (color_zip)

    def color_grin(self):   # Зеленое поле
        other_fields = [
            "#first-name",
            "#last-name",
            "#address",
            "#e-mail",
            "#phone",
            "#city",
            "#country",
            "#job-position",
            "#company",
        ]
        for field in other_fields:
            field_color = self._driver.find_element(
                By.CSS_SELECTOR, field).value_of_css_property(
                    "background-color")
        return (field_color)
