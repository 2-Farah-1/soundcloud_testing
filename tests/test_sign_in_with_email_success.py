from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time

# import all your functions directly
from pages.sign_in_page import *
from ui_selectors import SignInSelectors

# setup browser
service = Service(r"C:\browserdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://soundcloud.com/")
driver.maximize_window()
print(driver.title)

# define wait here
wait = WebDriverWait(driver, 20)

# VERY IMPORTANT: assign to functions file globals
import pages.sign_in_page
pages.login_page.driver = driver
pages.login_page.wait = wait


# =========================
# TEST FLOW: Successful Sign Up
# =========================

# Step 0: cookies
click_reject_all_cookies()

# Step 1: open auth
click_header_create_account()
switch_to_auth_iframe()
time.sleep(2)


# Step 2: email
auth_enter_email_or_url("farahelhebeishy@gmail.com")
time.sleep(2)
click_continue()
pause_for_manual_captcha()
# Step 3: password
enter_password("Test1test2Test3")
time.sleep(2)
click_continue_entered_password()
pause_for_manual_captcha()
if is_element_visible(SignInSelectors.SIGNED_IN_PROFILE_BTN):
    print("TEST PASSED - Signed in successfully!")
else:
    print("TEST FAILED - Signed in failed!")

############NEEEDS TO BE CONINUED
time.sleep(5)