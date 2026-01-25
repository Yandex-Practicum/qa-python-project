from unittest.mock import Mock

# Мок булочки
mock_bun = Mock()
mock_bun.get_name.return_value = "Биргер"
mock_bun.get_price.return_value = 1700.0

# Моки ингредиентов
mock_ingredient1 = Mock()
mock_ingredient1.get_name.return_value = "Лапка"
mock_ingredient1.get_type.return_value = "main"
mock_ingredient1.get_price.return_value = 85.0

mock_ingredient2 = Mock()
mock_ingredient2.get_name.return_value = "Боус"
mock_ingredient2.get_type.return_value = "sauce"
mock_ingredient2.get_price.return_value = 1250.0
