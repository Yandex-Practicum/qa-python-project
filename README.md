## Задание 1: Юнит-тесты Stellar Burgers (100% покрытие)

### Описание

Юнит-тесты для класса `Burger` — программы сборки бургера в Stellar Burgers
Тестируем логику изолированно: моки для `Bun` и `Ingredient`, параметризация для разных сценариев

### Что тестируем

`__init__` - пустой бургер: `bun is None`, нет ингредиентов 
`set_buns` - булочка сохраняется в объект 
`add_ingredient` - ингредиенты добавляются в конец списка 
`remove_ingredient` - удаление по индексу 
`move_ingredient` - перемещение слоя, проверка порядка 
`get_price` - 2 × булочка + сумма ингредиентов 
`get_receipt` - формат чека и итоговая цена 



### Установка и запуск

Как проверить покрытие 100%

1. Установить зависимости (из корня проекта Diplom_1):

   pip install -r requirements.txt

2. Запустить тесты с отчётом о покрытии:

   pytest --cov=praktikum.burger --cov-report=term-missing --cov-report=html tests/burger_test.py


4. Открыть HTML-отчёт:
   - после команды выше создаётся папка htmlcov/
   - открыть файл htmlcov/index.html в браузере
   - файл praktikum/burger.py должен быть полностью зелёным (100%)

5. Запуск с Allure:

   pytest tests/burger_test.py --alluredir=allure_results


### Технологии

- pytest, pytest-cov, allure-pytest
- unittest.mock (Mock)
