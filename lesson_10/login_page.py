from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """
    Page Object для страницы авторизации.

    Содержит методы для ввода логина, пароля
    и выполнения входа в систему.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы логина.

        :param driver: экземпляр WebDriver
        """
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def enter_username(self, username: str) -> None:
        """
        Вводит логин в поле Username.

        :param username: имя пользователя
        :return: None
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.username_input)
        ).send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Вводит пароль в поле Password.

        :param password: пароль пользователя
        :return: None
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.password_input)
        ).send_keys(password)

    def click_login(self) -> None:
        """
        Нажимает кнопку входа в систему.

        :return: None
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()
