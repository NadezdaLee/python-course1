import unittest
import warnings
import allure
from selenium import webdriver
from login_page import LoginPage
from main_shop_page import MainShopPage
from cart_page import CartPage
from checkout_page import CheckoutPage


warnings.filterwarnings("ignore", category=ResourceWarning)


class TestShop(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """Инициализация браузера Firefox перед всеми тестами"""
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        """Гарантированное закрытие браузера после всех тестов"""
        if cls.driver:
            cls.driver.quit()

    def setUp(self) -> None:
        """Подготовка перед каждым тестом — открываем сайт"""
        with allure.step("Открыть сайт saucedemo"):
            self.driver.get("https://www.saucedemo.com/")

    @allure.title("Полный цикл покупки в интернет-магазине")
    @allure.description(
        "Тест проверяет сценарий: логин → добавление товаров → "
        "checkout → проверка суммы"
          )
    @allure.feature("Интернет-магазин")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_shop_checkout(self) -> None:
        """Тест полного цикла покупки"""

        with allure.step("Авторизация пользователя"):
            login_page = LoginPage(self.driver)
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")
            login_page.click_login()

        with allure.step("Добавление товаров в корзину"):
            main_page = MainShopPage(self.driver)
            main_page.add_backpack_to_cart()
            main_page.add_bolt_tshirt_to_cart()
            main_page.add_onesie_to_cart()

        with allure.step("Переход в корзину"):
            main_page.go_to_cart()

        with allure.step("Переход к оформлению заказа"):
            cart_page = CartPage(self.driver)
            cart_page.click_checkout()

        with allure.step("Заполнение данных покупателя"):
            checkout_page = CheckoutPage(self.driver)
            checkout_page.fill_checkout_form(
                first_name="Винни Пух",
                last_name="Пухов",
                postal_code="12345098"
            )

        with allure.step("Получение итоговой суммы"):
            total = checkout_page.get_total_price()

        with allure.step("Проверка итоговой суммы"):
            self.assertEqual(
                total,
                "$58.29",
                f"Ошибка: ожидаемая сумма $58.29, но получена {total}"
            )


if __name__ == "__main__":
    unittest.main()
