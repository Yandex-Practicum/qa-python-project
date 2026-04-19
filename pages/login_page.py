from pages.base_page import BasePage
from data.locators import LoginPageLocators


class LoginPage(BasePage):

    def open_login(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def login(self, email, password):

        self.wait_visible(LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.wait_visible(LoginPageLocators.PASSWORD_INPUT).send_keys(password)

        self.click(LoginPageLocators.SUBMIT_BUTTON)

    def wait_login_success(self):
        # ключевой момент
        self.wait.until(
            lambda d: "/login" not in d.current_url
        )