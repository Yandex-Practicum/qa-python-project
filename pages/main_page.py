from pages.base_page import BasePage
from data.locators import MainPageLocators


class MainPage(BasePage):

    def go_to_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_TAB)

    def go_to_feed(self):
        self.click(MainPageLocators.FEED_TAB)

    def is_open(self):
        return self.wait_visible(MainPageLocators.CONSTRUCTOR_TITLE).is_displayed()