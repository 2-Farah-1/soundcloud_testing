import pytest
from selenium.webdriver.support.ui import WebDriverWait

import pages.home_page as home_page
import pages.auth_page as auth_page
import pages.sign_up_page as sign_up_page
import pages.cookies_page as cookies_page
import utils.browser_utils as browser_utils

from pages.cookies_page import click_reject_all_cookies
from pages.auth_page import (
    click_header_create_account,
    switch_to_auth_iframe,
    auth_enter_email_or_url,
    click_continue,
    enter_password,
    click_continue_entered_password,
)
from pages.sign_up_page import (
    fill_tell_us_more_about_you_form,
    click_continue_tell_us_more_about_you,
)
from utils.browser_utils import (
    is_element_visible,
    is_element_disabled,
    pause_for_manual_captcha,
)
from ui_selectors import AuthSelectors, SignUpSelectors


def setup_page(driver):
    driver.get("https://soundcloud.com/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    home_page.driver = driver
    home_page.wait = wait

    auth_page.driver = driver
    auth_page.wait = wait

    sign_up_page.driver = driver
    sign_up_page.wait = wait

    cookies_page.driver = driver
    cookies_page.wait = wait

    browser_utils.driver = driver
    browser_utils.wait = wait


EXISTING_EMAIL = "canalvbm+rayburn@gmail.com"
NEW_EMAIL = "brandnewemailfortesting123456@example.com"
INVALID_EMAIL = "test@"
VALID_PASSWORD = "Ray@123123123"
SHORT_PASSWORD = "1234"


def open_create_account_flow():
    click_reject_all_cookies()
    click_header_create_account()
    switch_to_auth_iframe()


def go_to_signup_with_email(email):
    open_create_account_flow()
    auth_enter_email_or_url(email)
    click_continue()


@pytest.mark.smoke
@pytest.mark.auth
def test_sign_up_invalid_email_format(driver):
    setup_page(driver)
    go_to_signup_with_email(INVALID_EMAIL)

    assert is_element_visible(AuthSelectors.ERROR_INVALID_EMAIL_OR_URL), (
        "Invalid email error was not shown."
    )


@pytest.mark.smoke
@pytest.mark.auth
def test_sign_up_duplicate_email_shows_account_exists(driver):
    setup_page(driver)
    go_to_signup_with_email(EXISTING_EMAIL)

    assert is_element_visible(SignUpSelectors.ACCOUNT_ALREADY_EXISTS_MSG), (
        "Account already exists message was not shown."
    )


@pytest.mark.auth
def test_sign_up_empty_email(driver):
    setup_page(driver)
    open_create_account_flow()
    click_continue()

    assert is_element_visible(AuthSelectors.ERROR_INVALID_EMAIL_OR_URL), (
        "Error was not shown for empty email field."
    )


@pytest.mark.auth
def test_sign_up_valid_email_reaches_password_step(driver):
    setup_page(driver)
    go_to_signup_with_email(NEW_EMAIL)

    assert is_element_visible(AuthSelectors.CONTINUE_ENTER_PASSWORD), (
        "Password step did not appear for a new valid email."
    )


@pytest.mark.auth
def test_sign_up_empty_password_continue_disabled(driver):
    setup_page(driver)
    go_to_signup_with_email(NEW_EMAIL)

    assert is_element_disabled(AuthSelectors.CONTINUE_ENTER_PASSWORD), (
        "Continue button was enabled with empty password."
    )


@pytest.mark.auth
def test_sign_up_short_password_continue_disabled(driver):
    setup_page(driver)
    go_to_signup_with_email(NEW_EMAIL)
    enter_password(SHORT_PASSWORD)

    assert is_element_disabled(AuthSelectors.CONTINUE_ENTER_PASSWORD), (
        "Continue button was not disabled for short password."
    )


@pytest.mark.auth
def test_sign_up_valid_password_enables_continue(driver):
    setup_page(driver)
    go_to_signup_with_email(NEW_EMAIL)
    enter_password(VALID_PASSWORD)

    assert not is_element_disabled(AuthSelectors.CONTINUE_ENTER_PASSWORD), (
        "Continue button stayed disabled for a valid password."
    )


@pytest.mark.auth
def test_sign_up_reaches_profile_step_after_valid_password(driver):
    setup_page(driver)
    go_to_signup_with_email(NEW_EMAIL)
    enter_password(VALID_PASSWORD)
    click_continue_entered_password()

    assert is_element_visible(SignUpSelectors.TELL_US_MORE_TITLE), (
        "Tell us more about you step did not appear."
    )


@pytest.mark.auth
def test_sign_up_profile_continue_after_filling_form(driver):
    setup_page(driver)
    go_to_signup_with_email(NEW_EMAIL)
    enter_password(VALID_PASSWORD)
    click_continue_entered_password()

    fill_tell_us_more_about_you_form(
        "Rayburn1",
        "May",
        "10",
        "2005",
        "Male",
    )

    assert not is_element_disabled(SignUpSelectors.CONTINUE_SUBMIT_SIGNUP), (
        "Continue button stayed disabled after filling profile form."
    )


@pytest.mark.auth
def test_sign_up_flow_until_profile_submission(driver):
#note: I will continue this test with the check your inbox! test in the future
    setup_page(driver)
    go_to_signup_with_email(NEW_EMAIL)
    enter_password(VALID_PASSWORD)
    click_continue_entered_password()
    pause_for_manual_captcha()

    fill_tell_us_more_about_you_form(
        "Rayburn1",
        "May",
        "10",
        "2005",
        "Male",
    )
    click_continue_tell_us_more_about_you()
    pause_for_manual_captcha()

    assert is_element_visible(SignUpSelectors.CHECK_YOUR_INBOX_TITLE), (
        "Check your inbox screen did not appear after registration."
    )