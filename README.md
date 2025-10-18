## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

project/
├── praktikum/
│   ├── __init__.py
│   ├── bun.py
│   ├── burger.py
│   ├── ingredient.py
│   ├── database.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   ├── bun_test.py
│   ├── burger_test.py
│   ├── ingredient_test.py
│   ├── database_test.py
│   └── conftest.py
├── requirements.txt
└── htmlcov/
    └── index.html

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`
