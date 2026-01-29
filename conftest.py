import pytest
from bun import Bun
from burger import Burger
from utils import generate_random_string, generate_random_float


@pytest.fixture
def bun():
    name = generate_random_string(10)
    price = generate_random_float(10)
    return Bun(name, price)


@pytest.fixture
def burger():
    return Burger()
