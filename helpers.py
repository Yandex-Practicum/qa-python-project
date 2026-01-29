def get_ingredient_count_by_type(ingredients, ingredient_type):
    return len([ingredient for ingredient in ingredients if ingredient.type == ingredient_type])

def get_bun_names(buns):
    return [bun.name for bun in buns]