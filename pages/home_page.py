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




def click_close_popup():
    close_popup = wait.until(
        EC.element_to_be_clickable(HomeSelectors.CLOSE_POPUP)
    )
    close_popup.click()



def click_header_sign_in():
    sign_in = wait.until(
        EC.element_to_be_clickable(HomeSelectors.HEADER_SIGN_IN)
    )
    sign_in.click()


def click_header_create_account():
    create_acc = wait.until(
        EC.element_to_be_clickable(HomeSelectors.HEADER_CREATE_ACCOUNT)
    )
    create_acc.click()

def click_bottom_create_account():
    create_acc = wait.until(
        EC.element_to_be_clickable(HomeSelectors.BOTTOM_CREATE_ACCOUNT)
    )
    create_acc.click()

def click_bottom_sign_in():
    sign_in = wait.until(
        EC.element_to_be_clickable(HomeSelectors.BOTTOM_SIGN_IN)
    )
    sign_in.click()
#===================signed in

def click_more_menu_dropdown():
    button = wait.until(EC.element_to_be_clickable(HomeSelectors.MORE_MENU_DROPDOWN))
    button.click()


def click_settings_button():
    button = wait.until(EC.element_to_be_clickable(HomeSelectors.SETTINGS_BTN))
    button.click()

