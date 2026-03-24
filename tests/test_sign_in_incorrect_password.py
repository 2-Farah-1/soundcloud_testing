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
# TEST FLOW 1: Successful Registration
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

# Step 3: password
enter_password("123456")
time.sleep(2)
click_continue_entered_password()#this is the same button, bad naming sorry

if is_element_visible(SignInSelectors.ERROR_INCORRECT_PASSWORD):
    print("TEST PASSED - Error shown!")
else:
    print("TEST FAILED")


time.sleep(5)