from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера Firefox
driver = webdriver.Firefox()

try:
    # Переход на страницу авторизации
    driver.get("http://the-internet.herokuapp.com/login")

    # Ожидание появления поля username и ввод логина
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(
        EC.presence_of_element_located(
            (By.ID, "username"))
    )
    username_field.send_keys("tomsmith")

    # Ввод пароля в поле password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    # Нажатие кнопки Login
    login_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # Ожидание появления сообщения об успешном входе
    success_message = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".flash.success"))
    )

    # Очищаем текст от символа закрытия (×) и лишних пробелов
    raw_text = success_message.text
    clean_message = raw_text.split('×')[0].strip()

    # Вывод очищенного сообщения в консоль
    print(f"Сообщение: {clean_message}")

finally:
    # Гарантированное закрытие браузера даже при ошибке
    driver.quit()
