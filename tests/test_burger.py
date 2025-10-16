import pytest

from ..burger import Burger
from ..bun import Bun
from ..ingredient import Ingredient
from ..ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.fixture
def sample_bun():
    return Bun("Classik", 100.0)


@pytest.fixture
def sample_filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, "cheese", 25.0)


@pytest.fixture
def sample_sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 10.0)

@pytest.fixture
def burger():
    return Burger()


def test_burger_constructor(burger):
    """Test Burger constructor."""
    assert burger.bun is None
    assert burger.ingredients == []
    assert isinstance(burger.ingredients, list)


def test_burger_set_buns(burger, sample_bun):
    """Test setting buns for the burger."""
    burger.set_buns(sample_bun)
    assert burger.bun == sample_bun


def test_burger_add_ingredient(burger, sample_filling, sample_sauce):
    """Test adding ingredients to the burger."""
    burger.add_ingredient(sample_filling)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == sample_filling
    
    burger.add_ingredient(sample_sauce)
    assert len(burger.ingredients) == 2
    assert burger.ingredients[1] == sample_sauce


def test_burger_remove_ingredient(burger, sample_filling, sample_sauce):
    """Test removing ingredients from the burger."""
    burger.add_ingredient(sample_filling)
    burger.add_ingredient(sample_sauce)
    
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == sample_sauce


def test_burger_move_ingredient(burger, sample_filling, sample_sauce):
    """Test moving ingredients within the burger."""
    burger.add_ingredient(sample_filling)
    burger.add_ingredient(sample_sauce)
    
    # Move sauce to the first position (index 1 to index 0)
    burger.move_ingredient(1, 0)
    
    assert burger.ingredients[0] == sample_sauce
    assert burger.ingredients[1] == sample_filling


def test_burger_get_price(burger, sample_bun, sample_filling, sample_sauce):
    """Test calculating the price of the burger."""
    
    # Test price with just bun
    burger.set_buns(sample_bun)
    assert burger.get_price() == 200.0  # 100 * 2
    
    # Test price with bun and one ingredient
    burger.add_ingredient(sample_filling)
    assert burger.get_price() == 225.0  # 200 + 25
    
    # Test price with bun and multiple ingredients
    burger.add_ingredient(sample_sauce)
    assert burger.get_price() == 235.0  # 200 + 25 + 10


def test_burger_get_receipt(burger, sample_bun, sample_filling, sample_sauce):
    """Test generating the receipt for the burger."""
    
    # Test receipt with bun and ingredients
    burger.set_buns(sample_bun)
    burger.add_ingredient(sample_filling)
    burger.add_ingredient(sample_sauce)
    
    receipt = burger.get_receipt()
    assert "(==== Classik ====)" in receipt
    assert "= filling cheese =" in receipt
    assert "= sauce ketchup =" in receipt
    assert "Price: 235.0" in receipt
    assert isinstance(receipt, str)