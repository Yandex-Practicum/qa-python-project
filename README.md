## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия `88%` - [отчет](http://localhost:63342/Diplom_1/htmlcov/index.html?_ijt=5sov2ma8lqerkf98tjs1f7vbuj&_ij_reload=RELOAD_ON_SAVE)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам -  `test_bun.py`, `test_burger.py`, `test_database.py` и `test_ingredient.py`
- `data` - файл, содержащий набор тестовых данных
- `conftest` - файл, содержащий фикстуры используемых в тестах
- `requirements` - файл, содержащий список внешних зависимостей
- `allure-results` - пакет, содержащий результаты прохождения отчётов
- `htmlcov` - пакет, содержащий данные о покрытии автотестов

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`
