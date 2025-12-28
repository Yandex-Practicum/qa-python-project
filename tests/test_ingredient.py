import generators
from data import DataIngredient
from praktikum.ingredient import Ingredient

class TestIngredient:
    def test_ingredient(self):
        ingredient_type = generators.generate_word()
        ingredient_name = generators.generate_word()
        ingredient_price = generators.generate_price()
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == ingredient_name
        assert ingredient.price == ingredient_price

    def test_get_ingredient_type(self):
        create_ingredient = Ingredient(DataIngredient.INGREDIENT_TYPE,
                                       DataIngredient.INGREDIENT_NAME,
                                       DataIngredient.INGREDIENT_PRICE)
        ingredient_type = create_ingredient.get_type()
        assert ingredient_type == DataIngredient.INGREDIENT_TYPE

    def test_get_ingredient_name(self):
        create_ingredient = Ingredient(DataIngredient.INGREDIENT_TYPE,
                                       DataIngredient.INGREDIENT_NAME,
                                       DataIngredient.INGREDIENT_PRICE)
        ingredient_name = create_ingredient.get_name()
        assert ingredient_name == DataIngredient.INGREDIENT_NAME

    def test_get_ingredient_price(self):
        create_ingredient = Ingredient(DataIngredient.INGREDIENT_TYPE,
                                       DataIngredient.INGREDIENT_NAME,
                                       DataIngredient.INGREDIENT_PRICE)
        ingredient_price = create_ingredient.get_price()
        assert ingredient_price == DataIngredient.INGREDIENT_PRICE