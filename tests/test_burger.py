import allure
from unittest.mock import Mock
from burger import Burger

@allure.feature('Burger')
class TestBurger:

    @allure.story('Проверяем метод set_buns (добавляет булки в бургер)')
    def test_set_buns(self, burger, bun_mock):
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    @allure.title('Проверяем метод add_ingredient (добавляет ингредиенты в бургер)')
    def test_add_ingredient(self, burger, cheese_mock):
        burger.add_ingredient(cheese_mock)
        assert cheese_mock in burger.ingredients

    @allure.title('Проверяем метод remove_ingredient (удаляет ингредиенты)')
    def test_remove_ingredient(self, burger, cheese_mock):
        burger.add_ingredient(cheese_mock)
        burger.remove_ingredient(0)
        assert cheese_mock not in burger.ingredients

    @allure.story('Проверяем метод move_ingredient (перемещает ингредиенты)')
    def test_move_ingredient(self, burger, cheese_mock, tomato_mock):
        ingr1 = cheese_mock
        ingr2 = tomato_mock
        ingr3 = Mock(get_name=lambda: 'Other Ingredient')

        burger.add_ingredient(ingr1)
        burger.add_ingredient(ingr2)
        burger.add_ingredient(ingr3)

        # Меняем местами ингредиенты
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [ingr2, ingr3, ingr1]

    @allure.story('Проверяем метод get_price (расчет цены бургера)')
    def test_get_price(self, burger, bun_mock, cheese_mock, tomato_mock):
        burger.set_buns(bun_mock)
        burger.add_ingredient(cheese_mock)
        burger.add_ingredient(tomato_mock)

        expected_price = 100 * 2 + 50 + 75
        assert burger.get_price() == expected_price

    @allure.story('Проверяем метод get_receipt (получение рецепта бургера и его стоимости)')
    def test_get_receipt(self, burger, bun_mock, cheese_mock, tomato_mock):
        burger.set_buns(bun_mock)
        burger.add_ingredient(cheese_mock)
        burger.add_ingredient(tomato_mock)

        expected_receipt = (
            "(==== Bun ====)\n"
            "= sauce Cheese =\n"
            "= filling Tomato =\n"
            "(==== Bun ====)\n\n"
            "Price: 325"
        )
        assert burger.get_receipt() == expected_receipt
