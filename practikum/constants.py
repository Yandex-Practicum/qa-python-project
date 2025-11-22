from practikum.bun import Bun
from practikum.ingredient import Ingredient
from practikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


#данные для Bun
H_BUNS = [                      #тестовые данные для параметризации Bun
    ("plasma bun", 250.0),
    ("ice bun", 100.0)
]
#данные для Burger
#Данные для тестового бургера
TB_NAME_BUN = "ice bun"
TB_PRICE_BUN = 100.0
TB_ING_CHEESE_PRICE = 33.0
TB_ING_CHEESE_NAME = "star cheese"
TB_ING_SAUSE_NAME = "hot plasma"
TB_ING_SAUSE_PEICE = 22.0
TB_ING_CUTLET_NAME = "space octopus"
TB_ING_CUTLET_PRICE = 111.0

#ожидаемый результат для вывода чека и состава бургера с тестовыми данными
EXPECTED_RECEIPT = (
    "(==== ice bun ====)\n"
    "= filling star cheese =\n"
    "= filling space octopus =\n"
    "= sauce hot plasma =\n"
    "(==== ice bun ====)\n"
    "\n"
    f"Price: {(TB_PRICE_BUN * 2) + TB_ING_CHEESE_PRICE + TB_ING_CUTLET_PRICE + TB_ING_SAUSE_PEICE}"
)

#данные для Ingredients

H_INGREDIENTS = [                    #тестовые данные для параметризации ингредиентов
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 40.0),
    (INGREDIENT_TYPE_FILLING, "onion", 15.0),
    (INGREDIENT_TYPE_SAUCE, "ketchup", 20.0),
    (INGREDIENT_TYPE_FILLING, "cheese", 35.0)]


#данные для Database
#данные, которые содержатся в исходной Database
H_DB_BUNS = [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
        ]
#данные, которые содержатся в исходной Database
H_DB_INGREDIENTS = [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),

    (INGREDIENT_TYPE_FILLING, "cutlet", 100),
    (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    (INGREDIENT_TYPE_FILLING, "sausage", 300)
    ]
#Мок данные для теста Database
H_DB =[
    ([Bun("rise bun", 50),
      Bun("rye bun", 75)],
     [Ingredient(INGREDIENT_TYPE_SAUCE, "cheese sauce", 30.0),
      Ingredient(INGREDIENT_TYPE_FILLING, "mayo", 20.0)]
     ),
    (
        [Bun("red bun", 350)], # мокированные данные, одноименные с исходными
        [Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 25.0)]
    )
    ]
