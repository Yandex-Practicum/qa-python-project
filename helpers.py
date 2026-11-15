import random


def random_price_int():
    return random.randint(10, 1000)

def random_price_float():
    return round(random.uniform(10.0, 1000.0), 2)
