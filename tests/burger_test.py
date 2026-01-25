class TestBurger:

    # проверяем метод выбора булки для бургера
    def test_set_buns_success(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun.name == 'bun_mock'

    # проверяем метод добавления ингредиента
    def test_add_ingredient_success(self, burger, mock_ingredient_sauce):
        burger.add_ingredient(mock_ingredient_sauce)
        assert len(burger.ingredients) == 1 and burger.ingredients[0].name == 'ketchup'

    # проверяем метод удаления ингредиента
    def test_remove_ingredient_success(self, burger, mock_ingredient_filling):
        burger.add_ingredient(mock_ingredient_filling)
        try:
            if len(burger.ingredients) == 1:
                burger.remove_ingredient(0)
        except:
            raise Exception('Проверьте индекс ингредиента, либо состав бургера')

        assert len(burger.ingredients) == 0

    # проверяем метод перемещения ингредиента
    def test_move_ingredient_success(self, burger, mock_ingredient_sauce, mock_ingredient_filling):
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_filling)
        burger.move_ingredient(0, 2)
        assert burger.ingredients[2].name == 'ketchup'

    # проверяем метод запроса цены бургера
    def test_get_price_success(self, burger, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        assert burger.get_price() == 240

    # проверяем метод запроса рецептуры бургера
    def test_get_receipt_success(self, burger, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        assert ((burger.bun.name in burger.get_receipt())
                and (burger.ingredients[0].name in burger.get_receipt())
                and (burger.ingredients[1].name in burger.get_receipt())
                and (str(burger.get_price()) in burger.get_receipt())
                )
