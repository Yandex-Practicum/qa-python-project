import pytest
import allure
from unittest.mock import Mock

from burger import Burger
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@allure.feature('Burger')
class TestBurger:

    @allure.title('bun при создании — None')
    def test_init_bun_is_none(self):
        burger = Burger()
        allure.attach(
            name="Входные данные", 
            body="Создаём пустой бургер", 
            attachment_type=allure.attachment_type.TEXT)
        assert burger.bun is None, "bun должен быть None "

    @allure.title('ingredients при создании — пустой список')
    def test_init_ingredients_is_empty_list(self):
        burger = Burger()
        allure.attach(
            name="Входные данные", 
            body="Создаём пустой бургер - проверяем ingredients", 
            attachment_type=allure.attachment_type.TEXT)
        assert burger.ingredients == [], "ingredients должен быть пустым списком"

    @allure.title('set_buns сохраняет булочку')
    def test_set_buns_sets_bun(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        allure.attach(
            name="Входные данные", 
            body="Ставим булочку через set_buns", 
            attachment_type=allure.attachment_type.TEXT)
        assert burger.bun == mock_bun, "set_buns должен сохранить булочку"

    @allure.title('add_ingredient увеличивает длину списка на 1')
    def test_add_ingredient_increases_length(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        allure.attach(
            name="Входные данные", 
            body="Добавляем 1 ингредиент - проверяем длину списка", 
            attachment_type=allure.attachment_type.TEXT)
        assert len(burger.ingredients) == 1, "Длина списка должна стать 1"

    @allure.title('add_ingredient добавляет элемент в конец')
    def test_add_ingredient_adds_to_end(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        allure.attach(
            name="Входные данные", 
            body="Добавляем 1 ингредиент - проверяем позицию в списке", 
            attachment_type=allure.attachment_type.TEXT)
        assert burger.ingredients[0] == mock_ingredient, "Элемент должен быть на позиции 0"

    @allure.title('add_ingredient собирает ингредиенты и сохраняет порядок')
    def test_add_multiple_ingredients_preserves_order(self):
        burger = Burger()
        m1, m2, m3 = Mock(), Mock(), Mock()
        burger.add_ingredient(m1)
        burger.add_ingredient(m2)
        burger.add_ingredient(m3)
        allure.attach(
            name="Входные данные", 
            body="Добавляем 3 ингредиента подряд - смотрим порядок", 
            attachment_type=allure.attachment_type.TEXT)
        assert burger.ingredients == [m1, m2, m3], "Список должен по порядку добавления"

    @allure.title('remove_ingredient уменьшает списка')
    def test_remove_ingredient_decreases_length(self):
        burger = Burger()
        m1, m2, m3 = Mock(), Mock(), Mock()
        burger.add_ingredient(m1)
        burger.add_ingredient(m2)
        burger.add_ingredient(m3)
        burger.remove_ingredient(1)
        allure.attach(
            name="Входные данные", 
            body="Добавляем 3 ингредиента - удаляем по индексу 1, проверяем длину", 
            attachment_type=allure.attachment_type.TEXT)
        assert len(burger.ingredients) == 2, "Длина должна быть 2"

    @allure.title('remove_ingredient удаляет элемент по индексу')
    def test_remove_ingredient_removes_element(self):
        burger = Burger()
        m1, m2, m3 = Mock(), Mock(), Mock()
        burger.add_ingredient(m1)
        burger.add_ingredient(m2)
        burger.add_ingredient(m3)
        burger.remove_ingredient(2)
        allure.attach(
            name="Входные данные", 
            body="Добавляем 3 ингредиента-удаляем по индексу 2", 
            attachment_type=allure.attachment_type.TEXT)
        assert m3 not in burger.ingredients, "Элемент не должен быть в списке"

    @allure.title('remove_ingredient сдвигает элементы')
    def test_remove_ingredient_shifts_elements(self):
        burger = Burger()
        m1, m2, m3 = Mock(), Mock(), Mock()
        burger.add_ingredient(m1)
        burger.add_ingredient(m2)
        burger.add_ingredient(m3)
        burger.remove_ingredient(1)
        allure.attach(
            name="Входные данные", 
            body="Добавляем 3 ингредиента - удаляем по индексу 1, проверяем порядок", 
            attachment_type=allure.attachment_type.TEXT)
        assert burger.ingredients == [m1, m3], "Порядок должен быть [m1, m3]"

    @allure.title('move_ingredient меняет позицию элемента')
    def test_move_ingredient_changes_position(self):
        burger = Burger()
        m1, m2, m3 = Mock(), Mock(), Mock()
        burger.add_ingredient(m1)
        burger.add_ingredient(m2)
        burger.add_ingredient(m3)
        burger.move_ingredient(0, 2)
        allure.attach(
            name="Входные данные", 
            body="Добавляем 3 ингредиента-перемещаем с индекса 0 на 2", attachment_type=allure.attachment_type.TEXT)
        assert burger.ingredients == [m2, m3, m1], "Порядок должен стать [m2, m3, m1]"

    @pytest.mark.parametrize('bun_price, ingredient_prices, expected', [
        (100, [], 200),
        (50, [30], 130),
        (50, [30, 40], 170),
        (0, [0], 0),
        (100, [10, 20, 30], 260),
    ], ids=[
        "булка=100, нет ингр.  - 200",
        "булка=50, 1 ингр.=30 - 130",
        "булка=50, 2 ингр.=[30,40] - 170",
        "пусто - 0",
        "булка=100, 3 ингр. - 260",
    ])
    @allure.title('get_price: булочка={bun_price}, ингредиенты={ingredient_prices} - {expected}')
    def test_get_price_parametrized(self, bun_price, ingredient_prices, expected):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredient_prices:
            mock_ing = Mock()
            mock_ing.get_price.return_value = price
            burger.add_ingredient(mock_ing)

        allure.attach(
            name="Входные данные", 
            body=f"Цена булочки: {bun_price}, цены ингред.: {ingredient_prices}, ждем цену {expected}", 
            attachment_type=allure.attachment_type.TEXT)
        assert burger.get_price() == expected, f"Должна быть цена: {expected}, получена: {burger.get_price()}"

    @pytest.mark.parametrize('bun_name, expected_line', [
        ("white bun", "(==== white bun ====)",),
        ("black bun", "(==== black bun ====)",),
    ], ids=[
        "white bun line",
        "black bun line",
    ])
    @allure.title('Чек содержит строку булочки: {bun_name}')
    def test_receipt_contains_bun_line(self, bun_name, expected_line):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)

        allure.attach(
            name="Входные данные", 
            body=f"Название булочки: {bun_name}, ждали строку: {expected_line}", 
            attachment_type=allure.attachment_type.TEXT)
        receipt = burger.get_receipt()
        allure.attach(name="Чек", body=receipt, attachment_type=allure.attachment_type.TEXT)
        assert expected_line in receipt, f"Чек должен содержать строку: {expected_line}"

    @pytest.mark.parametrize('bun_name', [
        "white bun",
        "black bun",
    ], ids=[
        "white bun count",
        "black bun count",
    ])
    @allure.title('Чек - булочка встречается дважды: {bun_name}')
    def test_receipt_bun_count_twice(self, bun_name):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)

        allure.attach(
            name="Входные данные", 
            body=f"Название булочки: {bun_name} - количество в чеке 2", 
            attachment_type=allure.attachment_type.TEXT)
        receipt = burger.get_receipt()
        allure.attach(
            name="Чек", body=receipt, 
            attachment_type=allure.attachment_type.TEXT)
        assert receipt.count(f"(==== {bun_name} ====)") == 2, f"Булочка '{bun_name}' должна встречаться в чеке 2 раза"

    @pytest.mark.parametrize('ingr_type, ingr_name, expected_format', [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", "= sauce hot sauce ="),
        (INGREDIENT_TYPE_SAUCE, "sour cream", "= sauce sour cream ="),
        (INGREDIENT_TYPE_FILLING, "cutlet", "= filling cutlet ="),
        (INGREDIENT_TYPE_FILLING, "sausage", "= filling sausage ="),
    ], ids=[
        "sauce: hot sauce",
        "sauce: sour cream",
        "filling: cutlet",
        "filling: sausage",
    ])
    @allure.title('Чек - формат ингредиента {ingr_type} — {ingr_name}')
    def test_receipt_ingredient_format(self, ingr_type, ingr_name, expected_format):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "white bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)

        mock_ingr = Mock()
        mock_ingr.get_type.return_value = ingr_type
        mock_ingr.get_name.return_value = ingr_name
        mock_ingr.get_price.return_value = 50.0
        burger.add_ingredient(mock_ingr)

        allure.attach(
            name="Входные данные", 
            body=f"Тип: {ingr_type}, название: {ingr_name}, ожидаемый формат: {expected_format}", 
            attachment_type=allure.attachment_type.TEXT)
        receipt = burger.get_receipt()
        allure.attach(
            name="Чек", 
            body=receipt, 
            attachment_type=allure.attachment_type.TEXT)
        assert expected_format in receipt, f"Чек должен содержать формат: {expected_format}"

    @allure.title('Чек - тип ингредиента в ниж. регистре')
    def test_receipt_type_lowercased(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "bun"
        mock_bun.get_price.return_value = 0
        burger.set_buns(mock_bun)

        mock_ingr = Mock()
        mock_ingr.get_type.return_value = "SAUCE"
        mock_ingr.get_name.return_value = "salsa"
        mock_ingr.get_price.return_value = 0
        burger.add_ingredient(mock_ingr)

        allure.attach(
            name="Входные данные", 
            body="Тип ингр.: SAUCE (верх. рег.), название: salsa ждем в чеке: '= sauce salsa ='", 
            attachment_type=allure.attachment_type.TEXT)
        receipt = burger.get_receipt()
        allure.attach(
            name="Чек", 
            body=receipt, 
            attachment_type=allure.attachment_type.TEXT)
        assert "= sauce salsa =" in receipt, "Тип ингредиента должен быть в нижнем регистре"


