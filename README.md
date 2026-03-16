## Дипломный проект. Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам. Например, `bun_test.py`, `burger_test.py` и т.д.

### Запуск автотестов

Клонируйте репозиторий
git clone ...
cd ... # ← ВАЖНО: перейти в папку проекта

Создайте виртуальное окружение
python -m venv venv или python3 -m venv venv

Активируйте виртуальное окружение
venv\Scripts\Activate.ps1 # Windows PS venv\Scripts\activate.bat # Windows CMD source venv/bin/activate # MacOS

Деактивация (необязательный шаг)
deactivate

Установите зависимости
pip install -r requirements.txt # Установка основных библиотек

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=. --cov-report=html`
