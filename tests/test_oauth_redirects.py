import pytest
import pages.sign_in_page
from selenium.webdriver.support.ui import WebDriverWait

#these tests just test that the app redirects nothing more

from pages.sign_in_page import (
    open_auth,
    switch_to_auth_iframe,
    click_google_button,
    click_facebook_button,
    click_apple_button,
)

def setup_page(driver):
    driver.get("https://soundcloud.com/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    pages.login_page.driver = driver
    pages.login_page.wait = wait


def switch_to_new_window_and_wait_for_url(driver, expected_text):
    original_window = driver.current_window_handle

    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

    for window in driver.window_handles:
        if window != original_window:
            driver.switch_to.window(window)
            break

    WebDriverWait(driver, 20).until(
        lambda d: expected_text in d.current_url.lower()
    )

def test_google_button_redirect(driver):
    setup_page(driver)

    open_auth()
    click_google_button()
    driver.switch_to.default_content()
    switch_to_new_window_and_wait_for_url(driver,"accounts.google.com")

    assert "accounts.google.com" in driver.current_url

def test_facebook_button_redirect(driver):
    setup_page(driver)

    open_auth()
    click_facebook_button()
    driver.switch_to.default_content()
    switch_to_new_window_and_wait_for_url(driver,"facebook.com")

    assert "facebook.com" in driver.current_url

def test_apple_button_redirect(driver):
    setup_page(driver)

    open_auth()
    click_apple_button()
    driver.switch_to.default_content()
    switch_to_new_window_and_wait_for_url(driver,"appleid.apple.com")

    assert "appleid.apple.com" in driver.current_url

