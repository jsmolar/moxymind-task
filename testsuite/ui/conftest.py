"""Conftest for UI tests"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(scope="session")
def driver(request):
    """Connects to the remote webdriver"""
    options = ChromeOptions()
    options.set_capability("acceptInsecureCerts", True)
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4444" + "/wd/hub", options=options)
    driver.implicitly_wait(5)
    request.addfinalizer(driver.quit)
    return driver


@pytest.fixture()
def page(driver):
    """Opens sauce demo page"""
    driver.delete_all_cookies()
    driver.get("https://www.saucedemo.com/")
    return driver
