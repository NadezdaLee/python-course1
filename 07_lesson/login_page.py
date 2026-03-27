from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def enter_username(self, username):
        # Вводит логин в поле «Username»
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.username_input)
        ).send_keys(username)

    def enter_password(self, password):
        # Вводит пароль в поле «Password»
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.password_input)
        ).send_keys(password)

    def click_login(self):
        # Нажимает кнопку входа
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()
