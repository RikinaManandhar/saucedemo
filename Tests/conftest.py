from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pathlib import Path
from dotenv import load_dotenv
import os
# ✅ Point to your actual .env location
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

@pytest.fixture(scope="function")
def basicsetup(request):
    options = Options()
    options.add_argument("--incognito")  # Enable incognito mode

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    base_url = os.getenv("BASE_URL")
    driver.get(base_url)

    request.cls.driver = driver
    yield driver
    driver.quit()
