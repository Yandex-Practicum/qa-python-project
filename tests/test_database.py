import pytest
from data import TestDataBase
from conftest import data_base


class TestDB:
    @pytest.mark.parametrize('index_bun, bun_name, bun_price', TestDataBase.TEST_BUN_FROM_DATABASE)
    def test_available_buns_db_success(self, data_base, index_bun, bun_name, bun_price):
        """
        Тест проверяет, что булочки из базы данных соответствуют ожидаемым значениям.
        """
        data_buns = data_base.available_buns()

        # Проверка имени булочки
        assert data_buns[
                   index_bun].get_name() == bun_name, f"Ожидалось имя булочки {bun_name}, но получено {data_buns[index_bun].get_name()}"

        # Проверка цены булочки
        assert data_buns[
                   index_bun].get_price() == bun_price, f"Ожидалась цена {bun_price}, но получено {data_buns[index_bun].get_price()}"

    @pytest.mark.parametrize('ingredient_index, type_ingredient, name_ingredient, price_ingredient',
                             TestDataBase.TEST_DATABASE_INGREDIENTS)
    def test_available_ingredients_db_success(self, data_base, ingredient_index, type_ingredient, name_ingredient,
                                              price_ingredient):
        """
        Тест проверяет, что ингредиенты из базы данных соответствуют ожидаемым значениям.
        """
        data_ingredients = data_base.available_ingredients()

        # Проверка имени ингредиента
        assert data_ingredients[
                   ingredient_index].get_name() == name_ingredient, f"Ожидалось имя ингредиента {name_ingredient}, но получено {data_ingredients[ingredient_index].get_name()}"

        # Проверка типа ингредиента
        assert data_ingredients[
                   ingredient_index].get_type() == type_ingredient, f"Ожидался тип {type_ingredient}, но получено {data_ingredients[ingredient_index].get_type()}"

        # Проверка цены ингредиента
        assert data_ingredients[
                   ingredient_index].get_price() == price_ingredient, f"Ожидалась цена {price_ingredient}, но получено {data_ingredients[ingredient_index].get_price()}"
