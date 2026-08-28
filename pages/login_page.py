import allure

from locators import LoginPageLocators, MainPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def wait_loaded(self):
        self.wait_page_loaded(LoginPageLocators.EMAIL_INPUT, "/login")

    @allure.step("Войти под тестовым пользователем")
    def login(self, email, password):
        self.wait_loaded()
        self.find_visible(LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.find_visible(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.click(LoginPageLocators.LOGIN_BUTTON)
        self.wait_url("/")
        self.find_visible(MainPageLocators.PAGE_TITLE)
