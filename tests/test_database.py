from praktikum.bun import Bun
from praktikum.ingredient import Ingredient



class TestDatabase:

    def test_available_buns(self, clean_data_base):
        buns = clean_data_base.available_buns()
        assert len(buns) == 3, "Неверное количество булок."


    def test_buns_are_instances_of_bun(self, clean_data_base):
        buns = clean_data_base.available_buns()
        assert all(isinstance(bun, Bun) for bun in buns), "Не все объекты — экземпляры Bun."


    def test_available_ingredients(self, clean_data_base):
        ingredients = clean_data_base.available_ingredients()
        assert len(ingredients) == 6, "Неверное количество ингредиентов."


    def test_ingredients_are_instances_of_ingredient(self, clean_data_base):
        ingredients = clean_data_base.available_ingredients()
        assert all(isinstance(ing, Ingredient) for ing in ingredients), "Не все объекты — экземпляры Ingredient."

