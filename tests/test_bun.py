import allure


class TestBun:
    
    @allure.title("Проверяем, что объект создаётся с корректными данными")
    def test_init_valid_data(self, bun):
        
        assert bun.name == "Булочка с маком" and bun.price == 45.0

    @allure.title("Проверяем, что get_name возвращает правильное имя")
    def test_get_name_return_correct_name(self, bun):

        assert bun.get_name() == "Булочка с маком"
    
    @allure.title("Проверяем, что get_name возвращает string")
    def test_get_name_return_string(self, bun):

        assert isinstance(bun.get_name(), str)

    @allure.title("Проверяем, что get_price возвращает правильную цену")
    def test_get_price_return_correct_price(self, bun):

        assert bun.get_price() == 45.0
    
    @allure.title("Проверяем, что get_price возвращает float")
    def test_get_price_return_float(self, bun):
        
        assert isinstance(bun.get_price(), float)