
##  Описание проекта

Проект содержит автоматизированные UI-тесты для веб-приложений с использованием:

* Selenium WebDriver
* Page Object Pattern
* Allure для отчетов

Реализованы тесты:

* калькулятора
* интернет-магазина (полный цикл покупки)

---

## Используемые технологии

* Python
* Selenium
* unittest
* Allure

---

## Cтруктура проекта

```
lesson_10/
│
├── pages/
│   ├── login_page.py
│   ├── main_shop_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── calculator_page.py
│
├── tests/
│   ├── test_shop.py
│   └── test_calculator.py
│
└── README.md
```

---

## Установка зависимостей

Установите зависимости:

```
pip install -r requirements.txt
```

Если файла requirements.txt нет:

```
pip install selenium pytest allure-pytest
```

---

## Запуск тестов

Для запуска тестов с генерацией Allure-отчета выполните:

```
pytest --alluredir=allure-results
```

После выполнения тестов будет создана папка:

```
allure-results/
```

---

##  Просмотр отчета Allure

Для просмотра отчета выполните:

```
allure serve allure-results
```

Откроется браузер с интерактивным отчетом.

---

## Важно

* Папки `allure-results` и `allure-report` не добавляются в репозиторий
* Перед запуском убедитесь, что установлен Allure CLI

---

##  Проверка кода (flake8)

Для проверки соответствия PEP8 выполните:

```
flake8 lesson_10
```

Исправьте ошибки, если они есть.

---

##  Как сдать задание

1. Создать ветку `lesson10`
2. Добавить изменения
3. Запушить в GitHub
4. Создать Pull Request в `main`

Пример ссылки:

```
https://github.com/username/repository/pull/1
```
