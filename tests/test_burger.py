import pytest
from unittest.mock import Mock 
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from test_data import ingredient_list, bun_list

class TestBurger:
    def test_create_burger_empty_data(self, burger):
        assert(burger.bun is None)
        assert(len(burger.ingredients) == 0)

    @pytest.mark.parametrize('bun_name, bun_price', bun_list)
    def test_set_bun_success(self, burger, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        burger.set_buns(bun)
        assert(burger.bun.get_name() == bun_name)
        assert(burger.bun.get_price() == bun_price)

    @pytest.mark.parametrize('ingredient_type, ingredient_name, ingredient_price', ingredient_list)
    def test_add_ingredient_success(self, burger, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        burger.add_ingredient(ingredient)
        assert(len(burger.ingredients)==1)
        assert(burger.ingredients[0].get_name() == ingredient_name)
        assert(burger.ingredients[0].get_price() == ingredient_price)
        assert(burger.ingredients[0].get_type() == ingredient_type)

    @pytest.mark.parametrize('ingredient_type, ingredient_name, ingredient_price', ingredient_list)
    def test_add_ingredient_twice_success(self, burger, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient)
        assert(len(burger.ingredients)==2)
        assert(burger.ingredients[0].get_name() == ingredient_name)
        assert(burger.ingredients[0].get_price() == ingredient_price)
        assert(burger.ingredients[1].get_name() == ingredient_name)
        assert(burger.ingredients[1].get_price() == ingredient_price)

    def test_add_ingredient_multiple_ingredients_success(self, burger, database):
        ingredients = database.available_ingredients()
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)
        assert(burger.ingredients==ingredients)

    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5])
    def test_remove_ingredient_existing_index_success(self, ready_burger, index):
        ready_burger.remove_ingredient(index)
        assert(len(ready_burger.ingredients) == 5)

    @pytest.mark.parametrize('ingredient_type, ingredient_name, ingredient_price', ingredient_list)
    def test_remove_ingredient_non_existing_index_throws_exception(
                self, burger, ingredient_type, ingredient_name, ingredient_price):
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = ingredient_name
        mock_ingredient.get_type.return_value = ingredient_type
        mock_ingredient.get_price.return_value = ingredient_price
        burger.add_ingredient(mock_ingredient)
        try:
            burger.remove_ingredient(5)
        except IndexError:
            assert(len(burger.ingredients)==1)
            assert(burger.ingredients[0].get_name() == ingredient_name)
            assert(burger.ingredients[0].get_type() == ingredient_type)
            assert(burger.ingredients[0].get_price() == ingredient_price)

    @pytest.mark.parametrize('ingredient_type, ingredient_name, ingredient_price', ingredient_list)
    def test_remove_ingredient_single_success_empty_burger(
            self, burger, ingredient_type, ingredient_name, ingredient_price):
        mock_ingredient = Mock()
        mock_ingredient.configure_mock(ingredient_type=ingredient_type, 
                                       name=ingredient_name, price=ingredient_price)
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert(len(burger.ingredients) == 0)

    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5])
    def test_remove_ingredient_empty_burger_throws_exception(self, burger, index):
        try:
            burger.remove_ingredient(index)
        except IndexError:
            assert(len(burger.ingredients) == 0)

    @pytest.mark.parametrize('index,new_index', [[0, 1],
                                                 [0, 2],
                                                 [0, 3],
                                                 [0, 4],
                                                 [0, 5],
                                                 [1, 2],
                                                 [1, 3],
                                                 [1, 4],
                                                 [1, 5],
                                                 [2, 3],
                                                 [2, 4],
                                                 [2, 5],
                                                 [3, 4],
                                                 [3, 5],
                                                 [4, 5]])
    def test_move_ingredient_existing_indexes_success(self, ready_burger, index, new_index):
        name1 = ready_burger.ingredients[index].name
        price1 = ready_burger.ingredients[index].price
        num_ingredients = len(ready_burger.ingredients)
        ready_burger.move_ingredient(index, new_index)
        
        assert(len(ready_burger.ingredients) == num_ingredients)
        assert(ready_burger.ingredients[new_index].get_name() == name1)
        assert(ready_burger.ingredients[new_index].get_price() == price1)

    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5])
    def test_move_ingredient_same_indexes_no_changes(self, ready_burger, index):
        name1 = ready_burger.ingredients[index].name
        price1 = ready_burger.ingredients[index].price
        num_ingredients = len(ready_burger.ingredients)
        ready_burger.move_ingredient(index, index)
        
        assert(len(ready_burger.ingredients) == num_ingredients)
        assert(ready_burger.ingredients[index].get_name() == name1)
        assert(ready_burger.ingredients[index].get_price() == price1)

    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5])
    def test_move_ingredient_non_existing_index_throws_exception(self, ready_burger, index):
        name1 = ready_burger.ingredients[index].get_name()
        price1 = ready_burger.ingredients[index].get_price()
        num_ingredients = len(ready_burger.ingredients)

        try:
            ready_burger.move_ingredient(10, index)
        except IndexError:
             assert(len(ready_burger.ingredients) == num_ingredients)
             assert(ready_burger.ingredients[index].get_name() == name1)
             assert(ready_burger.ingredients[index].get_price() == price1)

    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5])
    def test_move_ingredient_non_existing_new_index_throws_exception(self, ready_burger, index):
        name1 = ready_burger.ingredients[index].get_name()
        price1 = ready_burger.ingredients[index].get_price()
        num_ingredients = len(ready_burger.ingredients)

        try:
            ready_burger.move_ingredient(index, 10)
        except IndexError:
            assert(len(ready_burger.ingredients) == num_ingredients)
            assert(ready_burger.ingredients[index].get_name() == name1)
            assert(ready_burger.ingredients[index].get_price() == price1)

    @pytest.mark.parametrize('bun_name, bun_price', bun_list)
    def test_get_price_valid_params_success(self, ready_burger, bun_name, bun_price):
        mock_bun = Mock()
        mock_bun.configure_mock(name=bun_name, price=bun_price)
        mock_bun.get_price.return_value = bun_price
        ready_burger.set_buns(mock_bun)

        price_burger = ready_burger.get_price()
        price_reference = 1200 + bun_price * 2
        assert(price_burger == price_reference)

    def test_get_price_empty_burger_throws_exception(self, burger):
        price = 0
        try:
            price = burger.get_price()
        except AttributeError:
            assert(price == 0)

    @pytest.mark.parametrize('bun_name, bun_price', bun_list)
    def test_get_price_burger_without_ingredients(self, burger, bun_name, bun_price):
        mock_bun = Mock()
        mock_bun.configure_mock(name=bun_name, price=bun_price)
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        price_burger = burger.get_price()
        price_reference = bun_price * 2
        assert(price_burger == price_reference)

    @pytest.mark.parametrize('bun_name,bun_price,index,new_index', [[bun_list[0][0], bun_list[0][1], 0, 1],
                                                                    [bun_list[0][0], bun_list[0][1], 0, 2],
                                                                    [bun_list[0][0], bun_list[0][1], 0, 3],
                                                                    [bun_list[0][0], bun_list[0][1], 0, 4],
                                                                    [bun_list[0][0], bun_list[0][1], 0, 5],
                                                                    [bun_list[0][0], bun_list[0][1], 1, 2],
                                                                    [bun_list[0][0], bun_list[0][1], 1, 3],
                                                                    [bun_list[0][0], bun_list[0][1], 1, 4],
                                                                    [bun_list[1][0], bun_list[1][1], 1, 5],
                                                                    [bun_list[1][0], bun_list[1][1], 2, 3],
                                                                    [bun_list[1][0], bun_list[1][1], 2, 4],
                                                                    [bun_list[1][0], bun_list[1][1], 2, 5],
                                                                    [bun_list[1][0], bun_list[1][1], 3, 4],
                                                                    [bun_list[1][0], bun_list[1][1], 3, 5],
                                                                    [bun_list[1][0], bun_list[1][1], 4, 5]])
    def test_get_price_moved_ingredients_no_changes(self, ready_burger, bun_name, bun_price, index, new_index):
        mock_bun = Mock()
        mock_bun.configure_mock(name=bun_name, price=bun_price)
        mock_bun.get_price.return_value = bun_price
        ready_burger.set_buns(mock_bun)
        ready_burger.move_ingredient(index, new_index)
        price_burger = ready_burger.get_price()
        price_reference = 1200 + bun_price * 2
        assert(price_burger == price_reference)

    @pytest.mark.parametrize('bun_name,bun_price,index,ingredient_price', [[bun_list[0][0], bun_list[0][1], 0, 100],
                                                                           [bun_list[0][0], bun_list[0][1], 1, 200],
                                                                           [bun_list[1][0], bun_list[1][1], 2, 300],
                                                                           [bun_list[1][0], bun_list[1][1], 3, 100],
                                                                           [bun_list[1][0], bun_list[1][1], 4, 200],
                                                                           [bun_list[1][0], bun_list[1][1], 5, 300]])
    def test_get_price_removed_ingredient_succcess(self, ready_burger, bun_name, bun_price, index, ingredient_price):
        mock_bun = Mock()
        mock_bun.configure_mock(name=bun_name, price=bun_price)
        mock_bun.get_price.return_value = bun_price
        ready_burger.set_buns(mock_bun)
        ready_burger.remove_ingredient(index)
        price_burger = ready_burger.get_price()
        price_reference = 1200 + bun_price * 2 - ingredient_price
        assert(price_burger == price_reference)

    def test_get_receipt_valid_params_success(self, burger):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Флюоресцентная булка R2-D3'
        mock_bun.get_price.return_value = 988
        burger.set_buns(mock_bun)
        ingredient1_mock = Mock()
        ingredient1_mock.get_name.return_value = 'Соус с шипами Антарианского плоскоходца'
        ingredient1_mock.get_type.return_value = 'SAUCE'
        ingredient1_mock.get_price.return_value = 88

        ingredient2_mock = Mock()
        ingredient2_mock.get_name.return_value = 'Мясо бессмертных моллюсков Protostomia'
        ingredient2_mock.get_type.return_value = 'FILLING'
        ingredient2_mock.get_price.return_value = 1337

        burger.add_ingredient(ingredient1_mock)
        burger.add_ingredient(ingredient2_mock)

        receipt = burger.get_receipt()
        receipt_ref = '\n'.join([
            "(==== Флюоресцентная булка R2-D3 ====)",
            "= sauce Соус с шипами Антарианского плоскоходца =",
            "= filling Мясо бессмертных моллюсков Protostomia =",
            "(==== Флюоресцентная булка R2-D3 ====)\n",
            "Price: 3401"
        ])
        assert(receipt == receipt_ref)

    def test_get_receipt_moved_ingredient_success(self, burger):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Флюоресцентная булка R2-D3'
        mock_bun.get_price.return_value = 988
        burger.set_buns(mock_bun)
        ingredient1_mock = Mock()
        ingredient1_mock.get_name.return_value = 'Соус с шипами Антарианского плоскоходца'
        ingredient1_mock.get_type.return_value = 'SAUCE'
        ingredient1_mock.get_price.return_value = 88

        ingredient2_mock = Mock()
        ingredient2_mock.get_name.return_value = 'Мясо бессмертных моллюсков Protostomia'
        ingredient2_mock.get_type.return_value = 'FILLING'
        ingredient2_mock.get_price.return_value = 1337

        burger.add_ingredient(ingredient1_mock)
        burger.add_ingredient(ingredient2_mock)
        burger.move_ingredient(0, 1)

        receipt = burger.get_receipt()
        receipt_ref = '\n'.join([
            "(==== Флюоресцентная булка R2-D3 ====)",
            "= filling Мясо бессмертных моллюсков Protostomia =",
            "= sauce Соус с шипами Антарианского плоскоходца =",
            "(==== Флюоресцентная булка R2-D3 ====)\n",
            "Price: 3401"
        ])
        assert(receipt == receipt_ref)

    def test_get_receipt_empty_burger_throws_exception(self, burger):
        receipt = ""
        try:
            receipt = burger.get_receipt()
        except AttributeError:
            assert(receipt == "")

    def test_get_receipt_burger_without_ingredients_success(self, burger):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Флюоресцентная булка R2-D3'
        mock_bun.get_price.return_value = 988
        burger.set_buns(mock_bun)
        
        receipt = burger.get_receipt()
        receipt_ref = '\n'.join([
            "(==== Флюоресцентная булка R2-D3 ====)",
            "(==== Флюоресцентная булка R2-D3 ====)\n",
            "Price: 1976"
        ])
        assert(receipt == receipt_ref)