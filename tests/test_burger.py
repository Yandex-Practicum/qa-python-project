import pytest

from data import TEST_BURGER, TEST_ADD_INGREDIENTS, TEST_REMOVE_INGREDIENTS, TEST_MOVE_INGREDIENTS, TEST_RECEIPT_DATA
from praktikum.bun import Bun
from unittest.mock import patch, MagicMock
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns_bun_is_set(self):
        bun_data = TEST_BURGER[0]
        mock_bun = MagicMock(spec=Bun)
        mock_bun.get_name.return_value = bun_data['name']
        mock_bun.get_price.return_value = bun_data['price']
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun, f'Метод "set_buns" не установил булочку.'

    @pytest.mark.parametrize(
        'ingredient_data', TEST_ADD_INGREDIENTS
    )
    @patch('praktikum.ingredient.Ingredient')
    def test_add_ingredient_check_addition_of_ingredients_to_list(self, mockIngredient, ingredient_data):
        mock_ingredient = mockIngredient.return_value
        mock_ingredient.get_type.return_value = ingredient_data['ingredient_type']
        mock_ingredient.get_name.return_value = ingredient_data['name']
        mock_ingredient.get_price.return_value = ingredient_data['price']
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [
            mock_ingredient], f'Ингредиенты должны быть добавлены в список, но получили {burger.ingredients}'

    @pytest.mark.parametrize(
        'ingredient_data', TEST_REMOVE_INGREDIENTS
    )
    @patch('praktikum.ingredient.Ingredient')
    def test_remove_ingredient_removing_ingredients_from_list(self, mockingredient, ingredient_data):
        mock_ingredient = mockingredient.return_value
        mock_ingredient.get_type.return_value = ingredient_data['ingredient_type']
        mock_ingredient.get_name.return_value = ingredient_data['name']
        mock_ingredient.get_price.return_value = ingredient_data['price']
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == [], f'Ингредиенты должны быть удалены по индексу из списка.'

    @pytest.mark.parametrize(
        'ingredient_data', TEST_MOVE_INGREDIENTS
    )
    @patch('praktikum.ingredient.Ingredient')
    def test_move_ingredient_first_to_last(self, mockingredient, ingredient_data):
        mock_ingredient_1 = mockingredient.return_value
        mock_ingredient_1.get_type.return_value = ingredient_data['ingredient_type']
        mock_ingredient_1.get_name.return_value = ingredient_data['name']
        mock_ingredient_1.get_price.return_value = ingredient_data['price']

        mock_ingredient_2 = mockingredient.return_value
        mock_ingredient_2.get_type.return_value = ingredient_data['ingredient_type']
        mock_ingredient_2.get_name.return_value = ingredient_data['name']
        mock_ingredient_2.get_price.return_value = ingredient_data['price']

        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_1], \
            f'Первый ингредиент должен быть перемещен в конец.'

    def test_get_price_cost_calculation(self):
        mock_bun = MagicMock()
        mock_bun.get_price.return_value = 2.50
        mock_ingredient1 = MagicMock()
        mock_ingredient1.get_price.return_value = 1.00
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient1]
        expected_price = 2.50 * 2 + 1.00

        assert burger.get_price() == expected_price, f'Ожидаемая цена: {expected_price}, но получено: {burger.get_price()}'

    def test_get_receipt(self):
        data = TEST_RECEIPT_DATA[0]
        mock_bun = MagicMock()
        mock_bun.get_name.return_value = data['bun_name']
        mock_ingredient = MagicMock()
        mock_ingredient.get_name.return_value = data['ingredient_name']
        mock_ingredient.get_type.return_value = data['ingredient_type']
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        burger.get_price = MagicMock(return_value=data['price'])
        receipt = burger.get_receipt()

        assert receipt == data['expected_receipt'], \
            f'Ожидалось, что чек будет: {data["expected_receipt"]}, но получено: {receipt}'
