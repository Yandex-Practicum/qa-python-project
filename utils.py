'''Additional utils for testig'''


def set_burger_ingrs(burger, *ingredients, bun=None):
    burger.bun = bun
    burger.ingredients = list(ingredients)
    return burger  # set bun and ingredients to burger


def expected_price(*ingredients, bun):
    price = bun.get_price() * 2
    for ingredient in ingredients:
        price += ingredient.get_price()
    return price  # calculate expected price


def get_buns_data(buns):
    return [(bun.get_name(), bun.get_price()) for bun in buns]  # return bun data


def get_ingredients_data(ingredients):
    return [(
        ingredient.get_type(), ingredient.get_name(), ingredient.get_price()  # return ingredients data
    )
        for ingredient in ingredients
    ]
