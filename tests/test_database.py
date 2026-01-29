import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def database():
    return Database()

class TestDatabase:
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
    ])
    # Тест доступные булки
    def test_available_buns(self, database, name, price):
        #Получаем список доступных булочек из базы данных
        buns = database.available_buns()
        #Проверяем,что хотя бы один объект Bun в списке buns имеет имя name и цену price
        assert any(bun.name == name and bun.price == price for bun in buns)

    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_FILLING, "sausage", 300)
    ])
    #Тест доступные ингредиенты
    def test_available_ingredients(self, database, ingredient_type, ingredient_name, ingredient_price):
        #Получаем список доступных ингредиентов из базы данных
        available_ingredients = database.available_ingredients()
        #Проверяем, что хотя бы один объект Ingredient в списке available_ingredients имеет тип ingredient_type, имя ingredient_name и цену ingredient_price
        assert any(ingredient.type == ingredient_type and ingredient.name == ingredient_name and ingredient.price == ingredient_price for ingredient in available_ingredients)
