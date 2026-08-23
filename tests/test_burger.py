import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from helpers import generate_ingredient_mock, generate_bun_mock
import allure

class TestBurger: 
    def test_constructor_correct_initial_data(self):
        burger = Burger()
        assert burger.bun == None and burger.ingredients == []

    def test_set_buns_correct_data_bun_set(self):
        bun = Bun('Булочка с кунжутом', 20)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_correct_ingredient_added(self):
        burger = Burger()
        ingredient_mock = generate_ingredient_mock('тест1', 10, 'соус')
        burger.add_ingredient(ingredient_mock)
        assert burger.ingredients[0] == ingredient_mock

    @allure.title('проверка удаления ингредиента по корректному индексу')
    @pytest.mark.parametrize('index',[0,2,4])
    def test_remove_ingredient_correct_index_removed(self, index):
        burger = Burger()
        burger.add_ingredient(generate_ingredient_mock('тест1', 10, 'соус'))
        burger.add_ingredient(generate_ingredient_mock('тест2', 10, 'соус'))
        burger.add_ingredient(generate_ingredient_mock('тест3', 10, 'соус'))
        burger.add_ingredient(generate_ingredient_mock('тест4', 10, 'соус'))
        burger.add_ingredient(generate_ingredient_mock('тест5', 10, 'соус'))
        saveRemoveIngredient = burger.ingredients[index]
        burger.remove_ingredient(index)

        assert len(burger.ingredients) == 4 and saveRemoveIngredient not in burger.ingredients  

    
    @pytest.mark.parametrize('old,new,name', [[0,1,'тест1'], [2,3,'тест3'], [0,3,'тест1'], [3,4,'тест4'], [0,4,'тест1'], [4,0,'тест5']])
    def test_move_ingredient_correct_inputs_moved(self,old,new,name):
        burger = Burger()
        burger.add_ingredient(generate_ingredient_mock('тест1', 10, 'соус'))
        burger.add_ingredient(generate_ingredient_mock('тест2', 20, 'начинка'))
        burger.add_ingredient(generate_ingredient_mock('тест3', 30, 'соус'))
        burger.add_ingredient(generate_ingredient_mock('тест4', 30, 'соус'))
        burger.add_ingredient(generate_ingredient_mock('тест5', 30, 'соус'))
        burger.move_ingredient(old, new)

        assert burger.ingredients[new].get_name() == name

    @allure.title('проверка получения цены за бургер с ингредиентами')
    def test_get_price_with_ingredients_correct_price_returned(self):
        burger = Burger()
        burger.set_buns(generate_bun_mock(5))
        burger.add_ingredient(generate_ingredient_mock('тест1', 10, 'соус'))
        burger.add_ingredient(generate_ingredient_mock('тест2', 20, 'начинка'))
        burger.add_ingredient(generate_ingredient_mock('тест3', 30, 'соус'))

        assert burger.get_price() == 70

    def test_get_price_without_ingredients_correct_price_returned(self):
        burger = Burger()
        burger.set_buns(generate_bun_mock(5))
        assert burger.get_price() == 10
    
    def test_get_receipt_with_ingredients_correct_receipt(self):
        burger = Burger()
        burger.set_buns(generate_bun_mock(5, 'С кунжутом'))
        burger.add_ingredient(generate_ingredient_mock('тест1', 10, 'соус'))
        burger.add_ingredient(generate_ingredient_mock('тест2', 20, 'начинка'))
        burger.add_ingredient(generate_ingredient_mock('тест3', 30, 'соус'))
        print(burger.get_receipt())
        assert burger.get_receipt() == "(==== С кунжутом ====)\n= соус тест1 =\n= начинка тест2 =\n= соус тест3 =\n(==== С кунжутом ====)\n\nPrice: 70"

    def test_get_receipt_without_ingredients_correct_receipt(self):
        burger = Burger()
        burger.set_buns(generate_bun_mock(5, 'С кунжутом'))
        assert burger.get_receipt() == "(==== С кунжутом ====)\n(==== С кунжутом ====)\n\nPrice: 10"
