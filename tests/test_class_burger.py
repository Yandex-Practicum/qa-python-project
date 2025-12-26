import pytest

from unittest.mock import Mock
from data import BurgerComponents as BC, IngredientIndex as II, BurgerPrices as BP
from burger import Burger
from tests.conftest import burger


### Тесты, покрывающие класс Burger ###
class TestBurgerMethods:

    ### Тесты для конструктора __init__ ###
    # Проверяем, что при первоначальном создании объекта класса Burger
    # в нём нет ни одной булки
    def test_burger_bun_true(self):
        burger = Burger()
        assert burger.bun == None

    # Проверяем, что при первоначальном создании объекта класса Burger
    # в нём нет никаких ингредиентов
    def test_burger_ingredients_true(self):
        burger = Burger()
        assert burger.ingredients == []

    ### Тесты для метода set_buns() ###
    # Добавление 1 любой булки из ассортимента в бургер (3 варианта булок)
    @pytest.mark.parametrize('bun_name, bun_price',
                             [
                                 (BC.BUN_NAME_1, BC.BUN_PRICE_1),
                                 (BC.BUN_NAME_2, BC.BUN_PRICE_2),
                                 (BC.BUN_NAME_3, BC.BUN_PRICE_3)
                             ]
                             )
    def test_set_buns_1_bun_successfully(self, burger, bun_name, bun_price):
        mock_bun = Mock()
        mock_bun.name = bun_name
        mock_bun.price = bun_price
        burger.set_buns(mock_bun)
        assert burger.bun.name == bun_name and burger.bun.price == bun_price

    # Добавление двух булок (верхней и нижней) в бургер
    def test_set_buns_2_buns_successfully(self, burger):
        mock_bun_1 = Mock()
        mock_bun_1.name = BC.BUN_NAME_1
        mock_bun_1.price = BC.BUN_PRICE_1
        mock_bun_2 = Mock()
        mock_bun_2.name = BC.BUN_NAME_2
        mock_bun_2.price = BC.BUN_PRICE_2
        burger.set_buns(mock_bun_1)
        burger.set_buns(mock_bun_2)
        assert burger.bun.name == BC.BUN_NAME_2 and burger.bun.price == BC.BUN_PRICE_2

    ### Тесты для метода add_ingredient() ###
    # Добавление 1 любого ингредиента из ассортимента в бургер (6 вариантов ингредиентов)
    @pytest.mark.parametrize('ingredient_type, ingredient_name, ingredient_price',
                             [
                                 (BC.INGREDIENT_TYPE_1, BC.SAUCE_NAME_1, BC.SAUCE_PRICE_1),
                                 (BC.INGREDIENT_TYPE_1, BC.SAUCE_NAME_2, BC.SAUCE_PRICE_2),
                                 (BC.INGREDIENT_TYPE_1, BC.SAUCE_NAME_3, BC.SAUCE_PRICE_3),
                                 (BC.INGREDIENT_TYPE_2, BC.FILLING_NAME_1, BC.FILLING_PRICE_1),
                                 (BC.INGREDIENT_TYPE_2, BC.FILLING_NAME_2, BC.FILLING_PRICE_2),
                                 (BC.INGREDIENT_TYPE_2, BC.FILLING_NAME_3, BC.FILLING_PRICE_3)
                            ]
                             )
    def test_add_ingredient_1_ingredient_successfully(self, burger, ingredient_type, ingredient_name, ingredient_price):
        mock_ingredient = Mock()
        mock_ingredient.ingredient_type = ingredient_type
        mock_ingredient.name = ingredient_name
        mock_ingredient.price = ingredient_price
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    # Добавление 1 соуса и 1 начинки из ассортимента в бургер
    def test_add_ingredient_1_sauce_and_1_filling(self, burger, mock_sauce_1, mock_filling_1):
        burger.add_ingredient(mock_sauce_1)
        burger.add_ingredient(mock_filling_1)
        assert len(burger.ingredients) == 2 and burger.ingredients[0].name == BC.SAUCE_NAME_1 and burger.ingredients[1].name == BC.FILLING_NAME_1

    # Добавление 2 разных соусов и 2 разных начинок из ассортимента в бургер
    def test_add_ingredient_2_sauces_and_2_fillings(self, burger, mock_sauce_1, mock_sauce_2, mock_filling_1, mock_filling_2):
        burger.add_ingredient(mock_sauce_1)
        burger.add_ingredient(mock_sauce_2)
        burger.add_ingredient(mock_filling_1)
        burger.add_ingredient(mock_filling_2)
        assert len(burger.ingredients) == 4 and burger.ingredients[1].name == BC.SAUCE_NAME_2 and burger.ingredients[3].name == BC.FILLING_NAME_2

    # Добавление 3 одинаковых соусов и 3 одинаковых начинок из ассортимента в бургер
    def test_add_ingredients_3_same_sauces_and_3_same_fillings(self, burger, mock_sauce_3, mock_filling_3):
        burger.add_ingredient(mock_sauce_3)
        burger.add_ingredient(mock_sauce_3)
        burger.add_ingredient(mock_sauce_3)
        burger.add_ingredient(mock_filling_3)
        burger.add_ingredient(mock_filling_3)
        burger.add_ingredient(mock_filling_3)
        assert len(burger.ingredients) == 6 and burger.ingredients[2].name == BC.SAUCE_NAME_3 and burger.ingredients[5].name == BC.FILLING_NAME_3

    ### Тесты для метода remove_ingredient() ###
    # Удаляем единственный игредиент из списка
    def test_remove_ingredient_when_only_one_ingredient_in_list(self, burger, mock_sauce_1):
        burger.add_ingredient(mock_sauce_1)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    # Удаляем два ингредиента из списка из двух ингредиентов
    def test_remove_ingredient_remove_all_2_ingredients_in_list(self, burger, mock_sauce_1, mock_filling_1):
        burger.add_ingredient(mock_sauce_1)
        burger.add_ingredient(mock_filling_1)
        burger.remove_ingredient(0)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    # Удаляем первый ингредиент из списка из двух ингредиентов
    def test_remove_ingredient_remove_first_ingredient_from_2_ingredients_in_list(self, burger, mock_sauce_2, mock_filling_2):
        burger.add_ingredient(mock_sauce_2)
        burger.add_ingredient(mock_filling_2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1 and burger.ingredients[0].name == BC.FILLING_NAME_2

    ### Тесты для метода move_ingredient() ###
    # Переместить 2 ингредиента в списке и поменять их местами
    def test_move_ingredient_swap_2_ingredients(self, burger, mock_sauce_1, mock_filling_1):
        burger.add_ingredient(mock_sauce_1)
        burger.add_ingredient(mock_filling_1)
        burger.move_ingredient(II.FIRST_INGREDIENT, II.SECOND_INGREDIENT)
        assert len(burger.ingredients) == 2 and burger.ingredients[0].name == BC.FILLING_NAME_1 and burger.ingredients[1].name == BC.SAUCE_NAME_1

    # Переместить 2 ингредиента на другие места в списке из 4 ингредиентов
    def test_move_ingredient_swap_4_ingredients(self, burger, mock_sauce_1, mock_filling_1, mock_sauce_2, mock_filling_2):
        burger.add_ingredient(mock_sauce_1)
        burger.add_ingredient(mock_filling_1)
        burger.add_ingredient(mock_sauce_2)
        burger.add_ingredient(mock_filling_2)
        burger.move_ingredient(II.FIRST_INGREDIENT, II.FOURTH_INGREDIENT)
        burger.move_ingredient(II.SECOND_INGREDIENT, II.THIRD_INGREDIENT)
        assert (len(burger.ingredients) == 4 and
                burger.ingredients[0].name == BC.FILLING_NAME_1 and
                burger.ingredients[1].name == BC.FILLING_NAME_2 and
                burger.ingredients[2].name == BC.SAUCE_NAME_2 and
                burger.ingredients[3].name == BC.SAUCE_NAME_1)

    ### Тесты для метода get_price() ###
    # Проверяем стоимость бургера с 2 чёрными булочками, без ингредиентов
    def test_get_price_only_buns(self, burger, mock_black_bun):
        burger.set_buns(mock_black_bun)
        assert burger.get_price() == BP.BURGER_PRICE_BLACK_BUNS

    # Проверяем стоимость бургера с 2 чёрными булочками, 1 сметаной и 1 динозавром
    def test_get_price_buns_and_2_ingredients(self, burger, mock_black_bun, mock_sauce_2, mock_filling_2):
        burger.set_buns(mock_black_bun)
        burger.add_ingredient(mock_sauce_2)
        burger.add_ingredient(mock_filling_2)
        assert burger.get_price() == BP.BURGER_PRICE_BB_SC_D

    # Проверяем стоимость бургера с 2 чёрными булочками, 1 сметаной, 1 чили-соусом, 1 динозавром и 1 сосиской
    def test_get_price_buns_and_4_ingredients(self, burger, mock_black_bun, mock_sauce_2, mock_sauce_3, mock_filling_2, mock_filling_3):
        burger.set_buns(mock_black_bun)
        burger.add_ingredient(mock_sauce_2)
        burger.add_ingredient(mock_sauce_3)
        burger.add_ingredient(mock_filling_2)
        burger.add_ingredient(mock_filling_3)
        assert burger.get_price() == BP.BURGER_PRICE_BB_SC_HC_D_S

    ### Тесты для метода get_receipt() ###
    # Проверяем получение рецепта: 2 чёрные булки
    def test_get_receipt_2_black_buns(self, burger, mock_black_bun):
        burger.set_buns(mock_black_bun)
        receipt = burger.get_receipt()
        expected_receipt = (
            "(==== black bun ====)\n"
            "(==== black bun ====)\n"
            "\nPrice: 200.0"
        )
        assert len(receipt) > 0 and burger.get_receipt() == expected_receipt

    # Проверяем получение рецепта: 2 чёрные булки, сметана и динозавр
    def test_get_receipt_2_black_buns_1_sauce_1_cutlet(self, burger, mock_black_bun, mock_sauce_2, mock_filling_2):
        burger.set_buns(mock_black_bun)
        burger.add_ingredient(mock_sauce_2)
        burger.add_ingredient(mock_filling_2)
        receipt = burger.get_receipt()
        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce sour cream =\n"
            "= filling dinosaur =\n"
            "(==== black bun ====)\n"
            "\nPrice: 600.0"
        )
        assert len(receipt) > 0 and burger.get_receipt() == expected_receipt
