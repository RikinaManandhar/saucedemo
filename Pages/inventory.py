from selenium.webdriver.common.by import By

class Inventory:
    title=(By.CLASS_NAME, "title")
    inventory_item=(By.CLASS_NAME, "inventory_item")

    def __init__(self, driver):
        self.driver = driver

    def get_title_locater(self):
        return self.title
    
    def get_inventory_item_locater(self):
        return self.inventory_item
    
    def get_url(self):
        return self.driver.current_url

