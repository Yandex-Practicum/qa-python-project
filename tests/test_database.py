from praktikum.database import Database


class TestDatabase:

    #1 тест на проверку что метод available_buns возвращает правильный список булочек
    def test_database_available_buns_returns_correct_list(self):
        expected_names = ["black bun", "white bun", "red bun"]
        expected_prices = [100, 200, 300]
        db = Database()
        names = []
        prices = []
        for bun in db.available_buns():
            names.append(bun.get_name())
            prices.append(bun.get_price())
        assert (names == expected_names) and (prices == expected_prices)

    #2 тест на проверку что метод available_ingredient возвращает правильный список ингредиентов
    def test_database_available_ingredients_returns_correct_list(self):
        expected_types = ["SAUCE", "SAUCE", "SAUCE", "FILLING", "FILLING", "FILLING"]
        expected_names = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
        expected_prices = [100, 200, 300, 100, 200, 300]
        db = Database()
        types = []
        names = []
        prices = []
        for ingredient in db.available_ingredients():
            types.append(ingredient.get_type())
            names.append(ingredient.get_name())
            prices.append(ingredient.get_price())
        assert (types == expected_types) and (names == expected_names) and (prices == expected_prices)
