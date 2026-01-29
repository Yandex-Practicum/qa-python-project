## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 81% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам:
  - 'conftest.py' содержит три фикстуры (для bun без моков, для мокирования экзмепляра в БД и мокирование экземпляра бургера);
  - 'test_bun.py' содержит класс TestBun;
  - 'test_burger.py' содержит класс TestBurger;
  - 'test_database.py' содержит класс TestDataBase;
  - 'test_ingridient.py' содержит класс TestIngredient.
- 'data.py' содержит класс Ingredients для удобной работы.

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`
