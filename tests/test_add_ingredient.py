import pytest
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.data import Credentials


class TestAddIngredient:
    '''
    Проверяется метод добавления ингредиентов
    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)
    ''' 

    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", Credentials.ingredient_combination)
    def test_add_ingredient(self, ingredient_type, ingredient_name, ingredient_price, create_mock_ingredient):

        mok_ingredient = create_mock_ingredient(ingredient_type, ingredient_name, ingredient_price)
        burger = Burger()
        burger.add_ingredient(mok_ingredient)

        assert len(burger.ingredients) == 1, "Ингредиент не добавился в бургер"

        added_ingredient = burger.ingredients[0]  #получить добавленный ингредиент

        assert added_ingredient.get_type() == ingredient_type, \
            f"Ожидался тип '{ingredient_type}', получен '{added_ingredient.get_type()}'"
        assert added_ingredient.get_name() == ingredient_name, \
            f"Ожидалось имя '{ingredient_name}', получено '{added_ingredient.get_name()}'"
        assert added_ingredient.get_price() == ingredient_price, \
            f"Ожидалась цена {ingredient_price}, получена {added_ingredient.get_price()}"

    #Проверяем, что можно добавить разное количество ингредиентов
    @pytest.mark.parametrize("ingredients_count", [1, 2, 3, 4, 5])
    def test_add_multiple_ingredients_param(self, ingredients_count, create_mock_ingredient):
        burger = Burger()
  
        for i in range(ingredients_count):
            mock_ingredient = create_mock_ingredient(
                INGREDIENT_TYPE_SAUCE,
                f"sauce_{i}",
                i * 100
            )
            burger.add_ingredient(mock_ingredient)
       
        assert len(burger.ingredients) == ingredients_count, \
            f"Ожидалось {ingredients_count} ингредиентов, получено {len(burger.ingredients)}"
