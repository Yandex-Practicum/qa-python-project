from typing import List
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class BunData:
    bun_name = 'white bun'
    bun_price = 200

class AvailableIngredients:
    sauces = [
        {
            'name': 'hot sauce',
            'price': 100,
        },
        {
            'name': 'sour cream',
            'price': 200,
        },
        {
            'name': 'chili sauce',
            'price': 300,
        },
    ]
    fillings = [
        {
            'name': 'cutlet',
            'price': 100,
        },
        {
            'name': 'dinosaur',
            'price': 200,
        },
        {
            'name': 'sausage',
            'price': 300,
        },
    ]

class MockBun:
    @staticmethod
    def get_mock_bun() -> Bun:
        bun = Mock()
        bun.get_name.return_value = BunData.bun_name
        bun.get_price.return_value = BunData.bun_price
        return bun

class MockIngredient:
    @staticmethod
    def get_mock_ingredient(ingredient_type, ingredient_name, ingredient_price) -> Ingredient:
        ingredient = Mock()
        ingredient.get_type.return_value = ingredient_type
        ingredient.get_name.return_value = ingredient_name
        ingredient.get_price.return_value = ingredient_price
        return ingredient

class BurgerReceipt:
    @staticmethod
    def get_receipt(bun: Bun, ingredients: List[Ingredient]):
        price = bun.get_price() * 2
        receipt = f'(==== {bun.get_name()} ====)\n'
        for ingredient in ingredients:
            receipt += f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =\n'
            price += ingredient.get_price()
        receipt += f'(==== {bun.get_name()} ====)\n\n'
        receipt += f'Price: {price}'
        return receipt

class IngredientsCombinations:
    only_sauce = [MockIngredient.get_mock_ingredient(
        INGREDIENT_TYPE_SAUCE,
        AvailableIngredients.sauces[0]['name'],
        AvailableIngredients.sauces[0]['price']
    )]
    only_filling = [MockIngredient.get_mock_ingredient(
        INGREDIENT_TYPE_FILLING,
        AvailableIngredients.fillings[0]['name'],
        AvailableIngredients.fillings[0]['price']
    )]
    two_same_sauces = [
        MockIngredient.get_mock_ingredient(
            INGREDIENT_TYPE_SAUCE,
            AvailableIngredients.sauces[1]['name'],
            AvailableIngredients.sauces[1]['price']
        ),
        MockIngredient.get_mock_ingredient(
            INGREDIENT_TYPE_SAUCE,
            AvailableIngredients.sauces[1]['name'],
            AvailableIngredients.sauces[1]['price']
        )
    ]
    two_same_fillings = [
        MockIngredient.get_mock_ingredient(
            INGREDIENT_TYPE_FILLING,
            AvailableIngredients.fillings[1]['name'],
            AvailableIngredients.fillings[1]['price']
        ),
        MockIngredient.get_mock_ingredient(
            INGREDIENT_TYPE_FILLING,
            AvailableIngredients.fillings[1]['name'],
            AvailableIngredients.fillings[1]['price']
        )
    ]
    tree_different_ingredients = [
        MockIngredient.get_mock_ingredient(
            INGREDIENT_TYPE_SAUCE,
            AvailableIngredients.sauces[0]['name'],
            AvailableIngredients.sauces[0]['price']
        ),
        MockIngredient.get_mock_ingredient(
            INGREDIENT_TYPE_SAUCE,
            AvailableIngredients.sauces[2]['name'],
            AvailableIngredients.sauces[2]['price']
        ),
        MockIngredient.get_mock_ingredient(
            INGREDIENT_TYPE_FILLING,
            AvailableIngredients.fillings[1]['name'],
            AvailableIngredients.fillings[1]['price']
        )
    ]

burgers_variants = [
    (MockBun.get_mock_bun(), IngredientsCombinations.only_sauce, 500),
    (MockBun.get_mock_bun(), IngredientsCombinations.only_filling, 500),
    (MockBun.get_mock_bun(), IngredientsCombinations.two_same_sauces, 800),
    (MockBun.get_mock_bun(), IngredientsCombinations.two_same_fillings, 800),
    (MockBun.get_mock_bun(), IngredientsCombinations.tree_different_ingredients, 1000)
]