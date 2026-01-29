import allure
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger


class TestBurger:
    """
    ТЕСТЫ МЕТОДОВ КЛАССА Burger
    """

    @allure.title('set_buns() - добавление булочки')
    @allure.description('Проверяем, что булочка добавлена')
    def test_set_bun(self):
        self.burger = Burger()
        bun = Bun('Сырная', 4.5)
        self.burger.set_buns(bun)
        assert self.burger.bun.get_name() == "Сырная"

    @allure.title('add_ingredient() - добавление одного ингредиента')
    @allure.description('Проверяем, что добавлен один ингредиент - начинка')
    def test_add_one_ingredient(self):
        self.burger = Burger()
        ingredient = Ingredient('котлета', 'куриная', 3.30)
        self.burger.add_ingredient(ingredient)
        assert len(self.burger.ingredients) == 1

    @allure.title('remove_ingredient() - удаление ингредиента')
    @allure.description('Проверяем, что после удаления ингредиента в списоке осталось два ингредиента из трех')
    def test_remove_ingredient_remained_two(self):
        self.burger = Burger()
        self.burger.add_ingredient(Ingredient('котлета', 'куриная', 3.30))
        self.burger.add_ingredient(Ingredient('овощи', 'огурец', 2.20))
        self.burger.add_ingredient(Ingredient('овощи', 'салат', 2.20))
        self.burger.remove_ingredient(1)
        assert len(self.burger.ingredients) == 2

    @allure.title('remove_ingredient() - удаление ингредиента')
    @allure.description('Проверяем, что после удаления ингредиента в списоке один ингредиент из двух')
    def test_remove_ingredient_remained_one(self):
        self.burger = Burger()
        self.burger.add_ingredient(Ingredient('котлета', 'куриная', 3.30))
        self.burger.add_ingredient(Ingredient('овощи', 'салат', 2.20))
        self.burger.remove_ingredient(0)
        assert len(self.burger.ingredients) == 1

    @allure.title('move_ingredient() - перемещение ингредиента')
    @allure.description('Проверяем, что ингредиенты переместились')
    def test_move_ingredient(self):
        self.burger = Burger()
        ingredient1 = Ingredient('Котлета', 'Куриная', 5.50)
        ingredient2 = Ingredient('Котлета', 'Говяжья', 5.50)
        self.burger.add_ingredient(ingredient1)
        self.burger.add_ingredient(ingredient2)
        self.burger.move_ingredient(0, 1)
        assert self.burger.ingredients[1].get_name() == 'Куриная'

    @allure.title('get_price() - получение стоимости бургера')
    @allure.description('Проверяем, что метод возвращает правильную стоимость')
    def test_get_price(self):
        self.burger = Burger()
        bun = Bun('Сырный', 3.00)
        self.burger.set_buns(bun)
        ingredient1 = Ingredient('Основа', 'Котлета', 2.00)
        ingredient2 = Ingredient('Овощи', 'Салат', 0.50)
        self.burger.add_ingredient(ingredient1)
        self.burger.add_ingredient(ingredient2)
        assert self.burger.get_price() == 8.50

    @allure.title('get_receipt() - получение рецепта бургера')
    @allure.description('Проверяем, что рецепт содержит все ингредиенты')
    def test_get_receipt(self):
        bun = Bun('Сырный', 3.25)
        ingredient1 = Ingredient('Овощи', 'Помидор', 2.20)
        ingredient2 = Ingredient('Овощи', 'Огурец', 0.75)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        assert 'Сырный' in burger.get_receipt()
