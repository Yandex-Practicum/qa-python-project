import pytest


def get_bun_test_data():
    """Тестовые данные для булочек"""
    return [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
        ("special bun", 150.5),
        ("", 0),
        ("test bun", 0),
    ]


def get_bun_expected_data():
    """Ожидаемые данные булочек из базы"""
    return [
        {"name": "black bun", "price": 100},
        {"name": "white bun", "price": 200},
        {"name": "red bun", "price": 300},
    ]