# Задание 1. Юнит-тесты
## Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers
### Реализованные сценарии

Разработаны юнит-тесты для следующих классов:
- `Bun`
- `Burger`
- `Ingredient`
- `Database`

Использованы:
- `pytest`
- параметризация (`pytest.mark.parametrize`)
- моки (`unittest.mock`)

Процент покрытия кода — **78%**.

HTML-отчет о покрытии можно сгенерировать командой:

```bash
python3 -m pytest --cov=praktikum --cov-report=html
```

## Структура проекта

```text
praktikum/
    bun.py
    burger.py
    database.py
    ingredient.py
    ingredient_types.py
    praktikum.py

tests/
    conftest.py
    test_bun.py
    test_burger.py
    test_database.py
    test_ingredient.py
```

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск тестов

```bash
python3 -m pytest
```

## Запуск тестов с отчетом о покрытии

Отчет в консоли:

```bash
python3 -m pytest --cov=praktikum --cov-report=term-missing
```

HTML-отчет:

```bash
python3 -m pytest --cov=praktikum --cov-report=html
```