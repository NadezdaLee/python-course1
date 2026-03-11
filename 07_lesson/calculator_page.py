from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.result_field = (By.CSS_SELECTOR, ".screen")

    def set_delay(self, delay):
        # Находит поле задержки, очищает его и вводит значение
        delay_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.delay_input)
        )
        delay_element.clear()
        delay_element.send_keys(delay)

    def click_button(self, button_text):
        # Формирует XPath-локатор: ищет span с точным текстом
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        # Ожидает кликабельности и нажимает кнопку
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        ).click()

    def get_result(self):
        # Ожидает появления результата и возвращает его текст
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element(self.result_field, "15")
        )
        return self.driver.find_element(*self.result_field).text
