from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """
    Page Object для страницы калькулятора.

    Содержит методы для взаимодействия с элементами страницы:
    установка задержки, нажатие кнопок и получение результата.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.

        :param driver: экземпляр WebDriver
        """
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.result_field = (By.CSS_SELECTOR, ".screen")

    def set_delay(self, delay: str) -> None:
        """
        Устанавливает задержку выполнения вычислений.

        :param delay: значение задержки (в секундах)
        :return: None
        """
        delay_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.delay_input)
        )
        delay_element.clear()
        delay_element.send_keys(delay)

    def click_button(self, button_text: str) -> None:
        """
        Нажимает кнопку калькулятора по её тексту.

        :param button_text: текст кнопки (например, "7", "+", "=")
        :return: None
        """
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        ).click()

    def get_result(self) -> str:
        """
        Получает результат вычисления с экрана калькулятора.

        :return: строка с результатом вычисления
        """
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element(self.result_field, "15")
        )
        return self.driver.find_element(*self.result_field).text
