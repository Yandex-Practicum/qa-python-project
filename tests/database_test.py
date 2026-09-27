import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    """Тесты для класса Database"""

    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.db = Database()

    def test_database_initialization_has_buns(self):
        """Тест проверки что БД инициализируется с булочками"""
        assert len(self.db.buns) == 3
        assert isinstance(self.db.buns, list)

    def test_database_initialization_has_ingredients(self):
        """Тест проверки что БД инициализируется с ингредиентами"""
        assert len(self.db.ingredients) == 6
        assert isinstance(self.db.ingredients, list)

    @pytest.mark.parametrize("index, expected_name, expected_price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300),
    ])
    def test_available_buns_content(self, index, expected_name, expected_price):
        """Тест проверки содержимого списка доступных булочек"""
        buns = self.db.available_buns()

        assert len(buns) == 3
        bun = buns[index]
        assert bun.get_name() == expected_name
        assert bun.get_price() == expected_price

    def test_available_buns_returns_list_of_bun_objects(self):
        """Тест проверки что available_buns возвращает список объектов Bun"""
        buns = self.db.available_buns()

        for bun in buns:
            assert isinstance(bun, Bun)


    @pytest.mark.parametrize("index, expected_type, expected_name, expected_price", [
        (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
    ])
    def test_available_ingredients_content(self, index, expected_type, expected_name, expected_price):
        """Тест проверки содержимого списка доступных ингредиентов"""
        ingredients = self.db.available_ingredients()

        assert len(ingredients) == 6
        ingredient = ingredients[index]
        assert ingredient.get_type() == expected_type
        assert ingredient.get_name() == expected_name
        assert ingredient.get_price() == expected_price

    def test_available_ingredients_returns_list_of_ingredient_objects(self):
        """Тест проверки что available_ingredients возвращает список объектов Ingredient"""
        ingredients = self.db.available_ingredients()

        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)


    def test_buns_order_is_preserved(self):
        """Тест проверки сохранения порядка булочек"""
        buns = self.db.available_buns()

        assert buns[0].get_name() == "black bun"
        assert buns[1].get_name() == "white bun"
        assert buns[2].get_name() == "red bun"

    def test_ingredients_order_is_preserved(self):
        """Тест проверки сохранения порядка ингредиентов"""
        ingredients = self.db.available_ingredients()

        # Проверяем соусы
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[1].get_name() == "sour cream"
        assert ingredients[2].get_name() == "chili sauce"

        # Проверяем начинки
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[4].get_name() == "dinosaur"
        assert ingredients[5].get_name() == "sausage"

    def test_database_contains_only_valid_bun_objects(self):
        """Тест проверки что база содержит только валидные объекты Bun"""
        buns = self.db.available_buns()

        for bun in buns:
            assert hasattr(bun, 'get_name')
            assert hasattr(bun, 'get_price')
            assert callable(bun.get_name)
            assert callable(bun.get_price)

    def test_database_contains_only_valid_ingredient_objects(self):
        """Тест проверки что база содержит только валидные объекты Ingredient"""
        ingredients = self.db.available_ingredients()

        for ingredient in ingredients:
            assert hasattr(ingredient, 'get_name')
            assert hasattr(ingredient, 'get_price')
            assert hasattr(ingredient, 'get_type')
            assert callable(ingredient.get_name)
            assert callable(ingredient.get_price)
            assert callable(ingredient.get_type)

    @pytest.mark.parametrize("sauce_name", ["hot sauce", "sour cream", "chili sauce"])
    def test_all_sauces_have_correct_type(self, sauce_name):
        """Тест проверки что все соусы имеют правильный тип"""
        ingredients = self.db.available_ingredients()

        for ingredient in ingredients:
            if ingredient.get_name() == sauce_name:
                assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
                break
        else:
            pytest.fail(f"Sauce '{sauce_name}' not found")

    @pytest.mark.parametrize("filling_name", ["cutlet", "dinosaur", "sausage"])
    def test_all_fillings_have_correct_type(self, filling_name):
        """Тест проверки что все начинки имеют правильный тип"""
        ingredients = self.db.available_ingredients()

        for ingredient in ingredients:
            if ingredient.get_name() == filling_name:
                assert ingredient.get_type() == INGREDIENT_TYPE_FILLING
                break
        else:
            pytest.fail(f"Filling '{filling_name}' not found")

    def test_no_duplicate_buns(self):
        """Тест проверки отсутствия дубликатов булочек"""
        buns = self.db.available_buns()
        names = [bun.get_name() for bun in buns]

        assert len(names) == len(set(names))

    def test_no_duplicate_ingredients(self):
        """Тест проверки отсутствия дубликатов ингредиентов"""
        ingredients = self.db.available_ingredients()
        names = [ing.get_name() for ing in ingredients]

        assert len(names) == len(set(names))