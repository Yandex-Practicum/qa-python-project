from unittest.mock import Mock

import allure
import pytest

from praktikum.ingredient import Ingredient


@allure.feature('Burger')
@allure.story('Инициализация')
class TestBurgerInit:

    @allure.title('Новый бургер пустой: без булочки и ингредиентов')
    def test_burger_initial_state(self, burger):
        assert burger.bun is None
        assert burger.ingredients == []
        assert isinstance(burger.ingredients, list)


@allure.feature('Burger')
@allure.story('Назначение булочки')
class TestBurgerSetBuns:

    @allure.title('set_buns сохраняет переданную булочку')
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun
        mock_bun.get_name.assert_not_called()
        mock_bun.get_price.assert_not_called()

    @allure.title('set_buns с булочкой «{bun_name}» и ценой {bun_price}')
    @pytest.mark.parametrize(
        'bun_name, bun_price',
        [
            ('black bun', 100),
            ('white bun', 200),
            ('', 0),
            ('special bun', 999.99),
        ],
    )
    def test_set_buns_parametrized(self, burger, bun_name, bun_price):
        mock_bun_local = Mock()
        mock_bun_local.get_name.return_value = bun_name
        mock_bun_local.get_price.return_value = bun_price

        burger.set_buns(mock_bun_local)

        assert burger.bun is mock_bun_local


@allure.feature('Burger')
@allure.story('Добавление ингредиентов')
class TestBurgerAddIngredient:

    @allure.title('Добавление готового набора из фикстуры mock_ingredients')
    def test_add_ingredients_from_fixture(self, burger, mock_ingredients):
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        assert burger.ingredients == mock_ingredients

    @allure.title('Добавление {ingredient_count} ингредиент(а/ов)')
    @pytest.mark.parametrize('ingredient_count', [1, 3, 5, 10])
    def test_add_ingredient(self, burger, ingredient_count):
        mock_ingredients_local = [
            Mock(spec=Ingredient) for _ in range(ingredient_count)
        ]
        for ingredient in mock_ingredients_local:
            burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == ingredient_count
        assert burger.ingredients == mock_ingredients_local


@allure.feature('Burger')
@allure.story('Удаление ингредиентов')
class TestBurgerRemoveIngredient:

    @allure.title('Удаление ингредиента с индексом 2 из полного бургера')
    def test_remove_ingredient_from_full_burger(self, burger_with_ingredients, mock_ingredients):
        burger_with_ingredients.remove_ingredient(2)
        assert burger_with_ingredients.ingredients == [
            mock_ingredients[0],
            mock_ingredients[1],
            mock_ingredients[3],
        ]

    @allure.title('Удаление последнего ингредиента')
    def test_remove_last_ingredient(self, burger):
        mock_ingredient = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient)

        burger.remove_ingredient(0)

        assert burger.ingredients == []

    @allure.title('Удаление ингредиента по индексу {index}')
    @pytest.mark.parametrize(
        'index, expected_indices',
        [
            (0, [1, 2]),
            (1, [0, 2]),
            (2, [0, 1]),
        ],
    )
    def test_remove_ingredient(self, burger, index, expected_indices):
        ingredients = [Mock(spec=Ingredient) for _ in range(3)]
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)

        burger.remove_ingredient(index)

        expected = [ingredients[i] for i in expected_indices]
        assert burger.ingredients == expected

    @allure.title('IndexError при удалении по невалидному индексу {invalid_index}')
    @pytest.mark.parametrize('invalid_index', [1, 5, 10])
    def test_remove_ingredient_invalid_index_raises(self, burger, invalid_index):
        burger.add_ingredient(Mock(spec=Ingredient))

        with pytest.raises(IndexError):
            burger.remove_ingredient(invalid_index)


@allure.feature('Burger')
@allure.story('Перемещение ингредиентов')
class TestBurgerMoveIngredient:

    @allure.title('Перемещение первого ингредиента в конец списка')
    def test_move_first_ingredient_to_end(self, burger_with_ingredients, mock_ingredients):
        moved = mock_ingredients[0]

        burger_with_ingredients.move_ingredient(0, 3)

        assert burger_with_ingredients.ingredients[3] is moved
        assert burger_with_ingredients.ingredients == [
            mock_ingredients[1],
            mock_ingredients[2],
            mock_ingredients[3],
            mock_ingredients[0],
        ]

    @allure.title('Перемещение с индекса {index} на индекс {new_index}')
    @pytest.mark.parametrize(
        'index, new_index, expected_indices',
        [
            (0, 2, [1, 2, 0]),
            (2, 0, [2, 0, 1]),
            (1, 1, [0, 1, 2]),
        ],
    )
    def test_move_ingredient(self, burger, index, new_index, expected_indices):
        ingredients = [Mock(spec=Ingredient) for _ in range(3)]
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)

        burger.move_ingredient(index, new_index)

        expected = [ingredients[i] for i in expected_indices]
        assert burger.ingredients == expected

    @allure.title('IndexError при перемещении по невалидному индексу {invalid_index}')
    @pytest.mark.parametrize('invalid_index', [5, 10])
    def test_move_ingredient_invalid_index_raises(self, burger, invalid_index):
        for _ in range(3):
            burger.add_ingredient(Mock(spec=Ingredient))

        with pytest.raises(IndexError):
            burger.move_ingredient(invalid_index, 0)


