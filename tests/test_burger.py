from unittest.mock import Mock, patch

from praktikum.burger import Burger


class TestBurger:

    def test_burger_set_burger(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @patch('praktikum.ingredient.Ingredient')
    def test_burger_add_ingredient(self, mock_ingredient):
        burger = Burger()
        mock_ingredient.get_name.return_value = 'cutlet'
        mock_ingredient.type = 'INGREDIENT_TYPE_FILLING'
        mock_ingredient.price = 100
        burger.add_ingredient(mock_ingredient)
        current_ingredients = [mock_ingredient]
        assert burger.ingredients == current_ingredients

    def test_burger_remove_ingredient(self):
        burger = Burger()
        mock_first_ingredient = Mock()
        mock_first_ingredient.name = 'cutlet'
        mock_second_ingredient = Mock()
        mock_second_ingredient.name = 'dinosaur'
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)
        expected_ingredients = [mock_second_ingredient]
        burger.remove_ingredient(0)
        assert burger.ingredients == expected_ingredients

    def test_burger_with_bun_remove_ingredient(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.name = 'black bun'
        mock_first_ingredient = Mock()
        mock_first_ingredient.name = 'cutlet'
        mock_second_ingredient = Mock()
        mock_second_ingredient.name = 'dinosaur'
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)
        burger.remove_ingredient(1)
        expected_ingredients = [mock_first_ingredient]
        assert burger.ingredients == expected_ingredients

    @patch('praktikum.ingredient.Ingredient')
    @patch('praktikum.bun.Bun')
    def test_burger_get_price_one_ingredient(self, mock_ingredient, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        mock_bun.get_price.return_value = 100
        mock_ingredient.get_price.return_value = 300
        assert burger.get_price() == 500

    def test_burger_get_price_two_ingredients(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        mock_first_ingredient = Mock()
        mock_first_ingredient.get_price.return_value = 100
        mock_second_ingredient = Mock()
        mock_second_ingredient.get_price.return_value = 300
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)
        assert burger.get_price() == 600

    def test_burger_move_ingredient(self):
        burger = Burger()
        mock_first_ingredient = Mock()
        mock_second_ingredient = Mock()
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)
        index_first_ingredient = burger.ingredients[0]
        index_second_ingredient = burger.ingredients[1]
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == index_second_ingredient and burger.ingredients[1] == index_first_ingredient, (
            f'Wrong Indexes.\n'
            f'New index of the second ingredient {burger.ingredients[0]}\n'
            f'New index of the first ingredient {burger.ingredients[1]}'
        )

    def test_burger_get_receipt_burger_description_check(self):
        burger = Burger()
        mock_bun = Mock()
        mock_first_ingredient = Mock()
        mock_second_ingredient = Mock()

        mock_bun.get_name.return_value = 'white bun'
        mock_first_ingredient.get_name.return_value = 'hot sauce'
        mock_second_ingredient.get_name.return_value = 'sausage'

        mock_first_ingredient.get_type.return_value = 'SAUCE'
        mock_second_ingredient.get_type.return_value = 'FILLING'

        mock_bun.get_price.return_value = 100
        mock_first_ingredient.get_price.return_value = 200
        mock_second_ingredient.get_price.return_value = 300

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)

        assert (('(==== white bun ====)' and
                 '= sauce hot sauce =' and
                 '= filling sausage =' and
                 '(==== white bun ====)' and
                 'Price: 700') in burger.get_receipt())

    def test_burger_get_receipt_burger_total_price_check(self):
        burger = Burger()
        mock_bun = Mock()
        mock_first_ingredient = Mock()
        mock_second_ingredient = Mock()

        mock_bun.get_price.return_value = 100
        mock_first_ingredient.get_price.return_value = 200
        mock_second_ingredient.get_price.return_value = 200

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)

        assert 'Price: 600' in burger.get_receipt()


