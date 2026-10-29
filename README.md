
# Дипломный проект. Часть 1 — Юнит-тесты

## Stellar Burgers

Проект содержит юнит-тесты для класса `Burger` приложения Stellar Burgers.

## Реализованные тесты

Проверены все методы класса `Burger`:

- `__init__` — создание бургера.
- `set_buns` — установка булочки.
- `add_ingredient` — добавление ингредиента.
- `remove_ingredient` — удаление ингредиента.
- `move_ingredient` — перемещение ингредиента.
- `get_price` — расчёт стоимости бургера.
- `get_receipt` — формирование чека.

Для изоляции тестируемого класса используются моки `unittest.mock.Mock`.

Для проверки различных сценариев применяется параметризация `pytest.mark.parametrize`.

## Результаты тестирования

- Всего тестовых случаев: 18.
- Успешно пройдено: 18.
- Неуспешных тестов: 0.
- Покрытие класса `Burger`: 100%.

Покрытие измерено с помощью `pytest-cov`.

HTML-отчёт о покрытии находится в `htmlcov/index.html`.

## Структура проекта

- `praktikum/` — исходный код приложения.
- `tests/test_burger.py` — юнит-тесты класса `Burger`.
- `htmlcov/` — HTML-отчёт о покрытии.
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

## Запуск тестов с проверкой покрытия

```bash
python -m pytest tests/ -v --cov=praktikum.burger --cov-report=term-missing --cov-report=html:htmlcov
```

## Просмотр отчёта

После запуска тестов открыть файл `htmlcov/index.html` в браузере.

Покрытие класса `Burger` составляет 100%.
