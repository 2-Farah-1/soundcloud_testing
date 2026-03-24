import pytest
from selenium.webdriver.support.ui import WebDriverWait

import pages.settings_page.delete_account

from pages.settings_page.delete_account import (
    click_more_menu_dropdown,
    click_settings_button,
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


def setup_page(driver):
    driver.get("https://soundcloud.com/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    pages.settings_page.delete_account.driver = driver
    pages.settings_page.delete_account.wait = wait


@pytest.mark.smoke
@pytest.mark.settings
def test_delete_account(driver):
    setup_page(driver)

    click_more_menu_dropdown()
    click_settings_button()
    click_delete_account_button()
    switch_to_delete_account_iframe()

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
    click_delete_my_account_button()

    assert is_delete_account_success_title_visible(), "Delete account success title did not appear"

    click_delete_account_ok_got_it_button()

    driver.switch_to.default_content()

    assert is_signed_out_alert_visible(), "Signed out alert did not appear"