from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time

import pages.auth_page
import utils.browser_utils
import pages.sign_up_page
import pages.cookies_page

from pages.auth_page import (click_header_create_account, switch_to_auth_iframe,
                             auth_enter_email_or_url, click_continue, enter_password, click_continue_entered_password)

from utils.browser_utils import is_element_visible
from pages.cookies_page import click_reject_all_cookies
from ui_selectors import AuthSelectors
# setup br
# owser
service = Service(r"C:\browserdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://soundcloud.com/")
driver.maximize_window()
print(driver.title)




# define wait here
wait = WebDriverWait(driver, 20)

# VERY IMPORTANT: assign to functions file globals
pages.auth_page.driver = driver
pages.auth_page.wait = wait

utils.browser_utils.driver = driver
utils.browser_utils.wait = wait

pages.sign_up_page.driver = driver
pages.sign_up_page.wait = wait

pages.cookies_page.driver = driver
pages.cookies_page.wait = wait

# =========================
# TEST FLOW: Invalid URL
# =========================

click_reject_all_cookies()

click_header_create_account()
switch_to_auth_iframe()
time.sleep(2)

auth_enter_email_or_url("https://soundcloud.com/this_profile_should_not_exist_123456789")
time.sleep(2)
click_continue()

if is_element_visible(AuthSelectors.ERROR_URL_DOESNT_EXIST):
    print("TEST PASSED - Error shown")
else:
    print("TEST FAILED")

time.sleep(5)
