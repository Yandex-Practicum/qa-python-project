## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие класс  `Burger`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта
В файле test_burger.py подготовлено 6 тестов на проверку методов класса Burger:
1. Тест проверки добавления булочки в заказ с помощью метода set_buns - test_set_buns_add_bun_at_order.
2. Тест проверки добавления ингредиента в заказ с помощью метода add_ingredient - test_add_ingredient_add_ingriedient_at_order.
3. Тест проверки удаления ингредиента в заказе с помощью метода remove_ingredient - def test_remove_ingredient_remove_ingredient_from_order.   
4. Тест проверки перемещения ингредиента в заказе по позициям с помощью метода move_ingredient - def test_move_ingredient_swaps_positions_of_ingredients.
5. Тест проверки получения цены заказа с помощзью метода get_price - test_get_price_get_price_of_order.
6. Тест проверки получения подробностей заказа с помощью метода get_receipt test_get_receipt_get_check_of_order.


### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=burger --cov-report=html`
