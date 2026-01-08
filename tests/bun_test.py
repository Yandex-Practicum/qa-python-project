import pytest
from unittest.mock import Mock
from praktikum.bun import Bun


class TestBun:
    
    @pytest.mark.parametrize("name", [
        "black bun",
        "white bun", 
        "red bun",
        "",
        "special bun"
    ])
    def test_get_name_returns_correct_value_for_different_buns(self, name):
        bun = Bun(name, 100.0)
        
        result = bun.get_name()
        
        assert result == name
    
    @pytest.mark.parametrize("price", [
        100.0,
        200.0,
        300.0,
        0.0,
        999.99
    ])
    def test_get_price_returns_correct_value_for_different_prices(self, price):

        bun = Bun("test bun", price)
        
        result = bun.get_price()
        
        assert result == price
    
    def test_bun_creation_sets_name_attribute(self):
        bun = Bun("black bun", 100.0)
        
        assert bun.name == "black bun"
    
    def test_bun_creation_sets_price_attribute(self):
        bun = Bun("black bun", 100.0)
        
        assert bun.price == 100.0
    
    def test_mock_bun_get_name_returns_mocked_value(self):
        mock_bun = Mock(spec=Bun)
        expected_name = "mock bun"
        mock_bun.get_name.return_value = expected_name
        
        result = mock_bun.get_name()
        
        assert result == expected_name
        mock_bun.get_name.assert_called_once()
    
    def test_mock_bun_get_price_returns_mocked_value(self):
        mock_bun = Mock(spec=Bun)
        expected_price = 150.0
        mock_bun.get_price.return_value = expected_price
        
        result = mock_bun.get_price()
        
        assert result == expected_price
        mock_bun.get_price.assert_called_once()