from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_TAB = (By.XPATH, "//a[@href='/']")
    FEED_TAB = (By.XPATH, "//a[contains(@href,'/feed')]")

    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")
    FEED_TITLE = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")

class ConstructorPageLocators:
    INGREDIENT = (By.XPATH, "(//a[contains(@href,'ingredient')])[1]")
    COUNTER = (By.XPATH, "(//a[contains(@href,'ingredient')])[1]//p")
    BASKET = (By.XPATH, "//section[contains(@class,'BurgerConstructor_basket')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    TOTAL_PRICE = (By.XPATH, "//div[contains(@class,'BurgerConstructor_basket__totalContainer_')]//p[contains(@class,'text')]")

class ModalLocators:
    MODAL = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]")
    CLOSE = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")

class OrderModalLocators:
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class,'Modal_modal__title_shadow')]")
    CLOSE = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")

class FeedPageLocators:
    TOTAL_DONE = (By.XPATH, "//p[contains(text(),'Выполнено за все время')]/following-sibling::p")
    TODAY_DONE = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p")
    ORDER_ITEMS = (By.XPATH,"//div[contains(@class,'OrderFeed_orderStatusBox')]//ul[contains(@class,'OrderFeed_orderListReady')]//li")

class LoginPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")