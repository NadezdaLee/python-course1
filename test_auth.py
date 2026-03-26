import requests
import os
from dotenv import load_dotenv

load_dotenv('config.env')
token = os.getenv('YOUGILE_API_TOKEN')

print("=== ДЕТАЛЬНАЯ ИНФОРМАЦИЯ О ЗАПРОСЕ ===")
print(f"Токен из config.env: '{token}'")
print(f"Длина токена: {len(token)}")

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

url = "https://app.yougile.com/api-v2/companies"

print("Заголовки:")
for key, value in headers.items():
    print(f"  {key}: {value}")

response = requests.get(url, headers=headers)

print("\n=== ОТВЕТ СЕРВЕРА ===")
print(f"Статус-код: {response.status_code}")
print(f"Текст ответа: {response.text}")
print(f"Размер ответа: {len(response.text)} байт")
print(f"Заголовки ответа: {dict(response.headers)}")
