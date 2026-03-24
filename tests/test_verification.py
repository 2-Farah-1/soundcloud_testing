import time
import pages.sign_in_page

from selenium.webdriver.support.ui import WebDriverWait

from pages.auth_page import (
    open_auth,
    auth_enter_email_or_url,
    click_continue
)
from utils.browser_utils import (
    get_element_text,
    is_element_visible
)
from pages.sign_up_page import (
    click_open_gmail_button,
    click_help_center_link,
    click_send_again_button,
    click_back_to_login_button,
    click_close_button,
)

from ui_selectors import SignUpSelectors, AuthSelectors, SettingsSelectors
from utils.email_utils import get_verification_link


# =========================
# CONFIG
# =========================

GMAIL_ADDRESS = "softwaretestacc198@gmail.com"
GMAIL_APP_PASSWORD = "zupqwxwlerldqgcf"


def setup_page(driver):
    driver.get("https://soundcloud.com/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    pages.login_page.driver = driver
    pages.login_page.wait = wait


# =========================
# HELPERS
# =========================

def switch_to_new_window(driver):
    original_window = driver.current_window_handle

    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

    for window in driver.window_handles:
        if window != original_window:
            driver.switch_to.window(window)
            return original_window

    return original_window


def close_new_window_and_return(driver, original_window):
    driver.close()
    driver.switch_to.window(original_window)


def wait_for_non_blank_url(driver, timeout=20):
    WebDriverWait(driver, timeout).until(lambda d: d.current_url != "about:blank")


def go_to_check_your_inbox_page(email):
    open_auth()
    auth_enter_email_or_url(email)
    click_continue()


def wait_for_verification_email(gmail_address, app_password, timeout=60, poll_every=5):
    end_time = time.time() + timeout
    latest_link = None

    while time.time() < end_time:
        latest_link = get_verification_link(gmail_address, app_password)
        if latest_link:
            return latest_link
        time.sleep(poll_every)

    return None


def wait_for_new_verification_link(old_link, gmail_address, app_password, timeout=60, poll_every=5):
    end_time = time.time() + timeout

    while time.time() < end_time:
        candidate = get_verification_link(gmail_address, app_password)
        if candidate and candidate != old_link:
            return candidate
        time.sleep(poll_every)

    return None


def open_link_in_new_tab(driver, link):
    driver.execute_script("window.open(arguments[0], '_blank');", link)
    original_window = driver.current_window_handle

    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

    for window in driver.window_handles:
        if window != original_window:
            driver.switch_to.window(window)
            return original_window

    return original_window


def assert_displayed_email_matches(expected_email):
    displayed_email = get_element_text(SignUpSelectors.VERIFICATION_EMAIL_TEXT)
    assert displayed_email is not None, "Verification email text was not found"
    assert displayed_email.strip() == expected_email



# =========================
# MINI TEST 1
# user clicks on open gmail then we get verification link
# =========================

def test_open_gmail_then_get_verification_link(driver):
    setup_page(driver)
    test_email = GMAIL_ADDRESS

    # commented because soundcloud.com tends to flag me :(
    # Step 1: Reach "check your inbox" page
    # go_to_check_your_inbox_page(test_email)

    # putting this instead for the time being
    input("Manually reach the 'Check your inbox' page, then press Enter to continue...")
    assert_displayed_email_matches(test_email)

    original_window = driver.current_window_handle
    click_open_gmail_button()
    switch_to_new_window(driver)
    wait_for_non_blank_url(driver)

    assert "mail.google.com" in driver.current_url.lower(), \
        f"Expected Gmail to open, got: {driver.current_url}"

    driver.close()
    driver.switch_to.window(original_window)

    first_link = wait_for_verification_email(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
    assert first_link is not None, "Verification email/link was not received"


# =========================
# MINI TEST 2
# user clicks on help center then clicks on back to login
# then gets the verification link from gmail
# no displayed-email assert here
# =========================

def test_help_center_then_back_to_login_then_get_verification_link(driver):
    setup_page(driver)

    # commented because soundcloud.com tends to flag me :(
    # Step 1: Reach "check your inbox" page
    # go_to_check_your_inbox_page(test_email)

    # putting this instead for the time being
    input("Manually reach the 'Check your inbox' page, then press Enter to continue...")

    original_window = driver.current_window_handle
    click_help_center_link()
    switch_to_new_window(driver)
    wait_for_non_blank_url(driver)

    assert is_element_visible(SignUpSelectors.HELP_CENTER_PAGE_TITLE), \
        "Help Center page title was not visible"

    help_center_title = get_element_text(SignUpSelectors.HELP_CENTER_PAGE_TITLE)
    assert help_center_title is not None, "Help Center title text could not be read"
    assert help_center_title.strip() == "Verify your email"

    driver.close()
    driver.switch_to.window(original_window)

    click_back_to_login_button()
    assert is_element_visible(AuthSelectors.EMAIL), \
        "Back to login did not return to page with email textbox"

    first_link = wait_for_verification_email(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
    assert first_link is not None, "Verification email/link was not received"


# =========================
# MINI TEST 3
# user clicks on resend email and then gets the new verification link
# =========================

def test_resend_email_then_get_new_verification_link(driver):
    setup_page(driver)
    test_email = GMAIL_ADDRESS

    # commented because soundcloud.com tends to flag me :(
    # Step 1: Reach "check your inbox" page
    # go_to_check_your_inbox_page(test_email)

    # putting this instead for the time being
    input("Manually reach the 'Check your inbox' page, then press Enter to continue...")
    assert_displayed_email_matches(test_email)

    first_link = wait_for_verification_email(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
    assert first_link is not None, "First verification email/link was not received"

    click_send_again_button()
    assert is_element_visible(SignUpSelectors.LINK_SENT_AGAIN_MSG), \
        "Link sent again message did not appear"

    second_link = wait_for_new_verification_link(
        first_link,
        GMAIL_ADDRESS,
        GMAIL_APP_PASSWORD
    )

    assert second_link is not None, "Second verification email/link was not received"
    assert second_link != first_link, "Second link should be different from the first link"


# =========================
# MINI TEST 4
# user clicks on resend email and makes sure old link doesnt work
# then the new one does
# =========================

def test_resend_email_old_link_fails_new_link_works(driver):
    setup_page(driver)
    test_email = GMAIL_ADDRESS

    # commented because soundcloud.com tends to flag me :(
    # Step 1: Reach "check your inbox" page
    # go_to_check_your_inbox_page(test_email)

    # putting this instead for the time being
    input("Manually reach the 'Check your inbox' page, then press Enter to continue...")


    assert_displayed_email_matches(test_email)

    first_link = wait_for_verification_email(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
    assert first_link is not None, "First verification email/link was not received"

    click_send_again_button()
    assert is_element_visible(SignUpSelectors.LINK_SENT_AGAIN_MSG), \
        "Link sent again message did not appear"

    second_link = wait_for_new_verification_link(
        first_link,
        GMAIL_ADDRESS,
        GMAIL_APP_PASSWORD
    )

    assert second_link is not None, "Second verification email/link was not received"

    original_window = open_link_in_new_tab(driver, first_link)
    wait_for_non_blank_url(driver)

    assert is_element_visible(SettingsSelectors.LINK_EXPIRED_OR_INVALID_ERROR), \
        "Old verification link did not show expired/invalid error"

    driver.close()
    driver.switch_to.window(original_window)

    original_window = open_link_in_new_tab(driver, second_link)
    wait_for_non_blank_url(driver)

    assert is_element_visible(SignUpSelectors.EMAIL_CONFIRMED_TITLE), \
        "Second verification link did not reach email confirmed page"

    confirmed_title = get_element_text(SignUpSelectors.EMAIL_CONFIRMED_TITLE)
    assert confirmed_title is not None, "Email confirmed title could not be read"
    assert "your email is confirmed" in confirmed_title.lower()

    driver.close()
    driver.switch_to.window(original_window)


# =========================
# MINI TEST 5
# user clicks on close button then gets the verification link from email
# =========================

def test_close_button_then_get_verification_link(driver):
    setup_page(driver)
    test_email = GMAIL_ADDRESS

    # commented because soundcloud.com tends to flag me :(
    # Step 1: Reach "check your inbox" page
    # go_to_check_your_inbox_page(test_email)

    # putting this instead for the time being
    input("Manually reach the 'Check your inbox' page, then press Enter to continue...")


    assert_displayed_email_matches(test_email)

    click_close_button()

    first_link = wait_for_verification_email(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
    assert first_link is not None, "Verification email/link was not received after closing"


def test_check_your_inbox_full_flow(driver):
    setup_page(driver)

    test_email = GMAIL_ADDRESS

    # commented because soundcloud.com tends to flag me :(
    # Step 1: Reach "check your inbox" page
    # go_to_check_your_inbox_page(test_email)

    # putting this instead for the time being
    input("Manually reach the 'Check your inbox' page, then press Enter to continue...")

    # Step 2: Assert displayed email equals entered email
    displayed_email = get_element_text(SignUpSelectors.VERIFICATION_EMAIL_TEXT)
    assert displayed_email is not None, "Verification email text was not found"
    assert displayed_email.strip() == test_email

    # Step 3: Assert we received the first email/link
    first_link = wait_for_verification_email(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
    assert first_link is not None, "First verification email/link was not received"

    # Step 4: Click Send again and assert success alert appears
    click_send_again_button()
    assert is_element_visible(SignUpSelectors.LINK_SENT_AGAIN_MSG), \
        "Link sent again message did not appear"

    # Step 5: Assert a new link was received
    second_link = None
    end_time = time.time() + 60

    while time.time() < end_time:
        candidate = get_verification_link(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        if candidate and candidate != first_link:
            second_link = candidate
            break
        time.sleep(5)

    assert second_link is not None, "Second verification email/link was not received"
    assert second_link != first_link, "Second link should be different from the first link"

    # Step 6: Test Open Gmail button redirect
    original_window = driver.current_window_handle
    click_open_gmail_button()
    switch_to_new_window(driver)
    wait_for_non_blank_url(driver)

    assert "mail.google.com" in driver.current_url.lower(), \
        f"Expected Gmail to open, got: {driver.current_url}"

    driver.close()
    driver.switch_to.window(original_window)

    # Step 7: Test Help Center redirect and title
    click_help_center_link()
    switch_to_new_window(driver)
    wait_for_non_blank_url(driver)

    assert is_element_visible(SignUpSelectors.HELP_CENTER_PAGE_TITLE), \
        "Help Center page title was not visible"

    help_center_title = get_element_text(SignUpSelectors.HELP_CENTER_PAGE_TITLE)
    assert help_center_title is not None, "Help Center title text could not be read"
    assert help_center_title.strip() == "Verify your email"

    driver.close()
    driver.switch_to.window(original_window)

    # Step 8: Test Back to login
    click_back_to_login_button()
    assert is_element_visible(AuthSelectors.EMAIL), \
        "Back to login did not return to page with email textbox"

    # Step 9: Reopen flow because we left the inbox page
    go_to_check_your_inbox_page(test_email)

    # Step 10: First link should now be expired/invalid
    original_window = open_link_in_new_tab(driver, first_link)
    wait_for_non_blank_url(driver)

    assert is_element_visible(SettingsSelectors.LINK_EXPIRED_OR_INVALID_ERROR), \
        "Old verification link did not show expired/invalid error"

    driver.close()
    driver.switch_to.window(original_window)

    # Step 11: Second link should work
    original_window = open_link_in_new_tab(driver, second_link)
    wait_for_non_blank_url(driver)

    assert is_element_visible(SignUpSelectors.EMAIL_CONFIRMED_TITLE), \
        "Second verification link did not reach email confirmed page"

    confirmed_title = get_element_text(SignUpSelectors.EMAIL_CONFIRMED_TITLE)
    assert confirmed_title is not None, "Email confirmed title could not be read"
    assert "your email is confirmed" in confirmed_title.lower()

