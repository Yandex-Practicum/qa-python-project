import allure


class TestIngredient:
    
    @allure.title("Проверяем, что объект создаётся с корректными данными")
    def test_init_valid_data_ingredient(self, ingredient):
        
        assert (ingredient.type, ingredient.name, ingredient.price) == ("SAUCE", "сырный", 30.0)

    @allure.title("Проверяем, что get_price возвращает правильную цену")
    def test_get_price_return_correct_price(self, ingredient):

        assert ingredient.get_price() == 30
    
    @allure.title("Проверяем, что get_name возвращает правильное наименование")
    def test_get_name_return_correct_name(self, ingredient):

        assert ingredient.get_name() == 'сырный'

    @allure.title("Проверяем, что get_type возвращает правильный тип ингридиента")
    def test_get_type_return_correct_type(self, ingredient):
        
        assert ingredient.get_type() == 'SAUCE'
