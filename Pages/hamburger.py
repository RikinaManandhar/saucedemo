from selenium.webdriver.common.by import By
from Pages.basepage import BasePage
class Hamburger(BasePage):
    menu_id=(By.ID, "react-burger-menu-btn")
    reset_button_id=(By.ID, "reset_sidebar_link")
    def __init__(self, driver):
        self.driver = driver

    def open_sidebar(self):
        self.wait_for_clickable(self.menu_id).click()
    
    def click_reset_button(self):
        self.open_sidebar()
        self.wait_for_clickable(self.reset_button_id).click()
