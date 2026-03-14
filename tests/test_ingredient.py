from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
import allure

@allure.feature('Ingredient Logic')
class TestIngredient:

    @allure.title('Successfully create an ingredient and verify attributes')
    def test_create_ingredient_is_successfil(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Сырный соус', 10.25)
        assert (
                ingredient.type,
                ingredient.name,
                ingredient.price
               ) == (
                INGREDIENT_TYPE_SAUCE,
                'Сырный соус',
                10.25), f"Expected {(INGREDIENT_TYPE_SAUCE, 'Сырный соус', 10.25)}, but got {(ingredient.type, ingredient.name, ingredient.price)}"

    @allure.title('Verify get_price() returns the correct value')
    def test_get_price_return_correct_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Чили соус', 12.25)
        assert ingredient.get_price() == 12.25, f"Expected price 12.25, but got {ingredient.get_price()}"

    @allure.title('Verify get_name() returns the correct value')
    def test_get_name_return_correct_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Чили соус', 12.25)
        assert ingredient.get_name() == 'Чили соус', f"Expected name 'Чили соус', but got '{ingredient.get_name()}'"

    @allure.title('Verify get_type() returns the correct value')
    def test_get_type_return_correct_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Чили соус', 12.25)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE, f"Expected type {INGREDIENT_TYPE_SAUCE}, but got {ingredient.get_type()}"
