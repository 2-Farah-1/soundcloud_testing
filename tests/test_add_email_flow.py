import pytest
from selenium.webdriver.support.ui import WebDriverWait

import pages.home_page
import pages.settings_page.add_email
import utils.browser_utils

from utils.session_utils import load_cookies
from utils.browser_utils import pause_for_manual_captcha
from utils.email_utils import get_pass_reset_link

from pages.home_page import click_more_menu_dropdown, click_settings_button
from pages.settings_page.add_email import (
    scroll_to_add_email_section,
    click_add_email_address_button,
    enter_add_email_address,
    click_add_email_button,
    click_resend_confirmation_email_button,
    click_remove_address_button,
    click_delete_email_button,
    is_enter_email_address_alert_visible,
    is_invalid_email_address_alert_visible,
    is_resend_confirmation_email_button_visible,
    is_resent_confirmation_email_alert_visible,
    get_resent_confirmation_email_address_text,
    is_email_confirmed_alert_visible,
    refresh_settings_page,
    is_added_email_visible,
    is_make_primary_button_visible,
)

# i'll be starting from farahelhebeishy@gmail.com
path = r"D:\SeleniumPython\SoundCloudE2ETesting\logged_in_cookies_farah-elhebeishy.json"


def setup_page(driver):
    driver.get("https://soundcloud.com/")
    wait = WebDriverWait(driver, 20)

    pages.home_page.driver = driver
    pages.home_page.wait = wait

    pages.settings_page.add_email.driver = driver
    pages.settings_page.add_email.wait = wait

    utils.browser_utils.driver = driver
    utils.browser_utils.wait = wait

    load_cookies(driver, path)
    driver.refresh()
    pause_for_manual_captcha()

    print("URL:", driver.current_url)
    print("Title:", driver.title)
    print("Number of iframes:", len(driver.find_elements("tag name", "iframe")))

    driver.maximize_window()


@pytest.mark.smoke
@pytest.mark.settings
def test_add_email_address(driver):
    setup_page(driver)

    gmail_address = input("Enter Gmail address: ").strip()
    app_password = input("Enter 16-digit app password: ").strip()
    new_email = input("Enter the email address to add: ").strip()

    print("URL:", driver.current_url)
    print("Title:", driver.title)
    print("Number of iframes:", len(driver.find_elements("tag name", "iframe")))

    click_more_menu_dropdown()
    click_settings_button()

    scroll_to_add_email_section()
    click_add_email_address_button()

    click_add_email_button()
    assert is_enter_email_address_alert_visible(), "Enter your email address alert did not appear"

    enter_add_email_address("dhgsdjh")
    click_add_email_button()
    assert is_invalid_email_address_alert_visible(), "This email address is invalid alert did not appear"

    enter_add_email_address(new_email)
    click_add_email_button()


    assert is_resend_confirmation_email_button_visible(), "Resend confirmation email button did not appear"

    confirmation_link = get_pass_reset_link(gmail_address, app_password)
    assert confirmation_link is not None, "Confirmation link was not found in email before resend"

    click_resend_confirmation_email_button()

    assert is_resent_confirmation_email_alert_visible(), "Resent confirmation email alert did not appear"

    resent_email_address = get_resent_confirmation_email_address_text()
    assert resent_email_address == new_email, (
        f"Resent confirmation email address mismatch. Expected: {new_email}, Got: {resent_email_address}"
    )

    confirmation_link = get_pass_reset_link(gmail_address, app_password)
    assert confirmation_link is not None, "Confirmation link was not found in email after resend"

    original_window = driver.current_window_handle
    driver.execute_script("window.open(arguments[0], '_blank');", confirmation_link)
    driver.switch_to.window(driver.window_handles[-1])

    assert is_email_confirmed_alert_visible(), "Your email address is confirmed alert did not appear"

    driver.close()
    driver.switch_to.window(original_window)

    refresh_settings_page()


    scroll_to_add_email_section()

    assert is_added_email_visible(new_email), "Added email is not visible after confirmation"
    assert is_make_primary_button_visible(new_email), "Make primary button is not visible beside the added email"

    click_remove_address_button(new_email)
    click_delete_email_button()


    refresh_settings_page()

    assert not is_added_email_visible(new_email), "Email is still visible after deletion"