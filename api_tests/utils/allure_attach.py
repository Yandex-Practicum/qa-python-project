import allure
import json


def attach_request_response(response):
    """Прикрепление данных запроса и ответа к Allure отчету"""
    allure.attach(
        f"URL: {response.request.url}\n"
        f"Method: {response.request.method}\n"
        f"Headers: {dict(response.request.headers)}\n"
        f"Body: {response.request.body}",
        name="Request Details",
        attachment_type=allure.attachment_type.TEXT
    )

    allure.attach(
        f"Status Code: {response.status_code}\n"
        f"Headers: {dict(response.headers)}\n"
        f"Body: {json.dumps(response.json(), indent=2, ensure_ascii=False)}",
        name="Response Details",
        attachment_type=allure.attachment_type.TEXT
    )
