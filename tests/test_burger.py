import pytest
from unittest.mock import MagicMock
from prakticum.burger import Burger


@pytest.fixture
def burger():
    return Burger()

# set_buns
def test_set_buns_positive(burger):
    bun = MagicMock()
    burger.set_buns(bun)
    assert burger.bun is bun

def test_set_buns_negative(burger):
    with pytest.raises(AttributeError):
        burger.set_buns(None)
        _ = burger.bun.get_name()


# add_ingredient param
@pytest.mark.parametrize("ing_names", [["a"], ["a","b"]])
def test_add_ingredient_positive(burger, ing_names):
    for n in ing_names:
        ing = MagicMock()
        burger.add_ingredient(ing)
    assert len(burger.ingredients) == len(ing_names)

def test_add_ingredient_negative(burger):
    ingredient = None
    burger.add_ingredient(ingredient)  # type: ignore
    assert burger.ingredients[-1] is None


# remove_ingredient
@pytest.mark.parametrize("idx", [0,1])
def test_remove_ingredient_positive(burger, idx):
    burger.ingredients = [MagicMock(), MagicMock()]
    burger.remove_ingredient(idx)
    assert len(burger.ingredients)==1

def test_remove_ingredient_negative(burger):
    with pytest.raises(IndexError):
        burger.remove_ingredient(99)


# move_ingredient
def test_move_ingredient_positive(burger):
    a,b = MagicMock(), MagicMock()
    burger.ingredients=[a,b]
    burger.move_ingredient(0,1)
    assert burger.ingredients==[b,a]

def test_move_ingredient_negative(burger):
    with pytest.raises(IndexError):
        burger.move_ingredient(5,0)


# price param
@pytest.mark.parametrize("bun_price,ing_prices,expected", [
    (10, [],20),
    (5,[1,2],5*2+3)
])
def test_get_price_positive(burger,bun_price,ing_prices,expected):
    bun = MagicMock()
    bun.get_price.return_value=bun_price
    burger.set_buns(bun)
    for p in ing_prices:
        ing=MagicMock()
        ing.get_price.return_value=p
        burger.add_ingredient(ing)
    assert burger.get_price()==expected

def test_get_price_negative(burger):
    with pytest.raises(AttributeError):
        burger.get_price()


# receipt
def test_receipt_positive(burger):
    bun=MagicMock()
    bun.get_name.return_value="B"
    bun.get_price.return_value=5
    burger.set_buns(bun)
    ing=MagicMock()
    ing.get_name.return_value="X"
    ing.get_type.return_value="SAUCE"
    ing.get_price.return_value=1
    burger.add_ingredient(ing)
    r=burger.get_receipt()
    assert "B" in r and "sauce x" in r.lower()

def test_receipt_negative(burger):
    with pytest.raises(AttributeError):
        burger.get_receipt()
