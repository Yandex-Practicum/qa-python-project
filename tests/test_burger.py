import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_init_bun_is_none(self):
        # При создании Burger поле bun равно None
        burger = Burger()
        assert burger.bun is None

    def test_init_ingredients_empty(self):
        # При создании Burger список ингредиентов пуст
        burger = Burger()
        assert burger.ingredients == []

    def test_set_buns_sets_bun(self):
        # set_buns сохраняет переданный объект булки в поле bun
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun

    def test_add_ingredient_appends_to_list(self):
        # add_ingredient добавляет ингредиент в список
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_add_ingredient_multiple(self):
        # При добавлении нескольких ингредиентов порядок сохраняется
        burger = Burger()
        m1, m2 = Mock(), Mock()
        burger.add_ingredient(m1)
        burger.add_ingredient(m2)
        assert burger.ingredients == [m1, m2]

    @pytest.mark.parametrize("initial_count,remove_index,expected_count", [
        (1, 0, 0),
        (3, 0, 2),
        (3, 2, 2),
        (3, 1, 2),
    ])
    def test_remove_ingredient(self, initial_count, remove_index, expected_count):
        # remove_ingredient уменьшает длину списка на единицу
        burger = Burger()
        for i in range(initial_count):
            m = Mock()
            m.get_name.return_value = f"ingredient_{i}"
            burger.add_ingredient(m)
        burger.remove_ingredient(remove_index)
        assert len(burger.ingredients) == expected_count

    def test_remove_ingredient_removes_correct_item(self):
        # remove_ingredient удаляет элемент по индексу, остальные сохраняются
        burger = Burger()
        i1, i2, i3 = Mock(), Mock(), Mock()
        burger.add_ingredient(i1)
        burger.add_ingredient(i2)
        burger.add_ingredient(i3)
        burger.remove_ingredient(1)
        assert burger.ingredients == [i1, i3]

    @pytest.mark.parametrize("index,new_index,expected_order", [
        (0, 2, [1, 2, 0]),
        (2, 0, [2, 0, 1]),
        (0, 1, [1, 0, 2]),
        (1, 0, [1, 0, 2]),
    ])
    def test_move_ingredient(self, index, new_index, expected_order):
        # move_ingredient перемещает элемент, порядок остальных корректен
        burger = Burger()
        for i in range(3):
            m = Mock()
            m.get_name.return_value = f"ingredient_{i}"
            burger.add_ingredient(m)
        burger.move_ingredient(index, new_index)
        actual = [ing.get_name() for ing in burger.ingredients]
        expected = [f"ingredient_{i}" for i in expected_order]
        assert actual == expected

    def test_move_ingredient_same_index(self):
        # Перемещение на тот же индекс не меняет порядок
        burger = Burger()
        i1, i2, i3 = Mock(), Mock(), Mock()
        burger.add_ingredient(i1)
        burger.add_ingredient(i2)
        burger.add_ingredient(i3)
        burger.move_ingredient(1, 1)
        assert burger.ingredients == [i1, i2, i3]

    def test_move_ingredient_to_end(self):
        # Перемещение первого элемента в конец сдвигает остальные
        burger = Burger()
        i1, i2, i3 = Mock(), Mock(), Mock()
        burger.add_ingredient(i1)
        burger.add_ingredient(i2)
        burger.add_ingredient(i3)
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [i2, i3, i1]

    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_remove_ingredient_single_from_three(self, index):
        # Удаление одного элемента из трёх оставляет два
        burger = Burger()
        i1, i2, i3 = Mock(), Mock(), Mock()
        burger.add_ingredient(i1)
        burger.add_ingredient(i2)
        burger.add_ingredient(i3)
        burger.remove_ingredient(index)
        assert len(burger.ingredients) == 2

    def test_get_price_only_bun(self):
        # Цена бургера только с булкой: 2 * цена булки
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)
        assert burger.get_price() == 200.0

    def test_get_price_bun_and_ingredients(self):
        # Цена бургера с булкой и ингредиентами: сумма двух булок и всех ингредиентов
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)
        i1 = Mock()
        i1.get_price.return_value = 50.0
        i2 = Mock()
        i2.get_price.return_value = 75.0
        burger.add_ingredient(i1)
        burger.add_ingredient(i2)
        assert burger.get_price() == 325.0

    @pytest.mark.parametrize("bun_price,ingredient_prices,expected", [
        (100.0, [], 200.0),
        (50.0, [25.0], 125.0),
        (200.0, [100.0, 150.0, 50.0], 700.0),
        (0.0, [], 0.0),
        (100.0, [0.0, 0.0], 200.0),
    ])
    def test_get_price_parametrized(self, bun_price, ingredient_prices, expected):
        # Параметризованный тест расчёта цены для разных комбинаций
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        for price in ingredient_prices:
            m = Mock()
            m.get_price.return_value = price
            burger.add_ingredient(m)
        assert burger.get_price() == expected

    def test_get_price_no_ingredients_real_bun(self):
        # Расчёт цены с реальным объектом Bun: 2 * цена булки
        burger = Burger()
        burger.set_buns(Bun("white bun", 200))
        assert burger.get_price() == 400.0

    def test_get_receipt_format(self):
        # Формат чека с булкой и двумя ингредиентами
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "white bun"
        mock_bun.get_price.return_value = 200.0
        burger.set_buns(mock_bun)
        sauce = Mock()
        sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        sauce.get_name.return_value = "hot sauce"
        sauce.get_price.return_value = 100.0
        burger.add_ingredient(sauce)
        filling = Mock()
        filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        filling.get_name.return_value = "cutlet"
        filling.get_price.return_value = 100.0
        burger.add_ingredient(filling)
        expected = "\n".join([
            "(==== white bun ====)",
            "= sauce hot sauce =",
            "= filling cutlet =",
            "(==== white bun ====)\n",
            "Price: 600.0",
        ])
        assert burger.get_receipt() == expected

    def test_get_receipt_only_bun(self):
        # Формат чека для бургера без ингредиентов
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)
        expected = "\n".join([
            "(==== black bun ====)",
            "(==== black bun ====)\n",
            "Price: 200.0",
        ])
        assert burger.get_receipt() == expected

    @pytest.mark.parametrize("bun_name,ingredient_type,ingredient_name,bun_price,ingredient_price", [
        ("white bun", INGREDIENT_TYPE_SAUCE, "chili sauce", 50.0, 30.0),
        ("black bun", INGREDIENT_TYPE_FILLING, "beef", 100.0, 200.0),
    ])
    def test_get_receipt_parametrized(
        self, bun_name, ingredient_type, ingredient_name, bun_price, ingredient_price,
    ):
        # Параметризованный тест формата чека для разных булок и одного ингредиента
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        m = Mock()
        m.get_type.return_value = ingredient_type
        m.get_name.return_value = ingredient_name
        m.get_price.return_value = ingredient_price
        burger.add_ingredient(m)
        expected_price = bun_price * 2 + ingredient_price
        expected = "\n".join([
            f"(==== {bun_name} ====)",
            f"= {ingredient_type.lower()} {ingredient_name} =",
            f"(==== {bun_name} ====)\n",
            f"Price: {expected_price}",
        ])
        assert burger.get_receipt() == expected

    # --- Чек с реальными объектами Bun и Ingredient ---

    @pytest.fixture
    def burger_real(self):
        burger = Burger()
        burger.set_buns(Bun("black bun", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100))
        return burger

    def test_get_receipt_real_top_bun(self, burger_real):
        # Верхняя булка в чеке с реальными объектами
        lines = burger_real.get_receipt().split('\n')
        assert lines[0] == "(==== black bun ====)"

    def test_get_receipt_real_sauce_line(self, burger_real):
        # Строка соуса в чеке с реальными объектами
        lines = burger_real.get_receipt().split('\n')
        assert lines[1] == "= sauce hot sauce ="

    def test_get_receipt_real_filling_line(self, burger_real):
        # Строка начинки в чеке с реальными объектами
        lines = burger_real.get_receipt().split('\n')
        assert lines[2] == "= filling cutlet ="

    def test_get_receipt_real_bottom_bun(self, burger_real):
        # Нижняя булка в чеке с реальными объектами
        lines = burger_real.get_receipt().split('\n')
        assert lines[3] == "(==== black bun ====)"

    def test_get_receipt_real_price(self, burger_real):
        # Итоговая цена в чеке с реальными объектами
        lines = burger_real.get_receipt().split('\n')
        assert float(lines[-1].replace("Price: ", "")) == 400.0

    # --- Чек с двумя ингредиентами одного типа ---

    @pytest.fixture
    def burger_same_type(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "red bun"
        mock_bun.get_price.return_value = 300.0
        burger.set_buns(mock_bun)
        s1 = Mock()
        s1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        s1.get_name.return_value = "hot sauce"
        s1.get_price.return_value = 100.0
        s2 = Mock()
        s2.get_type.return_value = INGREDIENT_TYPE_SAUCE
        s2.get_name.return_value = "chili sauce"
        s2.get_price.return_value = 300.0
        burger.add_ingredient(s1)
        burger.add_ingredient(s2)
        return burger

    def test_get_receipt_same_type_top_bun(self, burger_same_type):
        # Верхняя булка в чеке с двумя соусами
        lines = burger_same_type.get_receipt().split('\n')
        assert lines[0] == "(==== red bun ====)"

    def test_get_receipt_same_type_first_sauce(self, burger_same_type):
        # Первый соус в чеке с двумя соусами
        lines = burger_same_type.get_receipt().split('\n')
        assert lines[1] == "= sauce hot sauce ="

    def test_get_receipt_same_type_second_sauce(self, burger_same_type):
        # Второй соус в чеке с двумя соусами
        lines = burger_same_type.get_receipt().split('\n')
        assert lines[2] == "= sauce chili sauce ="

    def test_get_receipt_same_type_bottom_bun(self, burger_same_type):
        # Нижняя булка в чеке с двумя соусами
        lines = burger_same_type.get_receipt().split('\n')
        assert lines[3] == "(==== red bun ====)"

    def test_get_receipt_same_type_price(self, burger_same_type):
        # Итоговая цена в чеке с двумя соусами
        lines = burger_same_type.get_receipt().split('\n')
        assert float(lines[-1].replace("Price: ", "")) == 1000.0

    @pytest.mark.parametrize("bun_name,bun_price,ingredients,expected_price", [
        ("white bun", 100.0, [], 200.0),
        ("black bun", 50.0, [("sauce", "sour cream", 200.0)], 300.0),
        ("red bun", 300.0, [
            ("sauce", "hot sauce", 100.0),
            ("filling", "cutlet", 100.0),
            ("filling", "sausage", 300.0),
        ], 1100.0),
    ])
    def test_get_receipt_full_parametrized(self, bun_name, bun_price, ingredients, expected_price):
        # Параметризованный тест: полный чек для разных комбинаций — строка целиком
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        for ing_type, ing_name, ing_price in ingredients:
            m = Mock()
            m.get_type.return_value = ing_type
            m.get_name.return_value = ing_name
            m.get_price.return_value = ing_price
            burger.add_ingredient(m)
        expected_lines = [f"(==== {bun_name} ====)"]
        for ing_type, ing_name, _ in ingredients:
            expected_lines.append(f"= {ing_type} {ing_name} =")
        expected_lines.append(f"(==== {bun_name} ====)\n")
        expected_lines.append(f"Price: {expected_price}")
        assert burger.get_receipt() == "\n".join(expected_lines)
