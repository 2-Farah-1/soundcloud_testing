import re
import pytest
from selenium.webdriver.support.ui import WebDriverWait

import pages.settings_page.password_reset
import utils.browser_utils
import pages.home_page

from utils.session_utils import load_cookies
from utils.browser_utils import pause_for_manual_captcha

from pages.home_page import click_more_menu_dropdown, click_settings_button
from pages.settings_page.password_reset import (
    scroll_to_send_password_reset_link_button,
    click_send_password_reset_link_button,
    is_password_reset_link_sent_alert_visible,
    get_password_reset_link_sent_alert_text,
)

# enter the email of the account already signed in with this cookies session
SIGNED_IN_EMAIL = "hasanhgsagin+burgess@gmail.com"

# i'll be starting from softwareacc198
path = r'D:\SeleniumPython\SoundCloudE2ETesting\logged_in_cookies_hassanburgess.json'


def setup_page(driver):
    wait = WebDriverWait(driver, 20)

    pages.home_page.driver = driver
    pages.home_page.wait = wait

    pages.settings_page.password_reset.driver = driver
    pages.settings_page.password_reset.wait = wait

    utils.browser_utils.driver = driver
    utils.browser_utils.wait = wait

    load_cookies(driver, path)
    pause_for_manual_captcha()
    driver.maximize_window()


def extract_email_from_alert(alert_text):
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', alert_text)
    return match.group(0) if match else None


@pytest.mark.smoke
@pytest.mark.settings
def test_send_password_reset_link(driver):  # starts with account logged in at home page
    setup_page(driver)

    click_more_menu_dropdown()
    click_settings_button()


    scroll_to_send_password_reset_link_button()


    click_send_password_reset_link_button()


    assert is_password_reset_link_sent_alert_visible(), \
        "Password reset link sent alert did not appear"

    alert_text = get_password_reset_link_sent_alert_text()
    print("Password reset alert text:", alert_text)

    alert_email = extract_email_from_alert(alert_text)

    assert alert_email is not None, \
        "No email was found inside the password reset alert text"

    assert alert_email.lower() == SIGNED_IN_EMAIL.lower(), \
        f"Expected email '{SIGNED_IN_EMAIL}' but found '{alert_email}'"

