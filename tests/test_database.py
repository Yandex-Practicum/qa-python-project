import allure
from ya_praktikum.database import Database

class TestDatabase:
    @allure.title('Проверка получения доступных булочек')
    @allure.description('Тест проверяет, что из базы данных можно получить названия булочек')
    def test_available_buns(self):
        database = Database()
        buns = database.available_buns()
        assert buns[0].name == 'black bun', f'Ожидается название: black bun, получено название {buns[0].name}'
        assert buns[1].name == 'white bun', f'Ожидается название: white bun, получено название {buns[1].name}'
        assert buns[2].name == 'red bun', f'Ожидается название: red bun, получено название {buns[2].name}'
        print('\nТест пройден!')
        print(f'В базе булочки с названием {buns[0].name}, {buns[1].name}, {buns[2].name}')

    @allure.title('Проверка получения доступных ингредиентов')
    @allure.description('Тест проверяет, что из базы данных можно получить названия ингредиентов')
    def test_available_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[0].name == 'hot sauce', f'Ожидается название: hot sauce, получено название {ingredients[0].name}'
        assert ingredients[1].name == 'sour cream', f'Ожидается название: sour cream, получено название {ingredients[1].name}'
        assert ingredients[2].name == 'chili sauce', f'Ожидается название: chili sauce, получено название {ingredients[2].name}'
        assert ingredients[3].name == 'cutlet', f'Ожидается название: cutlet, получено название {ingredients[3].name}'
        assert ingredients[4].name == 'dinosaur', f'Ожидается название: dinosaur, получено название {ingredients[4].name}'
        assert ingredients[5].name == 'sausage', f'Ожидается название: sausage, получено название {ingredients[5].name}'
        print('\nТест пройден!')
        print(f'В базе ингредиенты с названием {ingredients[0].name}, {ingredients[1].name}, {ingredients[2].name}, '
              f'{ingredients[3].name}, {ingredients[4].name}, {ingredients[5].name}')