import pytest
from burger import Burger
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

def test_burger_price_and_receipt():
    bun = Bun("white bun", 200.0)
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0))
    burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150.0))
    expected_price = bun.get_price() * 2 + 100.0 + 150.0
    assert burger.get_price() == expected_price

def test_burger_receipt_format():
    bun = Bun("black bun", 100.0)
    burger = Burger()
    burger.set_buns(bun)
    ing1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0)
    ing2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150.0)
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    receipt = burger.get_receipt()
    expected_lines = [
        f"(==== {bun.get_name()} ====)",
        f"= {ing1.get_type().lower()} {ing1.get_name()} =",
        f"= {ing2.get_type().lower()} {ing2.get_name()} =",
        f"(==== {bun.get_name()} ====)\n",
        f"Price: {burger.get_price()}",
    ]
    expected = "\n".join(expected_lines)
    assert receipt == expected

def test_burger_move_and_remove_ingredient():
    bun = Bun("sesame", 120.0)
    burger = Burger()
    burger.set_buns(bun)
    ing1 = Ingredient(INGREDIENT_TYPE_SAUCE, "sauce", 10.0)
    ing2 = Ingredient(INGREDIENT_TYPE_FILLING, "patty", 20.0)
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    burger.move_ingredient(0, 1)
    receipt_after_move = burger.get_receipt()
    assert ing2.get_name() in receipt_after_move
    burger.remove_ingredient(0)
    receipt_after_removal = burger.get_receipt()
    assert ing2.get_name() not in receipt_after_removal
    assert ing1.get_name() in receipt_after_removal

@pytest.mark.parametrize("bun_price, ing_prices, expected", [
    (100.0, [50.0, 60.0], 100.0*2 + 50 + 60),
    (150.0, [], 150.0*2),
    (200.0, [100.0], 200.0*2 + 100.0),
])
def test_burger_price_with_params(bun_price, ing_prices, expected):
    bun = Bun("test bun", bun_price)
    burger = Burger()
    burger.set_buns(bun)
    for p in ing_prices:
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "filling", p))
    assert burger.get_price() == expected