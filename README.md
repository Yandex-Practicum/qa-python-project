## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам. Например, `bun_test.py`, `burger_test.py` и т.д.

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`
open htmlcov/index.html

rm -rf htmlcov/
pytest tests/ -v --cov=. --cov-report=html
open htmlcov/index.html

pip install pytest-cov.  установка

pytest tests/ -v --cov=. --cov-report=term-missing - для терминала


rm -rf allure-results/
pytest tests/ -v --alluredir=allure-results
allure serve allure-results

zip -r htmlcov.zip htmlcov/
zip -r allure-results.zip allure-results/

git ls-files все файлы