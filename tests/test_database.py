from unittest.mock import patch

from src.database import Database


@patch("src.database.Ingredient")
@patch("src.database.Bun")
def test_database_creates_expected_objects(mock_bun, mock_ingredient):
    db = Database()

    # Ожидается 3 вызова Bun и 6 вызовов Ingredient
    assert mock_bun.call_count == 3
    assert mock_ingredient.call_count == 6

    # Проверяем, что списки совпадают с возвращёнными значениями
    assert db.buns == [mock_bun.return_value] * 3
    assert db.ingredients == [mock_ingredient.return_value] * 6


@patch("src.database.Ingredient")
@patch("src.database.Bun")
def test_available_buns_returns_list_of_buns(mock_bun, mock_ingredient):
    db = Database()
    buns = db.available_buns()

    assert buns == db.buns
    assert all(b is mock_bun.return_value for b in buns)
    assert len(buns) == 3


@patch("src.database.Ingredient")
@patch("src.database.Bun")
def test_available_ingredients_returns_list_of_ingredients(mock_bun, mock_ingredient):
    db = Database()
    ingredients = db.available_ingredients()

    assert ingredients == db.ingredients
    assert all(i is mock_ingredient.return_value for i in ingredients)
    assert len(ingredients) == 6
