from unittest.mock import Mock

# Мок булочки
mock_bun = Mock()
mock_bun.get_name.return_value = "Новая булка V-1"
mock_bun.get_price.return_value = 1111.0

# Моки ингредиентов
mock_ingredient1 = Mock()
mock_ingredient1.get_name.return_value = "Мясо krevetka"
mock_ingredient1.get_type.return_value = "main"
mock_ingredient1.get_price.return_value = 53.0

mock_ingredient2 = Mock()
mock_ingredient2.get_name.return_value = "Соус krevetka"
mock_ingredient2.get_type.return_value = "sauce"
mock_ingredient2.get_price.return_value = 113.0