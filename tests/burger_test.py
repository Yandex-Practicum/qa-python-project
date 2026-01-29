import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from unittest.mock import Mock


class TestBurger():

    def test_set_buns(self, burgers):
        mock_bun = Mock(spec=Bun)
        burgers.set_buns(mock_bun)
        assert burgers.bun == mock_bun, f'{burgers.bun} не содержит {mock_bun}'

    def test_add_ingredient(self, burgers):
        mock_ingredient = Mock(spec=Ingredient)
        burgers.add_ingredient(mock_ingredient)
        assert burgers.ingredients == [mock_ingredient], \
            f'Список {burgers.ingredients} не содержит {mock_ingredient}'

    def test_remove_ingredient(self, burgers):
        mock_ingredient = Mock(spec=Ingredient)
        burgers.add_ingredient(mock_ingredient)
        burgers.remove_ingredient(0)
        assert burgers.ingredients == [], f'Список {burgers.ingredients} не пустой'

    def test_move_ingredient(self, burgers):
        mock_first_ingredient = Mock(spec=Ingredient)
        mock_second_ingredient = Mock(spec=Ingredient)
        burgers.add_ingredient(mock_first_ingredient)
        burgers.add_ingredient(mock_second_ingredient)
        burgers.move_ingredient(0, 1)
        assert burgers.ingredients[0] == mock_second_ingredient and burgers.ingredients[1] == mock_first_ingredient

    def test_get_price(self, burgers):
        mock_bun = Mock(spec=Bun)
        mock_first_ingredient = Mock(spec=Ingredient)
        mock_second_ingredient = Mock(spec=Ingredient)
        mock_bun.get_price.return_value = 200
        mock_first_ingredient.get_price.return_value = 100
        mock_second_ingredient.get_price.return_value = 200
        burgers.set_buns(mock_bun)
        price_bun = burgers.get_price()
        burgers.add_ingredient(mock_first_ingredient)
        burgers.add_ingredient(mock_second_ingredient)
        price_bun_and_ingredients = burgers.get_price()
        assert price_bun == 400 and price_bun_and_ingredients == 700, \
            f'Цена булки без ингредиентов {price_bun} не равна 400 или цена булки с ингредиентами {price_bun_and_ingredients} не равна 600'

    @pytest.mark.parametrize('ingredient_name, ingredient_price, ingredient_type',
                             [("hot sauce", 100, INGREDIENT_TYPE_SAUCE),
                              ("cutlet", 100, INGREDIENT_TYPE_FILLING)])
    def test_get_receipt(self, burgers, ingredient_name, ingredient_price, ingredient_type):
        mock_bun = Mock(spec=Bun)
        mock_ingredient = Mock(spec=Ingredient)
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100
        mock_ingredient.get_name.return_value = ingredient_name
        mock_ingredient.get_price.return_value = ingredient_price
        mock_ingredient.get_type.return_value = ingredient_type
        burgers.set_buns(mock_bun)
        burgers.add_ingredient(mock_ingredient)
        receipt = burgers.get_receipt()
        excepted_receipt = [f'(==== {burgers.bun.get_name()} ====)']
        for ingredient in burgers.ingredients:
            excepted_receipt.append(f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =')
        excepted_receipt.append(f'(==== {burgers.bun.get_name()} ====)\n')
        excepted_receipt.append(f'Price: {burgers.get_price()}')
        assert receipt == '\n'.join(excepted_receipt), f'{receipt} не равно {excepted_receipt}'
