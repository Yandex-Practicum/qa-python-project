import pytest

class TestBurger():
    # проверка определения булочки в бургер
    def test_set_buns(self, bun, burger):
        burger.set_buns(bun)
        assert burger.bun != None

    # проверка добавления ингредиента в бургер
    @pytest.mark.parametrize('ingredient', ['sauce', 'filling'])
    def test_add_ingredient(self, ingredient, burger, request):
        ingredient_fixture = request.getfixturevalue(ingredient)
        burger.add_ingredient(ingredient_fixture)  # добавляем ингредиент
        assert ingredient_fixture in burger.ingredients # проверяем наличие ингредиента в списке ингредиентов бургера

    # проверка удаления ингредиента из списка ингредиентов бургера
    @pytest.mark.parametrize('ingredient', ['sauce', 'filling'])
    def test_remove_ingredient(self,ingredient, burger, request):
        ingredient_fixture = request.getfixturevalue(ingredient)
        burger.add_ingredient(ingredient_fixture) # добавляем ингредиент
        index = burger.ingredients.index(ingredient_fixture) # получаем индекс ингредиента в списке
        burger.remove_ingredient(index) # удаляем ингредиент из списка
        assert ingredient_fixture not in burger.ingredients # проверяем отсутствие ингредиента в списке ингредиентов бургера

    # проверка перемещения ингредиента в списке ингредиентов бургера
    def test_move_ingredient(self, burger, sauce, filling):
        burger.add_ingredient(sauce) # добавляем соус в список ингредиентов
        burger.add_ingredient(filling) # добавляем начинку в список ингредиентов
        index_sauce = burger.ingredients.index(sauce) # получаем индекс соуса в списке ингредиентов
        index_filling = burger.ingredients.index(filling) # получаем индекс начинки в списке ингредиентов
        burger.move_ingredient(index_filling, index_sauce) # переместили соус на место начинки
        assert burger.ingredients.index(sauce) == index_filling # проверяем, что индекс соуса поменялся на индекс начинки

    # проверка расчета цены бургера (только с булкой, с одним ингредиентом, с двумя ингредиентами)
    @pytest.mark.parametrize('burger_1', ['burger_with_bun', 'burger_with_ingredient', 'burger_with_ingredients'])
    def test_burger_get_price(self, burger_1, request):
        price = 0
        burger_fixture = request.getfixturevalue(burger_1)
        price = burger_fixture[0].get_price()
        assert price == burger_fixture[1] and type(price) == float

    # #проверка формирования рецепта бургера
    @pytest.mark.parametrize('burger_1', ['burger_with_bun', 'burger_with_ingredient', 'burger_with_ingredients'])
    def test_get_receipt(self, burger_1, request):
        list_receipt = []
        burger_fixture = request.getfixturevalue(burger_1)
        list_receipt = burger_fixture[0].get_receipt()
        assert list_receipt == '\n'.join(burger_fixture[2]+burger_fixture[3]) and type(list_receipt) == str
