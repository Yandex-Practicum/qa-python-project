import pytest
from bun import Bun


class TestBun:

    @pytest.mark.parametrize('name, price', [['Флюоренсцентная булка', 234.0],
                                             ['Краторная булка', 134.99],
                                             ['Space_Bun', 245.0]])
    def test_get_name_shows_true(self, name, price):
        bun = Bun(name, price)
        result_get_name = bun.get_name()
        assert len(result_get_name) != 0 and type(result_get_name) == str

    @pytest.mark.parametrize('name, price', [['Космическая булка', 574.0],
                                             ['Sweet_BUN', 432.99],
                                             ['SpaCe_Bun', 342.99]])
    def test_get_price_shows_true(self, name, price):
        bun = Bun(name, price)
        result_get_price = bun.get_price()
        assert result_get_price != None and result_get_price > 0.0 and type(result_get_price) == float
