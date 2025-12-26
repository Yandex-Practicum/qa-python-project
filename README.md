## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 77% (отчет: `htmlcov/index.html`)

### Структура проекта

-`praktikum` - пакет, содержащий код программы
-`tests` - пакет, содержащий тесты, разделенные по классам.

-'test_bun' - тесты на проверку класса 'Bun'включают в себя следующие тесты:
- test_bun_init_name_initialization_name_bun_is_successful - тест на проверку что корректно инициализируется имя булочки
- test_bun_init_price_initialization_price_bun_is_successful - тест на проверку что корректно инициализируется цена булочки
- test_bun_get_name_show_name_successful - тест на проверку что корректно работает метод get_name булочки
- test_bun_get_price_show_price_successful - тест на проверку что корректно работает метод get_price булочки

-  'test_burger' - тесты на проверку класса 'Burger' включают в себя следующие тесты:
- test_burger_init_bun_initialization_is_none - тест на проверку что bun инициализируется как None
- test_burger_init_ingredients_initialization_is_empty_list - тест на проверку что ingredients инициализируется как пустой список
- test_burger_set_buns_has_correct_name - тест на проверку что метод set_buns определяет булочку в бургере
- test_burger_add_ingredient_in_burger_is_successful - тест на проверку что метод add_ingredient добавляет ингредиент в бургер
- test_burger_remove_ingredient_in_burger_is_successful - тест на проверку что метод revome_ingredient удаляет ингредиент из бургера
- test_burger_move_ingredient_in_burger_is_successful - тест на проверку что метод move_ingredient изменяет позицию ингредиента в бургере
- test_burger_get_price_is_successful - тест на проверку что корректно работает метод get_price бургера
- test_burger_get_receipt_is_successful - тест на проверку что корректно работает метод get_receipt бургера

-  'test_database' - тесты на проверку класса 'Database' включают в себя следующие тесты:
- test_database_available_buns_returns_correct_list - тест на проверку что метод available_buns возвращает правильный список булочек
- test_database_available_ingredients_returns_correct_list - тест на проверку что метод available_ingredient возвращает правильный список ингредиентов

-  'test_ingredient' - тесты на проверку класса 'Ingredient' включают в себя следующие тесты:
- test_ingredient_init_type_initialization_is_correct - тест на проверку что корректно инициализируется type ингредиента
- test_ingredient_init_name_initialization_is_successful - тест на проверку что корректно инициализируется name ингредиента
- test_ingredient_init_price_initialization_is_successful - тест на проверку что корректно инициализируется price ингредиента
- test_ingredient_get_price_is_successful - тест на проверку что корректно работает метод get_price ингредиента
- test_ingredient_get_name_is_successful - тест на проверку что корректно работает метод get_name ингредиента
- test_ingredient_get_type_is_successful - тест на проверку что корректно работает метод get_type ингредиента

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`
