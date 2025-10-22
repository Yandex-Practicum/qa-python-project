from unittest.mock import MagicMock
from praktikum.burger import Burger

def _mk_ing(label: str):
    ing = MagicMock()
    ing.get_name.return_value = label
    ing.get_price.return_value = 1
    ing.get_type.return_value = "FILLING"
    return ing

def test_add_and_remove_by_index():
    b = Burger()
    bun = MagicMock(); bun.get_name.return_value="B"; bun.get_price.return_value=10
    b.set_buns(bun)

    a = _mk_ing("A"); c = _mk_ing("C"); d = _mk_ing("D")
    b.add_ingredient(a); b.add_ingredient(c); b.add_ingredient(d)
    assert [x.get_name() for x in b.ingredients] == ["A","C","D"]

    # удалить средний элемент
    b.remove_ingredient(1)
    assert [x.get_name() for x in b.ingredients] == ["A","D"]

def test_move_ingredient_changes_order():
    b = Burger()
    bun = MagicMock(); bun.get_name.return_value="B"; bun.get_price.return_value=10
    b.set_buns(bun)

    a = _mk_ing("A"); c = _mk_ing("C"); d = _mk_ing("D")
    b.add_ingredient(a); b.add_ingredient(c); b.add_ingredient(d)

    # переместить первый в конец
    b.move_ingredient(0, 2)
    assert [x.get_name() for x in b.ingredients] == ["C","D","A"]

    # а теперь последний в начало
    b.move_ingredient(2, 0)
    assert [x.get_name() for x in b.ingredients] == ["A","C","D"]
