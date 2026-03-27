import os
from dotenv import load_dotenv

load_dotenv('config.env')  # Загружаем из config.env вместо .env

BASE_URL = os.environ.get('YOUGILE_BASE_URL')
API_TOKEN = os.environ.get('YOUGILE_API_TOKEN')

if not BASE_URL or not API_TOKEN:
    raise ValueError(
        "Не заданы YOUGILE_BASE_URL или YOUGILE_API_TOKEN в config.env файле"
    )
