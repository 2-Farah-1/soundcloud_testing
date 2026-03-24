from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from ui_selectors import SettingsSelectors, SettingsAddEmailSection

driver = None
wait = None


def scroll_to_add_email_section():
    element = wait.until(EC.presence_of_element_located(SettingsSelectors.ADD_EMAIL_ADDRESS_BTN))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)


def click_add_email_address_button():
    wait.until(EC.element_to_be_clickable(SettingsSelectors.ADD_EMAIL_ADDRESS_BTN)).click()


def enter_add_email_address(email_text):
    element = wait.until(EC.visibility_of_element_located(SettingsAddEmailSection.NEW_EMAIL_INPUT))
    element.clear()
    element.send_keys(email_text)


def click_add_email_button():
    wait.until(EC.element_to_be_clickable(SettingsAddEmailSection.ADD_EMAIL_BTN)).click()


def click_resend_confirmation_email_button():
    wait.until(EC.element_to_be_clickable(SettingsAddEmailSection.RESEND_CONFIRMATION_EMAIL_BTN)).click()


def click_remove_address_button(email_address):
    button_locator = (
        By.XPATH,
        f"//span[contains(@class,'accountEmailControl__displayEmailText') and normalize-space()='{email_address}']"
        f"/ancestor::*[contains(@class,'accountEmailControl')][1]"
        f"//button[contains(@class,'accountEmailControl__remove')]"
    )
    wait.until(EC.element_to_be_clickable(button_locator)).click()


def click_delete_email_button():
    wait.until(EC.element_to_be_clickable(SettingsAddEmailSection.DELETE_EMAIL_BTN)).click()


def is_enter_email_address_alert_visible():
    try:
        wait.until(EC.visibility_of_element_located(SettingsAddEmailSection.ENTER_EMAIL_ADDRESS_ALERT))
        return True
    except Exception:
        return False


def is_invalid_email_address_alert_visible():
    try:
        wait.until(EC.visibility_of_element_located(SettingsAddEmailSection.INVALID_EMAIL_ADDRESS_ALERT))
        return True
    except Exception:
        return False


def is_resend_confirmation_email_button_visible():
    try:
        wait.until(EC.visibility_of_element_located(SettingsAddEmailSection.RESEND_CONFIRMATION_EMAIL_BTN))
        return True
    except Exception:
        return False


def is_resent_confirmation_email_alert_visible():
    try:
        wait.until(EC.visibility_of_element_located(SettingsAddEmailSection.RESENT_CONFIRMATION_EMAIL_ALERT))
        return True
    except Exception:
        return False


def get_resent_confirmation_email_address_text():
    element = wait.until(EC.visibility_of_element_located(SettingsAddEmailSection.RESENT_CONFIRMATION_EMAIL_ADDRESS))
    return element.text.strip()


def is_email_confirmed_alert_visible():
    try:
        wait.until(EC.visibility_of_element_located(SettingsAddEmailSection.EMAIL_CONFIRMED_ALERT))
        return True
    except Exception:
        return False


def refresh_settings_page():
    driver.refresh()


def is_added_email_visible(email_address):
    email_locator = (
        By.XPATH,
        f"//span[contains(@class,'accountEmailControl__displayEmailText') and normalize-space()='{email_address}']"
    )
    try:
        wait.until(EC.visibility_of_element_located(email_locator))
        return True
    except Exception:
        return False


def is_make_primary_button_visible(email_address):
    make_primary_locator = (
        By.XPATH,
        f"//span[contains(@class,'accountEmailControl__displayEmailText') and normalize-space()='{email_address}']"
        f"/ancestor::*[contains(@class,'accountEmailControl')][1]"
        f"//button[contains(@class,'accountEmailControl__makePrimary')]"
    )
    try:
        wait.until(EC.visibility_of_element_located(make_primary_locator))
        return True
    except Exception:
        return False