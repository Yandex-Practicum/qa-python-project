def filter_ingredients_by_type(ingredients, ingredient_type):
    """
    Фильтрует список ингредиентов по заданному типу.
    :param ingredients: список ингредиентов
    :param ingredient_type: тип ингредиента (например, INGREDIENT_TYPE_SAUCE или INGREDIENT_TYPE_FILLING)
    :return: отфильтрованный список ингредиентов
    """
    return [ingredient for ingredient in ingredients if ingredient.get_type() == ingredient_type]