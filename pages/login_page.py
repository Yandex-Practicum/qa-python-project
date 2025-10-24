import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()

    @allure.step("Открыть страницу логина")
    def open(self):
        return self.open_page("login")

    @allure.step("Ввести email: {email}")
    def enter_email(self, email):
        self.type_text(self.locators.EMAIL_INPUT, email)
        return self

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.type_text(self.locators.PASSWORD_INPUT, password)
        return self

    @allure.step("Кликнуть кнопку 'Войти'")
    def click_login_button(self):
        self.click(self.locators.LOGIN_BUTTON)
        return self.wait_for_page_loaded()

    @allure.step("Выполнить полный логин")
    def complete_login(self, email, password):
        return (self.enter_email(email)
                .enter_password(password)
                .click_login_button())

    @allure.step("Проверить наличие формы логина")
    def is_login_form_present(self):
        return self.is_visible(self.locators.LOGIN_FORM)
