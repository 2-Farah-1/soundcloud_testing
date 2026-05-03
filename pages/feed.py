import time

from selenium.webdriver.common.by import By
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selectors import FeedSelectors

class FeedPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def go_to_feed(self):
        self.wait.until(EC.element_to_be_clickable(FeedSelectors.FEED_BTN)).click()

    def go_to_library(self):
        self.wait.until(EC.element_to_be_clickable(FeedSelectors.LIBRARY_BTN)).click()

    def go_to_home(self):
        self.wait.until(EC.element_to_be_clickable(FeedSelectors.HOME_BTN)).click()

    def play_a_song(self):
        self.wait.until(EC.element_to_be_clickable(FeedSelectors.PLAY_BTN)).click()

    def like_a_song(self):
        self.wait.until(EC.element_to_be_clickable(FeedSelectors.LIKE_BTN)).click()

    def search_for_song(self, song_name):
       song = self.wait.until(EC.element_to_be_clickable(FeedSelectors.SEARCH_BAR))
       song.send_keys(song_name)
       self.wait.until(EC.presence_of_element_located(FeedSelectors.SEARCH_BAR_SONG_DD)).click()

    def search_for_user(self, user_name):
        user = self.wait.until(EC.element_to_be_clickable(FeedSelectors.SEARCH_BAR))
        user.send_keys(user_name)
        self.wait.until(EC.presence_of_element_located(FeedSelectors.SEARCH_BAR_USER_DD)).click()

    def get_current_time(self):
        time_element = self.driver.find_element(
            By.XPATH,
            "//div[contains(@class,'fixed') and contains(@class,'bottom-0')]//span[contains(text(),':')]"
        )
        return time_element.text

    def time_to_seconds(t):
        minutes, seconds = map(int, t.split(":"))
        return minutes * 60 + seconds

    def get_likes_count(self):
        like_button = self.driver.find_element(
            By.XPATH,
            "//button[contains(@aria-label, 'Like')]"
        )
        label = like_button.get_attribute("aria-label")  # e.g. "Like (5)"

        match = re.search(r"\((\d+)\)", label)
        return int(match.group(1)) if match else 0

    def is_song_visible(self, song_name):
        titles = self.driver.find_elements(
            By.XPATH,
            "//p[@class='text-white text-[13px] font-medium truncate']"
        )

        for t in titles:
            if song_name.lower() in t.text.lower():
                return True
        return False

    def is_user_visible(self, user_name):
        elements = self.driver.find_elements(
            By.XPATH,
            f"//p[@class='text-white text-[13px] font-medium truncate'][normalize-space()='{user_name}']"
        )
        return len(elements) > 0

