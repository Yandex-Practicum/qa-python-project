## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `tests` - пакет, содержащий тесты, разделенные по классам. Например, `test_bun.py`, `test_burger.py` и т. д.
- В корне лежит код программы, файл `conftest.py` с фикстурами и файл `pytest.ini` для автоматического добавления allure-отчётов в папку allure_results 

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов, cоздание Allure-отчёта и создание HTML-отчета о покрытии**

> `$ pytest --cov=praktikum --cov-report=html`
> `$ allure serve allure_results`