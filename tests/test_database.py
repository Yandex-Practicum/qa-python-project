from conftest import bun_mock, ingredient_mock, data_base_mock


class TestDatabase:

    def test_available_buns_mock_buns_success(self, data_base_mock, bun_mock):
        data_base_mock.buns = [bun_mock]

        assert data_base_mock.available_buns() == data_base_mock.buns and len(data_base_mock.buns) == 1

    def test_available_ingredients_mock_ingredients_success(self, data_base_mock, ingredient_mock):
        data_base_mock.ingredients = [ingredient_mock]

        assert data_base_mock.available_ingredients() == data_base_mock.ingredients and len(data_base_mock.ingredients) == 1