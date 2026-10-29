# Задание 1. Юнит-тесты Stellar Burgers

## Описание проекта

Автоматизированное тестирование класса `Burger` приложения Stellar Burgers.

Тесты написаны на Python с использованием `pytest`, `unittest.mock.Mock` и параметризации `pytest.mark.parametrize`.

## Реализованные проверки

Созданы тесты для методов класса `Burger`:

- `__init__` — создание бургера.
- `set_buns` — установка булочки.
- `add_ingredient` — добавление ингредиента.
- `remove_ingredient` — удаление ингредиента.
- `move_ingredient` — перемещение ингредиента.
- `get_price` — расчёт стоимости бургера.
- `get_receipt` — формирование чека.

Всего реализовано 16 тестовых сценариев.

**Результаты:**
- Успешно пройдено: 16 тестов.
- Покрытие `praktikum/burger.py`: 100%.
- Непокрытых строк: 0.

## Структура проекта

- `praktikum/` — пакет с исходным кодом приложения.
- `tests/test_burger.py` — юнит-тесты класса `Burger`.
- `pytest.ini` — настройки pytest.
- `requirements.txt` — зависимости проекта.
- `.gitignore` — исключения для Git.

## Установка зависимостей

```bash
python -m pip install -r requirements.txt
```

## Запуск тестов

```bash
python -m pytest tests/ -v
```

## Проверка покрытия кода

```bash
python -m pytest tests/ --cov=praktikum.burger --cov-report=term-missing
```

Результат: 100% покрытия файла `burger.py`.

## Используемые технологии

- Python
- pytest
- pytest-cov
- unittest.mock

## Ветка проекта

`develop1`