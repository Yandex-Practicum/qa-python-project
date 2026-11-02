import pytest

from database import Database


class TestDatabase:
    @pytest.mark.parametrize(
        "method, expected_names",
        [
            ("available_buns", ["black bun", "white bun", "red bun"]),
            ("available_ingredients",
            ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]),
        ],
    )
    def test_database_contents(self, method, expected_names):
        database = Database()
        items = getattr(database, method)()
        
        assert len(items) == len(expected_names)
        assert [i.get_name() for i in items] == expected_names