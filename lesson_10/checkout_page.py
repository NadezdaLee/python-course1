from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """
    Page Object для страницы оформления заказа.

    Содержит методы для заполнения формы покупателя
    и получения итоговой суммы заказа.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы оформления заказа.

        :param driver: экземпляр WebDriver
        """
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_price_label = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_form(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ) -> None:
        """
        Заполняет форму данными покупателя и переходит далее.

        :param first_name: имя пользователя
        :param last_name: фамилия пользователя
        :param postal_code: почтовый индекс
        :return: None
        """
        first_name_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name_input)
        )
        first_name_field.send_keys(first_name)

        last_name_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.last_name_input)
        )
        last_name_field.send_keys(last_name)

        postal_code_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.postal_code_input)
        )
        postal_code_field.send_keys(postal_code)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()

    def get_total_price(self) -> str:
        """
        Получает итоговую сумму заказа.

        :return: строка с итоговой суммой (например, "$58.29")
        """
        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_price_label)
        )
        total_text = total_element.text.replace("Total: ", "")
        return total_text
