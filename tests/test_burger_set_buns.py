import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from tests.data import TestData


class TestBurgerSetBuns:
    """Тесты для метода set_buns класса Burger"""
    
    def test_set_buns_success(self, sample_burger, mock_bun):
        """Тест успешной установки булочки"""
        sample_burger.set_buns(mock_bun)
        assert sample_burger.bun == mock_bun

    def test_set_buns_replace_existing(self, sample_burger, mock_bun):
        """Тест замены существующей булочки"""
        bun_mock1 = Mock(spec=Bun)
        bun_mock2 = Mock(spec=Bun)
        
        sample_burger.set_buns(bun_mock1)
        sample_burger.set_buns(bun_mock2)
        
        assert sample_burger.bun == bun_mock2