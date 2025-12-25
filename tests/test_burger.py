import pytest
from unittest.mock import Mock

from helpers import Helpers
from praktikum.burger import Burger


class TestBurger:

    def test_burger_object_has_none_bun_attribute(self):

        burger = Burger()

        assert burger.bun is None

    def test_burger_object_has_empty_ingredients_list(self):

        burger = Burger()

        assert burger.ingredients == []

    def test_set_buns_return_bun_object(self):

        mock_buns = Mock()
        mock_buns.name = 'bulichka'
        mock_buns.price = 1.5
        burger = Burger()

        burger.set_buns(mock_buns)

        assert burger.bun == mock_buns

    @pytest.mark.parametrize('ingredient_type, ingredient_name, price', [
        [Helpers.SOUSETS['ingredient_type'], Helpers.SOUSETS['name'], Helpers.SOUSETS['price']],
        [Helpers.LUCHOK['ingredient_type'], Helpers.LUCHOK['name'], Helpers.LUCHOK['price']]
    ])
    def test_add_ingredient_return_list_with_assigned_ingredient(self, ingredient_type, ingredient_name, price):

        mock_ingredient = Mock()
        mock_ingredient.ingredient_type = ingredient_type
        mock_ingredient.ingredient_name = ingredient_name
        mock_ingredient.price = price

        burger = Burger()

        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient_return_empty_ingredients_list(self):

        mock_sousets = Mock()
        mock_sousets.ingredient_type = Helpers.SOUSETS['ingredient_type']
        mock_sousets.name = Helpers.SOUSETS['name']
        mock_sousets.price = Helpers.SOUSETS['price']

        burger = Burger()

        burger.add_ingredient(mock_sousets)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient_return_mixed_list(self):

        #  Создаем мок-объекты класса Ингредиент – соусец и лучок, а также объект класса Бургер
        mock_ingredient1 = Mock()
        mock_ingredient1.ingredient_type = Helpers.SOUSETS['ingredient_type']
        mock_ingredient1.name = Helpers.SOUSETS['name']
        mock_ingredient1.price = Helpers.SOUSETS['price']

        mock_ingredient2 = Mock()
        mock_ingredient2.ingredient_type = Helpers.LUCHOK['ingredient_type']
        mock_ingredient2.name = Helpers.LUCHOK['name']
        mock_ingredient2.price = Helpers.LUCHOK['price']

        burger = Burger()

        #  Добавляем в бургер ингредиенты: сначала соусец, затем лучок
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        #  Перемещаем соусец с первого на второе место в списке ингредиентов
        burger.move_ingredient(0, 1)

        #  Проверяем, что соусец теперь действительно изменил свой индекс
        assert burger.ingredients == [mock_ingredient2, mock_ingredient1]

    def test_get_price_return_amount_of_bun_double_price_and_ingredients_price(self):

        # ingredient1 = Ingredient(Helpers.SOUSETS['ingredient_type'], Helpers.SOUSETS['name'], Helpers.SOUSETS['price'])
        # ingredient2 = Ingredient(Helpers.LUCHOK['ingredient_type'], Helpers.LUCHOK['name'], Helpers.LUCHOK['price'])
        # bun = Bun(Helpers.BULICHKA['name'], Helpers.BULICHKA['price'])

        mock_ingredient1 = Mock()
        mock_ingredient1.ingredient_type = Helpers.SOUSETS['ingredient_type']
        mock_ingredient1.name = Helpers.SOUSETS['name']
        mock_ingredient1.price = Helpers.SOUSETS['price']
        mock_ingredient1.get_price.return_value = Helpers.SOUSETS['price']

        mock_ingredient2 = Mock()
        mock_ingredient2.ingredient_type = Helpers.LUCHOK['ingredient_type']
        mock_ingredient2.name = Helpers.LUCHOK['name']
        mock_ingredient2.price = Helpers.LUCHOK['price']
        mock_ingredient2.get_price.return_value = Helpers.LUCHOK['price']

        mock_bun = Mock()
        mock_bun.name = Helpers.BULICHKA['name']
        mock_bun.price = Helpers.BULICHKA['price']
        mock_bun.get_price.return_value = Helpers.BULICHKA['price']

        burger = Burger()

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        assert \
            burger.get_price() == mock_ingredient1.price + mock_ingredient2.price + (mock_bun.price * 2)

    def test_get_receipt_return_string_with_buns_ingredients_and_amount_price_of_burger(self):

        mock_ingredient1 = Mock()
        mock_ingredient1.ingredient_type = Helpers.SOUSETS['ingredient_type']
        mock_ingredient1.name = Helpers.SOUSETS['name']
        mock_ingredient1.price = Helpers.SOUSETS['price']
        mock_ingredient1.get_name.return_value = Helpers.SOUSETS['name']
        mock_ingredient1.get_price.return_value = Helpers.SOUSETS['price']
        mock_ingredient1.get_type.return_value = Helpers.SOUSETS['ingredient_type']

        mock_ingredient2 = Mock()
        mock_ingredient2.ingredient_type = Helpers.LUCHOK['ingredient_type']
        mock_ingredient2.name = Helpers.LUCHOK['name']
        mock_ingredient2.price = Helpers.LUCHOK['price']
        mock_ingredient2.get_name.return_value = Helpers.LUCHOK['name']
        mock_ingredient2.get_price.return_value = Helpers.LUCHOK['price']
        mock_ingredient2.get_type.return_value = Helpers.LUCHOK['ingredient_type']

        mock_bun = Mock()
        mock_bun.name = Helpers.BULICHKA['name']
        mock_bun.price = Helpers.BULICHKA['price']
        mock_bun.get_name.return_value = Helpers.BULICHKA['name']
        mock_bun.get_price.return_value = Helpers.BULICHKA['price']

        burger = Burger()

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        amount_price = mock_ingredient1.price + mock_ingredient2.price + (mock_bun.price * 2)

        result = f'(==== {mock_bun.name} ====)\n' \
                 f'= {mock_ingredient1.ingredient_type.lower()} {mock_ingredient1.name} =\n' \
                 f'= {mock_ingredient2.ingredient_type.lower()} {mock_ingredient2.name} =\n' \
                 f'(==== {mock_bun.name} ====)\n' \
                 f'\nPrice: {amount_price}'

        assert burger.get_receipt() == result
