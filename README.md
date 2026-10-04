## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` — пакет, содержащий код программы
- `tests` — пакет, содержащий тесты, разделённые по классам:
  - `bun_test.py` — тесты для `Bun`
  - `burger_test.py` — тесты для `Burger` (с моками и параметризацией)
  - `database_test.py` — тесты для `Database`
  - `ingredient_test.py` — тесты для `Ingredient` (с параметризацией)

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчёта о покрытии**

> `$ pytest --cov=praktikum --cov-report=html`

**Проверка покрытия в терминале**

> `$ pytest --cov=praktikum --cov-report=term-missing`