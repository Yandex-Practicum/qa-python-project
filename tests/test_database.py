import pytest
import allure
from unittest import mock
from Diplom_1.bun import Bun
from Diplom_1.ingredient import Ingredient
from Diplom_1.database import Database
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    @allure.title("Тест на доступные булочки")
    def test_available_buns(self, mock_buns):
        with mock.patch.object(Database, '__init__', lambda x: None):
            db = Database()
            db.buns = mock_buns
            assert db.available_buns() == mock_buns

    @allure.title("Тест на доступные ингредиенты")
    def test_available_ingredients(self, mock_ingredients):
        with mock.patch.object(Database, '__init__', lambda x: None):
            db = Database()
            db.ingredients = mock_ingredients
            assert db.available_ingredients() == mock_ingredients

    @allure.title('Параметризованный тест для проверки наличия булочек')
    @pytest.mark.parametrize("bun_name, expected_price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
    ])
    def test_buns_with_parametrize(self, bun_name, expected_price, mock_buns):
        with mock.patch.object(Database, '__init__', lambda x: None):
            db = Database()
            db.buns = mock_buns
            bun = next(bun for bun in db.available_buns() if bun.name == bun_name)
            assert bun.price == expected_price

    @allure.title('Параметризованный тест для проверки наличия ингредиентов')
    @pytest.mark.parametrize("ingredient_name, expected_price, ingredient_type", [
        ("hot sauce", 100, INGREDIENT_TYPE_SAUCE),
        ("sour cream", 200, INGREDIENT_TYPE_SAUCE),
        ("chili sauce", 300, INGREDIENT_TYPE_SAUCE),
        ("cutlet", 100, INGREDIENT_TYPE_FILLING),
        ("dinosaur", 200, INGREDIENT_TYPE_FILLING),
        ("sausage", 300, INGREDIENT_TYPE_FILLING)
    ])
    def test_ingredients_with_parametrize(self, ingredient_name, expected_price, ingredient_type, mock_ingredients):
        with mock.patch.object(Database, '__init__', lambda x: None):
            db = Database()
            db.ingredients = mock_ingredients
            ingredient = next(ing for ing in db.available_ingredients() if ing.name == ingredient_name)
            assert ingredient.price == expected_price
            assert ingredient.type == ingredient_type

    @pytest.mark.parametrize("ingredient_name, expected_price, ingredient_type", [
        ("hot sauce", 100, INGREDIENT_TYPE_SAUCE),
        ("cutlet", 100, INGREDIENT_TYPE_FILLING),
        ("sausage", 300, INGREDIENT_TYPE_FILLING)
    ])
    @allure.title("Тест на получение ингредиентов по имени и типу")
    def test_get_ingredient_by_name(self, ingredient_name, expected_price, ingredient_type, populated_database):
        ingredients = populated_database.available_ingredients()
        filtered_ingredients = [ingredient for ingredient in ingredients if
                                ingredient.name == ingredient_name and ingredient.type == ingredient_type]

        assert len(filtered_ingredients) == 1
        assert filtered_ingredients[0].price == expected_price

    @allure.title("Тест на проверку и возврат всех булочек")
    def test_buns_initialization_and_available(self, database):
        buns = database.available_buns()
        assert isinstance(buns, list)
        assert len(buns) == 3
        assert buns[0].name == "black bun" and buns[0].price == 100
        assert buns[1].name == "white bun" and buns[1].price == 200
        assert buns[2].name == "red bun" and buns[2].price == 300

    @allure.title("Тест на проверку и возврат всех ингредиентов")
    def test_ingredients_initialization_and_available(self, database):
        ingredients = database.available_ingredients()
        assert isinstance(ingredients, list)
        assert len(ingredients) == 6
        assert ingredients[0].name == "hot sauce" and ingredients[0].price == 100 and ingredients[0].type == INGREDIENT_TYPE_SAUCE
        assert ingredients[1].name == "sour cream" and ingredients[1].price == 200 and ingredients[1].type == INGREDIENT_TYPE_SAUCE
        assert ingredients[2].name == "chili sauce" and ingredients[2].price == 300 and ingredients[2].type == INGREDIENT_TYPE_SAUCE
        assert ingredients[3].name == "cutlet" and ingredients[3].price == 100 and ingredients[3].type == INGREDIENT_TYPE_FILLING
        assert ingredients[4].name == "dinosaur" and ingredients[4].price == 200 and ingredients[4].type == INGREDIENT_TYPE_FILLING
        assert ingredients[5].name == "sausage" and ingredients[5].price == 300 and ingredients[5].type == INGREDIENT_TYPE_FILLING

    @allure.title("Тест на добавление булочек в базу данных")
    def test_add_bun(self, database):
        new_bun = Bun("green bun", 400)
        database.buns.append(new_bun)
        assert len(database.available_buns()) == 4
        assert database.available_buns()[3].name == "green bun"
        assert database.available_buns()[3].price == 400

    @allure.title("Тест на добавление ингредиентов в базу данных")
    def test_add_ingredient(self, database):
        new_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "new filling", 400)
        database.ingredients.append(new_ingredient)
        assert len(database.available_ingredients()) == 7
        assert database.available_ingredients()[6].name == "new filling"
        assert database.available_ingredients()[6].price == 400
        assert database.available_ingredients()[6].type == INGREDIENT_TYPE_FILLING

    @allure.title("Тест на удаление булочки из базы данных")
    def test_remove_bun(self, database):
        bun_to_remove = database.buns[0]
        database.buns.remove(bun_to_remove)
        assert len(database.available_buns()) == 2
        assert bun_to_remove not in database.available_buns()

    @allure.title("Тест на удаление ингредиента из базы данных")
    def test_remove_ingredient(self, database):
        ingredient_to_remove = database.ingredients[0]
        database.ingredients.remove(ingredient_to_remove)
        assert len(database.available_ingredients()) == 5
        assert ingredient_to_remove not in database.available_ingredients()

    @allure.title("Тест на получение пустого списка булочек")
    def test_available_buns_empty(self, empty_database):
        assert empty_database.available_buns() == []

    @allure.title("Тест на получение пустого списка ингредиентов")
    def test_available_ingredients_empty(self, empty_database):
        assert empty_database.available_ingredients() == []

    @allure.title("Тест на инициализацию пустой базы данных")
    def test_empty_database_initialization(self, empty_database):
        assert len(empty_database.available_buns()) == 0
        assert len(empty_database.available_ingredients()) == 0




