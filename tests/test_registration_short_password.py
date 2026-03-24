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
# TEST FLOW 3: Short Password (invalid)
# =========================

# Step 0: cookies
click_header_create_account()

# Step 1: open auth
click_header_sign_in()
switch_to_auth_iframe()
time.sleep(2)
# Step 2: email
auth_enter_email_or_url("test@example.com")
time.sleep(2)
click_continue()

# Step 3: password
enter_password("1234")
time.sleep(2)
click_continue_entered_password()

if is_button_disabled(SignUpSelectors.CONTINUE_ENTER_PASSWORD):
    print("TEST SUCCESS! button is disabled")
else:
    print("TEST FAIL")

time.sleep(5)