

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
# TEST FLOW: Check password visibility
# =========================


# initial state (should be hidden)
if is_password_hidden():
    print("Initially hidden ✅")
else:
    print("Initial state incorrect ❌")

# click to show password
click_show_password()

if is_password_visible():
    print("Password is visible after click ✅")
else:
    print("Password did NOT become visible ❌")

# click again to hide
click_show_password()

if is_password_hidden():
    print("Password hidden again ✅")
else:
    print("Password did NOT hide again ❌")