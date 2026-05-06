import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_price.return_value = 988
    bun.get_name.return_value = "Флюоресцентная булка"
    return bun

@pytest.fixture
def mock_ingredients():

    ing1 = Mock()
    ing1.get_price.return_value = 3000
    ing1.get_name.return_value = "Говяжий метеорит"
    ing1.get_type.return_value = "FILLING"

    ing2 = Mock()
    ing2.get_price.return_value = 15
    ing2.get_name.return_value = "Соус традиционный галактический"
    ing2.get_type.return_value = "SAUCE"

    ing3 = Mock()
    ing3.get_price.return_value = 4400
    ing3.get_name.return_value = "Мини-салат Экзо-Плантаго"
    ing3.get_type.return_value = "FILLING"

    ing4 = Mock()
    ing4.get_price.return_value = 4142
    ing4.get_name.return_value = "Сыр с астероидной плесенью"
    ing4.get_type.return_value = "FILLING"

    return [ing1, ing2, ing3, ing4]