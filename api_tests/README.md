# API Tests for Stellar Burgers

Автотесты для API сервиса Stellar Burgers.

## Структура проекта

- `tests/` - тестовые сценарии
- `helpers/` - вспомогательные классы
- `utils/` - утилиты для работы с Allure
- `requirements.txt` - зависимости

## Установка и запуск

1. Клонировать репозиторий:
```bash
git clone <repository-url>
cd api-tests

## Команды для запуска

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск всех тестов
pytest

# Запуск с детальным выводом
pytest -v

# Запуск конкретного тестового файла
pytest tests/test_user_api.py -v

# Запуск с генерацией Allure отчетов
pytest --alluredir=allure-results

# Просмотр Allure отчета
allure serve allure-results
