## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам. Например, `bun_test.py`, `burger_test.py` и т.д.

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`

# Юнит-тесты, разделенные по классам:

  # Класс TestBun:

    # Проверка работы метода get_name объекта класса Bun
    test_get_name_all_types
	
    # Проверка работы метода get_price объекта класса Bun
    test_get_price_all_types

  # Класс TestIngredient:

    # Проверка работы метода get_name объекта класса Ingredient
    test_get_name_all_types
	
    # Проверка работы метода get_price объекта класса Ingredient
    test_get_price_all_types
	
    # Проверка работы метода get_type объекта класса Ingredient
    test_get_type_all_types
	
  # Класс TestBurger:

    # Проверка возможности создать объект класса Burger с замокированной черной булкой методом set_buns
    test_set_buns_all_types
	
    # Проверка возможности создать объект класса Burger с 2 замокированными ингредиентами методом add_ingredient
    test_add_ingredient_add_2_ingredients
	
    # Проверка возможности создать объект класса Burger с 2 ингредиентами и поменять их местами методом move_ingredient
    test_move_ingredient_1_of_2_ingredients
	
    # Проверка возможности создать объект класса Burger с 2 ингредиентами и удалить один из них методом remove_ingredient
    test_remove_ingredient_1_of_2_ingredients
	
    # Проверка возможности создать объект класса Burger с булкой и 2 ингредиентами и сформировать его стоимость методом get_price
    test_get_price_bun_and_2_ingredients
	
    # Проверка возможности создать объект класса Burger с булкой и 2 ингредиентами и сформировать его рецепт методом get_receipt
    test_get_receipt_bun_and_2_ingredients
	
  # Класс TestDatabase:

    # Проверка возможности создать объект класса Database с добавлением и выводом списка доступных булок методом available_buns
    test_available_buns_list_of_3_and_7_buns
	
    # Проверка возможности создать объект класса Database с добавлением и выводом списка доступных ингредиентов методом available_ingredients
    test_available_ingredients_list_of_6_and_9_ingredients
