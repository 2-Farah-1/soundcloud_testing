import pytest
from selenium.webdriver.support.ui import WebDriverWait

import pages.cookies_page
import pages.home_page
import pages.auth_page
import utils.browser_utils

from pages.cookies_page import click_reject_all_cookies
from pages.home_page import click_header_create_account
from pages.auth_page import switch_to_auth_iframe, click_need_help
from utils.browser_utils import is_on_help_center, is_element_visible
from ui_selectors import SignUpSelectors


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
def test_need_help_opens_help_center(driver):
    setup_page(driver)

    click_reject_all_cookies()

    click_header_create_account()
    switch_to_auth_iframe()

    click_need_help()

    driver.switch_to.default_content()

    assert is_on_help_center(), "Did not navigate to Help Center"
    assert is_element_visible(SignUpSelectors.HELP_CENTER_PAGE_TITLE), "Help Center page title is not visible"