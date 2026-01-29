from data import NameOfIngridients

class TestBuns:
    def test_get_buns_name(self, kratornaya_bulka):
        assert kratornaya_bulka.get_name() == NameOfIngridients.BUN_ONE

    def test_get_price(self, kratornaya_bulka):
        assert kratornaya_bulka.get_price() == NameOfIngridients.PRICE_BUN