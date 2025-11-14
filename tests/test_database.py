import pytest
import allure
from prakticum.database import Database
from prakticum.bun import Bun
from prakticum.ingredient import Ingredient
from prakticum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:

    @allure.title("Проверка наличия булок по имени и цене")
    @pytest.mark.parametrize("expected_name, expected_price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
    ])
    def test_available_buns_content(self, expected_name, expected_price):
        db = Database()
        buns = db.available_buns()
        names = [bun.name for bun in buns]
        prices = [bun.price for bun in buns]
        assert expected_name in names
        assert expected_price in prices

    @allure.title("Проверка количества и типа булок")
    def test_available_buns_count_and_type(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)

    @allure.title("Проверка фильтрации ингредиентов по типу")
    @pytest.mark.parametrize("ingredient_type, expected_names", [
        (INGREDIENT_TYPE_SAUCE, {"hot sauce", "sour cream", "chili sauce"}),
        (INGREDIENT_TYPE_FILLING, {"cutlet", "dinosaur", "sausage"}),
    ])
    def test_available_ingredients_by_type(self, ingredient_type, expected_names):
        db = Database()
        ingredients = db.available_ingredients()
        filtered = [i.name for i in ingredients if i.type == ingredient_type]
        assert set(filtered) == expected_names

    @allure.title("Проверка количества и типа ингредиентов")
    def test_available_ingredients_count_and_type(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6
        assert all(isinstance(i, Ingredient) for i in ingredients)

    @allure.title("Добавление новой булки в базу данных")
    def test_add_bun(self):
        db = Database()
        new_bun = Bun("blue bun", 400)
        db.buns.append(new_bun)
        buns = db.available_buns()
        assert len(buns) == 4
        assert new_bun in buns

    @allure.title("Добавление нового ингредиента в базу данных")
    def test_add_ingredient(self):
        db = Database()
        new_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "mustard", 150)
        db.ingredients.append(new_ingredient)
        ingredients = db.available_ingredients()
        assert len(ingredients) == 7
        assert new_ingredient in ingredients

    @allure.title("Проверка фильтрации только соусов")
    def test_filter_ingredients_by_type(self):
        db = Database()
        sauces = [i.name for i in db.available_ingredients() if i.type == INGREDIENT_TYPE_SAUCE]
        assert "hot sauce" in sauces
        assert "sour cream" in sauces
        assert "chili sauce" in sauces

    @allure.title("Проверка поведения при пустой базе данных")
    def test_empty_database(self):
        db = Database()
        db.buns.clear()
        db.ingredients.clear()
        assert len(db.available_buns()) == 0
        assert len(db.available_ingredients()) == 0

    @allure.title("Проверка уникальности названий ингредиентов")
    def test_unique_ingredient_names(self):
        db = Database()
        ingredient_names = [ingredient.name for ingredient in db.available_ingredients()]
        assert len(ingredient_names) == len(set(ingredient_names))

    @allure.title("Проверка уникальности названий булок")
    def test_unique_bun_names(self):
        db = Database()
        bun_names = [bun.name for bun in db.available_buns()]
        assert len(bun_names) == len(set(bun_names))

    @allure.title("Проверка добавления дубликатов ингредиентов")
    def test_adding_duplicate_ingredient(self):
        db = Database()
        duplicate = db.available_ingredients()[0]
        db.ingredients.append(duplicate)
        names = [i.name for i in db.available_ingredients()]
        assert names.count(duplicate.name) >= 2

    @allure.title("Проверка удаления булки напрямую из списка базы данных")
    def test_direct_remove_bun(self):
        db = Database()
        initial_count = len(db.available_buns())
        bun_to_remove = db.available_buns()[0]
        db.buns.remove(bun_to_remove)
        assert bun_to_remove not in db.available_buns()
        assert len(db.available_buns()) == initial_count - 1

    @allure.title("Проверка удаления ингредиента напрямую из списка базы данных")
    def test_direct_remove_ingredient(self):
        db = Database()
        initial_count = len(db.available_ingredients())
        ingredient_to_remove = db.available_ingredients()[0]
        db.ingredients.remove(ingredient_to_remove)
        assert ingredient_to_remove not in db.available_ingredients()
        assert len(db.available_ingredients()) == initial_count - 1





