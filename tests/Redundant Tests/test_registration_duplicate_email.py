from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time

import pages.auth_page
import utils.browser_utils
import pages.cookies_page
from pages.cookies_page import click_reject_all_cookies
from pages.auth_page import (click_header_create_account, switch_to_auth_iframe,
                             auth_enter_email_or_url, click_continue)
from utils.browser_utils import is_element_visible
from ui_selectors import SignUpSelectors

# setup browser
service = Service(r"C:\browserdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://soundcloud.com/")
driver.maximize_window()
print(driver.title)

# define wait here
wait = WebDriverWait(driver, 20)

pages.auth_page.driver = driver
pages.auth_page.wait = wait

pages.cookies_page.driver = driver
pages.cookies_page.wait = wait


# =========================
# TEST FLOW 4: Registeration with Duplicate Email
# =========================

# Step 0: cookies
click_reject_all_cookies()

# Step 1: open auth
click_header_create_account()
#switch_to_auth_iframe()
time.sleep(2)


# Step 2: email
auth_enter_email_or_url("canalvbm+rayburn@gmail.com")
time.sleep(2)
click_continue()

if is_element_visible(SignUpSelectors.ACCOUNT_ALREADY_EXISTS_MSG):
    print("TEST SUCCESS - Account already exists message is visible")
else:
    print("TEST FAILED")


time.sleep(5)