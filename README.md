# Юнит-тесты для Stellar Burgers

Автоматизированные юнит-тесты для программы заказа бургеров в Stellar Burgers.

## Структура проекта
project/
├── praktikum/ # Исходный код программы
│ ├── init.py
│ ├── bun.py
│ ├── burger.py
│ ├── database.py
│ ├── ingredient.py
│ ├── ingredient_types.py
│ └── praktikum.py
├── tests/ # Тесты
│ ├── init.py
│ ├── conftest.py
│ ├── test_bun.py
│ ├── test_burger.py
│ ├── test_ingredient.py
│ └── test_database.py
├── requirements.txt
├── pytest.ini
└── README.md

## Запуск тестов

### Установка зависимостей
```bash
pip install -r requirements.txt
Запуск всех тестов с отчетом о покрытии
pytest
Запуск конкретных тестов
# Только тесты для Burger
pytest tests/test_burger.py -v

# Тесты с детальным отчетом о покрытии
pytest --cov=praktikum --cov-report=term-missing

# Генерация HTML отчета
pytest --cov=praktikum --cov-report=html
Покрытие кода
После запуска тестов будет сгенерирован HTML отчет в папке htmlcov/.
Откройте htmlcov/index.html в браузере для просмотра детального отчета о покрытии.

Требуемое покрытие: 100%

## 4. Команды для запуска

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск всех тестов
pytest

# Запуск с детальным отчетом
pytest -v

# Проверка покрытия
pytest --cov=praktikum --cov-report=term-missing

# Генерация HTML отчета
pytest --cov=praktikum --cov-report=html

# Просмотр отчета
open htmlcov/index.html  # Mac
# или
start htmlcov/index.html  # Windows
