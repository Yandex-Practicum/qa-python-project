# Юнит-тесты для Stellar Burgers

## Описание

Автоматизированные юнит-тесты для сервиса Stellar Burgers. Цель проекта — проверить основные сценарии работы с бургером, включая создание булочки, добавление ингредиентов и расчет итоговой стоимости.

## Стек технологий

- Python
- pytest
- pytest-cov
- coverage

### Реализованные сценарии

Созданы юнит-тесты, покрывающие класс `Burger`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

## Структура проекта

- praktikum/ — пакет с логикой приложения.
- tests/ — директория с тестами.
- requirements.txt — список зависимостей проекта.
- README.md — описание проекта и инструкции по запуску.

## Установка и запуск тестов

1. Клонируйте репозиторий:
   ```bash
   git clone <ссылка_на_репозиторий>
   cd Diplom_1
   ```

2. Создайте и активируйте виртуальное окружение.

   Для Windows:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   Для macOS:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Запустите тесты:
   ```bash
   pytest
   ```

5. Для просмотра отчета о покрытии выполните:
   ```bash
   python -m pytest --cov=praktikum.burger --cov-report=term-missing
   ```

