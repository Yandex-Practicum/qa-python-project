import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "Соус фирменный Space Sauce", 80),
        (INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 15),
        (INGREDIENT_TYPE_FILLING, "Филе Люминесцентного тетраодонтимформа", 988),
        (INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков Protostomia", 1337),
        (INGREDIENT_TYPE_FILLING, "Говяжий метеорит (отбивная)", 3000)
    ])
    def test_ingredient_creation(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    def test_ingredient_type_is_string(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Тестовый соус", 50)
        assert isinstance(ingredient.get_type(), str)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_ingredient_get_name_returns_string(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Тестовая начинка", 100)
        name = ingredient.get_name()
        assert isinstance(name, str)
        assert name == "Тестовая начинка"

    def test_ingredient_get_price_returns_number(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Тестовый соус", 50)
        price = ingredient.get_price()
        assert isinstance(price, (int, float))
        assert price == 50

    def test_ingredient_price_can_be_float(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Тестовый соус", 49.99)
        assert ingredient.get_price() == 49.99
        assert isinstance(ingredient.get_price(), float)

    def test_ingredient_with_sauce_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Кетчуп", 30)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredient.get_name() == "Кетчуп"
        assert ingredient.get_price() == 30

    def test_ingredient_with_filling_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Сыр", 50)
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING
        assert ingredient.get_name() == "Сыр"
        assert ingredient.get_price() == 50

    @pytest.mark.parametrize("name", [
        "Хрустящие минеральные кольца",
        "Плоды Фалленианского дерева",
        "Кристаллы марсианских альфа-сахаридов",
        "Мини-салат Экзо-Плантаго",
        "Сыр с астероидной плесенью",
        "Филе Люминесцентного тетраодонтимформа",
        "Мясо бессмертных моллюсков Protostomia",
        "Говяжий метеорит (отбивная)",
        "Биокотлета из марсианской Магнолии"
    ])
    def test_all_fillings_have_correct_type(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, name, 100)
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING

    @pytest.mark.parametrize("name", [
        "Соус фирменный Space Sauce",
        "Соус традиционный галактический"
    ])
    def test_all_sauces_have_correct_type(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 100)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE