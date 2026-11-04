from praktikum.bun import Bun

class TestBun:
    def test_bun_get_name_returns_correct_name(self):
        # Arrange: создаем булочку с именем и ценой
        bun = Bun("Краторная булка", 100)
        
        # Act & Assert: проверяем, что метод возвращает правильное имя
        assert bun.get_name() == "Краторная булка"

    def test_bun_get_price_returns_correct_price(self):
        # Arrange
        bun = Bun("Краторная булка", 100)
        
        # Act & Assert: проверяем цену
        assert bun.get_price() == 100
