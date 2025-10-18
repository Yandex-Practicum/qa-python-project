import allure


class UrlHelper:
    def __init__(self, base_url="https://stellarburgers.nomoreparties.site/"):
        self.base_url = base_url

    @allure.step("Получить базовый URL")
    def get_base_url(self):
        return self.base_url.rstrip('/')

    @allure.step("Получить URL для страницы: {page_name}")
    def get_url(self, page_name):
        base = self.base_url.rstrip('/')
        urls = {
            "main": base + "/",
            "login": base + "/login",
            "register": base + "/register",
            "forgot-password": base + "/forgot-password",
            "reset-password": base + "/reset-password",
            "profile": base + "/account/profile",
            "feed": base + "/feed"
        }
        return urls.get(page_name, base)
