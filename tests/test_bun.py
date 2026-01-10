import pytest



class TestBun:

    @pytest.mark.parametrize("name", [
        "Бородинская булка",
        "БУЛКА С РOЗМAРИНОМ",
        "",
        "2-ая булка",
        "Булка бесплатная",
        "Burger bun",
        "Булка с рисом!!!"
    ])
    def test_get_name_returns_correct_name(self, name, simple_bun):
        bun = simple_bun(name = name)
        assert bun.get_name() == name, f"Получено {bun.get_name()} вместо ожидаемого {name}"


    @pytest.mark.parametrize("price", [
        50,
        100,
        200.50,
        0,
        -10,
        99999999999999999999.99
    ])
    def test_get_price_returns_correct_price(self, price, simple_bun):
        bun = simple_bun(price=price)
        assert bun.get_price() == price, f"Получено {bun.get_price()} вместо ожидаемого {price}"









