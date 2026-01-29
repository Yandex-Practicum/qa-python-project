from ingredient import Ingredient


class TestIngredient:

    def test_init(self):
        # Проверка инициализации ингредиента с корректными параметрами
        ingredient = Ingredient("FILLING", "Kolbasa", 10.5)
        assert ingredient.type == "FILLING"
        assert ingredient.name == "Kolbasa"
        assert ingredient.price == 10.5

    def test_get_price(self):
        # Проверка метода get_price
        ingredient = Ingredient("SAUCE", "Gorchica", 2.0)
        price = ingredient.get_price()
        assert price == 2.0

    def test_get_name(self):
        # Проверка метода get_name
        ingredient = Ingredient("FILLING", "Pomidor", 5.0)
        name = ingredient.get_name()
        assert name == "Pomidor"

    def test_get_type_sauce(self):
        # Проверка метода get_type
        ingredient = Ingredient("SAUCE", "Mazik", 3.5)
        type_ = ingredient.get_type()
        assert type_ == "SAUCE"

    def test_get_type_filling(self):
        # Проверка метода get_type
        ingredient = Ingredient("FILLING", "Mazik", 3.5)
        type_ = ingredient.get_type()
        assert type_ == "FILLING"

    def test_check_ingredient_type(self):
        ingredient = Ingredient("FILLING", "Mazik", 3.5)
        type_ = ingredient.get_type()
        assert type(type_) is str

    def test_check_name_type(self):
        ingredient = Ingredient("FILLING", "Pomidor", 5.0)
        name = ingredient.get_name()
        assert type(name) is str

    def test_chech_price_type(self):
        ingredient = Ingredient("SAUCE", "Gorchica", 2.0)
        price = ingredient.get_price()
        assert type(price) is float