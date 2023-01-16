import pytest

from selenium.webdriver import Safari
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture(params=["chrome", "safari"])
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    # browser = request.param
    print(f"Creating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
    elif browser == "safari":
        print("INSIDE SAFARI")
        options = SafariOptions()
        my_driver = webdriver.Safari(options=options)
    else:
        raise TypeError(f"Expected 'chrome' or 'safari', but  got {browser}")
    my_driver.implicitly_wait(5)
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store",
                     default="chrome", help="browser to execute tests: chrome or safari")
