import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestBurger:
        @pytest.fixture
        def burgers(self):
            return Burger()
 
        @pytest.fixture
        def mock_bun(self):
            mock = Mock(spec=Bun)
            mock.get_name.return_value = "test_bun"
            mock.get_price.return_value = 100
            return mock

        @pytest.fixture
        def mock_ingredient(self):
            mock = Mock(spec=Ingredient)
            mock.get_name.return_value = "test_ingredient"
            mock.get_price.return_value = 50
            mock.get_type.return_value = "SAUCE"
            return mock        

        def test_init(self, burgers):
            """Проверка, что нет булочки и список ингридиентов пустой."""
            assert burgers.bun is None
            assert burgers.ingredients == []

        def test_set_buns(self, burgers, mock_bun):
            """Проверка получения булочки."""
            burgers.set_buns(mock_bun)
            assert burgers.bun == mock_bun

        def test_add_ingredients(self, burgers, mock_ingredient):
            """Проверка добавления ингридиента в бургер"""
            burgers.add_ingredient(mock_ingredient)
            assert len(burgers.ingredients) == 1   
           
        def test_remove_ingredient(self, burgers, mock_ingredient):
            """Проверка удаления ингридиентов."""
            burgers.add_ingredient(mock_ingredient)
            burgers.remove_ingredient(0)
            assert len(burgers.ingredients) == 0

        def test_move_ingredient(self, burgers, mock_ingredient):
            """Проверка перемещения ингридиентов."""
            new_ingredient = Mock(spec=Ingredient)
            burgers.add_ingredient(mock_ingredient)
            burgers.add_ingredient(new_ingredient)
            burgers.move_ingredient(0, 1)

            assert burgers.ingredients[0] is new_ingredient

        @pytest.mark.parametrize("bun_price, ingredient_price, final_price", [
            (100, [], 200),
            (200, [100], 500),
            (400, [25, 75, 100], 1000)
        ])
        def test_get_price(self, burgers, mock_bun, bun_price, ingredient_price, final_price):
            """Проверка получения стоимости бургера с использованием параметризации."""
            mock_bun.get_price.return_value = bun_price
            burgers.set_buns(mock_bun)
            for price in ingredient_price:
                ingredient_mock = Mock(spec=Ingredient)
                ingredient_mock.get_price.return_value = price
                burgers.add_ingredient(ingredient_mock)

            assert burgers.get_price() == final_price

        def test_get_receipt(self, burgers, mock_bun, mock_ingredient):
            """Проверка получения чека заказа."""
            burgers.set_buns(mock_bun)
            burgers.add_ingredient(mock_ingredient)

            receipt = burgers.get_receipt()

            final_receipt = (
                '(==== test_bun ====)\n'
                '= sauce test_ingredient =\n'
                '(==== test_bun ====)\n\n'
                'Price: 250'
            )

            assert receipt == final_receipt


     