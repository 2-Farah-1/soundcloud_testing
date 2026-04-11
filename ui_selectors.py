from selenium.webdriver.common.by import By

class AuthSelectors:
   # iFrame=(By.XPATH, "(//iframe[@scrolling='no'])[1]")
    iFrame=(By.CSS_SELECTOR, "iframe[src*='secure.soundcloud.com/web-auth']") #og soundcloud

    CONNECT_TITLE = (By.XPATH, "//h1[text()='Sign in or create an account']")
    CLOSE_BTN = (By.XPATH, "//button[@title='Close']")
    FACEBOOK_BUTTON =  (By.CSS_SELECTOR, "button.sc-button-facebook" ) #CSS_SELECTOR
    GOOGLE_BUTTON = (By.CSS_SELECTOR, "button.sc-button-google")
    APPLE_BUTTON = (By.CSS_SELECTOR, "button.sc-button-apple")

    #EMAIL =  (By.NAME, "email")
    EMAIL =  (
    By.XPATH,
    "//input[@type='email' and @placeholder='Your email address or profile URL']"
    )



    #CONTINUE_BTN =  (By.ID, 'sign_in_up_submit' ) #ID
    CONTINUE_BTN =   (
    By.XPATH,
    "//button[normalize-space()='Continue']"
    )

    CAPTCHA = (By.ID, "captcha-container")

    #NEED_HELP_LINK = (By.CSS_SELECTOR, "a.need-help-link")

    NEED_HELP_LINK = (By.XPATH, "//a[normalize-space()='Need help?']")

    BACK_BUTTON = (By.CSS_SELECTOR, "button.back-button")

    PASSWORD =  (By.XPATH, "//input[@type='password']")
    SHOW_PASSWORD_BTN =(By.XPATH, "//button[.//svg[contains(@class,'lucide-eye')]]")

    CONTINUE_ENTER_PASSWORD =  (By.XPATH, "//button[normalize-space()='Continue']")


    CONTINUE_BUTTON_DISABLED = (By.XPATH, "//button[@disabled and normalize-space()='Continue']")
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

    WELCOME_BACK_MSG = (By.XPATH, "//h1[normalize-space()='Welcome back!']")
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
    EMAIL =  (By.NAME, "email")
#create account page:
    CREATE_ACCOUNT_TITLE = (By.XPATH, "//h1[normalize-space()='Create an account']")
    #BACK_BUTTON_CREATE_ACCOUNT = (By.XPATH, "//button[@title='Create an account']")
    BACK_BUTTON = (By.XPATH, "//button[.//svg[contains(@class,'chevron-left')]]")
#Tell us more about you:
    TELL_US_MORE_TITLE = (By.XPATH, "//h1[normalize-space()='Tell us more about you']")    #BACK_BUTTON_TELL_US_MORE = (By.XPATH, "//button[@title='Tell us more about you']")
    DISPLAY_NAME_INPUT = (By.XPATH, "//input[@placeholder='Your display name']")
    MONTH_DROPDOWN = (By.XPATH, "//select[option[text()='January']]")
    DAY_DROPDOWN = (By.XPATH, "//select[option[text()='1'] and option[text()='31']]")
    YEAR_DROPDOWN = (By.XPATH, "//select[option[@value='2005']]")
    GENDER_DROPDOWN = (By.XPATH, "//select[option[text()='Male'] and option[text()='Female']]")
    CONTINUE_SUBMIT_SIGNUP = (By.XPATH, "//button[normalize-space()='Continue']")
    BACK_BUTTON_TELL_US_MORE = (By.XPATH, "//button[.//svg[contains(@class,'chevron-left')]]")
#================================================================
    CONSENT_EMAILS_CHECKBOX = (By.CSS_SELECTOR, "input[data-testid='consent-emails-checkbox']")

    CONSENT_RECOMMENDATIONS_CHECKBOX = (By.CSS_SELECTOR, "input[data-testid='consent-recommendations-checkbox']")


# this error is displayed when the age is too little or too much (13<age<??)
    ERROR_AGE = (By.XPATH, "//span[@role='alert' and text()=\"Sorry, but you don't meet SoundCloud's minimum age requirements\"]")
    #this is not displayed in our project because they handle the error differently



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
#======================Check your inbox equivalent in our project:
# title: "Verify your email"
    VERIFY_EMAIL_TITLE = (
        By.XPATH,
        "//h1[normalize-space()='Verify your email']"
    )

    # displayed email address under "We sent a 6-character code to"
    # this works even though the email value changes
    SENT_TO_EMAIL = (
        By.XPATH,
        "//p[contains(normalize-space(),'We sent a 6-character code to')]/following-sibling::p[1]"
    )

    # all 6 OTP input boxes
    OTP_INPUTS = (
        By.CSS_SELECTOR,
        "input[inputmode='text'][maxlength='1']"
    )

    # verify email button
    VERIFY_EMAIL_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Verify email']"
    )

    # resend code button
    RESEND_CODE_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Resend code']"
    )

    # back button
    VERIFY_EMAIL_BACK_BUTTON = (
        By.XPATH,
        "//h1[normalize-space()='Verify your email']/preceding-sibling::button[1]"
    )
    RESEND_CODE_ALERT = (
        By.XPATH,
        "//div[normalize-space()='A new code has been sent to your inbox.']"
    )
