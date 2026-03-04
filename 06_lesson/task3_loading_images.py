# дождаться загрузки всех картинок и получить src 3 картинки
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

    # Прокручиваем страницу вниз, чтобы активировать lazy loading
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )

    # Ждём появления элемента с ID 'award'
    award_image = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "award"))
    )

    # Ждём, пока атрибут src будет заполнен
    WebDriverWait(driver, 30).until(
        lambda d: (
            award_image.get_attribute("src")
            and award_image.get_attribute("src").strip() != ""
        )
    )

    src_value = award_image.get_attribute("src")
    print(
        f"SRC третьего изображения (ID 'award'): {src_value}"
    )

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    driver.quit()
