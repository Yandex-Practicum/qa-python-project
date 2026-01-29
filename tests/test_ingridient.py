class TestIngridient:

    def test_get_name(self, ingridient):
        name = ingridient.get_name()
        assert name == 'onion'


    def test_get_price(self, ingridient):
        name = ingridient.get_price()
        assert name == 50


    def test_get_type(self, ingridient):
        name = ingridient.get_type()
        assert name == 'filling'