import pytest
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize(
        'name, price',
        [
            ('Флюоресцентная булка R2-D3', 988),
            ('Краторная булка N-200i', 1255),
        ],
    )
    def test_bun_fields(self, name, price):
        bun = Bun(name, price)

        assert bun.name == name
        assert bun.price == price

    @pytest.mark.parametrize(
        'name, price',
        [
            ('Флюоресцентная булка R2-D3', 988),
            ('Краторная булка N-200i', 1255),
        ],
    )
    def test_get_bun_name(self, name, price):          # Проверяем метод get_name()bun = Bun(name, price)
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize(
        'name, price',
        [
            ('Флюоресцентная булка R2-D3', 988),
            ('Краторная булка N-200i', 1255),
        ],
    )
    def test_get_bun_price(self, name, price):          # Проверяем метод get_name()bun = Bun(name, price)
        bun = Bun(name, price)
        assert bun.get_price() == price