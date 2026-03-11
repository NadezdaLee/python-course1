import unittest
import warnings
from selenium import webdriver
from login_page import LoginPage
from main_shop_page import MainShopPage
from cart_page import CartPage
from checkout_page import CheckoutPage

# Игнорируем ResourceWarning
warnings.filterwarnings(
    "ignore",
    category=ResourceWarning
)


class TestShop(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Инициализация браузера Firefox перед всеми тестами"""
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        """Гарантированное закрытие браузера после всех тестов"""
        if cls.driver:
            cls.driver.quit()

    def setUp(self):
        """Подготовка перед каждым тестом — открываем сайт"""
        self.driver.get("https://www.saucedemo.com/")

    def test_shop_checkout(self):
        """Тест полного цикла покупки в интернет‑магазине"""
        print("Шаг 1: Авторизация в системе...")
        login_page = LoginPage(self.driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()
        print("Авторизация успешна!")

        print("Шаг 2: Добавление товаров в корзину...")
        main_page = MainShopPage(self.driver)
        main_page.add_backpack_to_cart()
        main_page.add_bolt_tshirt_to_cart()
        main_page.add_onesie_to_cart()
        print("Все товары добавлены в корзину!")

        print("Шаг 3: Переход в корзину и начало оформления заказа...")
        main_page.go_to_cart()
        cart_page = CartPage(self.driver)
        cart_page.click_checkout()
        print("Переход на страницу оформления заказа...")

        print("Шаг 4: Заполнение формы данных покупателя...")
        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_checkout_form(
            first_name="Винни Пух",
            last_name="Пухов",
            postal_code="12345098"
        )
        print("Форма заполнена: Винни Пух, индекс 12345098")

        print("Шаг 5: Проверка итоговой суммы...")
        total = checkout_page.get_total_price()
        print(f"Итоговая сумма: {total}")

        # Проверка, что итоговая сумма равна $58.29
        self.assertEqual(
            total,
            "$58.29",
            f"Ошибка: ожидаемая сумма $58.29, "
            f"но получена {total}"
        )
        print("Проверка пройдена! Итоговая сумма корректна: $58.29")


if __name__ == "__main__":
    unittest.main()
