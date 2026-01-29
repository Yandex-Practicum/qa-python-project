import random
import allure

@allure.step('Генерация рандомной цены')
def generate_float_price():
    return round(random.uniform(0, 99), 2)