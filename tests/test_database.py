import pytest
import DATA


@pytest.mark.parametrize('count', DATA.Count.ZERO_TO_TWO)
def test_available_buns_name(db, count):
    expected_buns = DATA.Database_fill.DATABASE_BUNS
    actual_buns = db.available_buns()
    assert actual_buns[count].name == expected_buns[count].name


@pytest.mark.parametrize('count', DATA.Count.ZERO_TO_TWO)
def test_available_buns_price(db, count):
    expected_buns = DATA.Database_fill.DATABASE_BUNS
    actual_buns = db.available_buns()
    assert actual_buns[count].price == expected_buns[count].price


def test_available_buns_count(db):
    expected_length = len(DATA.Database_fill.DATABASE_BUNS)
    actual_length = len(db.available_buns())
    assert actual_length == expected_length


@pytest.mark.parametrize('count', DATA.Count.ZERO_TO_FIVE)
def test_available_ingredients_names(db, count):
    expected_ingredients = DATA.Database_fill.DATABASE_INGRIDIENT
    actual_ingredients = db.available_ingredients()
    assert expected_ingredients[count].name == actual_ingredients[count].name


@pytest.mark.parametrize('count', DATA.Count.ZERO_TO_FIVE)
def test_available_ingredients_types(db, count):
    expected_ingredients = DATA.Database_fill.DATABASE_INGRIDIENT
    actual_ingredients = db.available_ingredients()
    assert expected_ingredients[count].type == actual_ingredients[count].type


@pytest.mark.parametrize('count', DATA.Count.ZERO_TO_FIVE)
def test_available_ingredients_price(db, count):
    expected_ingredients = DATA.Database_fill.DATABASE_INGRIDIENT
    actual_ingredients = db.available_ingredients()
    assert expected_ingredients[count].price == actual_ingredients[count].price


def test_available_ingredients_count(db):
    expected_length = len(DATA.Database_fill.DATABASE_INGRIDIENT)
    actual_length = len(db.available_ingredients())
    assert actual_length == expected_length
