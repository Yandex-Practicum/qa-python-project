from praktikum.database import Database


class TestClassDatabase:
    # Тестируем доступные булочки и название первой булочки
    def test_available_buns_create_object_database_count_buns_and_name_first_bun(self):
        data_b = Database()
        available_buns = data_b.available_buns()
        assert len(available_buns) == 3
        assert available_buns[0].get_name() == 'black bun'

    # Тестируем доступные ингредиенты и название первого соуса
    def test_available_ingredients_create_object_database_count_ingredients_and_name_first_ingredients(self):
        data_b = Database()
        available_ingredients = data_b.available_ingredients()
        assert len(available_ingredients) == 6
        assert available_ingredients[0].get_name() == 'hot sauce'

    # Тестируем получение цены на ингредиент
    def test_get_ingredients_price_create_object_database_get_price_successful(self):
        data_b = Database()
        ingredients = data_b.available_ingredients()
        price = {i.get_name(): i.get_price() for i in ingredients}
        assert price['sausage'] == 300