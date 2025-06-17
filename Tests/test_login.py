# from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.login import Login
from Pages.basepage import BasePage

import pytest

@pytest.mark.usefixtures("basicsetup")
class TestOrangeHRM:

    @pytest.mark.validlogin
    @pytest.mark.parametrize("username, password", BasePage.read_test_data("testdata.json")["login_credentials"])
    def test_login_with_valid_credentials(self,username,password):
        self.login_page = Login(self.driver)
        self.login_page.login(username,password)
        assert self.login_page.is_login_successful(), "Login should succeed with valid credentials"

    def test_login_with_empty_credentials(self):
        self.login_page = Login(self.driver)
        # self.base_page= BasePage(self.driver)

    
        self.login_page.login("", "")
        assert not self.login_page.is_login_successful(), "Login should fail for empty credentials"
        error_element=self.login_page.wait_for_visibility(self.login_page.error_message)
        actual_output = error_element.text
        expected_output = "Epic sadface: Username is required"

        assert actual_output == expected_output, f"Expected '{expected_output}', but got '{actual_output}'"

    def test_login_with_empty_passwordfield(self):
        self.login_page = Login(self.driver)
        # self.base_page= BasePage(self.driver)

        self.login_page.login("standard_user", "")
        assert not self.login_page.is_login_successful(), "Login should fail for empty credentials"
        error_element=self.login_page.wait_for_visibility(self.login_page.error_message)
        actual_output = error_element.text
        expected_output = "Epic sadface: Password is required"

        assert actual_output == expected_output, f"Expected '{expected_output}', but got '{actual_output}'"

    def test_login_with_empty_usernamefield(self):
        self.login_page = Login(self.driver)
        # self.base_page= BasePage(self.driver)

        self.login_page.login("","secret_sauce")
        assert not self.login_page.is_login_successful(), "Login should fail for empty credentials"
        error_element=self.login_page.wait_for_visibility(self.login_page.error_message)
        actual_output = error_element.text
        expected_output = "Epic sadface: Username is required"

        assert actual_output == expected_output, f"Expected '{expected_output}', but got '{actual_output}'"

    def test_verify_username_placeholder(self):
        self.login_page = Login(self.driver)
        # self.base_page= BasePage(self.driver)

        username=self.login_page.wait_for_visibility(self.login_page.username)
        actual_placeholder= username.get_attribute("placeholder")
        expected_placeholder="Username"

        assert actual_placeholder==expected_placeholder, f"Expected '{expected_placeholder}', but got '{actual_placeholder}'"
    
    def test_verify_password_placeholder(self):
        self.login_page = Login(self.driver)
        # self.base_page= BasePage(self.driver)

        password=self.login_page.wait_for_visibility(self.login_page.password)
        actual_placeholder= password.get_attribute("placeholder")
        expected_placeholder="Password"

        assert actual_placeholder==expected_placeholder, f"Expected '{expected_placeholder}', but got '{actual_placeholder}'"

    @pytest.mark.login_button
    def test_verify_loginbutton_text(self):
        self.login_page = Login(self.driver)

        loginbuton=self.login_page.wait_for_visibility(self.login_page.login_button)
        actual_text = loginbuton.get_attribute("value")
        expected_text="Login"

        assert actual_text==expected_text, f"Expected '{expected_text}', but got '{actual_text}'"