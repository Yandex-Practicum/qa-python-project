from praktikum.database import Database


def test_database_available_buns():
    db = Database()
    assert len(db.available_buns()) > 0


def test_database_available_ingredients():
    db = Database()
    assert len(db.available_ingredients()) > 0
