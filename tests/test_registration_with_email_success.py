from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time

import pages.auth_page
import utils.browser_utils
import pages.sign_up_page
import pages.cookies_page

from pages.auth_page import (click_reject_all_cookies, click_header_create_account, switch_to_auth_iframe,
                             auth_enter_email_or_url, click_continue, enter_password, click_continue_entered_password)

from utils.browser_utils import pause_for_manual_captcha
from pages.sign_up_page import fill_tell_us_more_about_you_form,click_continue_tell_us_more_about_you
from pages.cookies_page import click_reject_all_cookies

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
# TEST FLOW 1: Successful Registration
# =========================

# Step 0: cookies
click_reject_all_cookies()

# Step 1: open auth
click_header_create_account()
switch_to_auth_iframe()
time.sleep(2)
# Step 2: email
auth_enter_email_or_url("canalvbm+rayburn@gmail.com")
time.sleep(2)
click_continue()
pause_for_manual_captcha()

# Step 3: password
enter_password("Ray@123123123")
time.sleep(2)
click_continue_entered_password()
pause_for_manual_captcha()

# Step 4: profile
fill_tell_us_more_about_you_form(
    "Rayburn1", "May", "10", "2005", "Male"
)

time.sleep(2)

click_continue_tell_us_more_about_you()
pause_for_manual_captcha()


############NEEEDS TO BE CONINUED
time.sleep(5)