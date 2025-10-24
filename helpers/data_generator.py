from faker import Faker
import random
import string


class DataGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_user_data(self):
        """Генерация данных пользователя"""
        return {
            "email": self.fake.email(),
            "password": self.fake.password(length=10),
            "name": self.fake.first_name()
        }

    def generate_invalid_user_data(self, missing_field=None):
        """Генерация невалидных данных пользователя"""
        user_data = self.generate_user_data()
        if missing_field:
            user_data.pop(missing_field)
        return user_data

    def generate_random_hash(self, length=24):
        """Генерация случайного хеша"""
        characters = string.ascii_lowercase + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def generate_user_data(self):
        return {
            "email": self.fake.email(),
            "password": self.fake.password(length=10),
            "name": self.fake.first_name()
        }
