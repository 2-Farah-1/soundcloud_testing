from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time

from pages.sign_in_page import *
from ui_selectors import SignUpSelectors

service = Service(r"C:\browserdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://soundcloud.com/")
driver.maximize_window()
print(driver.title)

wait = WebDriverWait(driver, 20)

import pages.sign_in_page
pages.login_page.driver = driver
pages.login_page.wait = wait


# =========================
# TEST FLOW: Brand New Email (not in database)
# =========================

click_reject_all_cookies()

click_header_create_account()
switch_to_auth_iframe()
time.sleep(2)

auth_enter_email_or_url("brandnewemailfortesting123456@example.com")
time.sleep(2)
click_continue()

if is_element_visible(SignUpSelectors.CREATE_ACCOUNT_TITLE):
    print("TEST PASSED - Create account page appeared for new email!")
else:
    print("TEST FAILED")

time.sleep(5)
