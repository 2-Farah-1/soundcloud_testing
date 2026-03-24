import pytest
from selenium.webdriver.support.ui import WebDriverWait

import pages.home_page as home_page
import pages.auth_page as auth_page
import pages.sign_in_page as sign_in_page
import pages.cookies_page as cookies_page

#from utils.session_utils import load_cookies

from pages.auth_page import (
    open_auth,
    auth_enter_email_or_url,
    click_continue,
    enter_password,
    click_continue_entered_password,
)

from utils.browser_utils import (
    is_element_visible
)

from ui_selectors import SignInSelectors, AuthSelectors, SignUpSelectors





def setup_page(driver):
    driver.get("https://soundcloud.com/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    home_page.driver = driver
    home_page.wait = wait

    auth_page.driver = driver
    auth_page.wait = wait

    sign_in_page.driver = driver
    sign_in_page.wait = wait

    cookies_page.driver = driver
    cookies_page.wait = wait




VALID_EMAIL = "farahelhebeishy@gmail.com"
VALID_USERNAME = "farah-elhebeishy"
VALID_PASSWORD = "Test1test2Test3"
WRONG_PASSWORD = "123456"
INVALID_EMAIL = "test@d"
NEW_EMAIL = "brandnewemailfortesting123456@example.com"
INVALID_URL = "this_profile_should_not_exist_123456789"


# =========================
# HELPERS
# =========================

def go_to_sign_in_with_identifier(identifier):
    open_auth()
    auth_enter_email_or_url(identifier)
    click_continue()


def login_with_credentials(identifier, password):
    go_to_sign_in_with_identifier(identifier)
    enter_password(password)
    click_continue_entered_password()


# =========================
# TESTS Sign in
# =========================


@pytest.mark.smoke
@pytest.mark.auth
def test_sign_in_with_username_success(driver):

    setup_page(driver)
    login_with_credentials(VALID_USERNAME, VALID_PASSWORD)

    assert is_element_visible(SignInSelectors.SIGNED_IN_PROFILE_BTN), (
        "User was not signed in successfully using username."
    )


@pytest.mark.smoke
@pytest.mark.auth
def test_sign_in_with_email_success(driver):

    setup_page(driver)
    login_with_credentials(VALID_EMAIL, VALID_PASSWORD)

    assert is_element_visible(SignInSelectors.SIGNED_IN_PROFILE_BTN), (
        "User was not signed in successfully using email."
    )


@pytest.mark.auth
def test_sign_in_incorrect_password(driver):

    setup_page(driver)
    login_with_credentials(VALID_EMAIL, WRONG_PASSWORD)

    assert is_element_visible(SignInSelectors.ERROR_INCORRECT_PASSWORD), (
        "Incorrect password error was not shown."
    )


@pytest.mark.auth
def test_sign_in_invalid_email_format(driver):

    setup_page(driver)
    go_to_sign_in_with_identifier(INVALID_EMAIL)

    assert is_element_visible(AuthSelectors.ERROR_INVALID_EMAIL_OR_URL), (
        "Invalid email format error was not shown."
    )


@pytest.mark.auth
def test_sign_in_new_email_redirects_to_signup(driver):

    setup_page(driver)
    go_to_sign_in_with_identifier(NEW_EMAIL)

    assert is_element_visible(SignUpSelectors.CREATE_ACCOUNT_TITLE), (
        "User was not redirected to create account for new email."
    )


@pytest.mark.auth
def test_sign_in_invalid_url(driver):

    setup_page(driver)
    go_to_sign_in_with_identifier(INVALID_URL)

    assert is_element_visible(AuthSelectors.ERROR_URL_DOESNT_EXIST), (
        "Invalid URL error was not shown."
    )