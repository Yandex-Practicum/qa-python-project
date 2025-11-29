from praktikum.burger import Burger

class TestBurger:
    def test_burger_init_bun_is_none(self):
        burger = Burger()
        assert burger.bun is None, 'Атрибут bun при инициализации не None'

    def test_burger_init_ingredients_is_empty_list(self):
        burger = Burger()
        assert burger.ingredients == [], 'При инициализации не задан пустой список ингредиентов'

    def test_burger_set_buns_bun_is_set(self, create_bun_mock):
        burger = Burger()
        bun = create_bun_mock
        burger.set_buns(bun)
        assert burger.bun == bun, 'Булка не задана'

    def test_burger_add_ingredient_ingredient_is_added(self, create_bun_mock, create_ingredient_mock):
        burger = Burger()
        bun = create_bun_mock
        ingredient = create_ingredient_mock
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient], 'Ингредиент не добавлен'

    def test_burger_remove_ingredient_ingredient_is_removed(self, create_test_burger):
        burger = create_test_burger[0]
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1, 'Ингредиент не удален'

    def test_burger_move_ingredient_ingredient_is_moved(self, create_test_burger):
        burger, bun, ingredient_1, ingredient_2 = create_test_burger
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_2, ingredient_1], 'Ингредиент не перемещен'

    def test_burger_get_price_price_is_correct(self, create_test_burger):
        burger = create_test_burger[0]
        price = (burger.bun.price * 2) + burger.ingredients[0].price + burger.ingredients[1].price
        assert burger.get_price() == price, 'Вернулась некорректная цена бургера'

    def test_burger_get_receipt_bun_name_in_receipt(self, create_test_burger):
        burger = create_test_burger[0]
        bun_name = burger.bun.name
        assert bun_name in burger.get_receipt(), 'Название булки не найдено в рецепте или некорректно'

    def test_burger_get_receipt_sauce_name_in_receipt(self, create_test_burger):
        burger = create_test_burger[0]
        sauce_name = burger.ingredients[0].name
        assert sauce_name in burger.get_receipt(), 'Название соуса не найдено в рецепте или некорректно'

    def test_burger_get_receipt_filling_name_in_receipt(self, create_test_burger):
        burger = create_test_burger[0]
        filling_name = burger.ingredients[1].name
        assert filling_name in burger.get_receipt(), 'Название начинки не найдено в рецепте или некорректно'

    def test_burger_get_receipt_price_in_receipt_and_correct(self, create_test_burger):
        burger = create_test_burger[0]
        price = burger.get_price()
        assert f'Price: {price}' in burger.get_receipt(), 'Цена не найдена в рецепте или некорректна'