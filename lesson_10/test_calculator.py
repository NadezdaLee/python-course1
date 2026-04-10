import unittest
import allure
from selenium import webdriver
from calculator_page import CalculatorPage


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        """Инициализирует драйвер Chrome и открывает страницу калькулятора."""
        self.driver = webdriver.Chrome()

        with allure.step("Открыть страницу калькулятора"):
            self.driver.get(
                "https://bonigarcia.dev/"
                "selenium-webdriver-java/slow-calculator.html"
            )

    @allure.title("Проверка сложения 7 + 8")
    @allure.description("Тест проверяет корректность сложения в калькуляторе")
    @allure.feature("Калькулятор")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_calculator_addition(self) -> None:
        """Тестирует операцию сложения в калькуляторе."""

        calculator_page = CalculatorPage(self.driver)

        with allure.step("Установить задержку"):
            calculator_page.set_delay("45")

        with allure.step("Ввести выражение 7 + 8"):
            calculator_page.click_button("7")
            calculator_page.click_button("+")
            calculator_page.click_button("8")
            calculator_page.click_button("=")

        with allure.step("Получить результат"):
            result = calculator_page.get_result()

        with allure.step("Проверить результат"):
            self.assertEqual(
                result,
                "15",
                f"Ожидаемый результат 15, но получен {result}"
            )

    def tearDown(self) -> None:
        """Закрывает браузер после теста."""
        with allure.step("Закрыть браузер"):
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()
