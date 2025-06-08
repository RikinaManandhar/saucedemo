from selenium.webdriver.common.by import By
from Pages.basepage import BasePage
from selenium.common.exceptions import TimeoutException


class Login(BasePage):

    username = (By.ID, "user-name")
    password =  (By.ID, "password")
    login_button = (By.ID,"login-button")
    error_message= (By.CSS_SELECTOR, "h3[data-test='error']")
    inventory_element=(By.XPATH, "//span[@class='title' and @data-test='title' and text()='Products']")

    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
       

        self.wait_for_visibility(self.username).send_keys(username)
        self.wait_for_visibility(self.password).send_keys(password)
        self.wait_for_clickable(self.login_button).click()
    
        
    def is_login_successful(self):
        try:
            self.wait_for_visibility(self.inventory_element)
            return True
        except TimeoutException:
            return False
        
    def get_error_message(self):
        try:
            return self.wait_for_visibility(self.error_message).text
        except TimeoutException:
            return None
    
    def logout(self):
        self.wait_for_visibility(self.logout_button) 
        self.wait_for_clickable(self.logout_button).click()