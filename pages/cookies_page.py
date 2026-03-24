from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui_selectors import AuthSelectors, CookieSelectors, HomeSelectors, SignUpSelectors, SignInSelectors
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select

driver=None
wait=None


#================================================
#              Cookie Popup
#================================================
def click_reject_all_cookies():
    reject_all_cookies = wait.until(
        EC.element_to_be_clickable(CookieSelectors.REJECT_ALL)
    )
    reject_all_cookies.click()

def click_i_accept():
    accept_cookies = wait.until(
        EC.element_to_be_clickable(CookieSelectors.I_ACCEPT)
    )
    accept_cookies.click()

def click_manage_preferences():
    manage_preferences = wait.until(
        EC.element_to_be_clickable(CookieSelectors.MANAGE_PREFERENCES)
    )
    manage_preferences.click()

#================================================
#              Manage Your PPreferences form
#================================================


#needs to be done
