import pytest

from praktikum.praktikum import Database


def element_search(list_element, element):
    for i in range(len(list_element)):
        if list_element[i].name in element:
            return i


class TestBurger:

    @pytest.mark.parametrize("name_bun, price_bun",
                             [["black bun", 100], ["white bun", 200], ["red bun", 300]])
    def test_available_buns(self, name_bun, price_bun):
        db = Database()
        index = element_search(db.available_buns(), name_bun)
        bun = db.available_buns()[index]
        assert bun.name == name_bun and bun.price == price_bun

    @pytest.mark.parametrize("type_ingredient, name_ingredient, price_ingredient",
                             [["SAUCE", "hot sauce", 100], ["SAUCE", "sour cream", 200], ["SAUCE", "chili sauce", 300],
                              ["FILLING",  "cutlet", 100], ["FILLING", "dinosaur", 200], ["FILLING", "sausage", 300]])
    def test_available_ingredients(self, type_ingredient, name_ingredient, price_ingredient):
        db = Database()
        index = element_search(db.available_ingredients(), name_ingredient)
        ingredients = db.available_ingredients()[index]
        assert ingredients.type == type_ingredient and ingredients.name == name_ingredient and ingredients.price == price_ingredient