@allure.feature('Burger')
@allure.story('Расчёт цены')
class TestBurgerGetPrice:

    @allure.title('Цена полного космического бургера (фикстуры mock_bun_full + mock_ingredients)')
    def test_get_price_full_burger(self, burger, mock_bun_full, mock_ingredients):
        burger.set_buns(mock_bun_full)
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)

        price = burger.get_price()

        assert price == 13533
        assert mock_bun_full.get_price.call_count == 1
        for ingredient in mock_ingredients:
            ingredient.get_price.assert_called_once()

    @allure.title('Цена при bun_price={bun_price}, ингредиенты={ingredient_prices}')
    @pytest.mark.parametrize(
        'bun_price, ingredient_prices, expected_price',
        [
            (100, [], 200),
            (100, [50], 250),
            (100, [50, 75, 25], 350),
            (200, [100, 100], 600),
            (0, [0, 0], 0),
            (25.5, [10.1, 20.2, 30.3], 111.6),
        ],
    )
    def test_get_price(self, burger, bun_price, ingredient_prices, expected_price):
        mock_bun_local = Mock()
        mock_bun_local.get_price.return_value = bun_price
        burger.set_buns(mock_bun_local)
        for price in ingredient_prices:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        price = burger.get_price()

        assert price == pytest.approx(expected_price)
        assert mock_bun_local.get_price.call_count == 1


@allure.feature('Burger')
@allure.story('Формирование чека')
class TestBurgerGetReceipt:

    @allure.title('Чек полного космического бургера (фикстуры mock_bun_full + mock_ingredients)')
    def test_get_receipt_full_burger(self, burger, mock_bun_full, mock_ingredients):
        burger.set_buns(mock_bun_full)
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()

        expected_lines = [
            '(==== fluorescent bun ====)',
            '= filling beef meteorite =',
            '= sauce galactic sauce =',
            '= filling exo-plantago salad =',
            '= filling asteroid mold cheese =',
            '(==== fluorescent bun ====)',
            '',
            'Price: 13533',
        ]
        assert receipt.split('\n') == expected_lines
        assert mock_bun_full.get_name.call_count == 2

    @allure.title('Чек только с булочкой')
    def test_get_receipt_only_bun(self, burger):
        mock_bun_local = Mock()
        mock_bun_local.get_name.return_value = 'black bun'
        mock_bun_local.get_price.return_value = 100
        burger.set_buns(mock_bun_local)

        receipt = burger.get_receipt()

        assert receipt.split('\n') == [
            '(==== black bun ====)',
            '(==== black bun ====)',
            '',
            'Price: 200',
        ]
        assert mock_bun_local.get_name.call_count == 2

    @allure.title('Параметризованный чек — булочка «{bun_name}»')
    @pytest.mark.parametrize(
        'bun_name, bun_price, ingredients_data, expected_lines',
        [
            (
                'black bun',
                100,
                [],
                [
                    '(==== black bun ====)',
                    '(==== black bun ====)',
                    '',
                    'Price: 200',
                ],
            ),
            (
                'white bun',
                200,
                [
                    ('SAUCE', 'hot sauce', 100),
                    ('FILLING', 'cutlet', 150),
                ],
                [
                    '(==== white bun ====)',
                    '= sauce hot sauce =',
                    '= filling cutlet =',
                    '(==== white bun ====)',
                    '',
                    'Price: 650',
                ],
            ),
        ],
        ids=['empty_burger', 'burger_with_two_ingredients'],
    )
    def test_get_receipt(self, burger, bun_name, bun_price, ingredients_data, expected_lines):
        mock_bun_local = Mock()
        mock_bun_local.get_name.return_value = bun_name
        mock_bun_local.get_price.return_value = bun_price
        burger.set_buns(mock_bun_local)
        for ingredient_type, name, price in ingredients_data:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_type.return_value = ingredient_type
            mock_ingredient.get_name.return_value = name
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        assert receipt.split('\n') == expected_lines
        assert mock_bun_local.get_name.call_count == 2
