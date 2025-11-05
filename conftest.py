import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_bun():
    mock = Mock(spec=Bun)
    mock.get_name.return_value = "Краторная булка N-200i"
    mock.get_price.return_value = 1255
    return mock


@pytest.fixture
def mock_ingredient():
    return Mock(spec=Ingredient)


@pytest.fixture
def sample_burger():
    from praktikum.burger import Burger
    burger = Burger()
    
    bun = Mock(spec=Bun)
    bun.get_price.return_value = 1255
    bun.get_name.return_value = "Краторная булка N-200i"
    
    ingredient1 = Mock(spec=Ingredient)
    ingredient1.get_price.return_value = 3000
    ingredient1.get_name.return_value = "Говяжий метеорит (отбивная)"
    ingredient1.get_type.return_value = INGREDIENT_TYPE_FILLING
    
    ingredient2 = Mock(spec=Ingredient)
    ingredient2.get_price.return_value = 90
    ingredient2.get_name.return_value = "Соус Spicy-X"
    ingredient2.get_type.return_value = INGREDIENT_TYPE_SAUCE
    
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    
    return burger


@pytest.fixture
def russian_ingredients_data():
    return {
        "buns": [
            ("Краторная булка N-200i", 1255),
            ("Флюоресцентная булка R2-D3", 988)
        ],
        "sauces": [
            ("Соус Spicy-X", 90),
            ("Соус фирменный Space Sauce", 80),
            ("Соус традиционный галактический", 15),
            ("Соус с шипами Антарианского плоскоходца", 88)
        ],
        "fillings": [
            ("Мясо бессмертных моллюсков Protostomia", 1337),
            ("Говяжий метеорит (отбивная)", 3000),
            ("Биокотлета из марсианской Магнолии", 424),
            ("Филе Люминесцентного тетраодонтимформа", 988),
            ("Хрустящие минеральные кольца", 300),
            ("Плоды Фалленианского дерева", 874),
            ("Кристаллы марсианских альфа-сахаридов", 762),
            ("Мини-салат Экзо-Плантаго", 4400),
            ("Сыр с астероидной плесенью", 4142)
        ]
    }