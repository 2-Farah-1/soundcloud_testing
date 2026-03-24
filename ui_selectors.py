from selenium.webdriver.common.by import By

class AuthSelectors:
   # iFrame=(By.XPATH, "(//iframe[@scrolling='no'])[1]")
    iFrame=(By.CSS_SELECTOR, "iframe[src*='secure.soundcloud.com/web-auth']")
    CONNECT_TITLE = (By.XPATH, "//h1[text()='Sign in or create an account']")
    CLOSE_BTN = (By.XPATH, "//button[@title='Close']")
    FACEBOOK_BUTTON =  (By.CSS_SELECTOR, "button.sc-button-facebook" ) #CSS_SELECTOR
    GOOGLE_BUTTON = (By.CSS_SELECTOR, "button.sc-button-google")
    APPLE_BUTTON = (By.CSS_SELECTOR, "button.sc-button-apple")

    EMAIL =  (By.ID,'sign_in_up_email' )  #ID
    CONTINUE_BTN =  (By.ID, 'sign_in_up_submit' ) #ID


    CAPTCHA = (By.ID, "captcha-container")

    NEED_HELP_LINK = (By.CSS_SELECTOR, "a.need-help-link")

    BACK_BUTTON = (By.CSS_SELECTOR, "button.back-button")

    PASSWORD =  (By.ID,"enter_password_field" ) #ID
    SHOW_PASSWORD_BTN = (By.CSS_SELECTOR, "button.visibility-icon-button")

    CONTINUE_ENTER_PASSWORD = (By.ID, "enter_password_submit")

#BACK_BUTTON_SIGNIN_CREATE = (By.XPATH, "//button[@title='Sign in or create an account']")

    ERROR_URL_DOESNT_EXIST = (By.XPATH, "//span[@role='alert' and text()='That profile url does not exist']")
    ERROR_INVALID_EMAIL_OR_URL = (By.XPATH,
                                  "//span[@role='alert' and text()='Enter a valid email address or profile url.']")

    #this error happens when any invalid url, email are entered
   # ERROR=  (By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div/form/div[1]/div[1]/div/span' )  #XPATH



    TERMS_LINK = (By.XPATH, "//a[@href='https://soundcloud.com/terms-of-use']")
    PRIVACY_LINK = (By.XPATH, "//a[@href='https://soundcloud.com/pages/privacy']")



class SignInSelectors:
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Forgot your password?']")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=

    BACK_BUTTON_WELCOME_BACK = (By.XPATH, "//button[@title='Welcome back!']")

    ERROR_INCORRECT_PASSWORD = (By.XPATH, "//span[@role='alert' and text()='This password is incorrect.']")

    SIGNED_IN_PROFILE_BTN = (By.CSS_SELECTOR, "a[data-test-id='user-nav-btn']")

    RESET_PASSWORD_TITLE = (By.XPATH, "//span[text()='Reset password']")

    RESET_PASSWORD_EMAIL_INPUT = (By.ID, "forgot_password_email")

    RESET_PASSWORD_HELP_CENTER_LINK = (By.CSS_SELECTOR, "a.help-center-link")

    SEND_RESET_LINK_BTN = (By.ID, "forgot_password_submit")

    BACK_BUTTON_RESET_PASSWORD = (By.XPATH, "//button[@title='Reset password']")

    CHECK_YOUR_EMAIL_TITLE = (By.CSS_SELECTOR, "div.check-email-title")

    RESET_PASSWORD_INSTRUCTION_MSG = (By.CSS_SELECTOR, "p.instruction-message")

    BACK_TO_LOGIN_RESET_BTN = (By.ID, "forgot_password_confirmation_submit")









class SignUpSelectors:
#create account page:
    CREATE_ACCOUNT_TITLE = (By.XPATH, "//span[text()='Create an account']")
    #BACK_BUTTON_CREATE_ACCOUNT = (By.XPATH, "//button[@title='Create an account']")

