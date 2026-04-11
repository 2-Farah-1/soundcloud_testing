from selectors import LoginSelectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self,email, password):
        self.wait.until(EC.element_to_be_clickable(LoginSelectors.LOGIN_EMAIL_TXTBOX)).send_keys(email)
        continue_btn = self.wait.until(EC.element_to_be_clickable(LoginSelectors.CONTINUE_BTN))
        continue_btn.click()
        txtbox_pass = self.wait.until(EC.element_to_be_clickable(LoginSelectors.PASSWORD_TXTBOX))
        txtbox_pass.click()
        txtbox_pass.send_keys(password)
        continue_pass_btn = self.wait.until(EC.element_to_be_clickable(LoginSelectors.CONTINUE_BTN))
        continue_pass_btn.click()


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 50)
#         self.reject_cookies_button = (By.CSS_SELECTOR, "#onetrust-reject-all-handler")
#         self.sign_in_btn = (By.CSS_SELECTOR, "button[aria-label='Sign in']")
#         self.email_input = (By.ID, "sign_in_up_email")
#         self.password_input = (By.NAME, "password")
#         self.continue_btn = (By.XPATH, "//button[contains(text(),'Continue')]")
#
#     def login(self, email, password):
#         self.driver.find_element(*self.reject_cookies_button).click()
#         #self.driver.find_element(*self.sign_in_btn).click()
#         sign_in_element = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located(self.sign_in_btn)
#         )
#         self.driver.execute_script("arguments[0].scrollIntoView();", sign_in_element)
#         self.driver.execute_script("arguments[0].click();", sign_in_element)
#         email_element = WebDriverWait(self.driver, 10).until(
#             EC.visibility_of_element_located(self.email_input)
#         )
#         self.driver.execute_script("arguments[0].scrollIntoView();", email_element)
#         self.driver.execute_script("arguments[0].click();", email_element)
#         # self.driver.find_element(*self.email_input).click()
#         self.driver.find_element(*self.email_input).send_keys(email)
#         self.driver.find_element(*self.continue_btn).click()
#         self.driver.find_element(*self.password_input).send_keys(password)
#         self.driver.find_element(*self.continue_btn).click()

