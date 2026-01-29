from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

class TestBurger:
    #Создать пустой бургер
    def test_create_empty_burger(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []
    #Назначить бургеру булочку
    def test_setter_accept_right_bun(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun
    #Добавить в бургер начинку
    def test_successful_ingridient_adding(self):
        burger = Burger()
        mock_ingrdnt = Mock()
        mock_ingrdnt.name = 'Биокотлета из марсианской Магнолии'
        mock_ingrdnt.type = INGREDIENT_TYPE_FILLING
        mock_ingrdnt.price = 20.2
        burger.add_ingredient(mock_ingrdnt)
        assert burger.ingredients[0] == mock_ingrdnt
    #Удалить начинку
    def test_successful_ingridient_removing(self):
        burger = Burger()
        mock_ingrdnt = Mock()
        mock_ingrdnt.name = 'Соус фирменный Space Sauce'
        mock_ingrdnt.type = INGREDIENT_TYPE_SAUCE
        mock_ingrdnt.price = 20.2
        burger.add_ingredient(mock_ingrdnt)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0
    #Поменять начинку местами
    def test_move_ingredients(self, ingredient_filling, ingredient_sauce):
        burger = Burger()
        burger.add_ingredient(ingredient_filling)
        burger.add_ingredient(ingredient_sauce)
        burger.move_ingredient(1,0)
        assert burger.ingredients[1] == ingredient_filling
    #Получить стоимость бургера
    def test_getter_return_right_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 10.11
        mock_ingrdnt = Mock()
        mock_ingrdnt.get_price.return_value = 10.11
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingrdnt)
        assert burger.get_price() == 30.33
    #Получить рецепт бургера
    def test_getter_return_right_recipe(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 10.11
        mock_bun.get_name.return_value = 'Булочка'
        mock_ingrdnt = Mock()
        mock_ingrdnt.get_price.return_value = 10.11
        mock_ingrdnt.get_name.return_value = 'Биокотлета из марсианской Магнолии'
        mock_ingrdnt.get_type.return_value = 'FILLING'
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingrdnt)
        assert burger.get_receipt() == "(==== Булочка ====)\n= filling Биокотлета из марсианской Магнолии =\n(==== Булочка ====)\n\nPrice: 30.33"
