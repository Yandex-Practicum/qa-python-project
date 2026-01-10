import allure
import pytest
from praktikum.database import Database

class TestDatabase:

    @allure.title('Проверка названия и цены')
    @pytest.mark.parametrize('number, name, price', [
    (0, 'black bun', 100),
    (1, 'white bun', 200),
    (2, 'red bun', 300)
])
    def test_name_price_buns(self, number, name, price):
        database = Database()
        buns = database.available_buns()
        assert buns[number].get_name() == name and  buns[number].get_price() == price
