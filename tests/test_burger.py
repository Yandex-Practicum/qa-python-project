import pytest

from tests.test_data import MOVE_CASES, PRICE_CASES, RECEIPT_CASES


def test_set_buns(burger, make_bun):
    bun = make_bun()
    burger.set_buns(bun)
    assert burger.bun is bun


def test_add_ingredient(burger, make_ingredient):
    ing = make_ingredient()
    burger.add_ingredient(ing)
    assert burger.ingredients == [ing]


def test_add_ingredient_keeps_order(burger, make_ingredient):
    first, second = make_ingredient(), make_ingredient()
    burger.add_ingredient(first)
    burger.add_ingredient(second)
    assert burger.ingredients == [first, second]


def test_remove_ingredient(burger, make_ingredient):
    first, second = make_ingredient(), make_ingredient()
    burger.add_ingredient(first)
    burger.add_ingredient(second)
    burger.remove_ingredient(0)
    assert burger.ingredients == [second]


@pytest.mark.parametrize("index", [
    pytest.param(0, id="empty_burger"),
    pytest.param(5, id="out_of_range"),
])
def test_remove_ingredient_invalid_index_raises(burger, index):
    with pytest.raises(IndexError):
        burger.remove_ingredient(index)


@pytest.mark.parametrize("src, dst", MOVE_CASES)
def test_move_ingredient(burger, make_ingredient, src, dst):
    items = [make_ingredient(name=n) for n in "abc"]
    for item in items:
        burger.add_ingredient(item)

    expected = items.copy()
    expected.insert(dst, expected.pop(src))

    burger.move_ingredient(src, dst)

    assert burger.ingredients == expected


def test_move_ingredient_invalid_index_raises(burger):
    with pytest.raises(IndexError):
        burger.move_ingredient(0, 0)


@pytest.mark.parametrize("bun_price, ingredient_prices, expected", PRICE_CASES)
def test_get_price(burger, make_bun, make_ingredient,
                   bun_price, ingredient_prices, expected):
    burger.set_buns(make_bun(price=bun_price))
    for price in ingredient_prices:
        burger.add_ingredient(make_ingredient(price=price))

    assert burger.get_price() == pytest.approx(expected)


def test_get_price_counts_bun_twice(burger, make_bun):
    burger.set_buns(make_bun(price=7.0))

    assert burger.get_price() == 14.0


def test_get_price_without_bun_raises(burger):
    with pytest.raises(AttributeError):
        burger.get_price()


@pytest.mark.parametrize("bun_name, bun_price, ingredients, expected", RECEIPT_CASES)
def test_get_receipt(burger, make_bun, make_ingredient,
                     bun_name, bun_price, ingredients, expected):
    burger.set_buns(make_bun(name=bun_name, price=bun_price))
    for type_, name, price in ingredients:
        burger.add_ingredient(make_ingredient(type_, name, price))

    assert burger.get_receipt() == expected


def test_get_receipt_without_bun_raises(burger):
    with pytest.raises(AttributeError):
        burger.get_receipt()

        