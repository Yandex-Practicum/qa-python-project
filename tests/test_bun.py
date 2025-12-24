from praktikum.bun import Bun


class TestBun:
    def test_bun_get_name(self):
        bun = Bun('Сэндвич с вогонской плесенью', 1500)
        assert bun.get_name() == 'Сэндвич с вогонской плесенью', 'Unable to get bun name'

    def test_bun_get_price(self):
        bun = Bun('Сэндвич с вогонской плесенью', 1500)
        assert bun.get_price() == 1500, 'Unable to get bun price'
