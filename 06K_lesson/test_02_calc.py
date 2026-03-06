# калькулятор
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 50)

    driver.get(
        "https://bonigarcia.dev/"
        "selenium-webdriver-java/slow-calculator.html"
    )

    # ввод задержки
    delay = driver.find_element(By.ID, "delay")
    delay.clear()
    delay.send_keys("45")

    # нажимаем кнопки
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # ожидание результата
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "screen"),
            "15"
        )
    )

    result = driver.find_element(By.CLASS_NAME, "screen").text

    assert result == "15"

    driver.quit()
