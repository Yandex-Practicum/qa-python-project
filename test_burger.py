import pytest
from unittest.mock import Mock
from burger import Burger
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_assign_buns(self):
        sample = Burger()
        fake_bun = Mock(spec=Bun)

        sample.set_buns(fake_bun)

        assert sample.bun is fake_bun

    def test_insert_ingredient(self):
        sample = Burger()
        fake_ing = Mock(spec=Ingredient)

        sample.add_ingredient(fake_ing)

        assert len(sample.ingredients) == 1
        assert sample.ingredients[0] is fake_ing

    def test_delete_ingredient(self):
        sample = Burger()
        ing_a = Mock(spec=Ingredient)
        ing_b = Mock(spec=Ingredient)

        sample.add_ingredient(ing_a)
        sample.add_ingredient(ing_b)

        sample.remove_ingredient(0)

        assert len(sample.ingredients) == 1
        assert sample.ingredients[0] is ing_b

    def test_relocate_ingredient(self):
        sample = Burger()
        i1 = Mock(spec=Ingredient)
        i2 = Mock(spec=Ingredient)
        i3 = Mock(spec=Ingredient)

        for ing in (i1, i2, i3):
            sample.add_ingredient(ing)

        sample.move_ingredient(0, 2)

        assert sample.ingredients == [i2, i3, i1]

    @pytest.mark.parametrize(
        "bun_cost,ing_costs,total",
        [
            (100, [50, 75], 325),
            (50, [25, 30, 45], 200),
            (200, [], 400),
            (0, [10, 20], 30),
        ]
    )
    def test_cost_various_sets(self, bun_cost, ing_costs, total):
        sample = Burger()

        bun_mock = Mock(spec=Bun)
        bun_mock.get_price.return_value = bun_cost
        sample.set_buns(bun_mock)

        for value in ing_costs:
            ing_mock = Mock(spec=Ingredient)
            ing_mock.get_price.return_value = value
            sample.add_ingredient(ing_mock)

        calc = sample.get_price()
        assert calc == total
        bun_mock.get_price.assert_called_once()

    def test_price_triggers_methods(self):
        sample = Burger()

        bun_mock = Mock(spec=Bun)
        bun_mock.get_price.return_value = 100
        sample.set_buns(bun_mock)

        i1 = Mock(spec=Ingredient)
        i1.get_price.return_value = 50

        i2 = Mock(spec=Ingredient)
        i2.get_price.return_value = 75

        sample.add_ingredient(i1)
        sample.add_ingredient(i2)

        assert sample.get_price() == 325

        bun_mock.get_price.assert_called_once()
        i1.get_price.assert_called_once()
        i2.get_price.assert_called_once()

    @pytest.mark.parametrize(
        "bun_label,ings,expected",
        [
            (
                "black bun",
                [
                    (INGREDIENT_TYPE_SAUCE, "hot sauce"),
                    (INGREDIENT_TYPE_FILLING, "cutlet"),
                ],
                [
                    "(==== black bun ====)",
                    "= sauce hot sauce =",
                    "= filling cutlet =",
                    "(==== black bun ====)",
                    "",
                    "Price: 0",
                ],
            ),
            (
                "white bun",
                [
                    (INGREDIENT_TYPE_FILLING, "dinosaur"),
                    (INGREDIENT_TYPE_SAUCE, "sour cream"),
                ],
                [
                    "(==== white bun ====)",
                    "= filling dinosaur =",
                    "= sauce sour cream =",
                    "(==== white bun ====)",
                    "",
                    "Price: 0",
                ],
            ),
        ]
    )
    def test_receipt_structure(self, bun_label, ings, expected):
        sample = Burger()

        bun_mock = Mock(spec=Bun)
        bun_mock.get_name.return_value = bun_label
        bun_mock.get_price.return_value = 0
        sample.set_buns(bun_mock)

        for t, nm in ings:
            ing = Mock(spec=Ingredient)
            ing.get_type.return_value = t
            ing.get_name.return_value = nm
            ing.get_price.return_value = 0
            sample.add_ingredient(ing)

        result = sample.get_receipt().split("\n")

        assert len(result) == len(expected)
        for idx, line in enumerate(expected):
            assert result[idx] == line

    def test_receipt_price_display(self):
        sample = Burger()

        bun_mock = Mock(spec=Bun)
        bun_mock.get_name.return_value = "red bun"
        bun_mock.get_price.return_value = 100
        sample.set_buns(bun_mock)

        ing = Mock(spec=Ingredient)
        ing.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ing.get_name.return_value = "chili sauce"
        ing.get_price.return_value = 50

        sample.add_ingredient(ing)

        data = sample.get_receipt()

        assert "Price: 250" in data
        assert "(==== red bun ====)" in data
        assert "= sauce chili sauce =" in data

    def test_receipt_single_bun(self):
        sample = Burger()

        bun_mock = Mock(spec=Bun)
        bun_mock.get_name.return_value = "white bun"
        bun_mock.get_price.return_value = 200
        sample.set_buns(bun_mock)

        lines = sample.get_receipt().split("\n")

        expected = [
            "(==== white bun ====)",
            "(==== white bun ====)",
            "",
            "Price: 400",
        ]

        assert lines == expected

    def test_remove_out_of_range(self):
        sample = Burger()
        ing = Mock(spec=Ingredient)
        sample.add_ingredient(ing)

        with pytest.raises(IndexError):
            sample.remove_ingredient(99)

    def test_move_out_of_range(self):
        sample = Burger()
        ing = Mock(spec=Ingredient)
        sample.add_ingredient(ing)

        with pytest.raises(IndexError):
            sample.move_ingredient(10, 0)

    def test_receipt_lowercase_types(self):
        sample = Burger()

        bun_mock = Mock(spec=Bun)
        bun_mock.get_name.return_value = "test bun"
        bun_mock.get_price.return_value = 0
        sample.set_buns(bun_mock)

        sc = Mock(spec=Ingredient)
        sc.get_type.return_value = INGREDIENT_TYPE_SAUCE
        sc.get_name.return_value = "test sauce"
        sc.get_price.return_value = 0

        fl = Mock(spec=Ingredient)
        fl.get_type.return_value = INGREDIENT_TYPE_FILLING
        fl.get_name.return_value = "test filling"
        fl.get_price.return_value = 0

        sample.add_ingredient(sc)
        sample.add_ingredient(fl)

        data = sample.get_receipt()

        assert "= sauce test sauce =" in data
        assert "= filling test filling =" in data