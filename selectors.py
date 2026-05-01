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
    # 7AGET EL HOME
    HOME_BTN = (By.XPATH, "//a[normalize-space()='Home']")
    FEED_BTN = (By.XPATH, "//a[normalize-space()='Feed']")
    LIBRARY_BTN = (By.XPATH, "//a[normalize-space()='Library']")
    PROFILE_DD = (By.XPATH, "//div[@class='relative flex items-center gap-0']//*[name()='svg']")
    FOR_ARTISTS_BTN = (By.XPATH, "//a[normalize-space()='For Artists']")
    UPLOAD_BTN = (By.XPATH, "//a[@class='text-zinc-400 hover:text-white font-bold tracking-tight ml-1']")
    NOTIFS_BTN = (By.XPATH, "//button[@aria-label='Notifications']//*[name()='svg']")
    MSGS_BTN = (By.XPATH,
                "//div[@class='hidden md:flex items-center gap-5 text-sm']//a[@class='text-zinc-400 hover:text-white']//*[name()='svg']")
    OPTIONS_BTN = (By.XPATH, "//div[@class='hidden md:flex items-center gap-5 text-sm']//div[3]//*[name()='svg']")
    TRY_FREE_BTN = (By.XPATH,
                    "//button[@class='border border-orange-500 text-white hover:bg-orange-500 font-bold tracking-tight px-3 py-1 rounded-sm transition-colors duration-150 text-xs']")
    SEARCH_BAR = (By.XPATH, "//input[@placeholder='Search']")
    SEARCH_BAR_SONG_DD = (By.XPATH, "//p[@class='text-white text-[13px] font-medium truncate']")
    SEARCH_BAR_USER_DD = (By.XPATH, "//p[normalize-space()='@MiroMiro · 1 followers']")
    SC_BTN = (By.XPATH, "//*[name()='path' and contains(@d,'M23.999 14')]")
    PROFILE_BTN = (By.XPATH, "//span[@class='text-xs text-white font-bold']")
    # SIDEBAR
    UNLOCK_PRO_BTN = (By.XPATH, "//span[@class='px-1 text-[13px] font-medium tracking-tight leading-snug']")
    FOLLOW_BTN = (By.XPATH, "//div[@class='flex flex-col gap-3']//div[1]//button[1]")
    # MN AWEL HENA EL 7AGA BTA3ET EL FEED
    REPOSTS_TOGGLE = (By.XPATH,
                      "//button[@class='relative w-12 h-6 rounded-full transition-colors duration-200 focus:outline-none border-2 bg-orange-500 border-orange-500']")
    PLAY_BTN = (By.XPATH,
                "//body/div/div[@data-testid='feed-page']/div/div/div[@data-testid='feed-list']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]//*[name()='svg']//*[name()='polygon' and contains(@points,'2,0 14,7 2')]")
    LIKE_BTN = (By.XPATH,
                "//body/div/div[@data-testid='feed-page']/div/div/div[@data-testid='feed-list']/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]//*[name()='svg']")
    REPOST_BTN = (By.XPATH,
                  "//body//div//div[@data-testid='feed-page']//div//div//div[1]//div[2]//div[1]//div[1]//div[1]//div[3]//div[1]//button[2]//*[name()='svg']//*[name()='path' and contains(@d,'M13 18H7a2')]")
    SHARE_BTN = (By.XPATH,
                 "//body//div//div[@data-testid='feed-page']//div//div//div[1]//div[2]//div[1]//div[1]//div[1]//div[3]//div[1]//button[3]//*[name()='svg']//*[name()='line' and contains(@x1,'8.59')]")
    COPY_BTN = (By.XPATH,
                "//body//div//div[@data-testid='feed-page']//div//div//div[1]//div[2]//div[1]//div[1]//div[1]//div[3]//div[1]//button[4]//*[name()='svg']")
    MORE_BTN = (By.XPATH,
                "//body//div//div[@data-testid='feed-page']//div//div//div[1]//div[2]//div[1]//div[1]//div[1]//div[3]//div[1]//div[1]//button[1]//*[name()='svg']")
    ADD_TO_QUEUE_BTN = (By.XPATH, "//button[normalize-space()='Add to Next up']")
    ADD_TO_PLAYLIST_BTN = (By.XPATH, "//button[normalize-space()='Add to Playlist']")
    STATION_BTN = (By.XPATH, "//button[normalize-space()='Station']")
    # 7AGET EL LIBRARY
    OVERVIEW_BTN = (By.XPATH, "//button[normalize-space()='Overview']")
    LIKES_BTN = (By.XPATH, "//button[normalize-space()='Likes']")
    PLAYLISTS_BTN = (By.XPATH, "//button[normalize-space()='Playlists']")
    ALBUMS_BTN = (By.XPATH, "//button[normalize-space()='Albums']")
    STATIONS_BTN = (By.XPATH, "//button[normalize-space()='Stations']")
    FOLLOWING_BTN = (By.XPATH,
                     "//button[@class='px-5 py-3 transition-colors relative whitespace-nowrap'][normalize-space()='Following']")
    HISTORY_BTN = (By.XPATH, "//button[normalize-space()='History']")
    CLEAR_MY_HISTORY = (By.XPATH,
                        "//button[@class='text-xs text-zinc-400 hover:text-white transition-colors font-semibold']")
    FILTER_TXTBOX = (By.XPATH, "//input[@placeholder='Filter']")


class LoginSelectors:
    LOGIN_EMAIL_TXTBOX = (By.XPATH, "//input[@type='email']")
    CONTINUE_BTN = (By.XPATH, "//button[normalize-space()='Continue']")
    PASSWORD_TXTBOX = (By.XPATH, "//input[@placeholder='Your password']")
    CONTINUE_PASSWORD_BTN = (By.XPATH, "//button[@type='submit']")


