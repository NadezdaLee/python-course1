from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

try:
    # Переход на страницу
    driver.get("http://uitestingplayground.com/dynamicid")

    # Ожидание кнопки и клик (используем CSS‑селектор без ID)
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn")))
    button.click()

    print("Кнопка успешно нажата")

finally:
    # Закрытие браузера
    driver.quit()