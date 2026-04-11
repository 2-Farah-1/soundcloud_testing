import random

import pytest
from selenium.webdriver.support.ui import WebDriverWait

import pages.auth_page as auth_page
import pages.cookies_page as cookies_page
import pages.home_page as home_page
import pages.sign_up_page as sign_up_page
import utils.browser_utils as browser_utils
from pages.auth_page import (
    click_header_create_account,  # done
    auth_enter_email_or_url,
    click_continue,
    enter_password,
    click_continue_entered_password,
)
from pages.home_page import click_header_sign_in
from pages.sign_up_page import (
    sign_up_enter_email,
    fill_tell_us_more_about_you_form,
    click_continue_tell_us_more_about_you,
    enter_display_name,
    select_month,
    select_day,
    select_year,
    select_gender,
    enter_verification_code,
    click_verify_email_button
)
from ui_selectors import AuthSelectors, SignUpSelectors, SignInSelectors, HomeSelectors
from utils.browser_utils import (
    is_element_visible,
    is_element_disabled,
    pause_for_manual_captcha,
    get_element_text
)
from utils.email_utils.temp_mail_utils import *


def setup_page(driver):
    #driver.get("https://soundcloud.com/")
    driver.get("https://tunify.duckdns.org/signin")
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


EXISTING_EMAIL = "b.ik.e.a.bad.i.1.9.9@gmail.com"
NEW_EMAIL = 'softwaretestacc198@gmail.com'
INVALID_EMAIL = "test@"
VALID_PASSWORD = "Ray@123123123"
SHORT_PASSWORD = "1234"
def generate_random_unverified_email():
    return f"randomacc{random.randint(10, 99)}@gmail.com"

def open_create_account_flow():
    #click_reject_all_cookies()
    click_header_create_account()
    ##switch_to_auth_iframe()


def go_to_signup_with_email(email: object) -> None:
    open_create_account_flow()
    #auth_enter_email_or_url(email)
    sign_up_enter_email(email)
    #click_continue()

#returns a temp_mail and the mailbox to use
def new_temp_mail():
    mailbox_data = create_temp_mailbox()
    temp_email = mailbox_data["emailAddress"]
    mailbox_id = mailbox_data["id"]
    return temp_email, mailbox_id

def generate_random_display_name():
    return f"TestAcc{random.randint(1000, 999999)}"

#========================================================
#                    TEST M1-001
#========================================================

#Test M1-002
# @pytest.mark.auth
# def test_sign_up_flow_until_profile_submission(driver):
# #note: I will continue this test with the check your inbox! test in the future
#     setup_page(driver)
#     go_to_signup_with_email(NEW_EMAIL)
#     enter_password(VALID_PASSWORD)
#     click_continue_entered_password()
#     pause_for_manual_captcha()
#
#     fill_tell_us_more_about_you_form(
#         generate_random_display_name(),
#         "May",
#         "10",
#         "2005",
#         "Male",
#     )
#     click_continue_tell_us_more_about_you()
#     pause_for_manual_captcha()
#
#     assert is_element_visible(SignUpSelectors.CHECK_YOUR_INBOX_TITLE), (
#         "Check your inbox screen did not appear after registration."
#     )




#======================================================================================================
# helper: sign in after verification
def sign_in_after_verification(email_input, password):
    click_header_sign_in()
    auth_enter_email_or_url(email_input)
    click_continue()
    enter_password(password)
    click_continue_entered_password()


# helper: generic success check after sign in
def assert_account_is_usable_after_sign_in():
    assert not is_element_visible(SignUpSelectors.CHECK_YOUR_INBOX_TITLE), (
        "User was redirected back to Check your inbox instead of signing in successfully."
    )
    assert not is_element_visible(SignUpSelectors.VERIFY_EMAIL_TITLE), (
        "User was redirected back to Verify your email instead of signing in successfully."
    )


