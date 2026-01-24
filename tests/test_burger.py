from praktikum.burger import Burger
from unittest.mock import Mock

class TestBurger:
    mock_bun = Mock()
    mock_bun.name = 'Краторная булка N-200i'
    mock_bun.price = 1255
    mock_ingredient_1 = Mock()
    mock_ingredient_1.ingredient_type = 'FILLING'
    mock_ingredient_1.name = 'Мясо бессмертных моллюсков Protostomia'
    mock_ingredient_1.price = 1337
    mock_ingredient_2 = Mock()
    mock_ingredient_2.ingredient_type = 'FILLING'
    mock_ingredient_2.name = 'Говяжий метеорит (отбивная)'
    mock_ingredient_2.price = 3000
    burger = Burger()
    def test_burger_initialization(self):
        assert self.burger.bun == None
        assert self.burger.ingredients == []
    def test_set_buns(self):
        self.burger.set_buns(self.mock_bun)
        assert self.burger.bun == self.mock_bun
    def test_add_ingredient_adds_ingredient_to_list_of_ingridients(self):
        self.burger.add_ingredient(self.mock_ingredient_1)
        assert self.mock_ingredient_1 in self.burger.ingredients
        self.burger.ingredients.clear()

    def test_remove_ingredient_removes_ingredient_from_list_of_ingridients(self,):
        self.burger.ingredients.append(self.mock_ingredient_1)
        assert len(self.burger.ingredients) == 1
        self.burger.remove_ingredient(0)
        assert len(self.burger.ingredients) == 0
    def test_move_ingredient_moves_ingredient_to_new_index(self):
        self.burger.ingredients.append(self.mock_ingredient_1)
        self.burger.ingredients.append(self.mock_ingredient_2)
        self.burger.move_ingredient(0,1)
        assert self.burger.ingredients[1] == self.mock_ingredient_1
        self.burger.ingredients.clear()

    def test_get_price_returns_price_of_burger(self):
        self.burger.bun = self.mock_bun
        self.mock_bun.get_price.return_value = 1255
        self.mock_ingredient_1.get_price.return_value = 1337
        self.mock_ingredient_2.get_price.return_value = 3000
        self.burger.ingredients.append(self.mock_ingredient_1)
        self.burger.ingredients.append(self.mock_ingredient_2)
        expected_price = self.mock_bun.get_price() * 2 + self.mock_ingredient_1.get_price() + self.mock_ingredient_2.get_price()
        actual_price = self.burger.get_price()
        assert  actual_price == expected_price
        self.burger.ingredients.clear()

    def test_get_receipt_gets_receipt_with_correct_price(self):
        self.burger.bun = self.mock_bun
        self.mock_bun.get_name.return_value = 'Краторная булка N-200i'
        self.mock_bun.get_price.return_value = 1255
        self.burger.ingredients.append(self.mock_ingredient_1)
        self.mock_ingredient_1.get_type.return_value = 'FILLING'
        self.mock_ingredient_1.get_name.return_value = 'Мясо бессмертных моллюсков Protostomia'
        self.mock_ingredient_1.get_price.return_value = 1337
        mock_price = Mock()
        mock_price.get_price.return_value = 3847
        expected_receipt = (
            f'(==== {self.mock_bun.get_name.return_value} ====)\n'
            f'= {self.mock_ingredient_1.get_type.return_value.lower()} {self.mock_ingredient_1.get_name.return_value} =\n'
            f'(==== {self.mock_bun.get_name.return_value} ====)\n'
            f'\nPrice: {mock_price.get_price.return_value}'
        )
        assert expected_receipt == self.burger.get_receipt()
        self.burger.ingredients.clear()



