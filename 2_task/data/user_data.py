from utils.helpers import random_email, random_password, random_name


def get_valid_user():
    return {
        "email": random_email(),
        "password": random_password(),
        "name": random_name()
    }
