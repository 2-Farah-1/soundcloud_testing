import time

import pytest
from utils.driver_setup import get_driver
from pages.login import LoginPage
from pages.profile import ProfilePage

EMAIL = "yararamy88@gmail.com"
PASSWORD = "D!sMeYa8a"
DISPLAY_NAME = "Yaraaaa"
CITY = "Yara"
COUNTRY = "Testing"
BIO = "E2E Testing Bio hello"
LINK1 = "https://www.instagram.com/_yararamy_"
LINK2 = "https://www.youtube.com"
PFP_PATH = r"C:\Users\Yara\Downloads\4_Image.jpg"
HEADER_PATH = r"C:\Users\Yara\Downloads\sunset-beach-banner-header-seascape-sea-landscape-beautiful-colorful-sunrise-ocean-golden-sun-rays-breaking-303904276.webp"

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_update_profile_info(driver):
    driver.get("https://tunify.duckdns.org/")
    page = LoginPage(driver)
    page.login(EMAIL, PASSWORD)
    profile = ProfilePage(driver)
    time.sleep(1)
    profile.go_to_profile()
    edit_button = ProfilePage(driver)
    edit_button.update_info(DISPLAY_NAME, CITY, COUNTRY, BIO)
    # assert profile.get_display_name() == DISPLAY_NAME
    assert profile.get_city() == CITY
    assert profile.get_country() == COUNTRY
    # assert profile.get_bio() == BIO
    time.sleep(5)

def test_upload_profile_picture(driver):
    driver.get("https://tunify.duckdns.org/")
    page = LoginPage(driver)
    page.login(EMAIL, PASSWORD)
    profile = ProfilePage(driver)
    profile.go_to_profile()
    profile.upload_pfp(PFP_PATH)
    assert profile.is_profile_picture_uploaded()

def test_upload_header_picture(driver):
    driver.get("https://tunify.duckdns.org/")
    page = LoginPage(driver)
    page.login(EMAIL, PASSWORD)
    profile = ProfilePage(driver)
    profile.go_to_profile()
    profile.upload_header(HEADER_PATH)
    assert profile.is_header_picture_uploaded()

# 1. Profile Customization Test
def test_profile_customization(driver):
    driver.get("https://soundcloud.com/")

    login = LoginPage(driver)
    login.login(EMAIL, PASSWORD)

    profile = ProfilePage(driver)
    profile.go_to_profile()

    profile.update_profile_info(
        bio="E2E Testing Bio",
        location="Cairo",
        genre="Hip Hop"
    )

    assert "Cairo" in profile.get_location_text()


# 2. Account Tier Test (Artist vs Listener)
def test_account_tier(driver):
    driver.get("https://soundcloud.com/")

    login = LoginPage(driver)
    login.login(EMAIL, PASSWORD)

    profile = ProfilePage(driver)
    profile.go_to_profile()

    is_artist = profile.is_artist()

    assert isinstance(is_artist, bool)


# 3. Avatar Upload Test
def test_avatar_upload(driver):
    driver.get("https://soundcloud.com/")

    login = LoginPage(driver)
    login.login(EMAIL, PASSWORD)

    profile = ProfilePage(driver)
    profile.go_to_profile()

    old_avatar = profile.get_avatar_url()

    profile.upload_avatar("C:/Users/Yara/Downloads/4_Image.jpg")

    profile.wait_until_avatar_updated(old_avatar)

    new_avatar = profile.get_avatar_url()

    assert old_avatar != new_avatar


# 4. Social Links Test
def test_add_social_links(driver):
    driver.get("https://soundcloud.com/")

    login = LoginPage(driver)
    login.login(EMAIL, PASSWORD)

    profile = ProfilePage(driver)
    profile.go_to_profile()

    profile.add_social_link("https://www.instagram.com/_yararamy_")

    links = profile.get_social_links()

    assert any("instagram.com" in l for l in links)


