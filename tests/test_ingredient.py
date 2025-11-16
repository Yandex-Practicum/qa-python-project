class TestIngredient:


    def test_ingredient_type_true(self, ingredient):
        assert ingredient.type in ['Соус', 'Начинки']


    def test_ingredient_name_true(self, ingredient):
        assert ingredient.name in ['Соус Spicy-X', 'Мясо бессмертных моллюсков']


    def test_ingredient_price_true(self, ingredient):
        assert ingredient.price in [90, 1337]


    def test_ingredient_get_price_true(self, ingredient):
        assert ingredient.get_price() in [90, 1337]


    def test_ingredient_get_name_true(self, ingredient):
        assert ingredient.get_name() in ['Соус Spicy-X', 'Мясо бессмертных моллюсков']


    def test_ingredient_get_type_true(self, ingredient):
        assert ingredient.get_type() in ['Соус', 'Начинки']