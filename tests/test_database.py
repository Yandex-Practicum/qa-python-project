from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


# Тесты на класс Database
class TestDatabase:
    # Тест метода available_buns, проверяем, что в списке 3 булки
    def test_available_buns(self, mock_database):
        buns = mock_database.available_buns()
        assert len(buns) == 3

    # Тест метода available_ingredients, проверяем, что в списке 6 ингредиентов
    def test_available_ingredients(self, mock_database):
        ingredients = mock_database.available_ingredients()
        assert len(ingredients) == 6

    # Тест, что первая булка имеет корректное имя
    def test_first_bun(self, mock_database):
        first_bun = mock_database.available_buns()[0]
        assert first_bun.get_name() == "black bun"

        # Тест, что последний ингредиент имеет корректное имя

    def test_last_ingredient(self, mock_database):
        last_ingredient = mock_database.available_ingredients()[-1]
        assert last_ingredient.get_name() == "sausage"

        # Тест, что первый ингредиент является соусом

    def test_first_ingredient_type(self, mock_database):
        first_ingredient = mock_database.available_ingredients()[0]
        assert first_ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    # Тест, что последний ингредиент является начинкой
    def test_last_ingredient_type(self, mock_database):
        last_ingredient = mock_database.available_ingredients()[-1]
        assert last_ingredient.get_type() == INGREDIENT_TYPE_FILLING
