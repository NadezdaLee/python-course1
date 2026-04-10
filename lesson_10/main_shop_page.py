from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class MainShopPage:
    """
    Page Object для главной страницы интернет-магазина.

    Содержит методы для добавления товаров в корзину
    и перехода в корзину.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация главной страницы магазина.

        :param driver: экземпляр WebDriver
        """
        self.driver = driver
        self.backpack_add_button = (
            By.ID, "add-to-cart-sauce-labs-backpack"
        )
        self.bolt_tshirt_add_button = (
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        )
        self.onesie_add_button = (
            By.ID, "add-to-cart-sauce-labs-onesie"
        )
        self.cart_link = (
            By.CLASS_NAME, "shopping_cart_link"
        )

    def add_backpack_to_cart(self) -> None:
        """
        Добавляет рюкзак в корзину.

        :return: None
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.backpack_add_button)
        ).click()

    def add_bolt_tshirt_to_cart(self) -> None:
        """
        Добавляет футболку в корзину.

        :return: None
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.bolt_tshirt_add_button)
        ).click()

    def add_onesie_to_cart(self) -> None:
        """
        Добавляет комбинезон в корзину.

        :return: None
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.onesie_add_button)
        ).click()

    def go_to_cart(self) -> None:
        """
        Переходит в корзину.

        :return: None
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_link)
        ).click()
