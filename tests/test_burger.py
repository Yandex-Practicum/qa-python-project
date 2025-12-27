from unittest.mock import patch
import pytest
from unittest.mock import Mock
from burger import Burger


class TestBurger:

    mock_1 = Mock()
    mock_2 = Mock()
    test_data = {
        'bun_name': {
            'eng': 'Bulka',
            'rus': 'Булка',
            'int': 666
        },
        'sauce_name': {
            'eng': 'Sauce',
            'rus': 'Соус',
            'int': 777,
        },
        'type': {
            'eng': 'Spicy',
            'rus': 'Острый',
            'int': 777,

        },
        'price': {
            'float': 66.66,
            'int': 66,
            'zero_float': 0,
            'zero_int': 0.0
        }
    }

    def test_set_buns_success(self):

        burger = Burger()
        burger.set_buns(self.mock_1)

        assert burger.bun == self.mock_1

    def test_add_ingredient_success(self):

        burger = Burger()
        burger.add_ingredient(self.mock_1)

        assert self.mock_1 in burger.ingredients

    def test_remove_ingredient_success(self):

        burger = Burger()
        burger.add_ingredient(self.mock_1)
        burger.remove_ingredient(0)

        assert self.mock_1 not in burger.ingredients

    def test_move_ingredient_success(self):

        mock_ingredient_1 = self.mock_1
        mock_ingredient_2 = self.mock_1
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[1] == mock_ingredient_1


    @pytest.mark.parametrize('bun_price, ingredient_price, ingredients, expected_result', [
        [test_data['price']['int'], test_data['price']['int'], [mock_2, mock_2], 264],
        [test_data['price']['float'], test_data['price']['float'], [mock_2], 199.98],
        [test_data['price']['int'], test_data['price']['zero_int'], [], 132],
        [test_data['price']['zero_int'], test_data['price']['int'], [mock_2], 66.0],
        [test_data['price']['zero_float'], test_data['price']['zero_float'], [], 0]
    ])
    def test_get_price_success(self, bun_price, ingredient_price, ingredients, expected_result):

        burger = Burger()
        self.mock_1.get_price.return_value = bun_price
        self.mock_2.get_price.return_value = ingredient_price

        with patch.object(burger, 'bun', self.mock_1), \
             patch.object(burger, 'ingredients', ingredients):

            assert burger.get_price() == expected_result

    @pytest.mark.parametrize('bun_object, bun_name, ingredient_type, ingredient_name, ingredients, price, expected_result', [
        [mock_1, test_data['bun_name']['rus'], test_data['type']['rus'], test_data['sauce_name']['rus'], [mock_2, mock_2], '666',
         '(==== Булка ====)\n'
          '= острый Соус =\n'
          '= острый Соус =\n'
          '(==== Булка ====)\n'
          '\n'
          'Price: 666'],
        [mock_1, test_data['bun_name']['eng'], test_data['type']['eng'], test_data['sauce_name']['eng'], [mock_2], '666',
         '(==== Bulka ====)\n= spicy Sauce =\n(==== Bulka ====)\n\nPrice: 666'],
        [mock_1, test_data['sauce_name']['int'], test_data['type']['int'], test_data['sauce_name']['int'], [mock_2], '666',
         '(==== 777 ====)\n= 777 777 =\n(==== 777 ====)\n\nPrice: 666']
    ])
    def test_get_receipt_success(self, bun_object, bun_name, ingredient_type, ingredient_name, ingredients, price, expected_result):

        burger = Burger()
        self.mock_1.get_name.return_value = bun_name
        self.mock_2.get_type.return_value = ingredient_type
        self.mock_2.get_name.return_value = ingredient_name

        with patch.object(burger, 'bun', bun_object), \
             patch.object(burger, 'ingredients', ingredients), \
             patch('burger.Burger.get_price') as get_burger_price:

            get_burger_price.return_value = price
            assert burger.get_receipt() == expected_result
