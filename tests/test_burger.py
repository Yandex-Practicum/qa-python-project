from unittest.mock import Mock, patch
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from conftest import burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
import allure

@allure.feature('Burger Operations')
class TestBurger:

    @allure.title('Check default bun value is None')
    def test_init_default_value_bun(self, burger):
        assert burger.bun is None, f"Expected None, but got {burger.bun}"

    @allure.title('Check default ingredients is an empty list')
    def test_init_default_value_ingredients(self, burger):
        assert burger.ingredients == [], f"Expected empty list, but got {burger.ingredients}"

    @allure.title('Check ingredients type is list')
    def test_ingredients_type_is_list(self, burger):
        assert isinstance(burger.ingredients, list), f"Expected list type, but got {type(burger.ingredients)}"

    @allure.title('Set bun using Mock object')
    def test_set_buns_return_correct_bun(self, burger):
        mock_bun = Mock(spec=Bun)
        mock_bun.name = 'Мягкий лаваш'
        mock_bun.price = 234.80
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun, "The bun was not set correctly"

    @allure.title('Verify set bun belongs to Bun class')
    def test_set_buns_belongs_class_bun(self, burger):
        mock_bun = Mock(spec=Bun)
        mock_bun.name = 'Мягкий лаваш'
        mock_bun.price = 234.80
        burger.set_buns(mock_bun)
        assert isinstance(burger.bun, Bun), "The object is not an instance of Bun class"

    @allure.title('Verify bun name cannot be None')
    def test_set_buns_rejects_none(self, burger):
        mock_bun = Mock(spec=Bun)
        mock_bun.name = None
        mock_bun.price = 234.80
        assert burger.bun != mock_bun, "Bun name cannot be None"

    @allure.title('Verify ingredient belongs to Ingredient class')
    def test_ingredient_belongs_class_ingredient(self, burger):
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.type = INGREDIENT_TYPE_SAUCE
        mock_ingredient.name = 'кетчуп'
        mock_ingredient.price = 35.30
        burger.add_ingredient(mock_ingredient)
        assert isinstance(burger.ingredients[0], Ingredient), f"Ingredient does not belong to the Ingredient class"

    @allure.title('Add ingredient successfully using Mock')
    def test_add_ingredient_as_mock_success(self, burger):
        mock_ingredient = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0] == mock_ingredient, "Ingredient was not added to the burger"

    @allure.title('Remove ingredient successfully using Mock')
    def test_remove_ingredient_as_mock_success(self, burger):
        mock_ingredient_1 = Mock(spec=Ingredient)
        mock_ingredient_2 = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.remove_ingredient(0)
        assert burger.ingredients[0] == mock_ingredient_2, f"Ingredient {burger.ingredients[0]} was not removed"

    @allure.title('Move ingredient successfully in the list')
    def test_move_ingredient_succes(self, burger):
        mock_ingredient_1 = Mock(spec=Ingredient)
        mock_ingredient_2 = Mock(spec=Ingredient)
        mock_ingredient_3 = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.add_ingredient(mock_ingredient_3)
        burger.move_ingredient(2, 0)
        assert burger.ingredients == [mock_ingredient_3, mock_ingredient_1, mock_ingredient_2], f"Ingredient {burger.ingredients[2]} was not moved"

    @allure.title('Verify get_price() returns correct total value')
    @patch('praktikum.bun.Bun')
    def test_get_price_correct_result(self, mock_bun, burger):
        mock_bun.return_value.get_price.return_value = 100.20 # замокировали метод get_price класса Bun
        mock_ingredients = [Mock(get_price=Mock(return_value=20.50)),  # мок цены соуса
                            Mock(get_price=Mock(return_value=60.45))]  # мок цены начинки
        burger.set_buns(mock_bun())
        burger.ingredients = mock_ingredients
        assert burger.get_price() == 281.35, f"Expected 281.35, but got {burger.get_price()}"

    @allure.title('Verify get_receipt() formatting')
    @patch('praktikum.burger.Burger.get_price')
    def test_get_receipt(self, mock_get_price, burger):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'ржаная булка'
        burger.bun = mock_bun
        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_name.return_value = 'говяжья котлета'
        mock_ingredient_1.get_type.return_value = 'FILLING'
        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_name.return_value = 'кетчуп'
        mock_ingredient_2.get_type.return_value = 'SAUCE'
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        mock_get_price.return_value = 467
        expected_receipt = (
    "(==== ржаная булка ====)\n"
    "= filling говяжья котлета =\n"
    "= sauce кетчуп =\n"
    "(==== ржаная булка ====)\n"
    "\n"
    "Price: 467")

        assert burger.get_receipt() == expected_receipt
