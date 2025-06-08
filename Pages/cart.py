from selenium.webdriver.common.by import By
from Pages.basepage import BasePage
from selenium.common.exceptions import TimeoutException

class Cart(BasePage):
    add_backpack= (By.ID, "add-to-cart-sauce-labs-backpack")
    remove_backpack=(By.ID, "remove-sauce-labs-backpack")
    add_bikelight=(By.ID, "add-to-cart-sauce-labs-bike-light")
    remove_bikelight=(By.ID, "remove-sauce-labs-bike-light")
    add_bolt_tshirt=(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    remove_bolt_tshirt=(By.ID, "remove-sauce-labs-bolt-t-shirt")
    add_fleece_jacket=(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    remove_fleece_jacket=(By.ID, "remove-sauce-labs-fleece-jacket")
    add_onesie=(By.ID, "add-to-cart-sauce-labs-onesie")
    remove_onesie=(By.ID, "remove-sauce-labs-onesie")
    add_red_tshirt=(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    remove_red_tshirt=(By.ID, "remove-test.allthethings()-t-shirt-(red)")
    cart=(By.CLASS_NAME, "shopping_cart_link")
    cart_badge=(By.CLASS_NAME, "shopping_cart_badge") 
    cart_item=(By.CLASS_NAME, "cart_item") 
    
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self,locater):
        self.wait_for_clickable(locater).click()
    
    def remove_from_cart(self,locater):
        self.wait_for_clickable(locater).click()

    def open_cart_page(self):
        self.wait_for_clickable(self.cart).click()
    
    def get_cart_badge_number(self):
        item_count=self.scroll_into_view(self.cart_badge)
        return item_count.text
    
    def get_number_of_items_in_cart(self):
        try:
            items = self.wait_for_all_elements(self.cart_item)
            return len(items)
        except TimeoutException:
            # No items found within timeout -> cart is empty
            return 0






        

