from diplom_1.praktikum.database import Database

class TestDatabase:
    # Позитивные тесты
    def test_available_buns_returns_list(self):
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100
        assert buns[1].get_name() == "white bun"
        assert buns[1].get_price() == 200

    def test_available_ingredients_returns_list(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6

        # Проверяем соусы
        assert ingredients[0].get_type() == "SAUCE"
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[0].get_price() == 100

        # Проверяем начинки
        assert ingredients[3].get_type() == "FILLING"
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[3].get_price() == 100

    # Тесты на изменяемость списков
    def test_available_buns_returns_mutable_list(self):
        database = Database()
        buns = database.available_buns()
        buns.clear()
        assert len(database.available_buns()) == 0

    def test_available_ingredients_returns_mutable_list(self):
        database = Database()
        ingredients = database.available_ingredients()
        ingredients.clear()
        assert len(database.available_ingredients()) == 0