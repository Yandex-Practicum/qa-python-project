import data
import allure


class TestBurger:
    
    @allure.title("Проверяем, что объект создаётся с корректными данными")
    def test_init_valid_data(self, burger):
        
        assert burger.bun == None and burger.ingredients == []
        
    @allure.title("Проверяем, что set_buns присваивает значение")
    def test_set_buns_correct(self, mock_bun, burger):
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun
    
    @allure.title("Проверяем, что ингридиенты успешно добавляются в список")
    def test_add_ingredient_append_to_list(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients[0] == mock_ingredient

    @allure.title("Проверяем, что ингридиенты успешно удаляются")
    def test_remove_ingredient_from_list(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []
    
    @allure.title("Проверяем, что ингредиент меняет индекс в списке")
    def test_move_ingredient(self, mock_burger_with_two_ingredients):
        burger = mock_burger_with_two_ingredients
        burger.move_ingredient(1, 0)
        
        assert burger.ingredients[0].get_name() == data.INGREDIENT_SAUCE_NAME

    @allure.title("Проверяем цену бургера с учетом ингредиентов")
    def test_get_price_ingredient(self, mock_bun, mock_burger_with_two_ingredients):
        burger = mock_burger_with_two_ingredients
        burger.set_buns(mock_bun)

        assert burger.get_price() == 190

    @allure.title("Проверяем рецепт бургера")
    def test_get_receipt(self, mock_bun, burger, mock_burger_with_two_ingredients):
        burger = mock_burger_with_two_ingredients
        burger.set_buns(mock_bun)

        assert burger.get_receipt() == data.RECEIPT