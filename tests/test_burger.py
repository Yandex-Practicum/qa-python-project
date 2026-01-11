import allure
from unittest.mock import Mock
from ya_praktikum.burger import Burger
from ya_praktikum.ingredient import Ingredient

class TestBurger:
    @allure.title('Проверка инициализации бургера')
    @allure.description('Тест проверяет, что бургер инициализируется с данными по булочке и ингредиентам')
    def test_init_burger(self):
        burger = Burger()
        assert burger.bun is None, f'Ожидается название: None, получено: {burger.bun}'
        assert burger.ingredients == [], f'Ожидаются ингредиенты: [], получено: {burger.ingredients}'
        print('\nТест пройден!')
        print(f'Бургер инициализировался с булочкой {burger.bun} и ингредиентами {burger.ingredients}')

    @allure.title('Проверка добавления булочки в бургер')
    @allure.description('Тест проверяет, что в бургер можно добавить булочку')
    def test_set_buns(self):
        bun_data = {'name': 'Булочка', 'price': '100'}
        mock_bun = Mock()
        mock_bun.return_value = bun_data
        mock_bun.name = bun_data['name']
        mock_bun.price = bun_data['price']
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun.name == mock_bun.name, f'Ожидается булочка: {mock_bun.name}, получено: {burger.bun.name}'
        assert burger.bun.price == mock_bun.price, f'Ожидается булочка: {mock_bun.price}, получено: {burger.bun.price}'
        print('\nТест пройден!')
        print(f'В бургер добавилась булочка с названием {mock_bun.name} и ценой {burger.bun.price}')

    @allure.title('Проверка добавления ингредиента в бургер')
    @allure.description('Тест проверяет, что в бургер можно добавить ингредиент')
    def test_add_ingredient(self):
        bun_data = {'name': 'Булочка', 'price': '100'}
        ingredient_data = {'type': 'Соус', 'name': 'Сырный', 'price': '100'}
        mock_bun = Mock()
        mock_bun.return_value = bun_data
        burger = Burger()
        burger.set_buns(mock_bun)
        mock_ingredient = Mock()
        mock_ingredient.return_value = ingredient_data
        mock_ingredient.type = ingredient_data['type']
        mock_ingredient.name = ingredient_data['name']
        mock_ingredient.price = ingredient_data['price']
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients, f'Ожидается ингредиент: {mock_ingredient.type}, получено: {burger.ingredients}'
        print('\nТест пройден!')
        print(f'В бургер добавился ингредиент {burger.ingredients[0].type.lower()} {burger.ingredients[0].name} с ценой {burger.ingredients[0].price}')

    @allure.title('Проверка удаления ингредиента из бургера')
    @allure.description('Тест проверяет, что из бургера можно удалить ингредиент')
    def test_remove_ingredient(self, create_bun, create_ing):
        bun = create_bun
        ingredient = create_ing
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert ingredient not in burger.ingredients, f'Ингредиент {ingredient} был удален из {burger.ingredients}'
        print('\nТест пройден!')
        print(f'В бургере следующие ингредиенты: {burger.ingredients}')

    @allure.title('Проверка перемещения ингредиента в бургере')
    @allure.description('Тест проверяет, что в бургере можно перемещать ингредиенты')
    def test_move_ingredient(self, create_bun):
        bun = create_bun
        ingredient_1 = Ingredient('Соус', 'Сырный', 200)
        ingredient_2 = Ingredient('Начинка', 'Джем', 100)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == ingredient_1, f'Ингредиент {ingredient_1} перемещен на позицию 1'
        print('\nТест пройден!')
        print(f'В бургере следующие ингредиенты: {burger.ingredients[0].__dict__}, {burger.ingredients[1].__dict__}')

    @allure.title('Проверка получения цены бургера')
    @allure.description('Тест проверяет, что можно получить цену бургера')
    def test_get_price(self, create_bun, create_ing):
        bun = create_bun
        ingredient = create_ing
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == 350, f'Ожидается цена: 400, получена цена: {burger.get_price()}'
        print('\nТест пройден!')
        print(f'Цена бургера: {burger.get_price()}')

    @allure.title('Проверка получения чека на бургер')
    @allure.description('Тест проверяет, что можно получить чек с информацией и ценой бургера')
    def test_get_receipt(self, create_bun, create_ing):
        bun = create_bun
        ingredient = create_ing
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_receipt = (
            f'(==== {burger.bun.get_name()} ====)\n'
            f'= {ingredient.get_type().lower()} {ingredient.get_name()} =\n'
            f'(==== {burger.bun.get_name()} ====)\n\n'
            f'Price: {burger.get_price()}'
        )
        assert burger.get_receipt() == expected_receipt, f'Ожидается чек: {expected_receipt}, получен: {burger.get_receipt()}'
        print('\nТест пройден!')
        print(burger.get_receipt())