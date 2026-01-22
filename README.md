Задание 1: Юнит-тесты
Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Burger`
Класс `Burger` покрыт на 100% — согласно отчёту `htmlcov/index.html`.
Name                            Stmts   Miss  Cover
---------------------------------------------------
praktikum\bun.py                    8      1    88%
praktikum\burger.py                27      0   100%
praktikum\database.py              21     21     0%
praktikum\ingredient.py            11      2    82%
praktikum\ingredient_types.py       2      0   100%
praktikum\praktikum.py             20     20     0%
---------------------------------------------------
TOTAL                              89     44    51%


Проверены:

Установка булочки (set_buns)
Добавление ингредиентов (add_ingredient)
Удаление ингредиентов по индексу (remove_ingredient)
Перемещение ингредиентов (move_ingredient)
Расчёт итоговой стоимости (get_price)
Формирование чека (get_receipt) — здесь использован unittest.mock.Mock

DIPLOM_1/
├── htmlcov/          # Отчет о покрытии
├── praktikum/        # Основной код приложения
│   ├── __init__.py
│   ├── bun.py
│   ├── burger.py
│   ├── database.py
│   ├── ingredient.py
│   ├── ingredient_types.py
│   └── praktikum.py
├── tests/            # Тесты
│   ├── __init__.py
│   └── test_burger.py
├── .gitignore
├── README.md         # описание проекта
└── requirements.txt  # Зависимости



Установка зависимостей
> `$ pip install -r requirements.txt`

Запуск автотестов и создание HTML-отчета о покрытии
>  `$ pytest --cov=praktikum --cov-report=html`

Примечание
Bun и Ingredient — простые объекты данных без побочных эффектов, поэтому в большинстве тестов они используются «как есть».
Мок применяется только в тесте get_receipt(), чтобы изолировать форматирование чека от реализации других классов и гарантировать, что тест проверяет именно логику вывода, а не работу зависимостей.
