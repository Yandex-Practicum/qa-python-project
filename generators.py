from faker import Faker

fake = Faker()

def generate_word():
    return fake.word()

def generate_price():
    return fake.random_int(min=1, max=1000)