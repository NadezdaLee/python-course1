from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера Firefox
driver = webdriver.Firefox()

try:
    # Переход на страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Ожидание поля ввода
    wait = WebDriverWait(driver, 10)
    input_field = wait.until(
        EC.presence_of_element_located(
            (By.TAG_NAME, "input")))

    # Ввод текста "Sky"
    input_field.send_keys("Sky")

    # Очистка поля
    input_field.clear()

    # Ввод текста "Pro"
    input_field.send_keys("Pro")

    print("Операции с полем ввода выполнены")
finally:
    # Закрытие браузера
    driver.quit()
