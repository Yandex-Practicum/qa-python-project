from uuid import uuid4


def generate_user_data():
    unique_part = uuid4().hex
    return {
        "email": f"qa_baydashev_{unique_part}@yandex.ru",
        "password": f"Pwd_{unique_part[:12]}",
        "name": "Dmitry",
    }

