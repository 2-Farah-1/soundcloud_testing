from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time

import pages.auth_page
import utils.browser_utils
import pages.home_page
import pages.cookies_page

from pages.cookies_page import click_reject_all_cookies
from pages.auth_page import ( click_header_create_account, switch_to_auth_iframe,
                             auth_enter_email_or_url, click_continue, enter_password, click_continue_entered_password)

from utils.browser_utils import is_element_disabled
from pages.home_page import click_header_sign_in
from ui_selectors import SignUpSelectors


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

pages.home_page.driver = driver
pages.home_page.wait = wait

pages.cookies_page.driver = driver
pages.cookies_page.wait = wait
# =========================
# TEST FLOW 3: Short Password (invalid)
# =========================

# Step 0: cookies
click_reject_all_cookies()

# Step 1: open auth
click_header_create_account()
##switch_to_auth_iframe()
time.sleep(2)
# Step 2: email
auth_enter_email_or_url("test@example.com")
time.sleep(2)
click_continue()

# Step 3: password
enter_password("1234")
time.sleep(2)
click_continue_entered_password()

if is_element_disabled(SignUpSelectors.CONTINUE_ENTER_PASSWORD):
    print("TEST SUCCESS! button is disabled")
else:
    print("TEST FAIL")

time.sleep(5)