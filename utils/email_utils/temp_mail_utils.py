
import email

import requests
import re
import time


API_KEY = "zsG7D6Kx3SFO3r0JA2TsOO/h9akeaNZaHU3i+5QIa8HrGXGjMwxgPFhQ+8RU7krG"


def create_temp_mailbox():
    url = "https://gettestmail.com/api/gettestmail"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-API-Key": API_KEY
    }

    body = {
        # you can leave this fixed or change it later
        "expiresAt": "2026-04-11T23:59:59.000Z"
    }

    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()

    data = response.json()

    print("TEMP EMAIL:", data["emailAddress"])
    print("MAILBOX ID:", data["id"])

    return data


def get_temp_mailbox_message(mailbox_id, timeout_seconds=60, poll_every_seconds=5):
    url = f"https://gettestmail.com/api/gettestmail/{mailbox_id}"

    headers = {
        "Accept": "application/json",
        "X-API-Key": API_KEY
    }

    start_time = time.time()

    while time.time() - start_time < timeout_seconds:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()

        message = data.get("message")

        if message:
            print("Subject:", message.get("subject"))
            print("-" * 50)
            return data

        time.sleep(poll_every_seconds)

    print("No email arrived in time.")
    return None


def get_verification_link_temp(mailbox_id, timeout_seconds=60, poll_every_seconds=5):
    data = get_temp_mailbox_message(mailbox_id, timeout_seconds, poll_every_seconds)

    if not data:
        print("VERIFICATION LINK: None")
        return None

    message = data.get("message", {})
    text_body = message.get("text") or ""
    html_body = message.get("html") or ""
    body = text_body + "\n" + html_body

    links = re.findall(r'https?://[^\s"<>]+', body)

    for link in links:
        if "email-confirmation" in link:
            print("VERIFICATION LINK:", link)
            return link

    print("VERIFICATION LINK: None")
    return None


def get_pass_reset_link_temp(mailbox_id, timeout_seconds=60, poll_every_seconds=5):
    data = get_temp_mailbox_message(mailbox_id, timeout_seconds, poll_every_seconds)

    if not data:
        print("PASSWORD RESET LINK: None")
        return None

    message = data.get("message", {})
    text_body = message.get("text") or ""
    html_body = message.get("html") or ""
    body = text_body + "\n" + html_body

    links = re.findall(r'https?://[^\s"<>]+', body)

    for link in links:
        if "password-reset" in link:
            print("PASSWORD RESET LINK:", link)
            return link

    print("PASSWORD RESET LINK: None")
    return None

def get_verification_code_temp(mailbox_id, timeout_seconds=60, poll_every_seconds=5):
    url = f"https://gettestmail.com/api/gettestmail/{mailbox_id}"

    headers = {
        "Accept": "application/json",
        "X-API-Key": API_KEY
    }

    start_time = time.time()

    while time.time() - start_time < timeout_seconds:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        message = data.get("message")

        if message:
            print("Subject:", message.get("subject"))
            print("-" * 50)

            # combine text + html
            body = (message.get("text") or "") + "\n" + (message.get("html") or "")

            # 🔥 THIS IS THE IMPORTANT PART
            match = re.search(r"\b[A-Z0-9]{6}\b", body)

            if match:
                code = match.group(0)
                print("VERIFICATION CODE:", code)
                return code

        time.sleep(poll_every_seconds)

    print("VERIFICATION CODE: None")
    return None