#Tell us more about you:
    TELL_US_MORE_TITLE = (By.XPATH, "//span[text()='Tell us more about you']")
    #BACK_BUTTON_TELL_US_MORE = (By.XPATH, "//button[@title='Tell us more about you']")
    DISPLAY_NAME_INPUT = (By.ID, "sign_up_username")
    MONTH_DROPDOWN = (By.CSS_SELECTOR, "select#birthDate_month")
    DAY_DROPDOWN = (By.ID, "birthDate_day")

    YEAR_DROPDOWN = (By.ID, "birthDate_year")

    GENDER_DROPDOWN = (By.CSS_SELECTOR, "select#gender")
    CONTINUE_SUBMIT_SIGNUP=(By.ID, "submit_signup")

#================================================================
    CONSENT_EMAILS_CHECKBOX = (By.CSS_SELECTOR, "input[data-testid='consent-emails-checkbox']")

    CONSENT_RECOMMENDATIONS_CHECKBOX = (By.CSS_SELECTOR, "input[data-testid='consent-recommendations-checkbox']")


# this error is displayed when the age is too little or too much (13<age<??)
    ERROR_AGE = (By.XPATH, "//span[@role='alert' and text()=\"Sorry, but you don't meet SoundCloud's minimum age requirements\"]")


    ACCOUNT_ALREADY_EXISTS_MSG = (By.CSS_SELECTOR, "div.signup-attempt")


#Check your inbox!
    CHECK_YOUR_INBOX_TITLE = (By.XPATH, "//span[text()='Check your inbox!']")

    SEND_AGAIN_BTN = (By.XPATH, "//span[@class='send-again-button-link' and text()='Send again']")

    OPEN_GMAIL_BTN = (By.XPATH, "//div[contains(@class,'email-provider-button-content')]//span[text()='Open Gmail']")

    BACK_TO_LOGIN_BTN = (By.XPATH, "//span[@class='send-again-button-link' and text()='Back to login']")

    HELP_CENTER_LINK = (By.XPATH, "//a[@href='https://help.soundcloud.com/hc/articles/29056497797787-Verify-your-email']")

    LINK_SENT_AGAIN_MSG = (By.XPATH, "//span[text()=\"Link sent! If you still didn't receive it, try checking your spam folder.\"]")

    VERIFY_INSTRUCTION_MESSAGE = (By.CSS_SELECTOR, "p.verify-instruction-message")

    VERIFICATION_EMAIL_TEXT = (By.CSS_SELECTOR, "p.verify-instruction-message b")
     #//*[@id="app"]/div/main/div/div/div[2]/p/b/text()

#Help Center Page
    HELP_CENTER_PAGE_TITLE = (By.XPATH, "//h1[text()='HELP CENTER']")


#email address confirm page

    EMAIL_CONFIRMED_TITLE = (By.XPATH, "//h1[text()='Your email address is confirmed!']")

    DISCOVER_NEW_MUSIC_BTN = (By.ID, "emailConfirmation__action-discover")

    UPLOAD_FIRST_TRACK_BTN = (By.ID, "emailConfirmation__action-upload")

    LEGAL_BTN = (By.XPATH, "//a[@title='Terms of use' and text()='Legal']")

    PRIVACY_BTN = (By.XPATH, "//a[@title='Privacy policy' and text()='Privacy']")

    COOKIES_BTN = (By.XPATH, "//a[@href='https://soundcloud.com/pages/cookies']")

    IMPRINT_BTN = (By.XPATH, "//a[@href='https://soundcloud.com/imprint' and text()='Imprint']")

    LEGAL_PAGE_TITLE = (By.XPATH, "//h1[@id='soundcloud-terms-of-use']")

    PRIVACY_PAGE_TITLE = (By.XPATH, "//h2[@id='soundcloud-privacy-policy']")

    COOKIES_PAGE_TITLE = (By.XPATH, "//h1[@id='soundcloud-cookie-policy']")

    IMPRINT_PAGE_TITLE = (By.XPATH, "//h1[@id='company-information']")








'''
     <p class="validation-error" role="alert">This request didn’t pass our checks.
      <br> Try reloading the page. If you continue to have this problem, 
      please <a href="https://help.soundcloud.com/hc/sections/46266771825691" target="_blank">
      visit our Help center</a>.</p>
'''

