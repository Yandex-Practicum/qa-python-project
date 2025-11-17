## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers


В этом проекте протестирован класс `Burger` из приложения Stellar Burgers.

Тесты находятся в каталоге:

```

tests/test_burger.py

````

В тестах используются:

- `pytest`
- `pytest-cov`
- `unittest.mock.MagicMock`
- параметризация `@pytest.mark.parametrize`
- фикстуры (`@pytest.fixture`)

Покрытие выполняется **только файла burger.py**.


---

## Установка зависимостей

```bash
pip install -r requirements.txt
````

---

## Запуск тестов

```bash
pytest -v
```

---

## Запуск тестов с покрытием только для burger.py

```bash
pytest --cov=prakticum/burger.py --cov-report=term-missing -v
```

После выполнения покрытие должно быть 100%.

---

## Ожидаемый вывод (пример)

```
Burger ... PASSED
---------------------------------------
prakticum/burger.py      100%
---------------------------------------

