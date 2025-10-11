import pytest
from praktikum.bun import Bun

class TestBun:
    """Tests for the Bun class."""

    @pytest.mark.parametrize("name, price", [
        ("Fluorescent Bun R2-D3", 988),   # typical name and integer price
        ("Black Bun", 100.0),            # name with float price
    ])
    def test_get_name_and_price(self, name, price):
        """Bun.get_name returns the bun name, and Bun.get_price returns the price."""
        bun = Bun(name, price)
        assert bun.get_name() == name, "get_name() should return the name given in constructor"
        assert bun.get_price() == price, "get_price() should return the price given in constructor"
