from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time

# import all your functions directly
from pages.sign_in_page import *

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
# TEST FLOW 2: invalid email
# =========================

# Step 0: cookies (optional)
click_header_create_account()

# Step 1: open auth
click_header_sign_in()
switch_to_auth_iframe()
time.sleep(2)
# Step 2: email
auth_enter_email_or_url("test@")
time.sleep(2)
click_continue()


if is_element_visible(AuthSelectors.ERROR_INVALID_EMAIL_OR_URL):
    print("TEST SUCCESS - Enter a valid email message is visible")
else:
    print("TEST FAILED")


time.sleep(5)