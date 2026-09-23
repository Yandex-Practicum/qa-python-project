import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def database():
    #Создаёт экземпляр Database для тестов
    return Database()


# --- Инициализация БД: типы списков ---

@pytest.mark.parametrize("attr", ["buns", "ingredients"])
def test_database_init_attribute_is_list(database, attr):
    #Проверяет, что атрибуты buns и ingredients являются списками
    assert isinstance(getattr(database, attr), list)


# --- Инициализация БД: списки не пустые ---

@pytest.mark.parametrize("attr", ["buns", "ingredients"])
def test_database_init_attribute_not_empty(database, attr):
    #Проверяет, что списки buns и ingredients не пустые после инициализации
       assert len(getattr(database, attr)) > 0


# --- available_buns ---

def test_available_buns_returns_list(database):
    #Проверяет, что метод available_buns возвращает список
    assert isinstance(database.available_buns(), list)


def test_available_buns_all_are_bun_objects(database):
    #Проверяет, что все элементы в списке available_buns являются объектами Bun
    assert all(isinstance(bun, Bun) for bun in database.available_buns())


def test_available_buns_contains_black_bun(database):
    #Проверяет наличие булки с именем 'black bun' в списке доступных булочек
    assert any(bun.name == "black bun" for bun in database.available_buns())


def test_available_buns_black_bun_price(database):
    #Проверяет цену булки 'black bun' (должна быть 100)
    buns = database.available_buns()
    black_bun = next(bun for bun in buns if bun.name == "black bun")
    assert black_bun.price == 100


# --- available_ingredients: тип и содержимое ---

def test_available_ingredients_returns_list(database):
    #Проверяет, что метод available_ingredients возвращает список
    assert isinstance(database.available_ingredients(), list)


def test_available_ingredients_all_are_ingredient_objects(database):
    #Проверяет, что все элементы в списке available_ingredients являются объектами Ingredient
    assert all(isinstance(ing, Ingredient) for ing in database.available_ingredients())


@pytest.mark.parametrize("name", ["hot sauce", "cutlet"])
def test_available_ingredients_contains_item(database, name):
    #Проверяет наличие конкретных ингредиентов ('hot sauce', 'cutlet') в списке
    assert any(ing.name == name for ing in database.available_ingredients())


@pytest.mark.parametrize("name,expected_type", [
    ("hot sauce", INGREDIENT_TYPE_SAUCE),
    ("cutlet", INGREDIENT_TYPE_FILLING),
])
def test_available_ingredients_item_type(database, name, expected_type):
    #Проверяет тип ингредиента по его имени (соус или начинка)
    ingredients = database.available_ingredients()
    item = next(ing for ing in ingredients if ing.name == name)
    assert item.type == expected_type
