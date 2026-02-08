from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestData:
    buns = [
        ["black bun", 100],
        ["white bun", 200],
        ["red bun", 300]
    ]

    ingredients = [
        [INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
        [INGREDIENT_TYPE_SAUCE, "sour cream", 200],
        [INGREDIENT_TYPE_SAUCE, "chili sauce", 300],
        [INGREDIENT_TYPE_FILLING, "cutlet", 100],
        [INGREDIENT_TYPE_FILLING, "dinosaur", 200],
        [INGREDIENT_TYPE_FILLING, "sausage", 300]
    ]

    EXPECTED_CHECK = (
        f"(==== {buns[0][0]} ====)\n"
        f"= sauce {ingredients[0][1]} =\n"
        f"= filling {ingredients[3][1]} =\n"
        f"(==== {buns[0][0]} ====)\n\n"
        f"Price: {buns[0][1] * 2 + ingredients[0][2] + ingredients[3][2]}"
    )

    EXPECTED_CHECK_NO_INGREDIENT = (
    f"(==== {buns[0][0]} ====)\n"
    f"(==== {buns[0][0]} ====)\n\n"
    f"Price: {buns[0][1] * 2}"
)