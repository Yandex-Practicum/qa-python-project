from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_initial_buns_count(self, database):
        buns = database.available_buns()
        assert len(buns) == 3

    def test_initial_ingredients_count(self, database):
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6  # 3 соуса + 3 начинки

    def test_buns_content(self, database, black_bun, white_bun, red_bun):
        buns = database.available_buns()
        # Проверяем через сравнение атрибутов, так как это разные объекты
        assert buns[0].get_name() == black_bun.get_name()
        assert buns[0].get_price() == black_bun.get_price()
        assert buns[1].get_name() == white_bun.get_name()
        assert buns[1].get_price() == white_bun.get_price()
        assert buns[2].get_name() == red_bun.get_name()
        assert buns[2].get_price() == red_bun.get_price()

    def test_ingredients_content(self, database, hot_sauce, sour_cream, chili_sauce,
                                 cutlet, dinosaur, sausage):
        ingredients = database.available_ingredients()
        # Соусы
        assert ingredients[0].get_type() == hot_sauce.get_type()
        assert ingredients[0].get_name() == hot_sauce.get_name()
        assert ingredients[0].get_price() == hot_sauce.get_price()
        assert ingredients[1].get_type() == sour_cream.get_type()
        assert ingredients[1].get_name() == sour_cream.get_name()
        assert ingredients[1].get_price() == sour_cream.get_price()
        assert ingredients[2].get_type() == chili_sauce.get_type()
        assert ingredients[2].get_name() == chili_sauce.get_name()
        assert ingredients[2].get_price() == chili_sauce.get_price()
        # Начинки
        assert ingredients[3].get_type() == cutlet.get_type()
        assert ingredients[3].get_name() == cutlet.get_name()
        assert ingredients[3].get_price() == cutlet.get_price()
        assert ingredients[4].get_type() == dinosaur.get_type()
        assert ingredients[4].get_name() == dinosaur.get_name()
        assert ingredients[4].get_price() == dinosaur.get_price()
        assert ingredients[5].get_type() == sausage.get_type()
        assert ingredients[5].get_name() == sausage.get_name()
        assert ingredients[5].get_price() == sausage.get_price()

    def test_available_buns_returns_same_list(self, database):
        buns1 = database.available_buns()
        buns2 = database.available_buns()
        assert buns1 is buns2

    def test_available_ingredients_returns_same_list(self, database):
        ing1 = database.available_ingredients()
        ing2 = database.available_ingredients()
        assert ing1 is ing2