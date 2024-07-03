"""Tests for basic cart functionality"""

import pytest
from selenium.webdriver.common.by import By

BACKPACK = "Sauce Labs Backpack"
LIGHT = "Sauce Labs Bike Light"


@pytest.fixture(autouse=True)
def login(page):
    """Automatic login before each test"""
    page.find_element(By.ID, "user-name").send_keys("standard_user")
    page.find_element(By.ID, "password").send_keys("secret_sauce")
    page.find_element(By.ID, "login-button").click()


def add_item(page, item_name):
    """Adds item with specific name to the cart"""
    item = page.find_element(
        By.XPATH, f"//*[contains(@class, 'inventory_item_name') and text()='{item_name}']/../../.."
    )
    item.find_element(By.CLASS_NAME, "btn_inventory").click()


def test_add_to_cart(page):
    """Tests that shopping cart icon correctly shows item when added"""
    assert page.find_element(By.CLASS_NAME, "shopping_cart_link").text == ''
    add_item(page, BACKPACK)
    assert page.find_element(By.CLASS_NAME, "shopping_cart_link").text == '1'


def test_item_is_added(page):
    """Tests that item is added to the cart"""
    add_item(page, LIGHT)
    page.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    assert any(LIGHT in item.text for item in page.find_elements(By.CLASS_NAME, "cart_item"))


