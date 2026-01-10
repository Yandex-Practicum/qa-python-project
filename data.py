from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestBunData:

    name = "Краторная булка N-200i"
    price = 200.0

class TestIngredientData:
    ingredient_type = INGREDIENT_TYPE_SAUCE
    name = "Соус с шипами Антарианского плоскоходца"
    price = 100.0

class TestAnotherIngredientData:
    ingredient_type = INGREDIENT_TYPE_FILLING
    name = "Мини-салат Экзо-Плантаго"
    price = 110.0

class TestReceiptData:
    receipt = (
        "(==== Краторная булка N-200i ====)\n"
        "= sauce Соус с шипами Антарианского плоскоходца =\n"
        "= filling Мини-салат Экзо-Плантаго =\n"
        "(==== Краторная булка N-200i ====)\n"
        "\n"
        "Price: 610.0"
    )

test_ingredient_parametrize_data = [
    [INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 15.0],
    [INGREDIENT_TYPE_FILLING, "Говяжий метеорит (отбивная)", 3000.0],
]

buns_mock_data = [
    Bun("tasty bun", 300),
    Bun("hot bun", 100),
    Bun("draco bun", 200),
]

ingredients_mock_data = [
    Ingredient(INGREDIENT_TYPE_SAUCE, "dobby tears", 100),
    Ingredient(INGREDIENT_TYPE_SAUCE, "water sauce", 150),
    Ingredient(INGREDIENT_TYPE_SAUCE, "happy sauce", 200),
    Ingredient(INGREDIENT_TYPE_FILLING, "dragon", 250),
    Ingredient(INGREDIENT_TYPE_FILLING, "naggets", 300),
    Ingredient(INGREDIENT_TYPE_FILLING, "elf", 350),
]

main_expected_result = """
(==== tasty bun ====)
= sauce water sauce =
= filling dragon =
= filling naggets =
(==== tasty bun ====)

Price: 1300
""".lstrip()
