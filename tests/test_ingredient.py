from data import Data
from praktikum.ingredient import Ingredient


class TestIngredient:
    # Проверка, что метод возвращает верный тип ингредиента
    def test_get_type_return_true_type(self):
        ingredient = Ingredient(Data.ingredients[0].get("type"),
                                Data.ingredients[0].get("name"),
                                Data.ingredients[0].get("price"))
        type_ingredient = ingredient.get_type()

        assert type_ingredient == Data.ingredients[0].get("type")

    # Проверка, что метод возвращает верное название ингредиента
    def test_get_name_return_true_name(self):
        ingredient = Ingredient(Data.ingredients[1].get("type"),
                                Data.ingredients[1].get("name"),
                                Data.ingredients[1].get("price"))
        name = ingredient.get_name()

        assert name == Data.ingredients[1].get("name")

    # Проверка, что метод возвращает верную цену ингредиента
    def test_get_price_return_true_price(self):
        ingredient = Ingredient(Data.ingredients[2].get("type"),
                                Data.ingredients[2].get("name"),
                                Data.ingredients[2].get("price"))
        price = ingredient.get_price()

        assert price == Data.ingredients[2].get("price")