# Test M1-001
# original check your inbox logic
@pytest.mark.auth
def test_register_new_account_and_verify_successfully(driver):
    temp_email, mailbox_id = new_temp_mail()

    setup_page(driver)
    go_to_signup_with_email(temp_email)
    enter_password(VALID_PASSWORD)
    click_continue_entered_password()
    pause_for_manual_captcha()

    fill_tell_us_more_about_you_form(
        generate_random_display_name(),
        "May",
        "10",
        "2005",
        "Male",
    )
    click_continue_tell_us_more_about_you()
    #pause_for_manual_captcha()

    assert is_element_visible(SignUpSelectors.CHECK_YOUR_INBOX_TITLE, timeout=20), (
        "Check your inbox screen did not appear after registration."
    )

    verification_link = get_verification_link_temp(
        mailbox_id,
        timeout_seconds=60,
        poll_every_seconds=5,
    )
    assert verification_link is not None, "Verification link was not received."

    original_window = browser_utils.open_link_in_new_tab(verification_link)
    browser_utils.wait_for_non_blank_url()

    assert is_element_visible(SignUpSelectors.EMAIL_CONFIRMED_TITLE, timeout=20), (
        "Email confirmation page did not appear after opening the verification link."
    )

    driver.close()
    driver.switch_to.window(original_window)

    sign_in_after_verification(temp_email, VALID_PASSWORD)
    assert_account_is_usable_after_sign_in()


# Test M1-001 DUP
# SC-DUPE / OTP logic from Verify your email form
@pytest.mark.auth
@pytest.mark.sc_dupe
def test_register_new_account_and_verify_successfully_dup(driver):
    temp_email, mailbox_id = new_temp_mail()


    setup_page(driver)
    go_to_signup_with_email(temp_email)
    enter_password(VALID_PASSWORD)
    click_continue_entered_password()
    #pause_for_manual_captcha()

    fill_tell_us_more_about_you_form(
        generate_random_display_name(),
        "May",
        "10",
        "2005",
        "Male",
    )
    click_continue_tell_us_more_about_you()
    #pause_for_manual_captcha()

    assert is_element_visible(SignUpSelectors.VERIFY_EMAIL_TITLE, timeout=20), (
        "Verify your email screen did not appear after registration."
    )

    displayed_email = get_element_text(SignUpSelectors.SENT_TO_EMAIL)
    assert displayed_email is not None, "Displayed verification email was not found."
    assert displayed_email.strip() == temp_email, (
        f"Displayed email '{displayed_email}' did not match expected '{temp_email}'."
    )

    verification_code = get_verification_code_temp(
        mailbox_id,
        timeout_seconds=60,
        poll_every_seconds=5,
    )
    assert verification_code is not None, "Verification code was not received."

    enter_verification_code(verification_code)
    click_verify_email_button()
    assert is_element_visible(HomeSelectors.PROFILE_MENU_PROFILE, timeout=20), (
            "User is not correctly logged in"
        )
    assert not is_element_visible(SignUpSelectors.VERIFY_EMAIL_TITLE), (
            "User is still stuck on Verify your email after entering the OTP code."
        )































































































#====================================================================================================================================================

#Test M1-003 ACCOUNT EXISTS
@pytest.mark.smoke
@pytest.mark.auth
def test_duplicate_email_redirects_to_welcome_back(driver):
    setup_page(driver)
    go_to_signup_with_email(EXISTING_EMAIL)

    assert is_element_visible(SignInSelectors.WELCOME_BACK_MSG), (
        "Didn't go do welcome back form. Incorrectly handled account already exists."
    )

#========================================================
#                    TEST M1-003
#========================================================

#Test M1-003A ACCOUNT EXISTS
@pytest.mark.smoke
@pytest.mark.replica
#@pytest.mark.auth
#this test is guaranteed to fail because we dont even show the error. all it does is just
#opens the "Welcome Back" form
def test_sign_up_duplicate_email_shows_account_exists(driver):
    setup_page(driver)
    go_to_signup_with_email(EXISTING_EMAIL)

    assert is_element_visible(SignUpSelectors.ACCOUNT_ALREADY_EXISTS_MSG), (
        "Account already exists message was not shown."
    )

#Test M1-003 DUP ACCOUNT EXISTS
@pytest.mark.smoke
@pytest.mark.auth
@pytest.mark.sc_dupe
def test_duplicate_email_redirects_to_welcome_back(driver):
    setup_page(driver)
    #go_to_signup_with_email(EXISTING_EMAIL)
    open_create_account_flow()
    sign_up_enter_email(EXISTING_EMAIL)
    enter_password(VALID_PASSWORD)
    click_continue_entered_password()
    assert is_element_visible(SignInSelectors.WELCOME_BACK_MSG), (
        "Didn't go do welcome back form. Incorrectly handled account already exists."
    )


