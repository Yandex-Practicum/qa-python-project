from unittest.mock import MagicMock

import pytest


@pytest.fixture
def mk_ing():
    def _make(label: str, *, price: int = 1, type_: str = "FILLING"):
        ing = MagicMock()
        ing.get_name.return_value = label
        ing.get_price.return_value = price
        ing.get_type.return_value = type_
        return ing

    return _make
