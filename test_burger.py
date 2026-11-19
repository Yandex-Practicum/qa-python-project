import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

### ======================
### ФИКСТУРЫ
### ======================

@pytest.fixture
def burger():
    #Создает чистый бургер перед каждым тестом
    return Burger()

@pytest.fixture
def mock_bun():
    #Создает мок булочки с заданными параметрами
    bun = Mock()
    bun.get_name.return_value = "Тестовая булка"
    bun.get_price.return_value = 1255.0
    return bun

@pytest.fixture
def mock_ingredient():
    #Создает мок ингредиента с заданными параметрами
    ingredient = Mock()
    ingredient.get_name.return_value = "Тестовый ингредиент"
    ingredient.get_price.return_value = 3000.0
    ingredient.get_type.return_value = "FILLING" # Тип: начинка
    return ingredient

# --- ТЕСТЫ ---

# 1. Тестируем set_buns
def test_set_buns(burger, mock_bun):
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun

# 2. Тестируем add_ingredient
def test_add_ingredient(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == mock_ingredient

# 3. Тестируем remove_ingredient
def test_remove_ingredient(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0

# 4. Тестируем move_ingredient 
def test_move_ingredient(burger):
    ing1 = Mock()
    ing1.get_name.return_value = "Ing1"
    ing2 = Mock()
    ing2.get_name.return_value = "Ing2"
    
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    
    # Меняем местами 
    burger.move_ingredient(0, 1)
    
    assert burger.ingredients[0].get_name() == "Ing2"
    assert burger.ingredients[1].get_name() == "Ing1"

# 5. Тестируем get_price 
@pytest.mark.parametrize("bun_price, ing_price, expected_price", [
    (100.0, 50.0, 250.0),  # Булочка * 2 (200) + Ингредиент (50) = 250
    (200.0, 0.0, 400.0),   # Булочка * 2 (400) + Ингредиент (0) = 400
    (0.0, 100.0, 100.0),   # Булочка * 2 (0) + Ингредиент (100) = 100
])
def test_get_price(burger, bun_price, ing_price, expected_price):
    bun = Mock()
    bun.get_price.return_value = bun_price
    
    ingredient = Mock()
    ingredient.get_price.return_value = ing_price
    
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    
    assert burger.get_price() == expected_price

# 6. Тестируем get_receipt
def test_get_receipt(burger, mock_bun, mock_ingredient):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    
    # Ожидаемый текст чека
    expected_receipt = (
        '(==== Тестовая булка ====)\n'
        '= filling Тестовый ингредиент =\n'
        '(==== Тестовая булка ====)\n'
        '\n'
        'Price: 5510.0'
    )
    
    assert burger.get_receipt() == expected_receipt