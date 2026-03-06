# переименовать кнопку
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # Шаг 1: перейти на сайт
    driver.get("http://uitestingplayground.com/textinput")

    # Шаг 2: ввести текст в поле ввода
    input_field = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#newButtonName")
        )
    )
    input_field.send_keys("SkyPro")

    # Шаг 3: нажать на синюю кнопку
    submit_button = driver.find_element(
        By.CSS_SELECTOR,
        "#updatingButton",
    )
    submit_button.click()

    # Шаг 4: получить текст кнопки
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#updatingButton"),
            "SkyPro",
        )
    )
    button_text = driver.find_element(
        By.CSS_SELECTOR,
        "#updatingButton",
    ).text

    # Шаг 5: вывести текст в консоль
    print(button_text)

finally:
    driver.quit()
