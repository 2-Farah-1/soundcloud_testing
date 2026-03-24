from selenium.webdriver.support import expected_conditions as EC
from ui_selectors import AuthSelectors, CookieSelectors, HomeSelectors, SignUpSelectors, SignInSelectors
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import Select


driver=None
wait=None



def click_forgot_password():
    wait.until(
        EC.element_to_be_clickable(SignInSelectors.FORGOT_PASSWORD_LINK)
    ).click()

#================================================
#              Reset Your Password form
#================================================

def click_send_reset_link():
    wait.until(
        EC.element_to_be_clickable(SignInSelectors.SEND_RESET_LINK_BTN)
    ).click()


def click_visit_help_center():
    wait.until(
        EC.element_to_be_clickable(SignInSelectors.RESET_PASSWORD_HELP_CENTER_LINK)
    ).click()


def click_back_to_login():
    wait.until(
        EC.element_to_be_clickable(SignInSelectors.BACK_TO_LOGIN_RESET_BTN)
    ).click()

#=================================================================

