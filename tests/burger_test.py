import pytest
from data import Data


class TestBurger:

    # тест на получение названия булки
    @pytest.mark.parametrize('bun_object,result', [('bun_mock', 'bun_mock'), (None, None)])
    def test_set_buns_true(self, burger, bun_mock, bun_object, result):
        burger.set_buns(bun_object)
        assert burger.bun is result

    # тест на получение названия булки none
    def test_set_buns_none_true(self, burger):
        burger.set_buns(None)
        assert burger.bun is None

    # тест на добавление ингредиента
    def test_add_ingredient_true(self, burger, ingredient_sauce_mock):
        burger.add_ingredient(ingredient_sauce_mock)
        assert ingredient_sauce_mock in burger.ingredients

    # тест на удаление ингредиента
    def test_remove_ingredient_true(self, burger, ingredient_sauce_mock):
        burger.add_ingredient(ingredient_sauce_mock)
        burger.remove_ingredient(0)
        assert ingredient_sauce_mock not in burger.ingredients

    # тест на перемещение ингредиента
    def test_move_ingredient_true(self, burger, ingredient_sauce_mock, ingredient_filling_mock):
        burger.add_ingredient(ingredient_sauce_mock)
        burger.add_ingredient(ingredient_filling_mock)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_filling_mock, ingredient_sauce_mock]

    # тест на получение стоимости бургера
    @pytest.mark.parametrize('get_price_burger_components,result', [({"bun_price": Data.PRICE_300,
                                                                      "sauce_price": Data.PRICE_100,
                                                                      "filling_price": Data.PRICE_300,
                                                                      "bun_name": Data.RED_BUN,
                                                                      "sauce_name": Data.HOT_INGREDIENT_SAUCE,
                                                                      "filling_name":
                                                                          Data.SAUSAGE_INGREDIENT_FILLING
                                                                      }, 1000),
                                                                    ({"bun_price": Data.PRICE_100,
                                                                      "sauce_price": Data.PRICE_200,
                                                                      "filling_price": Data.PRICE_200,
                                                                      "bun_name": Data.BLACK_BUN,
                                                                      "sauce_name": Data.SOUR_INGREDIENT_SAUCE,
                                                                      "filling_name":
                                                                          Data.DINOSAUR_INGREDIENT_FILLING
                                                                      }, 600)],
                             indirect=["get_price_burger_components"])
    def test_get_price_true(self, get_price_burger_components, result):
        assert get_price_burger_components.get_price() == result

    # тест на получение чека
    @pytest.mark.parametrize('get_price_burger_components,result', [({"bun_price": Data.PRICE_300,
                                                                      "sauce_price": Data.PRICE_100,
                                                                      "filling_price": Data.PRICE_300,
                                                                      "bun_name": Data.RED_BUN,
                                                                      "sauce_name": Data.HOT_INGREDIENT_SAUCE,
                                                                      "filling_name":
                                                                          Data.SAUSAGE_INGREDIENT_FILLING},
                                                                     Data.RECEIPT_1),
                                                                    ({"bun_price": Data.PRICE_100,
                                                                      "sauce_price": Data.PRICE_200,
                                                                      "filling_price": Data.PRICE_200,
                                                                      "bun_name": Data.BLACK_BUN,
                                                                      "sauce_name": Data.SOUR_INGREDIENT_SAUCE,
                                                                      "filling_name":
                                                                          Data.DINOSAUR_INGREDIENT_FILLING},
                                                                     Data.RECEIPT_2)],
                             indirect=["get_price_burger_components"])
    def test_get_receipt_true(self, get_price_burger_components, result):
        assert get_price_burger_components.get_receipt() == result
