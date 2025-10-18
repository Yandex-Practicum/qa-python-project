from selenium.webdriver.common.by import By


class OrderModalLocators:
    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")

    # Детали ингредиента
    INGREDIENT_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")
    INGREDIENT_NAME = (By.XPATH, "//h2[text()='Детали ингредиента']/following-sibling::p[contains(@class, 'text')]")
    INGREDIENT_IMAGE = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//img")

    # Детали заказа
    ORDER_DETAILS = (By.XPATH, "//div[contains(@class, 'Modal_modal')][.//p[contains(@class, 'digits-large')]]")
    ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'digits-large')]")
    ORDER_STATUS = (By.XPATH, ".//p[contains(@class, 'status')]")
