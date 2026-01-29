import allure
from praktikum.burger import Burger
from unittest.mock import Mock, patch
from helpers.create_objects import create_burger


@allure.story('Проверка класса Burger')
class TestBurger:
    @allure.title('Проверка корректного создания объекта Burger')
    @allure.description('Создаётся объект с параметрами self.bun = None и self.ingredients = []')
    def test_creation_object_burger(self):
        new_burger = Burger()

        assert new_burger.bun == None and new_burger.ingredients == []

    @allure.title('Проверка выбора этих мягких французских булок для бургера')
    @allure.description('Атрибуту self.bun методом set_buns присваивается переданный объект')
    @patch('praktikum.bun.Bun')
    def test_set_buns(self, mock_bun):
        new_burger = create_burger()
        new_burger.set_buns(mock_bun)

        assert new_burger.bun == mock_bun

    @allure.title('Проверка добавления ингредиента из бургера')
    @allure.description('Объект ингредиента добавлется в список self.ingredients')
    @patch('praktikum.ingredient.Ingredient')
    def test_add_ingredient(self, mock_ingredient):
        new_burger = create_burger()
        new_burger.add_ingredient(mock_ingredient)

        assert new_burger.ingredients == [mock_ingredient]

    @allure.title('Проверка удаления ингредиента из бургера')
    @allure.description('Объект ингредиента удаляется из списка self.ingredients')
    @patch('praktikum.ingredient.Ingredient')
    def test_remove_ingredient(self, mock_ingredient):
        new_burger = create_burger()
        new_burger.ingredients = [mock_ingredient]
        new_burger.remove_ingredient(0)

        assert new_burger.ingredients == []

    @allure.title('Проверка изменения позиций элементов в списке ингредиентов бургера')
    @allure.description('Элементы списка self.ingredients меняются местами')
    def test_move_ingredient(self):
        mock_ingredient_0 = Mock()
        mock_ingredient_1 = Mock()

        new_burger = create_burger()
        new_burger.ingredients = [mock_ingredient_0, mock_ingredient_1]
        new_burger.move_ingredient(0, 1)

        assert new_burger.ingredients == [mock_ingredient_1, mock_ingredient_0]

    @allure.title('Проверка получения стоимости бургера')
    @allure.description('Получение корректной суммы стоимостей всех ингредиентов')
    def test_get_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 200

        mock_ingredient_0 = Mock()
        mock_ingredient_0.get_price.return_value = 200
        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_price.return_value = 300

        new_burger = create_burger()
        new_burger.bun = mock_bun
        new_burger.ingredients = [mock_ingredient_0, mock_ingredient_1]

        assert new_burger.get_price() == 900

    @allure.title('Проверка получения полного рецепта бургера')
    @allure.description('Получение полного состава бургера в корректном виде')
    def test_get_receipt(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Common bun'
        mock_bun.get_price.return_value = 2

        mock_ingredient_0 = Mock()
        mock_ingredient_0.get_price.return_value = 2
        mock_ingredient_0.get_type.return_value = 'ingredient_0_type'
        mock_ingredient_0.get_name.return_value = 'ingredient_0_name'

        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_price.return_value = 2
        mock_ingredient_1.get_type.return_value = 'ingredient_1_type'
        mock_ingredient_1.get_name.return_value = 'ingredient_1_name'

        new_burger = create_burger()
        new_burger.bun = mock_bun
        new_burger.ingredients = [mock_ingredient_0, mock_ingredient_1]

        assert (new_burger.get_receipt() == '(==== Common bun ====)\n' 
                                            '= ingredient_0_type ingredient_0_name =\n' 
                                            '= ingredient_1_type ingredient_1_name =\n' 
                                            '(==== Common bun ====)\n' 
                                            '\n' 
                                            'Price: 8')
