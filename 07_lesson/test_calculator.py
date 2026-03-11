import unittest
from selenium import webdriver
from calculator_page import CalculatorPage


class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Инициализирует драйвер Chrome и открывает страницу калькулятора."""
        self.driver = webdriver.Chrome()
        self.driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )

    def test_calculator_addition(self):
        """Тестирует операцию сложения в калькуляторе."""
        calculator_page = CalculatorPage(self.driver)
        calculator_page.set_delay("45")

        calculator_page.click_button("7")
        calculator_page.click_button("+")
        calculator_page.click_button("8")
        calculator_page.click_button("=")

        result = calculator_page.get_result()
        self.assertEqual(
            result,
            "15",
            f"Ожидаемый результат 15, "
            f"но получен {result}"
        )

    def tearDown(self):
        """Закрывает браузер после теста."""
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
