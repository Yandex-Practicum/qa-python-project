
class TestBun:
    def test_get_name_bun_with_valid_name_returns_expected_name(self, real_bun):   # тестирует get_name: возвращает имя заданное при создании объекта

        assert real_bun.get_name() == "Big bun", f"Ожидаемое имя булочки: 'Big bun', но получено: {real_bun.get_name()}"

    def test_get_price_bun_with_valid_price_returns_expected_price(self, real_bun): # тестирует get_price: возвращает корректную цену заданное при создании объекта

        assert real_bun.get_price() == 199.5, f"Ожидаемая цена булочки: 199.5, но получено: {real_bun.get_price()}"