#=================================================================================================================================================
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

    # HEADER_SIGN_IN = (By.XPATH,("//button[@class='g-opacity-transition frontHero__loginButton sc-button sc-button-medium "
    #                "loginButton sc-button-tertiary']")) og soundcloud
    HEADER_SIGN_IN = (By.XPATH, "//a[@href='/signin']")
    # HEADER_CREATE_ACCOUNT=(By.XPATH,("//button[@class='g-opacity-transition frontHero__createAccountButton sc-button "
    #                 "sc-button-medium signupButton sc-button-cta sc-button-primary']"))
    HEADER_CREATE_ACCOUNT=(By.XPATH, "//a[@href='/create-account']")
    CLOSE_POPUP=(By.XPATH,"//button[@aria-label='Close']//div//*[name()='svg']")
    BOTTOM_CREATE_ACCOUNT = (By.CSS_SELECTOR,
                        "button[class='g-opacity-transition signupModule__signupCta "
                        "sc-button sc-button-large signupButton sc-button-cta sc-button-primary']")

    BOTTOM_SIGN_IN = (By.CSS_SELECTOR,
                 "button[class='g-opacity-transition sc-button sc-button-large loginButton sc-button-tertiary'] ")


    MORE_BUTTON = (By.XPATH, "//span[normalize-space()='···']")

#In project and not in soundloud:
    HEADER_UPLOAD=(By.XPATH, "//a[@href='/upload']")



#======================================================================================
#signed in:

    MORE_MENU_DROPDOWN = (By.CSS_SELECTOR, "a.header__moreButton[aria-haspopup='true']")

    SETTINGS_BTN = (By.CSS_SELECTOR, "a.outgoing-settings")

    SIGN_OUT_BTN = (By.XPATH, "//a[@href='/logout' and text()='Sign out']")


    #PROFILE_MENU_PROFILE = (By.XPATH, "//a[contains(., 'Profile')]") og soundcloud
    PROFILE_MENU_PROFILE = (By.CSS_SELECTOR, 'a[title="My Profile"]') #migrated
    PROFILE_MENU_LIKES = (By.CSS_SELECTOR, "a[href='/you/likes']")
    PROFILE_MENU_STATIONS = (By.CSS_SELECTOR, "a[href='/you/stations']")
    PROFILE_MENU_WHO_TO_FOLLOW = (By.CSS_SELECTOR, "a[href='/people']")
    PROFILE_MENU_TRACKS = (By.CSS_SELECTOR, "a[href='/artists']")

    PROFILE_MENU_INSIGHTS = (By.XPATH, "//a[contains(., 'Insights')]")
    PROFILE_MENU_DISTRIBUTE = (By.XPATH, "//a[contains(., 'Distribute')]")
    PROFILE_MENU_TRY_ARTIST_PRO = (By.XPATH, "//a[contains(., 'Try Artist Pro')]")

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
#OG Soundcloud ->couldn't migrate
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

#OG Soundcloud -> couldn't migrate
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
#OG Soundcloud ->couldn't migrate
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


