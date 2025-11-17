from praktikum.burger import Burger

class TestBurger:
    def test_create_burger(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []
        
    def test_set_bun(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        assert mock_filling in burger.ingredients

    def test_remove_ingredient(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.remove_ingredient(0)
        assert mock_sauce not in burger.ingredients

    def test_move_ingredients(self, mock_filling, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sauce)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_sauce and burger.ingredients[1] == mock_filling

    def test_get_price(self, mock_bun, mock_filling, mock_sauce):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sauce)
        expected_price = (mock_bun.get_price() * 2 + mock_filling.get_price() + mock_sauce.get_price())
        assert burger.get_price() == expected_price

    def test_get_receipt(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        expected_receipt = ("(==== yellow bun ====)\n"
                            "= sauce teriyaki =\n"                
                            "= filling snake =\n"                                      
                            "(==== yellow bun ====)\n"
                            "\n"
                            f"Price: {burger.get_price()}")
        assert burger.get_receipt() == expected_receipt