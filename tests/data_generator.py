"""
Модуль для генерации тестовых данных
"""
import random
import string
from faker import Faker


class DataGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_email(self):
        return self.fake.email()

    def generate_password(self, length=10):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def generate_name(self):
        return self.fake.first_name()

    def generate_user_data(self):
        return {
            "email": self.generate_email(),
            "password": self.generate_password(),
            "name": self.generate_name()
        }

    def generate_random_hash(self, length=24):
        """Генерирует случайный хеш для тестирования невалидных ингредиентов"""
        characters = string.ascii_lowercase + string.digits
        return ''.join(random.choice(characters) for _ in range(length))
