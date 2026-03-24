import pytest
from selenium.webdriver.support.ui import WebDriverWait

import pages.sign_in_page
from pages.sign_in_page import (
    open_auth,  # YOU already have this
    auth_enter_email_or_url,
    click_continue,
    click_forgot_password,
    click_send_reset_link,
    click_visit_help_center,
    click_back_to_login,
    is_element_visible,
    is_on_help_center,
    switch_to_auth_iframe,
)
from ui_selectors import SignInSelectors, SignUpSelectors, AuthSelectors


TEST_EMAIL = "farahelhebeishy@gmail.com"


def setup_page(driver):
    driver.get("https://soundcloud.com/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    # inject driver + wait into your page functions
    pages.login_page.driver = driver
    pages.login_page.wait = wait


def go_to_forgot_password(email):
    open_auth()
    auth_enter_email_or_url(email)
    click_continue()
    click_forgot_password()


def go_to_check_your_email(email):
    go_to_forgot_password(email)
    click_send_reset_link()


# =========================
# TESTS
# =========================


@pytest.mark.smoke
@pytest.mark.auth
def test_sign_in_with_email_success(driver):
    setup_page(driver)
    go_to_forgot_password(TEST_EMAIL)

    assert is_element_visible(SignInSelectors.RESET_PASSWORD_TITLE), (
        "Reset password form did not appear."
    )

@pytest.mark.smoke
@pytest.mark.auth
def test_user_can_open_forgot_password_form(driver):
    setup_page(driver)
    go_to_forgot_password(TEST_EMAIL)

    assert is_element_visible(SignInSelectors.RESET_PASSWORD_TITLE), (
        "Reset password form did not appear."
    )


@pytest.mark.smoke
@pytest.mark.auth
def test_user_can_send_reset_link(driver):
    setup_page(driver)
    go_to_forgot_password(TEST_EMAIL)

    assert is_element_visible(SignInSelectors.RESET_PASSWORD_TITLE), (
        "Reset password form did not appear before sending reset link."
    )

    click_send_reset_link()

    assert is_element_visible(SignInSelectors.CHECK_YOUR_EMAIL_TITLE), (
        "Check your email screen did not appear after sending reset link."
    )


@pytest.mark.auth
def test_user_can_open_help_center_from_reset_form(driver):
    setup_page(driver)
    go_to_forgot_password(TEST_EMAIL)

    assert is_element_visible(SignInSelectors.RESET_PASSWORD_TITLE), (
        "Reset password form did not appear before sending reset link."
    )

    click_visit_help_center()

    assert is_on_help_center(), (
        "Help Center page did not open."
    )
    assert is_element_visible(SignUpSelectors.HELP_CENTER_PAGE_TITLE), (
        "Help Center title is not visible."
    )




@pytest.mark.auth
def test_user_can_open_help_center_from_check_email(driver):
    setup_page(driver)
    go_to_check_your_email(TEST_EMAIL)

    assert is_element_visible(SignInSelectors.CHECK_YOUR_EMAIL_TITLE), (
        "Check your email screen did not appear before opening Help Center."
    )

    click_visit_help_center()

    assert is_on_help_center(), (
        "Help Center page did not open."
    )
    assert is_element_visible(SignUpSelectors.HELP_CENTER_PAGE_TITLE), (
        "Help Center title is not visible."
    )


@pytest.mark.auth
def test_user_can_go_back_to_login_from_check_email(driver):
    setup_page(driver)
    go_to_check_your_email(TEST_EMAIL)

    assert is_element_visible(SignInSelectors.CHECK_YOUR_EMAIL_TITLE), (
        "Check your email screen did not appear before going back to login."
    )

    click_back_to_login()

    assert is_element_visible(AuthSelectors.PASSWORD), (
        "Did not return to login form from check your email screen."
    )


@pytest.mark.regression
@pytest.mark.auth
def test_forgot_password_full_flow(driver):
    setup_page(driver)
    original_tab = driver.current_window_handle

    go_to_forgot_password(TEST_EMAIL)

    assert is_element_visible(SignInSelectors.RESET_PASSWORD_TITLE), (
        "Reset password form did not appear."
    )

    click_send_reset_link()

    assert is_element_visible(SignInSelectors.CHECK_YOUR_EMAIL_TITLE), (
        "Check your email screen did not appear after sending reset link."
    )

    click_visit_help_center()

    assert is_on_help_center(), (
        "Help Center page did not open."
    )
    assert is_element_visible(SignUpSelectors.HELP_CENTER_PAGE_TITLE), (
        "Help Center title is not visible."
    )


    driver.close()
    driver.switch_to.window(original_tab)

     #just in case
   # switch_to_auth_iframe()


    click_back_to_login()

    assert is_element_visible(AuthSelectors.PASSWORD), (
        "Did not return to login form after clicking back to login."
    )