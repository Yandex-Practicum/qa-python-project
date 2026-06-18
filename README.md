## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам:
- Для `Bun` и `Ingredient` использована параметризация
- Для `Burger` использованы моки
- Для `Database` проверяются типы и контрольные значения

### Запуск автотестов

**Установка зависимостей**

> `pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**
python -m pytest -v
python -m pytest --cov=praktikum --cov-report=html

## Покрытие
```bash
python -m pytest -v
python -m pytest --cov=praktikum --cov-report=term-missing
python -m pytest --cov=praktikum --cov-report=html
```