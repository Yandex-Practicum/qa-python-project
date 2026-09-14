from unittest.mock import Mock

from praktikum.burger import Burger


class TestBurger:
    """Тесты для класса Burger."""

    def test_set_buns_saves_bun(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Краторная булка"

        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun is mock_bun