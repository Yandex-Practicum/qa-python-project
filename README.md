## Задание 1: Юнит-тесты
### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers
### Реализованные сценарии

Созданы юнит-тесты, покрывающие класс `Burger`

Проверяются следующие методы:
set_buns() — установка булочек;
add_ingredient() — добавление ингредиентов;
remove_ingredient() — удаление ингредиентов;
move_ingredient() — перемещение ингредиентов;
get_price() — расчёт стоимости бургера;
get_receipt() — формирование чека.

Используются моки (Mock), параметризация тестов (pytest.mark.parametrize), позитивные и негативные сценарии.

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта
praktikum — пакет с кодом программы;
tests — пакет с тестами;
tests/conftest.py — фикстуры;
tests/test_burger.py — тесты класса Burger;
htmlcov — HTML-отчёт о покрытии.

### Запуск автотестов

**Установка зависимостей**
pip install -r requirements.txt

**Запуск автотестов и создание HTML-отчета о покрытии**
pytest --cov=praktikum.burger --cov-report=term-missing --cov-report=html

**Запуск тестов**
pytest