import allure

from praktikum import Database


class TestDatabase:
    @allure.title('Проверка, что в базе данных есть булочки')
    def test_available_buns(self):
        database = Database()
        buns = database.available_buns()
        assert buns[0].name == "black bun" and buns[0].price == 100 \
               and buns[1].name == "white bun" and buns[1].price == 200 \
               and buns[2].name == "red bun" and buns[2].price == 300

    @allure.title('Проверка, что в базе данных есть соусы')
    def test_available_ingredients_sauce(self):
        database = Database()
        ingredients = database.available_ingredients()
        sauces = []
        for ingredient in ingredients:
            if ingredient.type == 'SAUCE':
                sauces.append(ingredient)
        assert sauces[0].name == 'hot sauce' and sauces[0].price == 100 \
               and sauces[1].name == 'sour cream' and sauces[1].price == 200 \
               and sauces[2].name == 'chili sauce' and sauces[2].price == 300

    @allure.title('Проверка, что в базе данных есть начинки')
    def test_available_ingredients_filling(self):
        database = Database()
        ingredients = database.available_ingredients()
        fillings = []
        for ingredient in ingredients:
            if ingredient.type == 'FILLING':
                fillings.append(ingredient)
        assert fillings[0].name == "cutlet" and fillings[0].price == 100 \
               and fillings[1].name == "dinosaur" and fillings[1].price == 200 \
               and fillings[2].name == "sausage" and fillings[2].price == 300


