from Pages.inventory import Inventory
from Pages.login import Login
from Pages.basepage import BasePage
from Pages.hamburger import Hamburger
import pytest

@pytest.mark.usefixtures("basicsetup")
class TestInventory:

    def test_verify_title(self):
        self.inventory_page= Inventory(self.driver)
        self.login_page= Login(self.driver)
        self.base_page= BasePage(self.driver)

        self.login_page.login("standard_user", "secret_sauce")
        title= self.base_page.wait_for_visibility(self.inventory_page.get_title_locater())
        actual_tile= title.text
        expected_title= "Products"

        assert actual_tile==expected_title,f"Expected title:{expected_title} but got {actual_tile}"

    def test_verify_number_of_products(self):
        self.inventory_page= Inventory(self.driver)
        self.login_page= Login(self.driver)
        self.base_page= BasePage(self.driver)

        self.login_page.login("standard_user", "secret_sauce")
        items=self.base_page.wait_for_all_elements(self.inventory_page.get_inventory_item_locater())
        actual_number_of_items= len(items)
        expected_number_of_items= 6

        assert expected_number_of_items== actual_number_of_items,f"expected number of item: {expected_number_of_items} but got :{actual_number_of_items}"

    def test_verify_url(self):
        self.inventory_page= Inventory(self.driver)
        self.login_page= Login(self.driver)
        self.base_page= BasePage(self.driver)

        self.login_page.login("standard_user", "secret_sauce")
        current_url= self.inventory_page.get_url()
        expected_url_part="/inventory"
        assert expected_url_part in current_url, f"Expected URL to contain '{expected_url_part}', but got '{current_url}'"

    @pytest.mark.logout
    def test_verify_logout(self):
        self.base_page= BasePage(self.driver)
        self.login_page= Login(self.driver)
        self.hamburger_page= Hamburger(self.driver)

        self.login_page.login("standard_user", "secret_sauce")
        

        self.hamburger_page.open_sidebar()
        self.login_page.logout()

        login_button = self.base_page.wait_for_visibility(self.login_page.login_button)
        assert login_button.is_displayed(),"Login button not present"


    @pytest.mark.verify_sorting
    def test_verify_higher_to_lower_price_sorting(self):
        self.base_page= BasePage(self.driver)
        self.login_page= Login(self.driver)
        self.inventory_page= Inventory(self.driver)

        data = self.login_page.read_test_data('testdata.json')
        self.login_page.login("standard_user", "secret_sauce")
        self.inventory_page.choose_filter(data["sort_option_value"])

        prices = self.inventory_page.get_all_prices()
        assert prices == sorted(prices), "Prices are not sorted low to high!"







