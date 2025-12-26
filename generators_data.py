from random import choice, randrange
from string import ascii_uppercase


def generate_random_bun_name(length=8):
    return ''.join(choice(ascii_uppercase) for _ in range(length))

def generate_random_ingredient_name(length=10):
    return ''.join(choice(ascii_uppercase) for _ in range(length))

def generate_random_bun_price(min_price=8, max_price=888):
    return randrange(min_price, max_price)

def generate_random_ingredient_price(min_price=4, max_price=444):
    return randrange(min_price, max_price)

bun_name = generate_random_bun_name() #переменная для генерации случайного имени булочки
ingredient_name = generate_random_ingredient_name()# переменная для генереции случкйного имени ингредиента
bun_price = generate_random_bun_price()# переменная для генерации случайной цены булочки 
ingredient_price = generate_random_ingredient_price()# переменная для генерации случаной цены ингредиента

