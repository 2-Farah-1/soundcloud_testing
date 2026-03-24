from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui_selectors import AuthSelectors, CookieSelectors, HomeSelectors, SignUpSelectors, SignInSelectors
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select



from ui_selectors import (
    HomeSelectors,
    SettingsSelectors,
    SettingsDeleteAccountSection,
)

driver=None
wait=None


def click_delete_account_button():
    button = wait.until(EC.element_to_be_clickable(SettingsSelectors.DELETE_ACCOUNT_BTN))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
    button.click()


def switch_to_delete_account_iframe():
    driver.switch_to.default_content()

    iframe = wait.until(
        EC.presence_of_element_located(
            (
                SettingsDeleteAccountSection.DELETE_ACCOUNT_IFRAME
            )
        )
    )
    driver.switch_to.frame(iframe)


def is_delete_account_title_visible():
    try:
        return wait.until(
            EC.visibility_of_element_located(
                SettingsDeleteAccountSection.DELETE_ACCOUNT_TITLE
            )
        ).is_displayed()
    except:
        return False


def click_delete_reason_another_account():
    element = wait.until(
        EC.presence_of_element_located(
            SettingsDeleteAccountSection.DELETE_REASON_ANOTHER_ACCOUNT
        )
    )
    driver.execute_script("arguments[0].click();", element)


def click_delete_reason_new_account():
    element = wait.until(
        EC.presence_of_element_located(
            SettingsDeleteAccountSection.DELETE_REASON_NEW_ACCOUNT
        )
    )
    driver.execute_script("arguments[0].click();", element)


def click_delete_reason_privacy_options():
    element = wait.until(
        EC.presence_of_element_located(
            SettingsDeleteAccountSection.DELETE_REASON_PRIVACY_OPTIONS
        )
    )
    driver.execute_script("arguments[0].click();", element)


def click_delete_reason_no_longer_creating():
    element = wait.until(
        EC.presence_of_element_located(
            SettingsDeleteAccountSection.DELETE_REASON_NO_LONGER_CREATING
        )
    )
    driver.execute_script("arguments[0].click();", element)


def click_delete_reason_copyright_issues():
    element = wait.until(
        EC.presence_of_element_located(
            SettingsDeleteAccountSection.DELETE_REASON_COPYRIGHT_ISSUES
        )
    )
    driver.execute_script("arguments[0].click();", element)


def click_delete_reason_no_pro():
    element = wait.until(
        EC.presence_of_element_located(
            SettingsDeleteAccountSection.DELETE_REASON_NO_PRO
        )
    )
    driver.execute_script("arguments[0].click();", element)


def click_delete_reason_switched_service():
    element = wait.until(
        EC.presence_of_element_located(
            SettingsDeleteAccountSection.DELETE_REASON_SWITCHED_SERVICE
        )
    )
    driver.execute_script("arguments[0].click();", element)


def click_delete_reason_hacked():
    element = wait.until(
        EC.presence_of_element_located(
            SettingsDeleteAccountSection.DELETE_REASON_HACKED
        )
    )
    driver.execute_script("arguments[0].click();", element)


def click_delete_reason_cant_remove_tracks():
    element = wait.until(
        EC.presence_of_element_located(
            SettingsDeleteAccountSection.DELETE_REASON_CANT_REMOVE_TRACKS
        )
    )
    driver.execute_script("arguments[0].click();", element)


def click_delete_reason_harassment():
    element = wait.until(
        EC.presence_of_element_located(
            SettingsDeleteAccountSection.DELETE_REASON_HARASSMENT
        )
    )
    driver.execute_script("arguments[0].click();", element)


def click_delete_reason_too_much_spam():
    element = wait.until(
        EC.presence_of_element_located(
            SettingsDeleteAccountSection.DELETE_REASON_TOO_MUCH_SPAM
        )
    )
    driver.execute_script("arguments[0].click();", element)


def click_delete_reason_other():
    element = wait.until(
        EC.presence_of_element_located(
            SettingsDeleteAccountSection.DELETE_REASON_OTHER
        )
    )
    driver.execute_script("arguments[0].click();", element)


def enter_delete_other_reason(text):
    input_field = wait.until(
        EC.visibility_of_element_located(
            SettingsDeleteAccountSection.DELETE_OTHER_REASON_INPUT
        )
    )
    input_field.clear()
    input_field.send_keys(text)


def click_delete_account_confirm_checkbox():
    checkbox = wait.until(
        EC.presence_of_element_located(
            SettingsDeleteAccountSection.DELETE_ACCOUNT_CONFIRM_CHECKBOX
        )
    )
    driver.execute_script("arguments[0].click();", checkbox)


def click_delete_my_account_button():
    button = wait.until(
        EC.presence_of_element_located(
            SettingsDeleteAccountSection.DELETE_MY_ACCOUNT_BTN
        )
    )
    driver.execute_script("arguments[0].click();", button)


def is_delete_account_success_title_visible():
    try:
        return wait.until(
            EC.visibility_of_element_located(
                SettingsDeleteAccountSection.DELETE_ACCOUNT_SUCCESS_TITLE
            )
        ).is_displayed()
    except:
        return False


def click_delete_account_ok_got_it_button():
    button = wait.until(
        EC.presence_of_element_located(
            SettingsDeleteAccountSection.DELETE_ACCOUNT_OK_GOT_IT_BTN
        )
    )
    driver.execute_script("arguments[0].click();", button)


def is_signed_out_alert_visible():
    try:
        return wait.until(
            EC.visibility_of_element_located(
                SettingsDeleteAccountSection.SIGNED_OUT_ALERT
            )
        ).is_displayed()
    except:
        return False