from selenium.webdriver.common.by import By

class ProfileSelectors:
    DISPLAY_NAME_LABEL = (By.XPATH, "//span[contains(@class,'text-white') and contains(@class,'font-bold')]")
    CITY_LABEL = (By.XPATH, "(//span[contains(@class,'text-gray-400')])[1]")
    COUNTRY_LABEL = (By.XPATH, "(//span[contains(@class,'text-gray-400')])[2]")
    EDIT_BTN = (By.XPATH, "//button[@title='Edit']")
    DISPLAY_NAME_TXTBOX = (By.XPATH, "//input[@placeholder='Enter display name']")
    CITY_TXTBOX = (By.XPATH, "//input[@placeholder='Enter city']")
    COUNTRY_TXTBOX = (By.XPATH, "//input[@placeholder='Enter country']")
    BIO_TXTBOX = (By.XPATH, "//textarea[@placeholder='Tell the world a little bit about yourself.']")
    ADD_LINK_BTN = (By.XPATH, "//button[normalize-space()='Add link']")
    ADD_LINK1_TXTBOX = (By.XPATH, "//input[@placeholder='Web or email address']")
    ADD_LINK_DROPDOWN = (By.XPATH, "//select[@class='w-36 flex-shrink-0 rounded-sm bg-zinc-800 border border-zinc-700 px-3 py-2 text-sm text-white outline-none focus:border-zinc-500 cursor-pointer']")
    DELETE_LINK_BTN = (By.XPATH, "//button[@aria-label='Remove link 1']//*[name()='svg']")
    PROFILE_PIC_UPLOAD = (By.XPATH, "//input[@aria-label='Upload avatar image']")
    PROFILE_PIC_UPLOAD_BTN = (By.XPATH, "//button[normalize-space()='Upload image']")
    HEADER_PIC_UPLOAD = (By.XPATH, "//button[normalize-space()='Upload header image']/following-sibling::input")
    SAVE_CHANGES_BTN = (By.XPATH, "//button[@class='inline-flex items-center gap-2 rounded-sm px-3 py-1.5 text-sm font-bold text-zinc-900 bg-white hover:text-zinc-400 cursor-pointer']")

# class UploadSelectors:


class FeedSelectors:
    PROFILE_BTN = (By.XPATH, "//span[@class='text-xs text-white font-bold']")

class LoginSelectors:
    LOGIN_EMAIL_TXTBOX = (By.XPATH, "//input[@type='email']")
    CONTINUE_BTN = (By.XPATH, "//button[normalize-space()='Continue']")
    PASSWORD_TXTBOX = (By.XPATH, "//input[@placeholder='Your password']")
    CONTINUE_PASSWORD_BTN = (By.XPATH, "//button[@type='submit']")


