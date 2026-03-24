from selenium.webdriver.support import expected_conditions as EC
from ui_selectors import AuthSelectors
from selenium.webdriver.common.action_chains import ActionChains
import time

#functions from other pages
from pages.cookies_page import click_reject_all_cookies
from pages.home_page import click_header_create_account

driver=None
wait=None



# switch directly to the iframe of sign up or create account
#dont forget switch_to_default_content() for returning to the main iframe
def switch_to_auth_iframe():
    iframe = wait.until(
        EC.presence_of_element_located(AuthSelectors.iFrame)
    )
    driver.switch_to.frame(iframe)
#dont forget switch_to_default_content() for returning to the main iframe



def open_auth():
    click_reject_all_cookies()
    click_header_create_account()
    switch_to_auth_iframe()


#=========================================================================================
'''
def click_facebook_button():
    button = wait.until(EC.element_to_be_clickable(AuthSelectors.FACEBOOK_BUTTON))
    button.click()


def click_google_button():
    button = wait.until(EC.element_to_be_clickable(AuthSelectors.GOOGLE_BUTTON))
    button.click()


def click_apple_button():
    button = wait.until(EC.element_to_be_clickable(AuthSelectors.APPLE_BUTTON))
    button.click()
# //button[@id='onetrust-reject-all-handler']
'''
def click_facebook_button():
    button = wait.until(EC.presence_of_element_located(AuthSelectors.FACEBOOK_BUTTON))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
    wait.until(EC.visibility_of(button))
    wait.until(EC.element_to_be_clickable(AuthSelectors.FACEBOOK_BUTTON))
    driver.execute_script("arguments[0].click();", button)


def click_google_button():
    button = wait.until(EC.presence_of_element_located(AuthSelectors.GOOGLE_BUTTON))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
    wait.until(EC.visibility_of(button))
    wait.until(EC.element_to_be_clickable(AuthSelectors.GOOGLE_BUTTON))
    driver.execute_script("arguments[0].click();", button)


def click_apple_button():
    button = wait.until(EC.presence_of_element_located(AuthSelectors.APPLE_BUTTON))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
    wait.until(EC.visibility_of(button))
    wait.until(EC.element_to_be_clickable(AuthSelectors.APPLE_BUTTON))
    driver.execute_script("arguments[0].click();", button)



def auth_enter_email_or_url(test_email):
    # locate the email input inside that iframe
    email_input = wait.until(
        EC.visibility_of_element_located(AuthSelectors.EMAIL)
    )

    # normal Selenium click
    ActionChains(driver).move_to_element(email_input).click(email_input).perform()

    time.sleep(1)

    # type into the focused element
    active = driver.switch_to.active_element
    active.send_keys(test_email)


'''
def auth_enter_email(test_email):
    email_input = wait.until(
        EC.visibility_of_element_located(AuthSelectors.gmail_address)
    )
    email_input.clear()
    email_input.send_keys(test_email)
'''

def click_continue():
    continue_button = wait.until(
        EC.element_to_be_clickable(AuthSelectors.CONTINUE_BTN)
    )
    continue_button.click()

def enter_password(test_password):
    pass_input = wait.until(
        EC.visibility_of_element_located(AuthSelectors.PASSWORD)
    )

    pass_input.clear()
    pass_input.send_keys(test_password)


def click_show_password():
    show_pass = wait.until(
        EC.element_to_be_clickable(AuthSelectors.SHOW_PASSWORD_BTN)
    )
    show_pass.click()
def is_password_visible():
    toggle = wait.until(
        EC.presence_of_element_located(AuthSelectors.SHOW_PASSWORD_BTN)
    )
    return toggle.get_attribute("aria-checked") == "true"
def is_password_hidden():
    toggle = wait.until(
        EC.presence_of_element_located(AuthSelectors.SHOW_PASSWORD_BTN)
    )
    return toggle.get_attribute("aria-checked") == "false"


def click_continue_entered_password():
    continue_button = wait.until(
    EC.element_to_be_clickable(AuthSelectors.CONTINUE_ENTER_PASSWORD)
    )
    continue_button.click()

def click_need_help():
    wait.until(
        EC.element_to_be_clickable(AuthSelectors.NEED_HELP_LINK)
    ).click()
    driver.switch_to.window(driver.window_handles[-1])
