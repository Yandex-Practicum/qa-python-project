def ingredient_exists(ingredients, ingredient_name):
    return any(ingredient.get_name() == ingredient_name for ingredient in ingredients)