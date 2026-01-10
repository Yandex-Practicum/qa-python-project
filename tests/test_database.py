from praktikum.database import Database
from data import Data




def test_available_buns_count():
    db = Database()
    buns = db.available_buns()
    # Проверяем, что количество булочек совпадает с ожидаемым
    assert len(buns) == len(Data.BUNS)

def test_available_bun_names():
    db = Database()
    buns = db.available_buns()
    # Проверяем, что имена булочек совпадают с ожидаемыми
    for i, (bun_name, _) in enumerate(Data.BUNS):
        assert buns[i].get_name() == bun_name

def test_available_bun_prices():
    db = Database()
    buns = db.available_buns()
    # Проверяем, что цены булочек совпадают с ожидаемыми
    for i, (_, bun_price) in enumerate(Data.BUNS):
        assert buns[i].get_price() == bun_price


def test_available_ingredients_count():
    db = Database()
    ingredients = db.available_ingredients()
    # Проверяем, что количество ингредиентов совпадает с ожидаемым
    assert len(ingredients) == len(Data.INGREDIENTS)

def test_available_ingredient_types():
    db = Database()
    ingredients = db.available_ingredients()
    # Проверяем, что типы ингредиентов совпадают с ожидаемыми
    for i, (ingredient_type, _, _) in enumerate(Data.INGREDIENTS):
        assert ingredients[i].get_type() == ingredient_type

def test_available_ingredient_names():
    db = Database()
    ingredients = db.available_ingredients()
    # Проверяем, что имена ингредиентов совпадают с ожидаемыми
    for i, (_, ingredient_name, _) in enumerate(Data.INGREDIENTS):
        assert ingredients[i].get_name() == ingredient_name

def test_available_ingredient_prices():
    db = Database()
    ingredients = db.available_ingredients()
    # Проверяем, что цены ингредиентов совпадают с ожидаемыми
    for i, (_, _, ingredient_price) in enumerate(Data.INGREDIENTS):
        assert ingredients[i].get_price() == ingredient_price
