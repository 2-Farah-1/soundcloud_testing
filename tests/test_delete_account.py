import pytest
from selenium.webdriver.support.ui import WebDriverWait

import pages.settings_page.delete_account
import utils.browser_utils
import pages.home_page

from utils.session_utils import load_cookies
from utils.browser_utils import pause_for_manual_captcha

from pages.home_page import     click_more_menu_dropdown, click_settings_button
from pages.settings_page.delete_account import (

    click_delete_account_button,
    switch_to_delete_account_iframe,
    is_delete_account_title_visible,
    click_delete_reason_another_account,
    click_delete_reason_new_account,
    click_delete_reason_privacy_options,
    click_delete_reason_no_longer_creating,
    click_delete_reason_copyright_issues,
    click_delete_reason_no_pro,
    click_delete_reason_switched_service,
    click_delete_reason_hacked,
    click_delete_reason_cant_remove_tracks,
    click_delete_reason_harassment,
    click_delete_reason_too_much_spam,
    click_delete_reason_other,
    enter_delete_other_reason,
    click_delete_account_confirm_checkbox,
    click_delete_my_account_button,
    is_delete_account_success_title_visible,
    click_delete_account_ok_got_it_button,
    is_signed_out_alert_visible,
)
#i'll be starting from softwareacc198
path=r'D:\SeleniumPython\SoundCloudE2ETesting\logged_in_cookies_softwaretestacc198.json'

def setup_page(driver):
    #driver.get("https://soundcloud.com/")
    #driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    pages.home_page.driver = driver
    pages.home_page.wait = wait

    pages.settings_page.delete_account.driver = driver
    pages.settings_page.delete_account.wait = wait

    utils.browser_utils.driver = driver
    utils.browser_utils.wait = wait

    #pause_for_manual_captcha()
    load_cookies(driver, path)
    pause_for_manual_captcha()
    print("URL:", driver.current_url)
    print("Title:", driver.title)
    print("Number of iframes:", len(driver.find_elements("tag name", "iframe")))

    driver.maximize_window()



@pytest.mark.smoke
@pytest.mark.settings
def test_delete_account(driver): #starts with account logged in at home page
    setup_page(driver)
    pause_for_manual_captcha()

    print("URL:", driver.current_url)
    print("Title:", driver.title)
    print("Number of iframes:", len(driver.find_elements("tag name", "iframe")))

    click_more_menu_dropdown()
    click_settings_button()

    click_delete_account_button()
    #pause_for_manual_captcha()

    #switch_to_delete_account_iframe()
    pause_for_manual_captcha()

    assert is_delete_account_title_visible(), "Delete account title did not appear"

    click_delete_reason_another_account()
    click_delete_reason_new_account()
    click_delete_reason_privacy_options()
    click_delete_reason_no_longer_creating()
    click_delete_reason_copyright_issues()
    click_delete_reason_no_pro()
    click_delete_reason_switched_service()
    click_delete_reason_hacked()
    click_delete_reason_cant_remove_tracks()
    click_delete_reason_harassment()
    click_delete_reason_too_much_spam()

    click_delete_reason_other()


    enter_delete_other_reason("i am not having fun")

    click_delete_account_confirm_checkbox()
    pause_for_manual_captcha()

    click_delete_my_account_button()
    pause_for_manual_captcha()


    assert is_delete_account_success_title_visible(), "Delete account success title did not appear"

    click_delete_account_ok_got_it_button()
    pause_for_manual_captcha()


    driver.switch_to.default_content()
    pause_for_manual_captcha()


    assert is_signed_out_alert_visible(), "Signed out alert did not appear"