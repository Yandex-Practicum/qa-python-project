from praktikum.burger import Burger
import pytest
import praktikum.ingredient_types as IT


class TestBurger:
    def test_burger_init_bun(self):
        burger = Burger()
        assert burger.bun == None

    def test_burger_init_ingr(self):
        burger = Burger()
        assert burger.ingredients == []

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun.name == mock_bun.name and burger.bun.price == mock_bun.price

    @pytest.mark.parametrize('type_ingredient', [IT.INGREDIENT_TYPE_FILLING, IT.INGREDIENT_TYPE_SAUCE])
    def test_add_ingredient(self, mock_ingredient_1, type_ingredient):
        burger = Burger()
        mock_ingredient_1.type = type_ingredient
        burger.add_ingredient(mock_ingredient_1)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].type == mock_ingredient_1.type
        assert burger.ingredients[0].name == mock_ingredient_1.name
        assert burger.ingredients[0].price == mock_ingredient_1.price

    @pytest.mark.parametrize('type_ingredient', [IT.INGREDIENT_TYPE_FILLING, IT.INGREDIENT_TYPE_SAUCE])
    def test_remove_ingredient(self, mock_ingredient_1, type_ingredient):
        burger = Burger()
        mock_ingredient_1.type = type_ingredient
        burger.add_ingredient(mock_ingredient_1)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, mock_ingredient_1, mock_ingredient_2):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_1]

    def test_get_price(self, mock_bun, mock_ingredient_1, mock_ingredient_2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        assert burger.get_price() == mock_bun.price * 2 + mock_ingredient_1.price + mock_ingredient_2.price

    def test_get_receipt(self, mock_bun, mock_ingredient_1, mock_ingredient_2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)

        correct_receipt = '\n'.join([
                        "(==== name_bun ====)",
                        "= filling name_ingredient_1 =",
                        "= sauce name_ingredient_2 =",
                        "(==== name_bun ====)",
                        "",
                        "Price: 250"
                        ])

        assert burger.get_receipt() == correct_receipt