class CookieSelectors:
    I_ACCEPT =(By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    REJECT_ALL = (By.XPATH,"//button[@id='onetrust-reject-all-handler']")
    MANAGE_PREFERENCES=(By.XPATH,"//button[@id='onetrust-pc-btn-handler']")
    #manage preferences still has a page that needs to be continued


class HomeSelectors:
#signed out:
    HEADER_SIGN_IN = (By.XPATH,("//button[@class='g-opacity-transition frontHero__loginButton sc-button sc-button-medium "
                   "loginButton sc-button-tertiary']"))
    HEADER_CREATE_ACCOUNT=(By.XPATH,("//button[@class='g-opacity-transition frontHero__createAccountButton sc-button "
                    "sc-button-medium signupButton sc-button-cta sc-button-primary']"))

    CLOSE_POPUP=(By.XPATH,"//button[@aria-label='Close']//div//*[name()='svg']")
    BOTTOM_CREATE_ACCOUNT = (By.CSS_SELECTOR,
                        "button[class='g-opacity-transition signupModule__signupCta "
                        "sc-button sc-button-large signupButton sc-button-cta sc-button-primary']")

    BOTTOM_SIGN_IN = (By.CSS_SELECTOR,
                 "button[class='g-opacity-transition sc-button sc-button-large loginButton sc-button-tertiary'] ")

#======================================================================================
#signed in:
    MORE_BUTTON = (By.CSS_SELECTOR, "a.header__moreButton")

    MORE_MENU_DROPDOWN = (By.CSS_SELECTOR, "a.header__moreButton[aria-haspopup='true']")

    SETTINGS_BTN = (By.CSS_SELECTOR, "a.outgoing-settings")

    SIGN_OUT_BTN = (By.XPATH, "//a[@href='/logout' and text()='Sign out']")

#=======================


class SettingsSelectors:
    SETTINGS_TITLE = (By.XPATH, "//h1[text()='Settings']")

    ADD_EMAIL_ADDRESS_BTN = (By.XPATH, "//button[normalize-space()='Add an email address']")


#adding/removing socials
    SOCIAL_HINT_BTN = (By.CSS_SELECTOR, "button.hintButton")

    ADD_FACEBOOK_ACCOUNT_BTN = (By.CSS_SELECTOR, "button.accountSocialConnect__facebookButton")
    ADD_GOOGLE_ACCOUNT_BTN = (By.CSS_SELECTOR, "button.accountSocialConnect__googleButton")
    ADD_APPLE_ACCOUNT_BTN = (By.CSS_SELECTOR, "button.accountSocialConnect__appleButton")

    DISCONNECT_ACCOUNT_BTN = (By.CSS_SELECTOR, "button.accountSocialItem__disconnectButton")
    ADDED_SOCIAL_NAME = (By.CSS_SELECTOR, "span.accountSocialItem__name")

    NO_SOCIAL_ACCOUNT_LINKED_ALERT = (By.CSS_SELECTOR, "div.accountSocial__empty")


    SEND_PASSWORD_RESET_LINK_BTN = (By.XPATH, "//button[@title='Send password-reset link']")


    DELETE_ACCOUNT_BTN = (By.CSS_SELECTOR, "button.accountSettings__deleteAccount")

class SettingsAddEmailSection:
#adding an email logic
    NEW_EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='Please enter your email address *']")

    ADD_EMAIL_BTN = (By.XPATH, "//button[@title='Add']")
    CANCEL_ADD_EMAIL_BTN = (By.XPATH, "//button[@title='Cancel']")

    ENTER_EMAIL_ADDRESS_ALERT = (By.XPATH, "//div[text()='Enter your email address.']")
    INVALID_EMAIL_ADDRESS_ALERT = (By.XPATH, "//div[text()='This email address is invalid.']")

    EMAIL_TYPO_SUGGESTION = (By.CSS_SELECTOR, "div.email__typo")
    EMAIL_TYPO_DOMAIN_LINK = (By.CSS_SELECTOR, "div.email__typo a")
    SAVE_EMAIL_ERROR = (By.XPATH, "//span[text()='An error occurred while saving. Try again.']")

    ADDED_EMAIL_TEXT = (By.CSS_SELECTOR, "span.accountEmailControl__displayEmailText")

