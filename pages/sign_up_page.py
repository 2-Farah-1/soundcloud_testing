from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui_selectors import AuthSelectors, CookieSelectors, HomeSelectors, SignUpSelectors, SignInSelectors
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import time

driver=None
wait=None

def sign_up_enter_email(test_email):
    # locate the email input inside that iframe
    email_input = wait.until(
        EC.visibility_of_element_located(SignUpSelectors.EMAIL)
    )

    # normal Selenium click
    ActionChains(driver).move_to_element(email_input).click(email_input).perform()

    time.sleep(1)

    # type into the focused element
    active = driver.switch_to.active_element
    active.send_keys(test_email)


#================================================
#              Tell Us More About You form
#================================================
def enter_display_name(name):
    wait.until(
        EC.visibility_of_element_located(SignUpSelectors.DISPLAY_NAME_INPUT)
    ).send_keys(name)

def select_month(month):
    dropdown = wait.until(
        EC.element_to_be_clickable(SignUpSelectors.MONTH_DROPDOWN)
    )
    Select(dropdown).select_by_visible_text(month)

def select_day(day):
    dropdown = wait.until(
        EC.element_to_be_clickable(SignUpSelectors.DAY_DROPDOWN)
    )
    Select(dropdown).select_by_visible_text(day)

def select_year(year):
    dropdown = wait.until(
        EC.element_to_be_clickable(SignUpSelectors.YEAR_DROPDOWN)
    )
    Select(dropdown).select_by_visible_text(year)

def select_gender(gender):
    dropdown = wait.until(
        EC.element_to_be_clickable(SignUpSelectors.GENDER_DROPDOWN)
    )
    Select(dropdown).select_by_visible_text(gender)


def fill_tell_us_more_about_you_form(name, month, day, year, gender):
    enter_display_name(name)
    select_month(month)
    select_day(day)
    select_year(year)
    select_gender(gender)

def click_continue_tell_us_more_about_you():
    continue_button = wait.until(
    EC.element_to_be_clickable(SignUpSelectors.CONTINUE_SUBMIT_SIGNUP)
    )
    continue_button.click()

#================================================
#              Check Your Inbox! form
#================================================
def click_open_gmail_button():
    button = wait.until(EC.presence_of_element_located(SignUpSelectors.OPEN_GMAIL_BTN))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
    wait.until(EC.visibility_of(button))
    wait.until(EC.element_to_be_clickable(SignUpSelectors.OPEN_GMAIL_BTN))
    driver.execute_script("arguments[0].click();", button)


def click_help_center_link():
    button = wait.until(EC.presence_of_element_located(SignUpSelectors.HELP_CENTER_LINK))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
    wait.until(EC.visibility_of(button))
    wait.until(EC.element_to_be_clickable(SignUpSelectors.HELP_CENTER_LINK))
    driver.execute_script("arguments[0].click();", button)


def click_send_again_button():
    button = wait.until(EC.presence_of_element_located(SignUpSelectors.SEND_AGAIN_BTN))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
    wait.until(EC.visibility_of(button))
    wait.until(EC.element_to_be_clickable(SignUpSelectors.SEND_AGAIN_BTN))
    driver.execute_script("arguments[0].click();", button)


def click_back_to_login_button():
    button = wait.until(EC.presence_of_element_located(SignUpSelectors.BACK_TO_LOGIN_BTN))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
    wait.until(EC.visibility_of(button))
    wait.until(EC.element_to_be_clickable(SignUpSelectors.BACK_TO_LOGIN_BTN))
    driver.execute_script("arguments[0].click();", button)


def click_close_button():
    button = wait.until(EC.presence_of_element_located(SignUpSelectors.CLOSE_BTN))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
    wait.until(EC.visibility_of(button))
    wait.until(EC.element_to_be_clickable(SignUpSelectors.CLOSE_BTN))
    driver.execute_script("arguments[0].click();", button)

#for the "Verify your email" `part
def enter_verification_code(code):
    otp_inputs = wait.until(
        EC.presence_of_all_elements_located(SignUpSelectors.OTP_INPUTS)
    )

    assert len(otp_inputs) >= len(code), (
        f"Expected at least {len(code)} OTP input boxes, but found {len(otp_inputs)}."
    )

    for i, char in enumerate(code):
        otp_inputs[i].clear()
        otp_inputs[i].send_keys(char)


def click_verify_email_button():
    button = wait.until(
        EC.element_to_be_clickable(SignUpSelectors.VERIFY_EMAIL_BUTTON)
    )
    button.click()