## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам. Например, `bun_test.py`, `burger_test.py` и т.д.

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`

<center>

# Список и структура тестов
</center>

## - bun.py
### Список проверок
1. Конструктор <br>
    1.1 Инициализация name <br>
        - str (англ, русс) <br>
        - int <br>
    1.2 Инициализация price<br>
        - float (0, не 0) <br>
        - int (0, не 0) str
2. get_name(self) -> str <br>
   - Возврат name <br>
3. get_price(self) -> float
   - Возврат price <br>
### Список тестов
1. test_get_name_success()
2. test_get_price_success()

## - burger.py
### Список проверок
1. set_buns(self, bun: Bun) - (встроенные методы - МОК) <br>
   - Выбор булки
2. add_ingredient(self, ingredient: Ingredient) - (встроенные методы - МОК) <br>
   - Добавление ингредиента
3. remove_ingredient(self, index: int) - (встроенные методы - МОК) <br>
   - Удаление ингредиента
4. move_ingredient(self, index: int, new_index: int) - (встроенные методы - МОК)
   - Перемещение ингредиента
5. get_price(self) -> float - (встроенные методы - МОК) <br>
   - Получение цены бургера
     - есть ингредиенты
       - несколько ингр., цена не 0, float
       - один ингр., цена не 0, int
       - нет булки
     - нет ингредиентов
       - только булка
       - нет ингр., нет булки
6. get_receipt(self) -> str - (Встроенные методы МОК)
   - Получение чека
      - булка русс., один ингр. русс.
      - булка англ., несколько ингредиентов англ.

### Список тестов
1. test_set_buns_success()
2. test_add_ingredient_success()
3. test_remove_ingredient_success()
3. test_move_ingredient_success()
4. test_get_price_success()
5. test_get_receipt_success()

## - ingredient.py
### Список проверок
1. Конструктор <br>
    1.1 Инициализация ingredient_type <br>
        - str, русс\англ <br>
        - int <br>
    1.2 Инициализация name<br>
        - float <br>
        - str, русс\англ <br>
    1.3 Инициализация price<br>
        - float <br>
        - int
2. get_price(self) -> float <br>
   - Возврат price <br>
3. get_name(self) -> str
   - Возврат name <br>
3. get_type(self) -> str
   - Возврат type <br>
### Список тестов
1. test_get_price_success()
2. test_get_name_success()
2. test_get_type_success()
