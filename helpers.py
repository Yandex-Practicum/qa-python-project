from praktikum.ingredient import Ingredient


def add_multiple_ingredients(burger, ingredients_list):
    for i in range(len(ingredients_list)):
        ingredient = Ingredient(*ingredients_list[i])
        burger.add_ingredient(ingredient)
    return burger