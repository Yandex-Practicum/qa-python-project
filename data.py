from practicum.ingredient_types import INGREDIENT_TYPE_SAUCE


BUN_DATA = {
    'Флюоресцентная булка R2-D3': 988,
    'Краторная булка N-200i': 1255
    }
SAUCE_DATA = {
    'Соус Spicy-X': 90, 
    'Соус фирменный Space Sauce': 80, 
    'Соус традиционный галактический': 15, 
    'Соус с шипами Антарианского плоскоходца': 88
    }
FILLING_NAMES = {
    'Мясо бессмертных моллюсков Protostomia': 1337, 
    'Говяжий метеорит (отбивная)': 3000, 
    'Биокотлета из марсианской Магнолии': 424,
    'Филе Люминесцентного тетраодонтимформа': 988, 
    'Хрустящие минеральные кольца': 300, 
    'Плоды Фалленианского дерева': 874, 
    'Кристаллы марсианских альфа-сахаридов': 762,
    'Мини-салат Экзо-Плантаго': 4400, 
    'Сыр с астероидной плесенью': 4142
    }

BURGER_PRICE = (BUN_DATA[list(BUN_DATA.keys())[0]] * 2) + SAUCE_DATA[list(SAUCE_DATA.keys())[0]]
BURGER_FULL_RECEIPT = ('(==== '+list(BUN_DATA.keys())[0]+' ====)\n'
                       '= '+INGREDIENT_TYPE_SAUCE.lower()+' '+list(SAUCE_DATA.keys())[0]+' =\n'
                       '(==== '+list(BUN_DATA.keys())[0]+' ====)\n\n'
                       'Price: '+str(BURGER_PRICE))