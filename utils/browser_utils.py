from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui_selectors import AuthSelectors
from selenium.common.exceptions import TimeoutException



driver=None
wait=None




#detects whether an element is disabled (useful for checks and asserts)
def is_element_disabled(locator):
    element = wait.until(
        EC.presence_of_element_located(locator)
    )
    return not element.is_enabled()



#checks whether an element is visible --- used for alerts like Enter a vlaid email! and whatnot
def is_element_visible(locator, timeout=3):
    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return True
    except TimeoutException:
        return False

#this one checks text of the element passed
def get_element_text(locator, timeout=3):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text
    except TimeoutException:
        return None

#helper function that detects whether this page is "Help Center"
def is_on_help_center(timeout=5):
    try:
        WebDriverWait(driver, timeout).until(
            EC.url_contains("https://help.soundcloud.com")
        )
        return True
    except TimeoutException:
        return False

#this one detects whether CAPTCHA window is open or not
def captcha_is_present():
    try:
        wait.until(
            EC.presence_of_element_located(AuthSelectors.CAPTCHA)
        )
        return True
    except TimeoutException:
        return False

#pauses for me to manually "solve" the CAPTCHA
def pause_for_manual_captcha():
    if captcha_is_present():
        print("Captcha detected. Solve it manually in the browser, then press Enter here.")
        input()

#switches to iframe zero (default iframe)
#used becuase we handle A LOT of iframes
def switch_to_default_content():
    driver.switch_to.default_content()

def wait_for_non_blank_url(timeout=20):
    WebDriverWait(driver, timeout).until(
        lambda d: d.current_url != "about:blank"
    )

def open_link_in_new_tab(link): #for checkk your inbox logic
    original_window = driver.current_window_handle

    driver.execute_script("window.open(arguments[0], '_blank');", link)

    WebDriverWait(driver, 10).until(
        lambda d: len(d.window_handles) > 1
    )

    for window in driver.window_handles:
        if window != original_window:
            driver.switch_to.window(window)
            return original_window

    return original_window