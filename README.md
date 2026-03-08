## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

В проекте реализованы юнит-тесты для программы, которая помогает заказать бургер в Stellar Burgers.

Тестами покрыт класс Burger из пакета praktikum.

🏁 Покрытие кода класса Burger — 100%
(HTML-отчёт: htmlcov/index.html)

### Реализованные сценарии
В проекте реализованы юнит-тесты для программы, которая помогает заказать бургер в Stellar Burgers.

Тестами покрыт класс Burger из пакета praktikum.

🏁 Покрытие кода класса Burger — 100%
HTML-отчёт: htmlcov/index.html

Проверены методы класса Burger:

set_buns
add_ingredient
remove_ingredient
move_ingredient
get_price
get_receipt

В тестах используются:
моки (unittest.mock) — для изоляции зависимостей (Bun, Ingredient)
параметризация (pytest.mark.parametrize)


Используемые библиотеки :

pytest
pytest-cov
### Структура проекта
Diplom_1
├── praktikum
│   ├── __init__.py
│   ├── bun.py
│   ├── burger.py
│   ├── database.py
│   ├── ingredient.py
│   └── ingredient_types.py
├── tests
│   └── test_burger.py
├── pytest.ini
├── requirements.txt
└── README.md
└── .gitignore

**Установка зависимостей**

> pip install -r requirements.txt

**Запуск автотестов и создание HTML-отчета о покрытии**

>  python -m pytest tests -q

Покрытие проверяется для класса Burger:

> python -m pytest tests --cov=praktikum.burger --cov-report=term-missing

HTML-отчёт можно получить командой:

> python -m pytest tests --cov=praktikum.burger --cov-report=html

Отчёт будет доступен в папке:

> htmlcov/index.html