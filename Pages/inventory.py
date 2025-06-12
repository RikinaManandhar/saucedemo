from selenium.webdriver.common.by import By
from Pages.basepage import BasePage
from selenium.webdriver.support.ui import Select

class Inventory(BasePage):
    title=(By.CLASS_NAME, "title")
    inventory_item=(By.CLASS_NAME, "inventory_item")
    filter=(By.CLASS_NAME, "product_sort_container")
    price_locator = (By.CLASS_NAME, "inventory_item_price")


    def __init__(self, driver):
        self.driver = driver

    def get_title_locater(self):
        return self.title
    
    def get_inventory_item_locater(self):
        return self.inventory_item
    
    def get_url(self):
        return self.driver.current_url
    
    def choose_filter(self, sorting_value):
        sort_dropdown = Select(self.wait_for_clickable(self.filter))
        sort_dropdown.select_by_value(sorting_value)

    def get_all_prices(self):
        elements = self.wait_for_all_elements(self.price_locator)
        prices = [float(e.text.replace("$", "")) for e in elements]
        return prices

   
        


