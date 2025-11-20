import random

import data
import mocks
from mocks import mock_ingredient
from praktikum.bun import Bun


def add_random_ingredient(burger):
    rand = random.randint(0, len(data.ingredients) - 1)
    ingredient = mock_ingredient(
        data.ingredients[rand][0],
        data.ingredients[rand][1],
        data.ingredients[rand][2]
    )
    burger.add_ingredient(ingredient)
    return burger


def burger_example(burger):
    ingredient_types = []
    ingredient_names = []
    ingredient_prices = []

    bun = Bun(data.bun[0], data.bun[1])
    burger.set_buns(bun)
    buns_price = bun.get_price() * 2

    for ingredient in data.ingredients:
        burger.add_ingredient(mock_ingredient(ingredient[0], ingredient[1], ingredient[2]))
        ingredient_types.append(ingredient[0].lower())
        ingredient_names.append(ingredient[1])
        ingredient_prices.append(ingredient[2])

    burger_price = buns_price + sum(ingredient_prices)
    testing_burger_data = [burger_price, bun, ingredient_types, ingredient_names, ingredient_prices]
    return testing_burger_data


def burger_example_receipt(burger):
    burger = burger_example(burger)
    receipt = (
         f'(==== {burger[1].get_name()} ====)\n'
         f'= {burger[2][0]} {burger[3][0]} =\n'
         f'= {burger[2][1]} {burger[3][1]} =\n'
         f'= {burger[2][2]} {burger[3][2]} =\n'
         f'= {burger[2][3]} {burger[3][3]} =\n'
         f'= {burger[2][4]} {burger[3][4]} =\n'
         f'= {burger[2][5]} {burger[3][5]} =\n'
         f'= {burger[2][6]} {burger[3][6]} =\n'
         f'(==== {burger[1].get_name()} ====)\n'
         f'\n'
         f'Price: {burger[0]}'
    )
    return receipt
