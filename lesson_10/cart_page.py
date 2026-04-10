from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """
    Page Object для страницы корзины.

    Содержит методы для взаимодействия с корзиной,
    например переход к оформлению заказа.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины.

        :param driver: экземпляр WebDriver
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def click_checkout(self) -> None:
        """
        Нажимает кнопку Checkout для перехода к оформлению заказа.

        :return: None
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()
