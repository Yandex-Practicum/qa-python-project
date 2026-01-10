from practikum.database import Database

def test_available_buns():
# Проверяем, что метод available_buns возвращает правильное количество булочек
    database = Database()
    buns = database.available_buns()
    assert len(buns) == 3  # Убедимся, что три булочки
    assert buns[0].get_name() == "black bun"
    assert buns[1].get_price() == 200

def test_available_ingredients():
# Проверяем, что метод available_ingredients возвращает правильное количество ингредиентов
    database = Database()
    ingredients = database.available_ingredients()
    assert len(ingredients) == 6  # Убедимся, что шесть ингредиентов
    assert ingredients[0].get_type() == "SAUCE"
    assert ingredients[3].get_name() == "cutlet"
