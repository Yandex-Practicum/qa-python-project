## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

test_bun.py
- test_bun_init_is_name, test_bun_init_is_price - проверка инициализации атрибутов булки
- test_bun_get_name_correct, test_bun_get_price_correct - проверка методов, возвращающих имя и цену

test_ingredient.py
- test_ingredient_init_is_type, test_ingredient_init_is_name, test_ingredient_init_is_price - проверка инициализации 
атрибутов ингредиента
- test_ingredient_get_type_correct, test_ingredient_get_name_correct, test_ingredient_get_price_correct - проверка 
методов, возвращающих тип, имя и цену 

test_burger.py
- test_burger_init_bun_is_none, test_burger_init_ingredients_is_empty_list - проверка инициализации атрибутов бургера
- test_burger_set_buns_bun_is_set - проверка метода, устанавливающего булку
- test_burger_add_ingredient_ingredient_is_added, test_burger_remove_ingredient_ingredient_is_removed, 
test_burger_move_ingredient_ingredient_is_moved - проверка методов, добавляющих, удаляющих и перемещающих ингредиент
- test_burger_get_price_price_is_correct - проверка метода, возвращающего цену бургера
- test_burger_get_receipt_bun_name_in_receipt, test_burger_get_receipt_sauce_name_in_receipt, 
test_burger_get_receipt_filling_name_in_receipt, test_burger_get_receipt_price_in_receipt_and_correct - проверка 
состава рецепта.

test_database.py
- test_database_init_buns_is_set, test_database_init_ingredients_is_set, test_database_init_sauces_in_ingredients, 
test_database_init_fillings_in_ingredients - проверка атрибутивного состава при инициализации
- test_database_available_buns_list_is_correct - проверка метода, возвращающего список булок
- test_database_available_ingredients_list_is_correct - проверка метода, возвращающего список ингредиентов

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам. Например, `test_bun.py`, `test_burger.py` и т.д.

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`
