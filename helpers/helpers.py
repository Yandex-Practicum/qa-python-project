from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class BunTestData:
    name = 'slim'
    price = 11.1


class BurgerTestInitData:
    bun = None
    ingredients = []


class BurgerTestData:
    exempl_bun = Bun("exo", 11.22)
    exempl_ingred = Ingredient('red', 'paper', 9.7)
    exempl_ingred_sec = Ingredient('ice', 'berry', 9.7)

    @staticmethod
    def gen_receipt(bun, ingredients_list):
        receipt = [f'(==== {bun.get_name()} ====)']
        price = bun.get_price() * 2
        for ingredient in ingredients_list:
            receipt.append(f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =')
            price += ingredient.get_price()
        receipt.append(f'(==== {bun.get_name()} ====)\n')
        receipt.append(f'Price: {price}')
        return '\n'.join(receipt)


class IngredientTestData:
    type = "green"
    name = 'onion'
    price = 3.3
