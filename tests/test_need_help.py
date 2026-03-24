from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time

# import all your functions directly
from pages.sign_in_page import *
from ui_selectors import SettingsSelectors

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
# TEST FLOW 5: Need Help
# =========================

# Step 0: cookies
click_reject_all_cookies()

# Step 1: open auth
click_header_create_account()
switch_to_auth_iframe()
time.sleep(2)

click_need_help()

if is_on_help_center() and is_element_visible(SignUpSelectors.HELP_CENTER_PAGE_TITLE):
    print("TEST PASSED - ON HELP CENTER PAGE")
else:
    print("TEST FAILED")


