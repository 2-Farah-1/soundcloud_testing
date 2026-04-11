import time

from selenium.webdriver.common.by import By
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selectors import LoginSelectors, ProfileSelectors, FeedSelectors


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def go_to_profile(self):
        self.wait.until(EC.element_to_be_clickable(FeedSelectors.PROFILE_BTN)).click()

    def update_info(self, dispName, cityName, countryName, bioTxt):
        self.wait.until(EC.element_to_be_clickable(ProfileSelectors.EDIT_BTN)).click()
        name = self.wait.until(EC.element_to_be_clickable(ProfileSelectors.DISPLAY_NAME_TXTBOX))
        name.clear()
        name.send_keys(dispName)
        city = self.wait.until(EC.element_to_be_clickable(ProfileSelectors.CITY_TXTBOX))
        city.clear()
        city.send_keys(cityName)
        country = self.wait.until(EC.element_to_be_clickable(ProfileSelectors.COUNTRY_TXTBOX))
        country.clear()
        country.send_keys(countryName)
        bio = self.wait.until(EC.element_to_be_clickable(ProfileSelectors.BIO_TXTBOX))
        bio.clear()
        bio.send_keys(bioTxt)
        self.wait.until(EC.element_to_be_clickable(ProfileSelectors.SAVE_CHANGES_BTN)).click()

    def get_display_name(self):
        return self.wait.until(EC.visibility_of_element_located(ProfileSelectors.DISPLAY_NAME_LABEL)).text

    def get_city(self):
        return self.wait.until(EC.visibility_of_element_located(ProfileSelectors.CITY_LABEL)).text

    def get_country(self):
        return self.wait.until(EC.visibility_of_element_located(ProfileSelectors.COUNTRY_LABEL)).text

    def upload_pfp(self, pic_path):
        # self.wait.until(EC.element_to_be_clickable(ProfileSelectors.PROFILE_PIC_UPLOAD_BTN)).click()
        pfp_input = self.wait.until(EC.presence_of_element_located(ProfileSelectors.PROFILE_PIC_UPLOAD))
        self.driver.execute_script("arguments[0].classList.remove('hidden');", pfp_input)
        pfp_input.send_keys(pic_path)
        time.sleep(5)

    def upload_header(self, header_path):
        header_input = self.wait.until(EC.presence_of_element_located(ProfileSelectors.HEADER_PIC_UPLOAD))
        self.driver.execute_script("arguments[0].classList.remove('hidden');", header_input)
        header_input.send_keys(header_path)
        time.sleep(5)

    def is_profile_picture_uploaded(self):
        img = self.wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Avatar']")))
        src = img.get_attribute("src")
        return src is not None and "blob:" in src

    def is_header_picture_uploaded(self):
        img = self.wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Header']")))
        src = img.get_attribute("src")
        return src is not None and "blob:" in src
    # def get_pfp_src(self):
    #     return self.wait.until(EC.presence_of_element_located(ProfileSelectors.PROFILE_PIC_UPLOAD)).value_of_css_property("background-image")
    # Navigation
    # def go_to_profile(self):
    #     self.driver.get("https://soundcloud.com/you")
    #
    # bio_input = (By.XPATH, "//textarea[@name='bio']")
    # location_input = (By.XPATH, "//input[@name='city']")
    # genre_tags = (By.XPATH, "//input[@placeholder='Add genres']")
    # upload_button = (By.XPATH, "//a[contains(@href,'upload')]")
    # avatar_upload = (By.XPATH, "//input[@type='file']")
    # social_input = (By.XPATH, "//input[contains(@placeholder,'http')]")
    #
    # def update_profile_info(self, bio, location, genre):
    #     self.driver.find_element(*self.bio_input).clear()
    #     self.driver.find_element(*self.bio_input).send_keys(bio)
    #
    #     self.driver.find_element(*self.location_input).clear()
    #     self.driver.find_element(*self.location_input).send_keys(location)
    #
    #     genre_field = self.driver.find_element(*self.genre_tags)
    #     genre_field.send_keys(genre)
    #
    #
    # def is_artist(self):
    #     return len(self.driver.find_elements(*self.upload_button)) > 0
    #
    #
    # def upload_avatar(self, file_path):
    #     self.driver.find_element(*self.avatar_upload).send_keys(file_path)
    #
    #
    # def add_social_link(self, link):
    #     self.driver.find_element(*self.social_input).send_keys(link)
    #
    #
    # def get_location_text(self):
    #     location_element = self.wait.until(
    #         EC.visibility_of_element_located(
    #             (By.CSS_SELECTOR, "h3.profileHeaderInfo__additional")
    #         )
    #     )
    #     return location_element.text
    #
    # def wait_until_avatar_updated(self, old_avatar, timeout=30):
    #     WebDriverWait(self.driver, timeout).until(
    #         lambda d: self.get_avatar_url() != old_avatar
    #     )
    #
    # def get_avatar_url(self):
    #     element = self.wait.until(
    #         EC.presence_of_element_located(
    #             (By.CSS_SELECTOR, "span[aria-label*='avatar']")
    #         )
    #     )
    #
    #     style = element.get_attribute("style")
    #
    #     match = re.search(r'url\("(.+?)"\)', style)
    #     return match.group(1) if match else None
    #
    # def get_social_links(self):
    #     elements = self.wait.until(
    #         EC.presence_of_all_elements_located(
    #             (By.CSS_SELECTOR, "a.web-profile")
    #         )
    #     )
    #     return [el.get_attribute("href") for el in elements]