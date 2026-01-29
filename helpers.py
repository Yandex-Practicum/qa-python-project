from praktikum.ingredient import Ingredient


#добавление ингредиента в бургер
def add_ingredient_in_burger(ingredient_type, ingredient_name, ingredient_price, burger):
    ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
    burger.add_ingredient(ingredient)
    return burger.ingredients


