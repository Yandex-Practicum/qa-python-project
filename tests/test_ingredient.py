import pytest
import allure

from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @allure.title('Ingredient сохраняет тип: {param_id}')
    @pytest.mark.parametrize('ingredient_type, name, price', [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_FILLING, "sausage", 300),
    ], ids=[
        "SAUCE - hot sauce",
        "SAUCE - sour cream",
        "SAUCE - chili sauce",
        "FILLING - cutlet",
        "FILLING - dinosaur",
        "FILLING - sausage",
    ])
    def test_ingredient_init_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        allure.attach(
            name="Входные данные",
            body=f"Type: {ingredient_type}\nName: {name}\nPrice: {price}",
            attachment_type=allure.attachment_type.TEXT
        )
        assert ingredient.type == ingredient_type, f"Тип должен быть {ingredient_type}"

    @allure.title('Ingredient сохраняет название: {param_id}')
    @pytest.mark.parametrize('ingredient_type, name, price', [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_FILLING, "sausage", 300),
    ], ids=[
        "SAUCE - hot sauce",
        "SAUCE - sour cream",
        "SAUCE - chili sauce",
        "FILLING - cutlet",
        "FILLING - dinosaur",
        "FILLING - sausage",
    ])
    def test_ingredient_init_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        allure.attach(
            name="Входные данные",
            body=f"Type: {ingredient_type}\nName: {name}\nPrice: {price}",
            attachment_type=allure.attachment_type.TEXT
        )
        assert ingredient.name == name, f"Название должно быть {name}"

    @allure.title('Ingredient сохраняет цену: {param_id}')
    @pytest.mark.parametrize('ingredient_type, name, price', [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_FILLING, "sausage", 300),
    ], ids=[
        "SAUCE - hot sauce — 100",
        "SAUCE - sour cream — 200",
        "SAUCE - chili sauce — 300",
        "FILLING - cutlet — 100",
        "FILLING - dinosaur — 200",
        "FILLING - sausage — 300",
    ])
    def test_ingredient_init_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        allure.attach(
            name="Входные данные",
            body=f"Type: {ingredient_type}\nName: {name}\nPrice: {price}",
            attachment_type=allure.attachment_type.TEXT
        )
        assert ingredient.price == price, f"Цена должна быть {price}"

    @allure.title('get_price возвращает цену: {param_id}')
    @pytest.mark.parametrize('ingredient_type, name, price', [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    ], ids=[
        "hot sauce — 100",
        "dinosaur — 200",
    ])
    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        allure.attach(
            name="Входные данные",
            body=f"Type: {ingredient_type}\nName: {name}\nPrice: {price}",
            attachment_type=allure.attachment_type.TEXT
        )
        assert ingredient.get_price() == price, f"get_price должен вернуть {price}"

    @allure.title('get_name возвращает название: {param_id}')
    @pytest.mark.parametrize('ingredient_type, name, price', [
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
    ], ids=[
        "chili sauce",
        "cutlet",
    ])
    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        allure.attach(
            name="Входные данные",
            body=f"Type: {ingredient_type}\nName: {name}\nPrice: {price}",
            attachment_type=allure.attachment_type.TEXT
        )
        assert ingredient.get_name() == name, f"get_name должен вернуть {name}"

    @allure.title('get_type возвращает тип: {param_id}')
    @pytest.mark.parametrize('ingredient_type, name, price', [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
    ], ids=[
        "SAUCE (соус)",
        "FILLING (начинка)",
    ])
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        allure.attach(
            name="Входные данные",
            body=f"Type: {ingredient_type}\nName: {name}\nPrice: {price}",
            attachment_type=allure.attachment_type.TEXT
        )
        assert ingredient.get_type() == ingredient_type, f"get_type должен вернуть {ingredient_type}"

