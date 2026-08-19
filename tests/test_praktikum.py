import builtins
from unittest.mock import Mock, call

import praktikum


def _prepare_main_dependencies(monkeypatch):
    fake_buns = [Mock(name="bun_0"), Mock(name="bun_1")]
    fake_ingredients = [Mock(name=f"ingredient_{index}") for index in range(6)]
    fake_database = Mock(
        available_buns=Mock(return_value=fake_buns),
        available_ingredients=Mock(return_value=fake_ingredients),
    )
    fake_burger = Mock()
    fake_burger.get_receipt = Mock(return_value="test receipt")

    database_ctor = Mock(return_value=fake_database)
    burger_ctor = Mock(return_value=fake_burger)
    print_mock = Mock()

    monkeypatch.setattr(praktikum, "Database", database_ctor)
    monkeypatch.setattr(praktikum, "Burger", burger_ctor)
    monkeypatch.setattr(builtins, "print", print_mock)

    return {
        "database_ctor": database_ctor,
        "burger_ctor": burger_ctor,
        "database": fake_database,
        "burger": fake_burger,
        "buns": fake_buns,
        "ingredients": fake_ingredients,
        "print_mock": print_mock,
    }


def test_main_requests_buns_and_ingredients_from_database(monkeypatch):
    deps = _prepare_main_dependencies(monkeypatch)

    praktikum.main()

    deps["database_ctor"].assert_called_once_with()
    deps["database"].available_buns.assert_called_once_with()
    deps["database"].available_ingredients.assert_called_once_with()


def test_main_sets_first_bun_from_database(monkeypatch):
    deps = _prepare_main_dependencies(monkeypatch)

    praktikum.main()

    deps["burger"].set_buns.assert_called_once_with(deps["buns"][0])


def test_main_adds_expected_ingredients(monkeypatch):
    deps = _prepare_main_dependencies(monkeypatch)

    praktikum.main()

    deps["burger"].add_ingredient.assert_has_calls(
        [
            call(deps["ingredients"][1]),
            call(deps["ingredients"][4]),
            call(deps["ingredients"][3]),
            call(deps["ingredients"][5]),
        ]
    )


def test_main_moves_and_removes_ingredient(monkeypatch):
    deps = _prepare_main_dependencies(monkeypatch)

    praktikum.main()

    deps["burger"].move_ingredient.assert_called_once_with(2, 1)
    deps["burger"].remove_ingredient.assert_called_once_with(3)


def test_main_prints_burger_receipt(monkeypatch):
    deps = _prepare_main_dependencies(monkeypatch)

    praktikum.main()

    deps["burger"].get_receipt.assert_called_once_with()
    deps["print_mock"].assert_called_once_with("test receipt")
