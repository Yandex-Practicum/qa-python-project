Задание 1 Юнит-тесты

Косач Евгений 29-я когорта

Diplom1/
├── .gitignore
├── requirements.txt
├── praktikum/
│   ├── __init__.py
│   ├── bun.py
│   ├── burger.py
│   ├── database.py
│   ├── ingredient.py
│   ├── ingredient_types.py
│   └── praktikum.py
└── tests/
    ├── data/
    │    ├── __init__.py
    │    └── test_data.py
    ├── __init__.py
    ├── conftest.py
    ├── test_burger_parametrized.py
    └── test_burger.py

    # Установка зависимостей
pip install -r requirements.txt

# Запуск тестов с проверкой покрытия
pytest --cov=praktikum --cov-report=html