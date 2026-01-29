import random

class BurgerHelper:
    @staticmethod
    def add_a_few_ingredients(burger, mocks_ingredients, slise: list):
        ingredients = mocks_ingredients[slise[0]: slise[1]]
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)
        return ingredients

    @staticmethod
    def add_ingredients_and_give_price(burger, mocks_ingredients, number):
        price_ingredients = 0
        for i in range(number):
            ingredient = mocks_ingredients[i]
            burger.add_ingredient(ingredient)
            price_ingredients += ingredient.get_price()
        return price_ingredients

    @staticmethod
    def add_ingredients_and_give_data(burger, mocks_ingredients, number):
        price_ingredients = 0
        part_receipt = ''
        for i in range(number):
            ingredient = mocks_ingredients[i]
            price_ingredients += ingredient.get_price()
            burger.add_ingredient(ingredient)
            part_receipt += f"= {ingredient.get_type()} {ingredient.get_name()} =\n"
        return part_receipt, price_ingredients



class DataBun:
    name = ['Флюоресцентная', 'Краторная']
    price = [988, 1255]

    @classmethod
    def get_data_bun(cls):
        return random.choice(cls.name), random.choice(cls.price)


class DataIngredient:
    name = ['Spicy-X', 'Space Sauce']
    price = [90, 80]
    type = ['sauce', 'filling']

    @classmethod
    def get_data_ingredient(cls):
        return random.choice(cls.name), random.choice(cls.price), random.choice(cls.type)

