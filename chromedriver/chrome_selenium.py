from selenium import webdriver

# Запуск Google Chrome
driver = webdriver.Chrome()
driver.get("http://www.google.com")
print(driver.title)
driver.quit()