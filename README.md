## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

├── praktikum - #пакет, содержащий код программы
├── tests # Автотесты
│ ├── test_bun.py`
│ ├── test_burger.py 
│ ├── test_database.py 
│ └── test_ingredient.py
├── data.py # тестовые данные
├── conftest.py # фикстуры
├── requirements.txt # Зависимости проекта
├── htmlcov # отчеты о покрытии 
└── README.md # Документация

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`
