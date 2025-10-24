import random
import string
import allure


class DataHelper:
    @staticmethod
    def generate_email():
        username = ''.join(random.choices(string.ascii_lowercase, k=8))
        domain = ''.join(random.choices(string.ascii_lowercase, k=6))
        return f"test_{username}@{domain}.com"

    @staticmethod
    def generate_password():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    @staticmethod
    def generate_name():
        return ''.join(random.choices(string.ascii_letters, k=10))

    @staticmethod
    @allure.step("Получить email тестового пользователя")
    def get_test_user_email():
        return "test_user_12345@example.com"

    @staticmethod
    @allure.step("Получить пароль тестового пользователя")
    def get_test_user_password():
        return "TestPassword123!"

    @staticmethod
    @allure.step("Сгенерировать данные пользователя")
    def generate_user_data():
        return {
            "email": DataHelper.generate_email(),
            "password": DataHelper.generate_password(),
            "name": DataHelper.generate_name()
        }
