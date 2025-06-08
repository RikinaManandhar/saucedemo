from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope="function")
def basicsetup(request):
    options = Options()
    options.add_argument("--incognito")  # Enable incognito mode

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    request.cls.driver = driver
    yield driver
    driver.quit()