#resending verfification/confirmation link
    RESEND_CONFIRMATION_EMAIL_BTN = (By.CSS_SELECTOR, "a.accountEmailControl__resendConfirmation")

    EMAIL_SENT_TO_ALERT = (By.CSS_SELECTOR, "div.gritter-item-wrapper[role='alert']")
    EMAIL_SENT_TO_ALERT_TEXT = (By.XPATH, "//div[@role='alert']//p")
    EMAIL_SENT_TO_ALERT_CLOSE_BTN = (By.CSS_SELECTOR, "div.gritter-item-wrapper[role='alert'] a.gritter-close")

    RESENT_CONFIRMATION_EMAIL_ALERT = (By.CSS_SELECTOR, "div.accountEmailControl__confirmationSentMessage")
    RESENT_CONFIRMATION_EMAIL_ADDRESS = (By.CSS_SELECTOR, "span.accountEmailControl__confirmationSentAddress")

#confirming email page link error (gmail hyperlink redirect)
    CONFIRMING_EMAIL_TITLE = (By.XPATH, "//h1[text()='Confirming your email']")

    LINK_EXPIRED_OR_INVALID_ERROR = (By.XPATH, "//p[text()='The link is either expired or invalid.']")

    NEW_CONFIRMATION_EMAIL_LINK = (By.XPATH, "//p[contains(@class,'tokenValidation__hint')]//a[contains(@href,'soundcloud.com/settings')]")

#email address is confirmed page (gmail hyperlink redirexct)
    EMAIL_CONFIRMED_ALERT = (By.XPATH, "//h1[text()='Your email address is confirmed!']")

    DISCOVER_NEW_MUSIC_BTN = (By.ID, "emailConfirmation__action-discover")

    UPLOAD_FIRST_TRACK_BTN = (By.ID, "emailConfirmation__action-upload")
    UPLOAD_PAGE_TITLE = (By.XPATH, "//h2[text()='Upload']")

#email is confirmed! (this is back at settings page)
    MAKE_PRIMARY_BTN = (By.CSS_SELECTOR, "button.accountEmailControl__makePrimary")

#after pressing make primary an iframe is opened
    VERIFY_EMAIL_FOR_MAKING_PRIMARY_IFRAME=(By.CSS_SELECTOR, "iframe[title='Enter One Time Password']")

    VERIFY_EMAIL_TITLE = (By.XPATH, "//h1[text()='Verify email address']")
    VERIFY_EMAIL_CLOSE_BTN = (By.XPATH, "//button[@title='Close']")
    VERIFY_EMAIL_BACK_BTN = (By.XPATH, "//button[text()='Back']")

    SEND_VERIFICATION_CODE_BTN = (By.XPATH, "//button[text()='Send verification code']")

    CONTACT_SUPPORT_LINK = (By.XPATH, "//a[contains(@href,'help.soundcloud.com')]")
#pressed SEND_VERIFICATION_CODE_BTN
    ENTER_CODE_TITLE = (By.XPATH, "//h1[text()='Enter code']")

    OTP_INPUT = (By.CSS_SELECTOR, "input[data-input-otp='true']")

    RESEND_CODE_BTN = (By.XPATH, "//button[text()='Resend it']")

    OTP_BACK_BTN = (By.XPATH, "//button[text()='Back']")

    CONFIRM_OTP_BTN = (By.XPATH, "//button[text()='Confirm']")

    OTP_ERROR_MSG = (By.XPATH, "//h2[contains(text(),'Application error')]")

#succesfuly made the other one primary

    PRIMARY_EMAIL_CHANGED_ALERT = (By.CSS_SELECTOR, "div.gritter-item-wrapper.big-success[role='alert']")
    PRIMARY_EMAIL_CHANGED_ALERT_TEXT = (By.XPATH, "//div[contains(@class,'big-success')]//p")
    PRIMARY_EMAIL_CHANGED_CLOSE_BTN = (By.CSS_SELECTOR, "div.big-success a.gritter-close")

    PRIMARY_EMAIL_TEXT = (By.CSS_SELECTOR, "span.accountEmailControl__displayEmailText")
    PRIMARY_EMAIL_LABEL = (By.XPATH, "//span[text()='(Primary)']")

