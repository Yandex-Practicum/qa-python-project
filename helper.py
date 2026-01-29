import random


def get_random_bun(dbs):
    return random.choice(dbs.available_buns())


def get_random_ingredient(dbs):
    return random.choice(dbs.available_ingredients())
