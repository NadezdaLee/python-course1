from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://example.com")

print("Страница загружена:", driver.title)

driver.quit()