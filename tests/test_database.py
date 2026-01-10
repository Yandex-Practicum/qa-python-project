import data
from praktikum.database import Database


class TestDatabase:

    # Проверка возможности создать объект класса Database с добавлением и выводом списка доступных булок методом available_buns
    def test_available_buns_list_of_3_and_7_buns(self, mock_bun):
        database_test = Database()
        for name, price in data.buns_list():
            mock_bun.name, mock_bun.price, mock_bun.get_name.return_value, mock_bun.get_price.return_value = name, price, name, price
            database_test.buns.append(mock_bun)
        # проверим, что они добавились в список
        assert type(database_test.available_buns()) == list and len(database_test.available_buns()) == 10, f'database_test.available_buns() == {database_test.available_buns()}'

    # Проверка возможности создать объект класса Database с добавлением и выводом списка доступных ингредиентов методом available_ingredients
    def test_available_ingredients_list_of_6_and_9_ingredients(self, mock_ingredient_1):
        database_test = Database()
        for i_type, name, price in data.ingredients_list():
            (mock_ingredient_1.type, mock_ingredient_1.name, mock_ingredient_1.price, mock_ingredient_1.get_type.return_value,
             mock_ingredient_1.get_name.return_value, mock_ingredient_1.get_price.return_value) = i_type, name, price, i_type, name, price
            database_test.ingredients.append(mock_ingredient_1)
        # проверим, что они добавились в список
        assert type(database_test.available_ingredients()) == list and len(database_test.available_ingredients()) == 15, f'database_test.available_buns() == {database_test.available_buns()}'
