import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabaseRealObjects:
    """Тесты для класса Database с реальными объектами"""

    def test_database_initializes_with_correct_buns(self):
        """Проверяем корректность инициализации булочек"""
        db = Database()

        # Проверяем количество и тип булочек
        assert len(db.available_buns()) == 3
        assert all(isinstance(bun, Bun) for bun in db.available_buns())

        # Проверяем конкретные булочки
        bun_names = {bun.get_name() for bun in db.available_buns()}
        assert bun_names == {"black bun", "white bun", "red bun"}

        bun_prices = {bun.get_price() for bun in db.available_buns()}
        assert bun_prices == {100, 200, 300}

    def test_database_initializes_with_correct_ingredients(self):
        """Проверяем корректность инициализации ингредиентов"""
        db = Database()

        # Проверяем количество и тип ингредиентов
        assert len(db.available_ingredients()) == 6
        assert all(isinstance(ing, Ingredient) for ing in db.available_ingredients())

        # Разделяем соусы и начинки
        sauces = [ing for ing in db.available_ingredients()
                  if ing.get_type() == INGREDIENT_TYPE_SAUCE]
        fillings = [ing for ing in db.available_ingredients()
                    if ing.get_type() == INGREDIENT_TYPE_FILLING]

        # Проверяем соусы
        assert len(sauces) == 3
        sauce_names = {ing.get_name() for ing in sauces}
        assert sauce_names == {"hot sauce", "sour cream", "chili sauce"}

        sauce_prices = {ing.get_price() for ing in sauces}
        assert sauce_prices == {100, 200, 300}

        # Проверяем начинки
        assert len(fillings) == 3
        filling_names = {ing.get_name() for ing in fillings}
        assert filling_names == {"cutlet", "dinosaur", "sausage"}

        filling_prices = {ing.get_price() for ing in fillings}
        assert filling_prices == {100, 200, 300}

    def test_available_methods_return_lists(self):
        """Проверяем, что методы возвращают списки"""
        db = Database()

        buns = db.available_buns()
        ingredients = db.available_ingredients()

        assert isinstance(buns, list)
        assert isinstance(ingredients, list)
