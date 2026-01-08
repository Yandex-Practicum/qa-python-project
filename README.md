## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам:
  - `bun_test.py` - тесты для класса Bun
  - `burger_test.py` - тесты для класса Burger  
  - `ingredient_test.py` - тесты для класса Ingredient
  - `database_test.py` - тесты для класса Database
- `htmlcov/` - отчет о покрытии тестами 

### Запуск автотестов

**Установка зависимостей**
```bash
pip install -r requirements.txt
```

**Запуск всех тестов**
```bash
python -m pytest tests/
```

**Запуск автотестов и создание HTML-отчета о покрытии**
```bash
python -m pytest --cov=praktikum --cov-report=html tests/
```