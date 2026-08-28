from selenium.webdriver.common.by import By


class HeaderLocators:
    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//a[@href='/' and .//p[normalize-space()='Конструктор']]",
    )
    ORDER_FEED_LINK = (
        By.XPATH,
        "//a[@href='/feed' and .//p[normalize-space()='Лента Заказов']]",
    )


class LoginPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "form input[type='text']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "form input[type='password']")
    LOGIN_BUTTON = (By.XPATH, "//form//button[normalize-space()='Войти']")


class MainPageLocators:
    PAGE_TITLE = (By.XPATH, "//h1[normalize-space()='Соберите бургер']")
    FIRST_BUN = (
        By.CSS_SELECTOR,
        "a[href='/ingredient/61c0c5a71d1f82001bdaaa6d']",
    )
    FIRST_FILLING = (
        By.CSS_SELECTOR,
        "a[href='/ingredient/61c0c5a71d1f82001bdaaa6f']",
    )
    FIRST_FILLING_COUNTER = (
        By.CSS_SELECTOR,
        "a[href='/ingredient/61c0c5a71d1f82001bdaaa6f'] "
        "[class*='counter_counter__num']",
    )
    CONSTRUCTOR_BASKET = (
        By.CSS_SELECTOR,
        "section[class*='BurgerConstructor_basket']",
    )
    ORDER_BUTTON = (By.XPATH, "//button[normalize-space()='Оформить заказ']")
    ORDER_NUMBER = (
        By.CSS_SELECTOR,
        "section[class*='Modal_modal_opened'] .text_type_digits-large",
    )


class IngredientModalLocators:
    MODAL = (By.CSS_SELECTOR, "section[class*='Modal_modal_opened']")
    TITLE = (By.XPATH, "//h2[normalize-space()='Детали ингредиента']")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button[class*='Modal_modal__close']")
    OVERLAY = (By.CSS_SELECTOR, "div[class*='Modal_modal_overlay']")


class FeedPageLocators:
    PAGE_TITLE = (By.XPATH, "//h1[normalize-space()='Лента заказов']")
    TOTAL_ALL = (
        By.XPATH,
        "//p[normalize-space()='Выполнено за всё время:']/following-sibling::p[1]",
    )
    TOTAL_TODAY = (
        By.XPATH,
        "//p[normalize-space()='Выполнено за сегодня:']/following-sibling::p[1]",
    )
    IN_PROGRESS_ORDERS = (
        By.CSS_SELECTOR,
        "ul[class*='OrderFeed_orderListReady'] li",
    )

