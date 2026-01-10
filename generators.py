from random import choice, randrange
from string import ascii_uppercase

# переменная для генерации рандомного имени булки;
bun_name = ''.join(choice(ascii_uppercase) for b in range(10))
# переменная для генерации рандомного имени ингредиента;
ingredient_name = ''.join(choice(ascii_uppercase) for i in range(10))
# переменная для генерации рандомной цены булки;
bun_price = randrange(100, 1000)
# переменная для генерации рандомной цены ингредиента;
ingredient_price = randrange(100, 1000)
