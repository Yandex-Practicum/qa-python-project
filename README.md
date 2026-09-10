Тестирование класса Burger

## Что было сделано
- Реализован класс `Burger` с методами:
  - `set_buns` — установка булочки
  - `add_ingredient` — добавление ингредиента
  - `remove_ingredient` — удаление ингредиента
  - `move_ingredient` — перемещение ингредиента
  - `get_price` — расчёт стоимости бургера
  - `get_receipt` — формирование чека

- Написаны юнит-тесты для класса `Burger` с использованием:
  - параметризации
  - моков — для классов `Bun` и `Ingredient`

-Достигнуто 100% покрытие кода тестами

Запуск тестов
pip install -r requirements.txt
pytest --cov=praktikum --cov-report=html