from praktikum.burger import Burger

class TestBurger:


    def test_init_true(self,burger):
        assert burger.bun == None and burger.ingredients == []

    def test_set_buns(self,burger,mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self,burger,mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self,burger,mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self,burger,mock_ingredient,mock_ingredient_1):
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient_1)
        burger.move_ingredient(1,0)
        assert burger.ingredients[0] == mock_ingredient_1

    def test_get_price(self,burger,mock_bun,mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 2810

    def test_get_receipt(self,burger,mock_bun,mock_ingredient,mock_ingredient_1):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient_1)
        burger.get_price()
        receipt = burger.get_receipt()
        assert 'Краторная булка N-200i' in receipt and '2900' in receipt


        

    
