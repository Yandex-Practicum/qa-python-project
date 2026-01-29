import pytest
from praktikum.burger import Burger
import data

class TestBurger:
    def test_burger_initialization(self): #тест_инициализации_бургера
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self,database): #тест_установки_булок
        burger = Burger()
        bun = database.available_buns()[0]
        burger.set_buns(bun)
        assert burger.bun == bun

    @pytest.mark.parametrize("ing_type, name, price", data.Ingredients.data_ingredients)
    def test_add_ingredient(self,database, ing_type, name, price): #тест_добавления_ингридиентов
        burger = Burger()
        ingredient = next((i for i in database.available_ingredients() if i.get_name() == name), None)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        added_ingredient = burger.ingredients[0]
        assert added_ingredient.get_name() == name
        assert added_ingredient.get_type() == ing_type
        assert added_ingredient.get_price() == price

    def test_remove_ingredient(self,database): #тест_удаление_ингридиентов
        burger = Burger()
        ingredient = database.available_ingredients()[0]
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self,database):#тест_перемещение_элементов
        burger = Burger()
        ingredient1, ingredient2 = database.available_ingredients()[:2]
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient2 and burger.ingredients[1] == ingredient1

    def test_get_price(self,database): #тест_расчет_цены
        burger = Burger()
        bun = database.available_buns()[0]
        burger.set_buns(bun)
        ingredients = database.available_ingredients()[:2]
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)
        assert burger.get_price() == bun.get_price() * 2 + sum(ingredient.get_price() for ingredient in ingredients)

    def test_get_receipt(self,database): #тест_получения_чека
        burger = Burger()
        bun = database.available_buns()[0]
        burger.set_buns(bun)
        ingredients = database.available_ingredients()[:2]
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)
        assert f'(==== {bun.get_name()} ====)' in burger.get_receipt()
        for ingredient in ingredients:
            assert f'= {ingredient.get_type().lower()} {ingredient.get_name()} =' in burger.get_receipt()