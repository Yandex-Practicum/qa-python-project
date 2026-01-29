from praktikum import ingredient_types
from praktikum.ingredient import Ingredient
from praktikum.database import Database


# В тест-сете присутсвуют тесты на проверку получения данных из базы данных
class TestIngredients:

    def test_ingredient_get_name(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE,
                                'Соус традиционный галактический',
                                15)
        assert ingredient.get_name() == 'Соус традиционный галактический'

    def test_ingredient_get_type(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE,
                                'Соус Spicy-X',
                                90)
        assert ingredient.get_type() == ingredient_types.INGREDIENT_TYPE_SAUCE

    def test_ingredient_get_price(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE,
                                'Соус фирменный Space Sauce',
                                80)
        assert ingredient.get_price() == 80

    def test_ingredient_from_database_get_name(self):
        database = Database()
        ingredients_list = database.available_ingredients()
        current_ingredient = ingredients_list[1]
        assert current_ingredient.get_name() == 'sour cream'

    def test_ingredient_from_database_get_type(self):
        database = Database()
        ingredients_list = database.available_ingredients()
        current_ingredient = ingredients_list[5]
        assert current_ingredient.get_type() == 'FILLING'

    def test_ingredient_from_database_get_price(self):
        database = Database()
        ingredients_list = database.available_ingredients()
        current_ingredient = ingredients_list[4]
        assert current_ingredient.get_price() == 200


