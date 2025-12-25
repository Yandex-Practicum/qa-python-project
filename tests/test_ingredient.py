from praktikum.ingredient import Ingredient


class TestIngredient:

    #  Тест поля "type" метод-конструктор класса Ингридиент
    def test_type_of_ingredient_is_equals_the_assigned(self):

        ingredient = Ingredient('SAUCE', 'sousets', 0.5)

        assert ingredient.type == 'SAUCE'

    #  Тест поля "name" метод-конструктор класса Ингридиент
    def test_name_of_ingredient_is_equals_the_assigned(self):

        ingredient = Ingredient('SAUCE', 'sousets', 0.5)

        assert ingredient.name == 'sousets'

    #  Тест поля "price" метод-конструктор класса Ингридиент
    def test_price_of_ingredient_is_equals_the_assigned(self):

        ingredient = Ingredient('SAUCE', 'sousets', 0.5)

        assert ingredient.price == 0.5

    #  Тест, проверяющий метод get_name класса Ingredient
    def test_get_name_of_ingredient_return_assigned_name(self):

        ingredient = Ingredient('SAUCE', 'sousets', 0.5)

        assert ingredient.get_name() == 'sousets'

    #  Тест, проверяющий метод get_type класса Ingredient
    def test_get_type_of_ingredient_return_assigned_name(self):
        ingredient = Ingredient('SAUCE', 'sousets', 0.5)

        assert ingredient.get_type() == 'SAUCE'

    def test_get_price_of_ingredient_return_assigned_price(self):

        ingredient = Ingredient('SAUCE', 'sousets', 0.5)

        assert ingredient.get_price() == 0.5
        