#removing non-primary address
    REMOVE_ADDRESS_BTN = (By.CSS_SELECTOR, "button.accountEmailControl__remove")

    REMOVE_EMAIL_CONFIRM_CONTAINER = (By.CSS_SELECTOR, "div.accountEmailControl__confirmRemoveState")

    DELETE_EMAIL_BTN = (By.CSS_SELECTOR, "button.accountEmailControl__confirmRemove")
    CANCEL_DELETE_EMAIL_BTN = (By.CSS_SELECTOR, "button.accountEmailControl__cancelRemove")


class SettingsResetPasswordSection:
    PASSWORD_RESET_LINK_SENT_ALERT = (By.CSS_SELECTOR, "p.accountSettings__resetNotice")

    RESET_PASSWORD_EMAIL_LINK = (By.XPATH, "//a[contains(@href,'secure.soundcloud.com/password-reset/')]")

    CHANGE_YOUR_PASSWORD_TITLE = (By.XPATH, "//h1[text()='Change your password']")

    NEW_PASSWORD_INPUT = (By.ID, "password")
    CONFIRM_NEW_PASSWORD_INPUT = (By.ID, "passwordConfirmation")
    SIGN_ME_OUT_EVERYWHERE_CHECKBOX = (By.CSS_SELECTOR, "input[data-testid='invalidate-all-tokens-checkbox']")

    SAVE_NEW_PASSWORD_BTN = (By.XPATH, "//button[@type='submit' and text()='Save']")

    PASSWORD_MIN_8_ALERT = (By.XPATH, "//span[@role='alert' and text()='Password must be at least 8 characters.']")
    REPEAT_PASSWORD_ALERT = (By.XPATH, "//span[@role='alert' and text()='Please repeat your password.']")
    DATA_BREACH_PASSWORD_ALERT = (By.XPATH,
                                  "//span[@role='alert' and text()='This password is listed in a public data breach. "
                                  "Please choose a different one.']")

    PASSWORD_HELP_CENTER_LINK = (By.XPATH,
                                 "//a[@href='https://help.soundcloud.com/hc/articles/115003450547-How-to-have-a-secure-account']")

    PASSWORD_RESET_SUCCESS_TITLE = (By.XPATH, "//h1[text()='You have successfully changed your password.']")

    PASSWORD_RESET_SUCCESS_SIGNIN_BTN = (By.XPATH, "//a[@href='/signin' and text()='Sign in']")

