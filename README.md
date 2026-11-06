## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы 'Bun', 'Burger', 'Ingredient', 'Database'.

Процент покрытия — 100% (отчёт: 'htmlcov/index.html').

### Структура проекта

- 'praktikum' - пакет, содержащий код программы;
- 'tests' — пакет, содержащий тесты, разделённые по классам ('test_bun.py', 'test_burger.py', 'test_database.py', 'test_ingredient.py');
- 'tests/conftest.py' - общие фикстуры (моки булочки и ингредиента);
- '.coveragerc' - настройки покрытия (исключает демо-скрипт 'praktikum.py' и папку 'tests').

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов**

> '$ pytest'

**Запуск автотестов и создание HTML-отчёта о покрытии**

> '$ pytest --cov=. --cov-report=term-missing --cov-report=html'

HTML-отчёт сохраняется в 'htmlcov/index.html'.