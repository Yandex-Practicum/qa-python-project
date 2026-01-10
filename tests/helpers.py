from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def create_mock_ingredient(name: str, ingredient_type: str, price: float) -> Mock:
    ingredient = Mock()
    ingredient.get_name = Mock(return_value=name)
    ingredient.get_type = Mock(return_value=ingredient_type)
    ingredient.get_price = Mock(return_value=price)
    return ingredient


def create_mock_bun(name: str, price: float) -> Mock:
    bun = Mock()
    bun.get_name = Mock(return_value=name)
    bun.get_price = Mock(return_value=price)
    return bun


def setup_burger_with_bun_and_ingredients(burger, bun, *ingredients):
    burger.set_buns(bun)
    for ingredient in ingredients:
        burger.add_ingredient(ingredient)
    return burger


def add_multiple_ingredients_to_burger(burger, ingredient_list):
    for ingredient in ingredient_list:
        burger.add_ingredient(ingredient)
    return burger


def calculate_burger_price(bun_price: float, ingredient_prices: list) -> float:
    return (bun_price * 2) + sum(ingredient_prices)


def extract_price_from_receipt(receipt: str) -> float:
    price_line = [line for line in receipt.split('\n') if line.startswith('Price:')]
    if price_line:
        return float(price_line[0].replace('Price: ', ''))
    return 0.0


def verify_ingredients_in_receipt(receipt: str, ingredient_names: list) -> bool:
    return all(name in receipt for name in ingredient_names)


def create_ingredients_list(count: int, ingredient_type: str, price: float) -> list:
    return [
        create_mock_ingredient(f"Ingredient_{i}", ingredient_type, price)
        for i in range(count)
    ]