#Test M1-003A DUP ACCOUNT EXISTS
@pytest.mark.smoke
@pytest.mark.replica
@pytest.mark.sc_dupe
#@pytest.mark.auth
#this test is guaranteed to fail because we dont even show the error. all it does is just
#opens the "Welcome Back" form
def test_sign_up_duplicate_email_shows_account_exists_dup(driver):
    setup_page(driver)
    #go_to_signup_with_email(EXISTING_EMAIL)
    open_create_account_flow()
    sign_up_enter_email(EXISTING_EMAIL)
    enter_password(VALID_PASSWORD)
    click_continue_entered_password()

    assert is_element_visible(SignUpSelectors.ACCOUNT_ALREADY_EXISTS_MSG), (
        "Account already exists message was not shown."
    )


#========================================================
#                    TEST M1-004
#========================================================

#Test M1-004
@pytest.mark.smoke
@pytest.mark.auth
def test_sign_up_invalid_email_format(driver):
    setup_page(driver)
    go_to_signup_with_email(INVALID_EMAIL)

    assert is_element_visible(AuthSelectors.ERROR_INVALID_EMAIL_OR_URL), (
        "Invalid email error was not shown."
    )
#Test M1-004 DUP
@pytest.mark.smoke
@pytest.mark.auth
@pytest.mark.sc_dupe
def test_sign_up_invalid_email_format_dup(driver):
    setup_page(driver)
    go_to_signup_with_email(INVALID_EMAIL)
    enter_password(VALID_PASSWORD)
    click_continue_entered_password()
    assert is_element_visible(AuthSelectors.ERROR_INVALID_EMAIL_OR_URL), (
        "Invalid email error was not shown."
    )


#========================================================
#                    TEST M1-005
#========================================================
@pytest.mark.auth
def test_sign_up_short_password_continue_disabled(driver):
    setup_page(driver)
    random_email = generate_random_unverified_email()

    go_to_signup_with_email(random_email)
    enter_password(SHORT_PASSWORD)

    assert is_element_disabled(AuthSelectors.CONTINUE_ENTER_PASSWORD), (
        "Continue button was not disabled for short password."
    )

#========================================================
#                    TEST M1-006
#========================================================
def reach_tell_us_more_page(driver):
    setup_page(driver)
    open_create_account_flow()
    random_email = generate_random_unverified_email()

    sign_up_enter_email(random_email)
    enter_password(VALID_PASSWORD)
    click_continue_entered_password()

    assert is_element_visible(SignUpSelectors.TELL_US_MORE_TITLE), (
        "Tell us more about you page did not appear."
    )

# M1-006
# all empty
@pytest.mark.auth
def test_signup_rejects_missing_year(driver):
    reach_tell_us_more_page(driver)
    assert is_element_disabled(SignUpSelectors.CONTINUE_SUBMIT_SIGNUP), (
        "Continue button should be disabled when display name is missing."
    )

# M1-006-A
# display name empty
@pytest.mark.auth
def test_signup_rejects_missing_display_name(driver):
    reach_tell_us_more_page(driver)

    select_month("October")
    select_day("13")
    select_year("2005")
    select_gender("Male")
    assert is_element_disabled(SignUpSelectors.CONTINUE_SUBMIT_SIGNUP), (
        "Continue button should be disabled when display name is missing."
    )



# M1-006-B
# month empty
@pytest.mark.auth
def test_signup_rejects_missing_month(driver):
    reach_tell_us_more_page(driver)

    enter_display_name(generate_random_display_name())
    select_day("13")
    select_year("2005")
    select_gender("Male")
    assert is_element_disabled(SignUpSelectors.CONTINUE_SUBMIT_SIGNUP), (
        "Continue button should be disabled when display name is missing."
    )



# M1-006-C
# day empty
@pytest.mark.auth
def test_signup_rejects_missing_day(driver):
    reach_tell_us_more_page(driver)

    enter_display_name(generate_random_display_name())
    select_month("October")
    select_year("2005")
    select_gender("Male")
    assert is_element_disabled(SignUpSelectors.CONTINUE_SUBMIT_SIGNUP), (
        "Continue button should be disabled when display name is missing."
    )



# M1-006-D
# year empty
@pytest.mark.auth
def test_signup_rejects_missing_year(driver):
    reach_tell_us_more_page(driver)

    enter_display_name(generate_random_display_name())
    select_month("October")
    select_day("13")
    select_gender("Male")
    assert is_element_disabled(SignUpSelectors.CONTINUE_SUBMIT_SIGNUP), (
        "Continue button should be disabled when display name is missing."
    )


# M1-006-E
# gender empty
@pytest.mark.auth
def test_signup_rejects_missing_gender(driver):
    reach_tell_us_more_page(driver)

    enter_display_name(generate_random_display_name())
    select_month("October")
    select_day("13")
    select_year("2005")
    assert is_element_disabled(SignUpSelectors.CONTINUE_SUBMIT_SIGNUP), (
        "Continue button should be disabled when display name is missing."
    )