class UploadSelectors:

    # =========================
    # Header / Navigation
    # =========================
    HEADER_UPLOAD_BUTTON = (By.CSS_SELECTOR, "a.uploadButton[href='/upload']")

    # =========================
    # Upload Page Actions
    # =========================
    CHOOSE_FILES_BUTTON = (By.XPATH, "//button[.//text()[contains(., 'Choose files')]]")

    CONTINUE_WITHOUT_PLAN = (
        By.XPATH,
        "//button[contains(., 'continue without a paid plan')]"
    )

    # =========================
    # Track Info Section
    # =========================
    TRACK_INFO_HEADER = (By.ID, "uploadHeader")

    TRACK_TITLE = (
        By.CSS_SELECTOR,
        "#uploadHeader span.MuiTypography-caption"
    )

    PLAY_BUTTON = (
        By.CSS_SELECTOR,
        "#uploadHeader button[aria-label='Play']"
    )

    REPLACE_TRACK_BUTTON = (
        By.XPATH,
        "//button[.='Replace track']"
    )

    CLOSE_UPLOAD_BUTTON = (
        By.CSS_SELECTOR,
        "#uploadHeader button[aria-label='Close']"
    )

    # =========================
    # File Upload (IMPORTANT)
    # =========================
    FILE_INPUT = (
        By.CSS_SELECTOR,
        "#uploadHeader input[type='file']"
    )

    # =========================
    # Artwork
    # =========================
    ADD_ARTWORK_BUTTON = (
        By.CSS_SELECTOR,
        "button[aria-label='Add artwork']"
    )

    # =========================
    # Track Info Inputs
    # =========================

    # Track Title
    TRACK_TITLE_LABEL = (By.CSS_SELECTOR, "label[for='title']")
    TRACK_TITLE_INPUT = (By.ID, "title")

    # Track Link (Permalink)
    TRACK_PERMALINK_INPUT = (By.ID, "trackPermalink")

    # Artist
    ARTIST_INPUT = (By.ID, "artist")

    # Genre
    GENRE_INPUT = (By.ID, "primaryGenre")

    # Tags
    TAGS_INPUT = (By.ID, "tags")

    # Description
    DESCRIPTION_TEXTAREA = (By.ID, "description")

    # =========================
    # Privacy
    # =========================
    PUBLIC_RADIO = (
        By.XPATH,
        "//input[@type='radio' and @value='Public']"
    )

    PRIVATE_RADIO = (
        By.XPATH,
        "//input[@type='radio' and @value='Private']"
    )

    # =========================
    # Advanced Details Section
    # =========================
    ADVANCED_DETAILS_SECTION = (
        By.XPATH,
        "//h4[text()='Advanced details']"
    )

    BUY_LINK_INPUT = (By.ID, "purchaseUrl")

    RECORD_LABEL_INPUT = (By.ID, "labelName")

    RELEASE_DATE_INPUT = (
        By.XPATH,
        "//input[@placeholder='MM/DD/YYYY']"
    )

    RELEASE_DATE_PICKER_BUTTON = (
        By.CSS_SELECTOR,
        "button[aria-label='Choose date']"
    )

    PUBLISHER_INPUT = (By.ID, "publisher")

    ISRC_INPUT = (By.ID, "isrc")

    EXPLICIT_CHECKBOX = (
        By.XPATH,
        "//input[@type='checkbox' and @name='explicit']"
    )

    P_LINE_INPUT = (By.ID, "pLineForDisplay")

    # =========================
    # Permissions Section
    # =========================
    PERMISSIONS_SECTION = (
        By.XPATH,
        "//h4[text()='Permissions']"
    )

    ENABLE_DOWNLOADS_TOGGLE = (By.ID, "downloadable")

    OFFLINE_LISTENING_TOGGLE = (By.ID, "no_offline_sync")

    INCLUDE_IN_FEED_TOGGLE = (By.ID, "feedable")

    DISPLAY_EMBED_TOGGLE = (By.ID, "embeddable")

    APP_PLAYBACK_TOGGLE = (By.ID, "apiStreamable")

    # =========================
    # Licensing
    # =========================
    LICENSING_SECTION = (
        By.XPATH,
        "//h4[text()='Licensing']"
    )

    ALL_RIGHTS_RESERVED_RADIO = (
        By.XPATH,
        "//input[@type='radio' and @value='all-rights-reserved']"
    )

    CREATIVE_COMMONS_RADIO = (
        By.XPATH,
        "//input[@type='radio' and @value='commons']"
    )

    # =========================
    # Terms & Upload
    # =========================
    TERMS_OF_USE_LINK = (
        By.XPATH,
        "//a[contains(@href, 'terms-of-use')]"
    )

    FINAL_UPLOAD_BUTTON = (
        By.CSS_SELECTOR,
        "button[aria-label='Upload']"
    )
    # =========================
    # Upload Success
    # =========================
    UPLOAD_SUCCESS_MESSAGE = (
        By.XPATH,
        "//div[contains(text(), 'Saved to SoundCloud')]"
    )

    VIEW_TRACK_BUTTON = (
        By.XPATH,
        "//a[contains(., 'View track')]"
    )

    UPLOAD_SUCCESS_CLOSE_BUTTON = (
        By.CSS_SELECTOR,
        "button[aria-label='Close']"
    )


class ProfileTrack:

    # =========================
    # Track Actions
    # =========================
    EDIT_TRACK_BUTTON = (
        By.CSS_SELECTOR,
        "button[aria-label='Edit']"
    )

class ProfileTrackSelectors:

    # =========================
    # Track Actions
    # =========================
    EDIT_TRACK_BUTTON = (
        By.CSS_SELECTOR,
        "button[aria-label='Edit']"
    )