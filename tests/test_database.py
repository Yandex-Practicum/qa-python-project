import allure

from data import TestData


class TestDatabase:

    @allure.title("Проверка получения списка доступных булочек")
    def test_available_buns(self, database):
        actual_buns = database.available_buns()

        expected_buns = TestData.expected_buns

        assert len(expected_buns) == len(actual_buns)
        for bun in actual_buns:
            assert bun.get_name() in expected_buns
            assert bun.get_price() == expected_buns[bun.get_name()]

    @allure.title("Проверка получения списка доступных ингредиентов")
    def test_available_ingredients(self, database):
        actual_ingredients = database.available_ingredients()

        expected_ingredients = TestData.expected_ingredients

        assert len(actual_ingredients) == len(expected_ingredients)
        for ingredient in actual_ingredients:
            assert ingredient.get_name() in expected_ingredients

            correct_ingredient_data = expected_ingredients[ingredient.get_name()]
            assert ingredient.get_type() == correct_ingredient_data[0]
            assert ingredient.get_price() == correct_ingredient_data[1]
