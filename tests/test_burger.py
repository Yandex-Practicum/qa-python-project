from data import *



class TestBurger:
    #Добавление булочки.
    def test_set_bun_burger(self, mock_bun, burger):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    #Добавление ингредиента.
    def test_add_ingredient(self, mock_topping, burger):
        burger.add_ingredient(mock_topping)
        assert mock_topping in burger.ingredients

    #Удаление ингредиента.
    def test_remove_ingredient(self, mock_topping, burger):
        burger.add_ingredient(mock_topping)
        assert len(burger.ingredients) == 1
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    #Перемещение ингредиентов.
    def test_move_ingredient(self, burger, mock_topping):
        burger.add_ingredient(mock_topping)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 1

    #Получение стоимости бургера.
    def test_get_price_burger(self, mock_bun, burger, mock_topping):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_topping)
        assert burger.get_price() == 180

    #Получение чека.
    def test_get_receipt_burger(self, mock_bun, mock_topping, burger, mock_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_topping)
        burger.add_ingredient(mock_sauce)
        expected_receipt = (f'(==== {mock_bun.get_name()} ====)\n'
                            f'= {str(mock_topping.get_type()).lower()} {mock_topping.get_name()} =\n'
                            f'= {str(mock_sauce.get_type()).lower()} {mock_sauce.get_name()} =\n'
                            f'(==== {mock_bun.get_name()} ====)\n\n'
                            f'Price: {burger.get_price()}')
        assert burger.get_receipt() == expected_receipt