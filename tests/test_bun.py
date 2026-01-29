from unittest.mock import Mock

class TestBun:

    #Тест получение названия булочки
    def test_get_name(self):
        #Создаем мок-объект булочки mock_bun
        mock_bun = Mock()
        #Присваиваем mock_bun.name значение, например "Зерновая".
        mock_bun.name = "Зерновая"
        #Присваиваем mock_bun.price значение цены, например 100.
        mock_bun.price = 100
        #Проверяем, что значение mock_bun.name равно "Зерновая".
        assert mock_bun.name == "Зерновая"

    #Тест получение цены булочки
    def test_get_price(self):
        # Создаем мок-объект булочки mock_bun
        mock_bun = Mock()
        # Присваиваем mock_bun.name значение, например "Зерновая".
        mock_bun.name = "Зерновая"
        # Присваиваем mock_bun.price значение цены, например 100.
        mock_bun.price = 100
        #Проверяем, что значение mock_bun.price равно 100.
        assert mock_bun.price == 100
