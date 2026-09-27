import random
import string


def generate_unique_email():
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"test_user_{random_part}@yandex.ru"