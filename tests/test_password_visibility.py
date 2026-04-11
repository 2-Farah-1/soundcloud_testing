import pytest
from selenium.webdriver.support.ui import WebDriverWait

import pages.home_page
import pages.auth_page
import utils.browser_utils
import pages.cookies_page
from pages.cookies_page import click_reject_all_cookies
from pages.home_page import click_header_create_account

from pages.auth_page import (
    switch_to_auth_iframe,
    is_password_hidden,
    click_show_password,
    is_password_visible,
    auth_enter_email_or_url,
    click_continue,
    enter_password
)
from utils.browser_utils import pause_for_manual_captcha


def setup_page(driver):
    driver.get("https://soundcloud.com/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    pages.cookies_page.driver = driver
    pages.cookies_page.wait = wait

    pages.home_page.driver = driver
    pages.home_page.wait = wait

    pages.auth_page.driver = driver
    pages.auth_page.wait = wait

    utils.browser_utils.driver = driver
    utils.browser_utils.wait = wait


@pytest.mark.smoke
@pytest.mark.auth
def test_password_visibility_toggle(driver):
    setup_page(driver)

    click_reject_all_cookies()
    click_header_create_account()
    #switch_to_auth_iframe()

    auth_enter_email_or_url("test@gexample.com")
    click_continue()

    pause_for_manual_captcha()

    enter_password("123456")

    assert is_password_hidden(), "Password is not hidden initially"

    click_show_password()
    assert is_password_visible(), "Password did not become visible after clicking show"

    click_show_password()
    assert is_password_hidden(), "Password did not become hidden again after clicking show"