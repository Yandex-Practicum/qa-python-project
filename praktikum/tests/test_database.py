import pytest
import praktikum.ingredient_types as ingredient_types

from praktikum.database import Database

class TestDatabase:
    def test_database_init_buns_is_set(self):
        db = Database()
        assert len(db.buns) == 3, 'При инициализации БД некорректно задан список buns'

    def test_database_init_ingredients_is_set(self):
        db = Database()
        assert len(db.ingredients) == 6, 'При инициализации БД некорректно задан список ingredients'

    @pytest.mark.parametrize('ingredient_index', [0, 1, 2])
    def test_database_init_sauces_in_ingredients(self, ingredient_index):
        db = Database()
        expected_ingredient_type = ingredient_types.INGREDIENT_TYPE_SAUCE
        actual_ingredient_type = db.ingredients[ingredient_index].type
        assert actual_ingredient_type == expected_ingredient_type, ('Некорректно инициализирован тип ингредиента. '
                                                                    'Индекс: {ingredient_index}, '
                                                                    'ожидаемый тип: {expected_ingredient_type}')

    @pytest.mark.parametrize('ingredient_index', [3, 4, 5])
    def test_database_init_fillings_in_ingredients(self, ingredient_index):
        db = Database()
        expected_ingredient_type = ingredient_types.INGREDIENT_TYPE_FILLING
        actual_ingredient_type = db.ingredients[ingredient_index].type
        assert actual_ingredient_type == expected_ingredient_type, ('Некорректно инициализирован тип ингредиента. '
                                                                    'Индекс: {ingredient_index}, '
                                                                    'ожидаемый тип: {expected_ingredient_type}')

    def test_database_available_buns_list_is_correct(self):
        db = Database()
        assert db.available_buns() == db.buns, 'Метод вернул список булок, который не совпадает со списком buns'

    def test_database_available_ingredients_list_is_correct(self):
        db = Database()
        assert db.available_ingredients() == db.ingredients, ('Метод вернул список ингредиентов, '
                                                              'который не совпадает со списком buns')