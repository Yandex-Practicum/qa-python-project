import pytest
from praktikum.bun import Bun
from data import Data


class TestBun:
    """
    Тесты для класса Bun, который представляет булочку.
    """

    @pytest.mark.parametrize(
        'bun_key',
        [
            "black",  # Черная булочка
            "red",    # Красная булочка
            "white",  # Белая булочка
        ],
    )
    def test_get_name(self, bun_key: str) -> None:
        """
        Тестирует метод get_name(), который возвращает название булочки.
        """
        name = Data.buns[bun_key]["name"]
        price = Data.buns[bun_key]["price"]
        bun = Bun(name, price)
        assert bun.get_name() == name, f"Expected {name}, but got {bun.get_name()}"

    @pytest.mark.parametrize(
        'bun_key',
        [
            "black",  # Черная булочка
            "red",    # Красная булочка
            "white",  # Белая булочка
        ],
    )
    def test_get_price(self, bun_key: str) -> None:
        """
        Тестирует метод get_price(), который возвращает цену булочки.
        """
        name = Data.buns[bun_key]["name"]
        price = Data.buns[bun_key]["price"]
        bun = Bun(name, price)
        assert bun.get_price() == price, f"Expected {price}, but got {bun.get_price()}"

    @pytest.mark.parametrize(
        'bun_key, invalid_price',
        [
            ("black", -1.0),  # Негативный случай
        ],
    )
    def test_invalid_price(self, bun_key: str, invalid_price: float) -> None:
        """
        Тестирует обработку некорректной цены.
        """
        name = Data.buns[bun_key]["name"]
        with pytest.raises(ValueError, match="Price must be non-negative"):
            Bun(name, invalid_price)