class SettingsDeleteAccountSection:
    DELETE_ACCOUNT_IFRAME=(  By.XPATH,
                "//iframe[contains(@src, '/n/pages/standby') and @title='SoundCloud']")
    DELETE_ACCOUNT_MODAL = (By.CSS_SELECTOR, "div.deleteAccountContent__form")
    DELETE_ACCOUNT_TITLE = (By.XPATH, "//h2[text()='Delete account']")
    DELETE_ACCOUNT_SUBTITLE = (By.XPATH, "//h3[text()='Why are you choosing to delete your account?']")
    DELETE_ACCOUNT_CLOSE_BTN = (By.XPATH, "//button[@title='Close']")

    DELETE_REASON_ANOTHER_ACCOUNT = (By.XPATH, "//span[text()='I have another account']")
    DELETE_REASON_NEW_ACCOUNT = (By.XPATH, "//span[text()='I want to make a new account']")
    DELETE_REASON_PRIVACY_OPTIONS = (By.XPATH, "//span[text()='There aren’t enough privacy options']")
    DELETE_REASON_NO_LONGER_CREATING = (By.XPATH, "//span[text()='I am no longer creating content for this account']")
    DELETE_REASON_COPYRIGHT_ISSUES = (By.XPATH, "//span[text()='I had copyright issues with a track or tracks']")
    DELETE_REASON_NO_PRO = (By.XPATH, "//span[text()='I don’t want to subscribe to SoundCloud Pro anymore']")
    DELETE_REASON_SWITCHED_SERVICE = (By.XPATH, "//span[text()='I switched to another music or audio service']")
    DELETE_REASON_HACKED = (By.XPATH, "//span[text()='My account got hacked']")
    DELETE_REASON_CANT_REMOVE_TRACKS = (By.XPATH, "//span[text()='I can’t remove my tracks']")
    DELETE_REASON_HARASSMENT = (By.XPATH, "//span[text()='People are harassing me']")
    DELETE_REASON_TOO_MUCH_SPAM = (By.XPATH, "//span[text()='Too much spam on the platform']")
    DELETE_REASON_OTHER = (By.XPATH, "//span[text()='Other, please specify']")

    DELETE_PRIVACY_OPTIONS_HINT = (By.XPATH, "//p[text()='What options do you need that are currently missing?']")
    DELETE_PRIVACY_OPTIONS_INPUT = (By.XPATH, "//div[@data-field='reasonPrivacyOptions']//input")

    DELETE_PRO_CANCEL_HINT = (By.XPATH, "//div[@data-field='reasonPro']//a[contains(@href,'/you/subscriptions')]")

    DELETE_SWITCH_SERVICE_HINT = (By.XPATH, "//p[text()='Which service are you switching to?']")
    DELETE_SWITCH_AMAZON = (By.CSS_SELECTOR, "label[data-radio-value='Amazon']")
    DELETE_SWITCH_BANDCAMP = (By.CSS_SELECTOR, "label[data-radio-value='Bandcamp']")
    DELETE_SWITCH_ITUNES = (By.CSS_SELECTOR, "label[data-radio-value='iTunes']")
    DELETE_SWITCH_SPOTIFY = (By.CSS_SELECTOR, "label[data-radio-value='Spotify']")
    DELETE_SWITCH_TIDAL = (By.CSS_SELECTOR, "label[data-radio-value='Tidal']")
    DELETE_SWITCH_YOUTUBE = (By.CSS_SELECTOR, "label[data-radio-value='YouTube']")
    DELETE_SWITCH_OTHER = (By.CSS_SELECTOR, "label[data-radio-value='other']")
    DELETE_SWITCH_OTHER_INPUT = (By.XPATH, "//div[@data-field='reasonSwitch']//input")

    DELETE_HACKED_RESET_PASSWORD_LINK = (By.XPATH, "//div[@data-field='reasonHacked']//a[contains(@href,'Resetting-your-password')]")
    DELETE_HACKED_SETTINGS_LINKS = (By.XPATH, "//div[@data-field='reasonHacked']//a[@href='/settings']")
    DELETE_REMOVE_TRACKS_HELP_LINK = (By.XPATH, "//div[@data-field='reasonConfused']//a[contains(@href,'115003562248')]")
    DELETE_HARASSMENT_BLOCK_LINK = (By.XPATH, "//div[@data-field='reasonHarrassment']//a[contains(@href,'115003566048')]")
    DELETE_HARASSMENT_CONTACT_LINK = (By.XPATH, "//div[@data-field='reasonHarrassment']//a[contains(@href,'requests/new')]")
    DELETE_OTHER_REASON_INPUT = (By.CSS_SELECTOR, "div.deleteAccountContent__other input")

    DELETE_ACCOUNT_CONFIRM_CHECKBOX = (By.XPATH, "//span[text()='Yes, I want to delete my account and all my tracks, comments and stats.']")
    DELETE_ACCOUNT_CONFIRM_VALIDATION = (By.XPATH, "//div[text()='Confirm that you want to delete your account.']")
    DELETE_ACCOUNT_CANCEL_BTN = (By.XPATH, "//button[@title='Cancel']")
    DELETE_MY_ACCOUNT_BTN = (By.XPATH, "//button[@title='Delete my account']")

    DELETE_ACCOUNT_SUCCESS_CONTAINER = (By.CSS_SELECTOR, "div.deleteAccountContent__success")
    DELETE_ACCOUNT_SUCCESS_TITLE = (By.XPATH, "//h1[text()='You deleted your account']")
    DELETE_ACCOUNT_SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(),'We’ve received your request to delete your account')]")
    DELETE_ACCOUNT_SUCCESS_HELP_CENTER_LINK = (By.XPATH, "//a[contains(@href,'My-account-was-deleted-but-I-want-to-sign-back-in')]")
    DELETE_ACCOUNT_OK_GOT_IT_BTN = (By.XPATH, "//button[@title='Ok, got it']")
    DELETE_ACCOUNT_SUCCESS_CLOSE_BTN = (By.XPATH, "//button[@title='Close']")

    SIGNED_OUT_ALERT = (By.XPATH, "//h1[text()=\"You've signed out. Now go mobile!\"]")

