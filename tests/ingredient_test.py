from praktikum.ingredient import Ingredient
import data_for_tests as dft


class TestIngredient:

    # Тест 003 - Позитивный - Проверка получения типа ингредиента
    def test_get_type_of_ingredient(self):
        ingredient = Ingredient(dft.type_of_ingredient, dft.name_of_ingredient, dft.price_of_ingredient)
        result = ingredient.get_type()

        assert dft.type_of_ingredient == result, \
            f'Тип ингредиента "{result}", а должен быть "{dft.type_of_ingredient}"!'

    # Тест 004 - Позитивный - Проверка получения названия ингредиента
    def test_get_name_of_ingredient(self):
        ingredient = Ingredient(dft.type_of_ingredient, dft.name_of_ingredient, dft.price_of_ingredient)
        result = ingredient.get_name()

        assert dft.name_of_ingredient == result, \
            f'Название ингредиента "{result}", а должно быть "{dft.name_of_ingredient}"!'

    # Тест 005 - Позитивный - Проверка получения цены ингредиента
    def test_get_price_of_ingredient(self):
        ingredient = Ingredient(dft.type_of_ingredient, dft.name_of_ingredient, dft.price_of_ingredient)
        result = ingredient.get_price()

        assert dft.price_of_ingredient == result, \
            f'Цена ингредиента "{result}", а должна быть "{dft.price_of_ingredient}"!'
