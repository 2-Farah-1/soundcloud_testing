# for the screenshot part
import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    service = Service(r"C:\browserdrivers\chromedriver.exe")

    options = webdriver.ChromeOptions()
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)

    yield driver

    driver.quit()

# hook for screenshots
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks (we don't really have any but for future expansion)
    outcome = yield
    report = outcome.get_result()

    # screnshot el failed test
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            # create screenshots folder if it doesn't exist
            screenshots_dir = "tests/screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            # generate file name (testname_time&date)
            test_name = item.name
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{test_name}_{timestamp}.png"

            file_path = os.path.join(screenshots_dir, file_name)

            # take screenshot
            driver.save_screenshot(file_path)

            print(
                f"\n Screenshot saved: {file_path}")  # basivally it would have the test name and time on the screenshot
