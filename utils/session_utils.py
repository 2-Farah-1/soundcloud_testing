import json

def load_cookies(driver, path="cookies.json"):
    # Step 1: open domain first
    driver.get("https://soundcloud.com")

    # Step 2: load cookies
    with open(path, "r") as f:
        cookies = json.load(f)

    for cookie in cookies:
        # fix common issues
        if "sameSite" in cookie:
            del cookie["sameSite"]

        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(f"Skipping cookie: {cookie.get('name')} -> {e}")

    # Step 3: apply cookies
    driver.refresh()