from random import choice, randrange
from string import ascii_uppercase


mock_bun_name = ''.join(choice(ascii_uppercase) for b in range(10))
mock_ingredient_name = ''.join(choice(ascii_uppercase) for i in range(10))
mock_bun_price = randrange(100, 1000)
mock_ingredient_price = randrange(100, 1000)

