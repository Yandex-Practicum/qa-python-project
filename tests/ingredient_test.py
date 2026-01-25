class TestIngredient:

    # проверяем тип ингредиента при создании объекта
    def test_ingredient_type_true(self, ingredient):
        assert ingredient.type == 'sauce'

    # проверяем название ингредиента при создании объекта
    def test_ingredient_name_true(self, ingredient):
        assert ingredient.name == 'spicy'

    # проверяем цену ингредиента при создании объекта
    def test_ingredient_price_true(self, ingredient):
        assert ingredient.price == 20

    # проверяем метод запроса типа ингредиента
    def test_get_type_success(self, ingredient):
        assert ingredient.get_type() == 'sauce'

    # проверяем метод запроса названия ингредиента
    def test_get_name_success(self, ingredient):
        assert ingredient.get_name() == 'spicy'

    # проверяем метод запроса цены ингредиента
    def test_get_price_success(self, ingredient):
        assert ingredient.get_price() == 20
