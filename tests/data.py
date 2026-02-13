#data.py

from unittest.mock import Mock


def get_price_test_cases():
    return [
        (100.0, [100.0, 200.0], 500.0),  # 100*2 + 100 + 200 = 500 (а не 400!)
        (200.0, [100.0, 200.0, 300.0], 1000.0),  # 200*2 + 100 + 200 + 300 = 1000 (а не 800!)
        (300.0, [], 600.0),  # 300*2 = 600 ✓
        (150.0, [50.0], 350.0),  # 150*2 + 50 = 350 ✓
    ]


def get_receipt_test_cases():
    return [
        (
            "black bun",
            100.0,
            [],
            ["(==== black bun ====)", "(==== black bun ====)", "", "Price: 200.0"]  # Пустая строка есть!
        ),
        (
            "white bun",
            200.0,
            [("SAUCE", "hot sauce", 100.0)],
            ["(==== white bun ====)", "= sauce hot sauce =", "(==== white bun ====)", "", "Price: 500.0"]  # Пустая строка есть!
        ),
        (
            "red bun",
            300.0,
            [
                ("SAUCE", "sour cream", 200.0),
                ("FILLING", "cutlet", 100.0)
            ],
            ["(==== red bun ====)", "= sauce sour cream =", "= filling cutlet =", "(==== red bun ====)", "", "Price: 900.0"]  # Пустая строка есть!
        ),
    ]


def create_burger_for_price_test(bun_price, ingredient_prices):
    """Создает бургер для теста цены"""
    from praktikum.burger import Burger
    
    burger = Burger()
    
    # Создаем булку
    mock_bun = Mock()
    mock_bun.get_price.return_value = bun_price
    
    # Настраиваем бургер
    burger.set_buns(mock_bun)
    
    # Добавляем ингредиенты
    for price in ingredient_prices:
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = price
        burger.add_ingredient(mock_ingredient)
    
    return burger


def create_burger_for_receipt_test(bun_name, bun_price, ingredients_data):
    """Создает бургер для теста рецепта"""
    from praktikum.burger import Burger
    
    burger = Burger()
    
    # Создаем булку
    mock_bun = Mock()
    mock_bun.get_name.return_value = bun_name
    mock_bun.get_price.return_value = bun_price
    burger.set_buns(mock_bun)
    
    # Добавляем ингредиенты
    for ingredient_type, name, price in ingredients_data:
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ingredient_type
        mock_ingredient.get_name.return_value = name
        mock_ingredient.get_price.return_value = price
        burger.add_ingredient(mock_ingredient)
    
    return burger