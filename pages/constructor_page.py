from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from data.locators import ConstructorPageLocators

class ConstructorPage(BasePage):

    def go_to_ingredient(self):
        self.scroll_to(ConstructorPageLocators.INGREDIENT)
        self.click(ConstructorPageLocators.INGREDIENT)

    def add_ingredient_to_order(self):
        ingredient = self.wait_visible(
            ConstructorPageLocators.INGREDIENT
        )

        basket = self.wait_visible(
            ConstructorPageLocators.BASKET
        )

        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];

            function triggerDragAndDrop(sourceNode, targetNode) {
                const dataTransfer = new DataTransfer();

                sourceNode.dispatchEvent(new DragEvent('dragstart', {
                    dataTransfer: dataTransfer,
                    bubbles: true
                }));

                targetNode.dispatchEvent(new DragEvent('dragenter', {
                    dataTransfer: dataTransfer,
                    bubbles: true
                }));

                targetNode.dispatchEvent(new DragEvent('dragover', {
                    dataTransfer: dataTransfer,
                    bubbles: true
                }));

                targetNode.dispatchEvent(new DragEvent('drop', {
                    dataTransfer: dataTransfer,
                    bubbles: true
                }));

                sourceNode.dispatchEvent(new DragEvent('dragend', {
                    dataTransfer: dataTransfer,
                    bubbles: true
                }));
            }

            triggerDragAndDrop(source, target);
            """,
            ingredient,
            basket
        )


    def get_counter(self):
        text = self.get_text(
            ConstructorPageLocators.COUNTER
        )
        return int(text)

    def place_order(self):
        self.click(
            ConstructorPageLocators.ORDER_BUTTON
        )
    
    def get_total_price(self):
        price = self.get_text(ConstructorPageLocators.TOTAL_PRICE)
        return int(price)
    
    def wait_price_changed(self, old_price):
        self.wait.until(
            lambda d: self.get_total_price() != old_price
        )