import allure
import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
class TestIngredient:
   @pytest.mark.parametrize("ingredient_type_expected, name_expected, price_expected", [
       ("sauce", "tomato", 10),
       ("filling", "apple", 20),
       ("sauce", "chicken", 30),
   ])
   @allure.title("Проверка установки типа, имени и прайса для ингредиента")
   def test_ingredient_properties(self, ingredient_fixture, ingredient_type_expected, name_expected, price_expected):
        ingredient_fixture.type = ingredient_type_expected
        ingredient_fixture.name = name_expected
        ingredient_fixture.price = price_expected
        assert ingredient_fixture.type == ingredient_type_expected
        assert ingredient_fixture.name== name_expected
        assert ingredient_fixture.price== price_expected

   @allure.title("Проверка метода get_type")
   @pytest.mark.parametrize('type_expected', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING, ''])
   def test_get_type(self, ingredient_fixture, type_expected):
        ingredient_fixture.type = type_expected
        assert ingredient_fixture.get_type() == type_expected

   @pytest.mark.parametrize('name_expected', ['tomato', 'apple', 'chicken', ''])
   @allure.title("Проверка метода get_name")
   def test_get_name(self, ingredient_fixture, name_expected):
        ingredient_fixture.name = name_expected
        assert ingredient_fixture.get_name() == name_expected

   @allure.title("Проверка метода get_price")
   @pytest.mark.parametrize('price_expected', [1000.0001, 0])
   def test_get_price(self, ingredient_fixture, price_expected):
        ingredient_fixture.price = price_expected
        assert ingredient_fixture.get_price() == price_expected