import time

import pytest
from utils.driver_setup import get_driver
from pages.login import LoginPage
from pages.feed import FeedPage

EMAIL = "yararamy88@gmail.com"
PASSWORD = "Test1234!"
SONG_NAME = "Angel of Small Death and the Codeine Scene"
USER_NAME = "MiroMiro"

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_play_from_feed(driver):
    driver.get("https://tunify.duckdns.org/signin")
    page = LoginPage(driver)
    page.login(EMAIL, PASSWORD)
    time.sleep(10)
    feed_page = FeedPage(driver)
    feed_page.go_to_feed()
    time.sleep(2)
    feed_page.play_a_song()
    time.sleep(10)
    t1 = feed_page.time_to_seconds(feed_page.get_current_time())
    time.sleep(2)
    t2 = feed_page.time_to_seconds(feed_page.get_current_time())
    assert t2 > t1, f"Playback not progressing (t1={t1}, t2={t2})"

def test_like_from_feed(driver):
    driver.get("https://tunify.duckdns.org/signin")
    page = LoginPage(driver)
    page.login(EMAIL, PASSWORD)
    time.sleep(2)
    feed_page = FeedPage(driver)
    feed_page.go_to_feed()
    time.sleep(2)
    likes_before = feed_page.get_likes_count()
    feed_page.like_a_song()
    time.sleep(10)
    likes_after = feed_page.get_likes_count()
    assert likes_after > likes_before, \
        f"Like failed: before={likes_before}, after={likes_after}"

def test_search_for_song(driver):
    driver.get("https://tunify.duckdns.org/signin")
    page = LoginPage(driver)
    page.login(EMAIL, PASSWORD)
    time.sleep(2)
    feed_page = FeedPage(driver)
    feed_page.search_for_song(SONG_NAME)
    time.sleep(2)
    assert feed_page.is_song_visible(SONG_NAME), \
        f"Song '{SONG_NAME}' not found in search results"

def test_search_for_user(driver):
    driver.get("https://tunify.duckdns.org/signin")
    page = LoginPage(driver)
    page.login(EMAIL, PASSWORD)
    time.sleep(2)
    feed_page = FeedPage(driver)
    feed_page.search_for_user(USER_NAME)
    time.sleep(2)
    assert feed_page.is_user_visible(USER_NAME), \
        f"User '{USER_NAME}' not found in search results"