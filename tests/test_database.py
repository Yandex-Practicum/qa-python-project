import allure
from data import Data
import pytest

class TestDataBase:
    @allure.title('Проверка имени и стоимости  булочки методом available_buns через параметризацию')
    @pytest.mark.parametrize('buns_number, buns_name, buns_price', Data.buns_data_for_test_database)
    def test_avalable_buns_database(self, data_base_fixture, buns_number, buns_name, buns_price):
        test_buns = data_base_fixture.available_buns()
        assert test_buns[buns_number].get_name() == buns_name
        assert test_buns[buns_number].get_price() == buns_price

    @allure.title('Проверка типа, имени, цены добавок к бургерам методом available_ingredients через праметризацию')
    @pytest.mark.parametrize('ingridients_number, ingridients_type, ingridients_name, ingridieints_price', Data.ingredients_data_for_test_database)
    def test_available_ingredients_database(self, data_base_fixture, ingridients_number, ingridients_type, ingridients_name, ingridieints_price):
        test_buns = data_base_fixture.available_ingredients()
        assert test_buns[ingridients_number].get_name() == ingridients_name
        assert test_buns[ingridients_number].get_price() == ingridieints_price
        assert test_buns[ingridients_number].get_type() == ingridients_type
