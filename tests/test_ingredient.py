from data import TEST_INGREDIENTS
from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_get_price_return_price(self):
        ingredient_data = TEST_INGREDIENTS[0]
        ingredient = Ingredient(
            ingredient_type=ingredient_data['ingredient_type'],
            name=ingredient_data['name'],
            price=ingredient_data['price']
        )

        assert ingredient.get_price() == ingredient_data[
            'price'], f'Ожидалось, что цена будет {ingredient_data["price"]}, но получено {ingredient.get_price()}'

    def test_get_name_return_name(self):
        ingredient_data = TEST_INGREDIENTS[0]
        ingredient = Ingredient(
            ingredient_type=ingredient_data['ingredient_type'],
            name=ingredient_data['name'],
            price=ingredient_data['price']
        )

        assert ingredient.get_name() == ingredient_data[
            'name'], f'Ожидалось, что название будет "{ingredient_data["name"]}", но получено {ingredient.get_name()}'

    def test_get_type_return_type(self):
        ingredient_data = TEST_INGREDIENTS[0]
        ingredient = Ingredient(
            ingredient_type=ingredient_data['ingredient_type'],
            name=ingredient_data['name'],
            price=ingredient_data['price']
        )

        assert ingredient.get_type() == ingredient_data['ingredient_type'], \
            f'Ожидалось, что тип будет "{ingredient_data["ingredient_type"]}", но получено {ingredient.get_type()}'
