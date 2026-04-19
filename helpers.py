import random
import requests
from data.urls import BASE_URL, REGISTER, LOGIN, USER


def generate_user():
    number = random.randint(10000, 99999)
    return {
        "email": f"user{number}@mail.com",
        "password": "Password123",
        "name": f"User{number}"
    }


def create_user(payload):
    return requests.post(BASE_URL + REGISTER, json=payload)


def login_user(email, password):
    return requests.post(
        BASE_URL + LOGIN,
        json={
            "email": email,
            "password": password
        }
    )


def delete_user(token):
    requests.delete(
        BASE_URL + USER,
        headers={"Authorization": token}
    )