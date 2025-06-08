from Pages.login import Login
from Pages.hamburger import Hamburger
from Pages.cart import Cart
import pytest

@pytest.mark.usefixtures("basicsetup")
class TestCart:

    def test_add_to_cart(self):
        self.login_page= Login(self.driver)
        # self.base_page= BasePage(self.driver)
        self.cart_page= Cart(self.driver)

        self.login_page.login("standard_user", "secret_sauce")
        self.cart_page.add_to_cart(self.cart_page.add_backpack)

        remove_button = self.cart_page.wait_for_visibility(self.cart_page.remove_backpack)
        assert remove_button.is_displayed(), "Backpack not added to cart (Remove button not visible)"

    def test_verify_item_count_in_badge_and_cart(self):
        self.login_page= Login(self.driver)
        # self.base_page= BasePage(self.driver)
        self.cart_page= Cart(self.driver)

        self.login_page.login("standard_user", "secret_sauce")
        self.cart_page.add_to_cart(self.cart_page.add_backpack)
        self.cart_page.add_to_cart(self.cart_page.add_bolt_tshirt)
        self.cart_page.add_to_cart(self.cart_page.add_bikelight)

        badge_count= self.cart_page.get_cart_badge_number()
        self.cart_page.open_cart_page()
        item_count= self.cart_page.get_number_of_items_in_cart()

        assert str(badge_count)==str(item_count),f"badge count doesnot equal to item count. badge count: {badge_count}  item count: {item_count}"
    
    @pytest.mark.reset
    def test_verify_reset(self):
        self.login_page= Login(self.driver)
        self.cart_page= Cart(self.driver)
        self.hamburger_page= Hamburger(self.driver)

        self.login_page.login("standard_user", "secret_sauce")
        self.cart_page.add_to_cart(self.cart_page.add_backpack)
        self.cart_page.open_cart_page()
        item_count= self.cart_page.get_number_of_items_in_cart()
        assert item_count==1,"item is not added to cart"

        self.hamburger_page.click_reset_button()
        self.cart_page.open_cart_page()
        item_count= self.cart_page.get_number_of_items_in_cart()
        assert item_count==0,"reset button is not working"

    




    