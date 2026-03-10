import pytest
from praktikum.burger import Burger
from praktikum.data import MOVE_INGREDIENT_DATA, REMOVE_INGREDIENT_DATA


class TestBurger:
    def test_burger_initialization_bun_is_none(self, empty_burger):
        assert empty_burger.bun is None

    def test_burger_initialization_ingredients_empty(self, empty_burger):
        assert len(empty_burger.ingredients) == 0

    def test_burger_set_buns_bun_set_correctly(self, empty_burger, mock_bun):
        empty_burger.set_buns(mock_bun)
        assert empty_burger.bun == mock_bun

    def test_burger_add_ingredient_increases_length(self, empty_burger, mock_ingredient_sauce):
        empty_burger.add_ingredient(mock_ingredient_sauce)
        assert len(empty_burger.ingredients) == 1

    def test_burger_add_ingredient_adds_correct_ingredient(self, empty_burger, mock_ingredient_sauce):
        empty_burger.add_ingredient(mock_ingredient_sauce)
        assert empty_burger.ingredients[0] == mock_ingredient_sauce

    @pytest.mark.parametrize("test_data", REMOVE_INGREDIENT_DATA)
    def test_burger_remove_ingredient_decreases_length(self, empty_burger, mock_ingredient_sauce, 
                                                      mock_ingredient_filling, test_data):
        empty_burger.add_ingredient(mock_ingredient_sauce)
        empty_burger.add_ingredient(mock_ingredient_filling)
        empty_burger.remove_ingredient(test_data["index_to_remove"])
        assert len(empty_burger.ingredients) == test_data["expected_count"]

    def test_burger_remove_ingredient_removes_correct_index(self, empty_burger, mock_ingredient_sauce, 
                                                           mock_ingredient_filling):
        empty_burger.add_ingredient(mock_ingredient_sauce)
        empty_burger.add_ingredient(mock_ingredient_filling)
        empty_burger.remove_ingredient(0)
        assert empty_burger.ingredients[0] == mock_ingredient_filling

    def test_burger_move_ingredient_from_0_to_1(self, empty_burger, mock_ingredient_sauce,
                                                mock_ingredient_filling):
        empty_burger.add_ingredient(mock_ingredient_sauce)
        empty_burger.add_ingredient(mock_ingredient_filling)

        empty_burger.move_ingredient(0, 1)

        assert empty_burger.ingredients[0] == mock_ingredient_filling
        assert empty_burger.ingredients[1] == mock_ingredient_sauce

    def test_burger_move_ingredient_from_1_to_0(self, empty_burger, mock_ingredient_sauce,
                                                mock_ingredient_filling):
        empty_burger.add_ingredient(mock_ingredient_sauce)
        empty_burger.add_ingredient(mock_ingredient_filling)

        empty_burger.move_ingredient(1, 0)

        
        assert empty_burger.ingredients[0] == mock_ingredient_filling
        assert empty_burger.ingredients[1] == mock_ingredient_sauce



    def test_burger_move_ingredient_same_index_no_change(self, empty_burger, mock_ingredient_sauce, 
                                                        mock_ingredient_filling):
        empty_burger.add_ingredient(mock_ingredient_sauce)
        empty_burger.add_ingredient(mock_ingredient_filling)
        empty_burger.move_ingredient(0, 0)
        assert empty_burger.ingredients[0] == mock_ingredient_sauce

    def test_burger_get_price_calculates_correctly_with_mocks(self, burger_with_mocks, mock_bun, 
                                                             mock_ingredient_sauce):
        mock_bun.get_price.return_value = 100
        mock_ingredient_sauce.get_price.return_value = 100
        price = burger_with_mocks.get_price()
        assert price == 300  # 100*2 + 100

    def test_burger_get_price_without_bun_raises_error(self, empty_burger):
        with pytest.raises(AttributeError):
            empty_burger.get_price()

    def test_burger_get_receipt_contains_bun_name(self, burger_with_mocks, mock_bun):
        mock_bun.get_name.return_value = "black bun"
        receipt = burger_with_mocks.get_receipt()
        assert "black bun" in receipt

    def test_burger_get_receipt_contains_ingredient_info(self, burger_with_mocks, mock_ingredient_sauce):
        mock_ingredient_sauce.get_type.return_value = "SAUCE"
        mock_ingredient_sauce.get_name.return_value = "hot sauce"
        receipt = burger_with_mocks.get_receipt()
        assert "hot sauce" in receipt

    def test_burger_get_receipt_contains_price(self, burger_with_mocks):
        receipt = burger_with_mocks.get_receipt()
        assert "Price:" in receipt

    def test_burger_get_receipt_returns_string(self, burger_with_mocks):
        receipt = burger_with_mocks.get_receipt()
        assert isinstance(receipt, str)

    def test_burger_add_two_ingredients_length_two(self, empty_burger, mock_ingredient_sauce, 
                                                  mock_ingredient_filling):
        empty_burger.add_ingredient(mock_ingredient_sauce)
        empty_burger.add_ingredient(mock_ingredient_filling)
        assert len(empty_burger.ingredients) == 2