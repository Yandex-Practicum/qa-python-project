from unittest.mock import patch

from data import TEST_BUNS, TEST_AVAILABLE_INGREDIENTS
from praktikum.database import Database


class TestDataBase:
    @patch('praktikum.database.Bun', autospec=True)
    def test_available_buns_return_buns(self, mockbun):
        bun_data = TEST_BUNS[0]
        mock_bun1 = mockbun.return_value
        mock_bun1.get_name.return_value = bun_data['name']
        mock_bun1.get_price.return_value = bun_data['price']
        database = Database()
        database.buns = [mock_bun1]
        buns = database.available_buns()

        assert buns == [
            mock_bun1], f'Метод "available_buns" должен возвращать булочку с именем \
            "{bun_data["name"]}" и ценой {bun_data["price"]}.'

    @patch('praktikum.database.Ingredient', autospec=True)
    def test_available_ingredients_return_ingredients(self, mockingredient):
        ingredient_data = TEST_AVAILABLE_INGREDIENTS[0]
        mock_ingredient1 = mockingredient.return_value
        mock_ingredient1.get_name.return_value = ingredient_data['name']
        mock_ingredient1.get_type.return_value = ingredient_data['ingredient_type']
        database = Database()
        database.ingredients = [mock_ingredient1]
        ingredients = database.available_ingredients()

        assert ingredients == [
            mock_ingredient1], f'Метод "available_ingredients" должен возвращать ингредиент с названием \
            "{ingredient_data["name"]}" и типом {ingredient_data["ingredient_type"]}.'
