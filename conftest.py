from typing import List
import pytest
from bun import Bun
from burger import Burger
from database import Database
from ingredient import Ingredient


@pytest.fixture(scope="function")
def things():
    database: Database = Database()
    buns: List[Bun] = database.available_buns()
    ingredients: List[Ingredient] = database.available_ingredients()
    burger: Burger = Burger()
    return buns, ingredients, burger
