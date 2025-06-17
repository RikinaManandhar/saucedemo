from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
import os

class BasePage:
    
    logout_button=(By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver

    def wait_for_visibility(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))
    
    def wait_for_all_elements(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_all_elements_located(locator))
    
    def scroll_into_view(self, locator):
        element = self.wait_for_visibility(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)
        return element
    
    def get_text(self,locator):
        element = self.wait_for_visibility(locator)
        return element.text
        
    @staticmethod
    def read_test_data(filename):
        filepath = os.path.join(os.path.dirname(__file__), '..', 'data', filename)
        with open(filepath, 'r') as file:
            return json.load(file)

   



 
 


        

        
