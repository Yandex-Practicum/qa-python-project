from data import DataBun


# class for tests Bun methods
class TestsBun:

    def test_get_name(self, new_bun):
        name = new_bun.get_name()
        assert name == DataBun.BUN_NAME

    def test_get_price(self, new_bun):
        assert new_bun.get_price() == DataBun.BUN_PRICE
