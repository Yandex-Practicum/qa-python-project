from unittest.mock import Mock

import data.ingredient_types as ingredient_types


class BurgerData:

    SAUCE_1 = (ingredient_types.INGREDIENT_TYPE_SAUCE, 'Ketchup', 1.1)
    SAUCE_2 = (ingredient_types.INGREDIENT_TYPE_SAUCE, 'Cheese sauce', 0.8)

    FILLING_1 = (ingredient_types.INGREDIENT_TYPE_FILLING, 'CHEESE', 2.5)
    FILLING_2 = (ingredient_types.INGREDIENT_TYPE_FILLING, 'BEEF', 100.9)

    DB_BUNS_NAMES = ["black bun", "white bun", "red bun"]
    DB_BUNS_PRICES = [100, 200, 300]

    DB_SAUCES = ["hot sauce", "sour cream", "chili sauce"]
    DB_FILLINGS = ["cutlet", "dinosaur", "sausage"]

    BUN_1 = ("BIG BUN", 1.0)
    BUN_2 = ("Булка с кунжутом", 10)
    BUN_3 = ("Best Bun", 0.5)


class MockData:
    mock_bun = Mock()
    mock_bun.get_name.return_value = "Mock Bun"
    mock_bun.get_price.return_value = 1.0

    mock_ingredient_1 = Mock()
    mock_ingredient_1.get_type.return_value = ingredient_types.INGREDIENT_TYPE_SAUCE
    mock_ingredient_1.get_name.return_value = "Mock sauce"
    mock_ingredient_1.get_price.return_value = 1.1

    mock_ingredient_2 = Mock()
    mock_ingredient_2.get_type.return_value = ingredient_types.INGREDIENT_TYPE_FILLING
    mock_ingredient_2.get_name.return_value = "Mock filling"
    mock_ingredient_2.get_price.return_value = 2.5

    MOCK_RECEIPT = "(==== Mock Bun ====)\n" \
                   "= sauce Mock sauce =\n" \
                   "= sauce Mock sauce =\n" \
                   "= filling Mock filling =\n" \
                   "(==== Mock Bun ====)\n\n" \
                   "Price: 6.7"