#========================================================
#                    TEST M1-007
#========================================================

#Test M1-007
@pytest.mark.auth
def test_sign_in_before_email_verification_is_completed(driver):
    random_email = generate_random_unverified_email()

    # Step 1: register new account without completing verification
    setup_page(driver)
    go_to_signup_with_email(random_email)
    enter_password(VALID_PASSWORD)
    click_continue_entered_password()

    fill_tell_us_more_about_you_form(
        generate_random_display_name(),
        "May",
        "10",
        "2005",
        "Male",
    )
    click_continue_tell_us_more_about_you()

    assert is_element_visible(SignUpSelectors.CHECK_YOUR_INBOX_TITLE), (
        "Check your inbox screen did not appear after registration."
    )

    # Step 2: try to sign in before verifying email
    setup_page(driver)
    click_header_sign_in()
    auth_enter_email_or_url(random_email)
    click_continue()


    enter_password(VALID_PASSWORD)
    click_continue_entered_password()
    # import time
    # time.sleep(10)

    # Expected: account is still blocked / verification state is shown
    assert is_element_visible(SignUpSelectors.CHECK_YOUR_INBOX_TITLE), (
        "Verification prompt was not shown."
    )
@pytest.mark.auth
@pytest.mark.sc_dupe
def test_sign_in_before_email_verification_is_completed_dup(driver):#migrated to work with our project
    random_email = generate_random_unverified_email()

    # Step 1: register new account without completing verification
    setup_page(driver)
    go_to_signup_with_email(random_email)

    enter_password(VALID_PASSWORD+"yaRabEr7amni##")
    click_continue_entered_password()

    fill_tell_us_more_about_you_form(
        generate_random_display_name(),
        "May",
        "10",
        "2005",
        "Male",
    )
    click_continue_tell_us_more_about_you()

    # assert is_element_visible(SignUpSelectors.CHECK_YOUR_INBOX_TITLE), (
    #     "Check your inbox screen did not appear after registration."
    # )
    assert is_element_visible(SignUpSelectors.VERIFY_EMAIL_TITLE), (
        "Verify your email screen did not appear after registration."
    )

    # Step 2: try to sign in before verifying email
    setup_page(driver)
    click_header_sign_in()


    auth_enter_email_or_url(random_email)


    click_continue()

    enter_password(VALID_PASSWORD)
    click_continue_entered_password()


    # Expected: verification state is shown
    assert is_element_visible(SignUpSelectors.VERIFY_EMAIL_TITLE), (
        "Verification prompt was not shown."
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
@pytest.mark.sc_dupe
def test_sign_up_empty_email_dup(driver):
    setup_page(driver)
    open_create_account_flow()
    enter_password(VALID_PASSWORD)
    click_continue_entered_password()

    assert is_element_visible(AuthSelectors.ERROR_INVALID_EMAIL_OR_URL), (
        "Error was not shown for empty email field."
    )

#========================================================
#                    TEST M1-029
#========================================================
@pytest.mark.auth
def test_sign_up_empty_password_continue_disabled(driver):
    setup_page(driver)
    go_to_signup_with_email(NEW_EMAIL)

    assert is_element_disabled(AuthSelectors.CONTINUE_ENTER_PASSWORD), (
        "Continue button was enabled with empty password."
    )
#========================================================
#                    TEST M1-030
#========================================================
@pytest.mark.auth
def test_sign_up_valid_password_enables_continue(driver):
    setup_page(driver)
    go_to_signup_with_email(NEW_EMAIL)
    enter_password(VALID_PASSWORD)

    assert not is_element_disabled(AuthSelectors.CONTINUE_ENTER_PASSWORD), (
        "Continue button stayed disabled for a valid password."
    )


#==================================================================================================
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
        generate_random_display_name(),
        "May",
        "10",
        "2005",
        "Male",
    )

    assert not is_element_disabled(SignUpSelectors.CONTINUE_SUBMIT_SIGNUP), (
        "Continue button stayed disabled after filling profile form."
    )

@pytest.mark.auth
def test_sign_up_valid_email_reaches_password_step(driver):
    setup_page(driver)
    go_to_signup_with_email(NEW_EMAIL)

    assert is_element_visible(AuthSelectors.CONTINUE_ENTER_PASSWORD), (
        "Password step did not appear for a new valid email."
    )
