# Задание 1: Юнит-тесты

## Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

## Реализованные сценарии

Созданы юнит-тесты для классов `Bun`, `Burger`, `Ingredient`, `Database`.

В тестах используются:
- параметризация;
- моки;
- `pytest`;
- `pytest-cov`.

Покрытие проекта — 100%.

HTML-отчёт о покрытии формируется в папке `htmlcov`.

## Структура проекта

- `praktikum` — пакет с кодом приложения;
- `tests` — пакет с юнит-тестами;
- `main.py` — файл запуска программы;
- `requirements.txt` — зависимости проекта;
- `.gitignore` — список игнорируемых файлов и папок.

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск тестов

```bash
python -m pytest -v
```

## Запуск тестов с отчётом покрытия

```bash
python -m pytest --cov=praktikum --cov-report=term-missing --cov-report=html
```

## Отчёт покрытия

После запуска команды с `pytest-cov` HTML-отчёт будет доступен в файле:

```bash
htmlcov/index.html
```