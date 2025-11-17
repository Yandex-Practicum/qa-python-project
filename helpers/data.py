from unittest.mock import Mock

mock_bun = Mock()
mock_bun.get_name.return_value = 'Булка'
mock_bun.get_price.return_value = 100

mock_filling = Mock()
mock_filling.get_name.return_value = 'Котлета'
mock_filling.get_type.return_value = "main"
mock_filling.get_price.return_value = 20

mock_sauce = Mock()
mock_sauce.get_name.return_value = 'Кетчуп'
mock_sauce.get_type.return_value = "sauce"
mock_sauce.get_price.return_value = 1