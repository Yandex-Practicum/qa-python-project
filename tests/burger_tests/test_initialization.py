import pytest
from unittest.mock import Mock
from burger import Burger
from bun import Bun

class TestBurgerInitialization:
    
    def setup_method(self):
        self.burger = Burger()
    
    def test_initial_burger_has_no_bun(self):
        assert self.burger.bun is None
    
    def test_initial_burger_has_empty_ingredients(self):
        assert self.burger.ingredients == []
    
    def test_set_buns_sets_bun_correctly(self):
        mock_bun = Mock(spec=Bun)
        self.burger.set_buns(mock_bun)
        assert self.burger.bun == mock_bun