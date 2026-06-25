Проект содержит юнит-тесты для класса Burger.

Проверяются методы:
- set_buns
- add_ingredient
- remove_ingredient
- move_ingredient
- get_price
- get_receipt

В тестах используются:
- pytest
- pytest-cov
- unittest.mock.Mock
- pytest.mark.parametrize

Запуск тестов:

python -m pytest -v

Проверка покрытия класса Burger:

python -m pytest --cov=praktikum.burger --cov-report=term-missing