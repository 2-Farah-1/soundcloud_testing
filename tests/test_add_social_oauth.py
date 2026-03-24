import pytest
from selenium.webdriver.support.ui import WebDriverWait

import pages.settings_page.settings
import utils.browser_utils

from utils.session_utils import load_cookies
from utils.browser_utils import pause_for_manual_captcha

from pages.home_page import    click_more_menu_dropdown, click_settings_button
from pages.settings_page.settings import (

    click_add_facebook_account_button,
    click_add_google_account_button,
    click_add_apple_account_button,
)

# I'll be starting from softwareacc198
path = r'D:\SeleniumPython\SoundCloudE2ETesting\logged_in_cookies_softwaretestacc198.json'


def setup_page(driver):
    # driver.get("https://soundcloud.com/")
    # driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    pages.settings_page.settings.driver = driver
    pages.settings_page.settings.wait = wait

    utils.browser_utils.driver = driver
    utils.browser_utils.wait = wait

    pages.home_page.driver = driver
    pages.home_page.wait = wait

    load_cookies(driver, path)
    pause_for_manual_captcha()

    print("URL:", driver.current_url)
    print("Title:", driver.title)
    print("Number of iframes:", len(driver.find_elements("tag name", "iframe")))

    driver.maximize_window()


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


@pytest.mark.smoke
@pytest.mark.settings
def test_add_facebook_account_redirect(driver):
    setup_page(driver)
    pause_for_manual_captcha()

    # print("URL:", driver.current_url)
    # print("Title:", driver.title)
    # print("Number of iframes:", len(driver.find_elements("tag name", "iframe")))

    click_more_menu_dropdown()
    click_settings_button()
    pause_for_manual_captcha()

    click_add_facebook_account_button()
    driver.switch_to.default_content()

    switch_to_new_window_and_wait_for_url(driver, "facebook.com")

    assert "facebook.com" in driver.current_url.lower()


@pytest.mark.smoke
@pytest.mark.settings
def test_add_google_account_redirect(driver):
    setup_page(driver)
    pause_for_manual_captcha()

    # print("URL:", driver.current_url)
    # print("Title:", driver.title)
    # print("Number of iframes:", len(driver.find_elements("tag name", "iframe")))

    click_more_menu_dropdown()
    click_settings_button()
    pause_for_manual_captcha()

    click_add_google_account_button()
    driver.switch_to.default_content()

    switch_to_new_window_and_wait_for_url(driver, "accounts.google.com")

    assert "accounts.google.com" in driver.current_url.lower()


@pytest.mark.smoke
@pytest.mark.settings
def test_add_apple_account_redirect(driver):
    setup_page(driver)
    pause_for_manual_captcha()

    # print("URL:", driver.current_url)
    # print("Title:", driver.title)
    # print("Number of iframes:", len(driver.find_elements("tag name", "iframe")))

    click_more_menu_dropdown()
    click_settings_button()
    pause_for_manual_captcha()

    click_add_apple_account_button()
    driver.switch_to.default_content()

    switch_to_new_window_and_wait_for_url(driver, "appleid.apple.com")

    assert "appleid.apple.com" in driver.current_url.lower()