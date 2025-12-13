# Автотесты для Stellar Burgers

## Описание проекта
Юнит-тесты для проверки программы, которая помогает заказать бургер в Stellar Burgers.

## Структура проекта
- `praktikum/` - исходный код приложения
- `tests/` - тесты для приложения
  - `conftest.py` - фикстуры для тестов
  - `test_data.py` - тестовые данные
  - `test_bun.py` - тесты для класса Bun
  - `test_ingredient.py` - тесты для класса Ingredient
  - `test_burger.py` - тесты для класса Burger
  - `test_database.py` - тесты для класса Database
  - `test_praktikum.py` - тесты для основного модуля

## Покрытие кода
Цель: 100% покрытие кода тестами.

## Используемые технологии
- Python 3.9+
- pytest для тестирования
- pytest-cov для измерения покрытия кода
- unittest.mock для создания моков

## Отчет о покрытии: 100%
Все тесты успешно пройдены. Покрытие кода составляет 100%.

[📊 Посмотреть отчет о покрытии](https://htmlpreview.github.io/?https://github.com/Nadezhda-20/Diplom_1/blob/develop1/htmlcov/index.html) (откроется в новом окне)

Отчет также доступен в папке [htmlcov/index.html](htmlcov/index.html)

## Запуск тестов
```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск тестов с отчетом о покрытии
pytest --cov=praktikum --cov-report=html EOF
