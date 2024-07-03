"""Tests for Login page"""

import pytest
from selenium.webdriver.common.by import By


def test_correct_credentials(page):
    """Tests that user is logged in with correct credentials"""
    page.find_element(By.ID, "user-name").send_keys("standard_user")
    page.find_element(By.ID, "password").send_keys("secret_sauce")
    page.find_element(By.ID, "login-button").click()

    assert page.find_element(By.CLASS_NAME, "app_logo").text == "Swag Labs"
    assert page.find_element(By.CLASS_NAME, "shopping_cart_link").is_displayed()


@pytest.mark.parametrize(
    "name, password, error_msg",
    [
        pytest.param("test", "", "Epic sadface: Password is required", id="Empty password"),
        pytest.param("", "test", "Epic sadface: Username is required", id="Empty name"),
        pytest.param("", "", "Epic sadface: Username is required", id="Empty credentials"),
        pytest.param(
            "locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out.",
            id="Lockout user"
        ),
    ],
)
def test_incorrect_credentials(page, name, password, error_msg):
    """Tests error messages for incorrect logins"""
    page.find_element(By.ID, "user-name").send_keys(name)
    page.find_element(By.ID, "password").send_keys(password)
    page.find_element(By.ID, "login-button").click()

    assert page.find_element(By.CLASS_NAME, "error-message-container").text == error_msg
