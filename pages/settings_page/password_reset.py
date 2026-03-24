from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from ui_selectors import SettingsSelectors,SettingsResetPasswordSection

driver = None
wait = None


def scroll_to_send_password_reset_link_button():
    element = wait.until(
        EC.presence_of_element_located(SettingsSelectors.SEND_PASSWORD_RESET_LINK_BTN)
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)


def click_send_password_reset_link_button():
    button = wait.until(
        EC.element_to_be_clickable(SettingsSelectors.SEND_PASSWORD_RESET_LINK_BTN)
    )
    button.click()


def is_password_reset_link_sent_alert_visible():
    try:
        wait.until(
            EC.visibility_of_element_located(SettingsResetPasswordSection.PASSWORD_RESET_LINK_SENT_ALERT)
        )
        return True
    except:
        return False


def get_password_reset_link_sent_alert_text():
    alert = wait.until(
        EC.visibility_of_element_located(SettingsResetPasswordSection.PASSWORD_RESET_LINK_SENT_ALERT)
    )
    return alert.text