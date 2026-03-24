import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    service = Service(r"C:\browserdrivers\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()