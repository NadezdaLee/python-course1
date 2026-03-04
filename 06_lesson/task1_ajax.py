# нажать на кнопку и получить текст
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # Переход на страницу
    print("Открываем страницу http://uitestingplayground.com/ajax...")
    driver.get("http://uitestingplayground.com/ajax")

    # Ждём кликабельной кнопки и нажимаем (таймаут 15 секунд)
    print("Ждём появления синей кнопки...")
    wait = WebDriverWait(driver, 15)
    button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn"))
    )
    button.click()
    print("Кнопка нажата")

    # Ждём появления зелёной плашки с текстом
    print("Ждём загрузки данных через AJAX...")
    green_alert = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )

    # Получаем и выводим текст
    text = green_alert.text
    print(f"Полученный текст: {text}")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()
