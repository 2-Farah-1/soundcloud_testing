from selenium.webdriver.support import expected_conditions as EC
from ui_selectors import SettingsSelectors

driver = None
wait = None



def click_add_facebook_account_button():
    wait.until(EC.element_to_be_clickable(SettingsSelectors.ADD_FACEBOOK_ACCOUNT_BTN)).click()


def click_add_google_account_button():
    wait.until(EC.element_to_be_clickable(SettingsSelectors.ADD_GOOGLE_ACCOUNT_BTN)).click()


def click_add_apple_account_button():
    wait.until(EC.element_to_be_clickable(SettingsSelectors.ADD_APPLE_ACCOUNT_BTN)).click()