from ingredient import Ingredient
import pytest


class TestBun:

    test_data = {
        'name': {
            'eng': 'TarTatar',
            'rus': 'Мазик',
            'int': 666
        },
        'type': {
            'eng': 'Sauce',
            'rus': 'Соус',
            'int': 777,

        },
        'price': {
            'float': 66.66,
            'int': 66,
            'zero_float': 0,
            'zero_int': 0.0
        }
    }

    @pytest.mark.parametrize('price', [test_data['price']['float'],
                                       test_data['price']['int'],
                                       test_data['price']['zero_float'],
                                       test_data['price']['zero_int']
                                       ])
    def test_get_name_success(self, price):

        ingredient = Ingredient(self.test_data['type']['type_eng'], self.test_data['name']['eng'], price)

        assert ingredient.get_price() == price

    @pytest.mark.parametrize('name', [test_data['name']['eng'],
                                      test_data['name']['rus'],
                                      test_data['name']['int']
                                      ])
    def test_get_name_success(self, name):

        ingredient = Ingredient(self.test_data['type']['eng'], name, self.test_data['price']['float'])

        assert ingredient.get_name() == name

    @pytest.mark.parametrize('type', [test_data['type']['eng'],
                                      test_data['type']['rus'],
                                      test_data['type']['int']
                                      ])
    def test_get_type_success(self, type):

        ingredient = Ingredient(type, self.test_data['name']['eng'], self.test_data['price']['float'])

        assert ingredient.get_type() == type
