## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- Исходные файлы (`bun.py`, `burger.py`, `ingredient.py`, `ingredient_types.py`, `database.py`) находятся в корне проекта
- `praktikum.py` — демонстрационный скрипт (не тестируется)
- `tests/` — тесты (`test_bun.py`, `test_burger.py`, `test_ingredient.py`, `test_database.py`)
- `testdata/` — тестовые данные (`data_bun.py`, `data_burger.py`, `data_ingredient.py`, `data_database.py`)
- Конфигурация pytest в `pyproject.toml`

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов**

> `$ pytest`

**Проверка линтером и типизации**

> `$ ruff check tests/ testdata/`

> `$ mypy tests/ testdata/ --explicit-package-bases --check-untyped-defs`
