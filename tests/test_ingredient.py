import pytest

class TestIngredient:

    def test_ingredient_get_type_return_correct_type(self, mock_ingredient_data):
   
        assert mock_ingredient_data.get_type() == "начинка"

    def test_ingredient_get_name_return_correct_name(self, mock_ingredient_data):
 
        assert mock_ingredient_data.get_name() == "Котлета"

    def test_ingredient_get_price_return_correct_price(self, mock_ingredient_data):
  
        assert mock_ingredient_data.get_price() == 250