import pytest
import allure

class TestDatabase:

    @allure.title("Проверяем, что база содержит 3 булочки")
    def test_database_initialization_contains_buns(self, db):
        buns = db.available_buns()

        assert [bun.get_name() for bun in buns] == ["black bun", "white bun", "red bun"]

    @allure.title("Проверяем, что база содержит 6 ингредиентов")
    def test_database_initialization_contains_ingredients(self, db):
        ingredients = db.available_ingredients()

        assert [ing.get_name() for ing in ingredients] == [
            "hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"
        ]

    @allure.title("Проверяем названия булочек через параметризацию")
    @pytest.mark.parametrize("expected_names", [
        (["black bun", "white bun", "red bun"])
    ])
    def test_available_buns_has_correct_names(self, db, expected_names):
        buns = db.available_buns()

        assert [bun.get_name() for bun in buns] == expected_names

    @allure.title("Проверяем названия ингредиентов через параметризацию")
    @pytest.mark.parametrize("expected_names", [
        (["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"])
    ])
    def test_available_ingredients_has_correct_names(self, db, expected_names):
        ingredients = db.available_ingredients()
        
        assert [ing.get_name() for ing in ingredients] == expected_names