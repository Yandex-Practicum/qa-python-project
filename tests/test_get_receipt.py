from unittest.mock import patch
import pytest
from tests.data import Credentials
from praktikum.burger import Burger


class TestGetReceipt:
   
    '''Проверяется метод получения рецепта на бургер
    def get_receipt(self) -> str:
        receipt: List[str] = [f'(==== {self.bun.get_name()} ====)']

        for ingredient in self.ingredients:
            receipt.append(f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =')

        receipt.append(f'(==== {self.bun.get_name()} ====)\n')
        receipt.append(f'Price: {self.get_price()}')

        return '\n'.join(receipt)
    ''' 
  
    @pytest.mark.parametrize("bun_name, ingredients_data, mock_price, expected_receipt", Credentials.receipt_data)
    @patch('praktikum.burger.Burger.get_price')
    def test_get_receipt(self, mock_get_price, bun_name, ingredients_data, mock_price, expected_receipt, create_mock_burger):

        burger = create_mock_burger(bun_name, ingredients_data)        
        mock_get_price.return_value = mock_price
        receipt = burger.get_receipt()

        assert receipt == expected_receipt
        