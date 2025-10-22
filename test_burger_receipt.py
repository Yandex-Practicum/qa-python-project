from praktikum.burger import Burger
from unittest.mock import MagicMock

def test_receipt_contains_bun_names_types_and_total():
    b = Burger()

    bun = MagicMock()
    bun.get_name.return_value = "Black Bun"
    bun.get_price.return_value = 100
    b.set_buns(bun)

    sauce = MagicMock()
    sauce.get_type.return_value = "SAUCE"    # должно стать 'sauce' в чеке
    sauce.get_name.return_value = "spicy"
    sauce.get_price.return_value = 30

    filling = MagicMock()
    filling.get_type.return_value = "FILLING"  # 'filling' в чеке
    filling.get_name.return_value = "beef"
    filling.get_price.return_value = 70

    b.add_ingredient(sauce)
    b.add_ingredient(filling)

    text = b.get_receipt()
    # Структура: "верхняя булка", список ровно в таком формате, "нижняя булка", Price
    assert "(==== Black Bun ====)" in text
    assert "= sauce spicy =" in text
    assert "= filling beef =" in text
    assert "Price: 300" in text   # 2*100 + 30 + 70
