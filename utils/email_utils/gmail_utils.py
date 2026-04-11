import imaplib
import email
import re



def get_verification_link(gmail_address, app_password):
    mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    mail.login(gmail_address, app_password)
    mail.select("inbox")

    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()

    latest_email_id = email_ids[-1]

    status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = msg_data[0][1]

    msg = email.message_from_bytes(raw_email)

    print("Subject:", msg["Subject"])
    print("-" * 50)

    body = ""

    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))

            if "attachment" in content_disposition.lower():
                continue

            if content_type == "text/plain" or content_type == "text/html":
                payload = part.get_payload(decode=True)
                if payload:
                    body += payload.decode(errors="ignore") + "\n"
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            body = payload.decode(errors="ignore")

    links = re.findall(r'https?://[^\s"<>]+', body)

    for link in links:
        if "email-confirmation" in link:
            print("VERIFICATION LINK:", link)
            mail.logout()
            return link

    print("VERIFICATION LINK: None")
    mail.logout()
    return None

def get_pass_reset_link(gmail_address, app_password):
    mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    mail.login(gmail_address, app_password)
    mail.select("inbox")

    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()

    latest_email_id = email_ids[-1]

    status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = msg_data[0][1]

    msg = email.message_from_bytes(raw_email)

    print("Subject:", msg["Subject"])
    print("-" * 50)

    body = ""

    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))

            if "attachment" in content_disposition.lower():
                continue

            if content_type == "text/plain" or content_type == "text/html":
                payload = part.get_payload(decode=True)
                if payload:
                    body += payload.decode(errors="ignore") + "\n"
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            body = payload.decode(errors="ignore")

    links = re.findall(r'https?://[^\s"<>]+', body)

    for link in links:
        if "password-reset" in link:
            print("PASSWORD RESET LINK:", link)
            mail.logout()
            return link

    print("PASSWORD RESET LINK: None")
    mail.logout()
    return None


#get_verification_link('softwaretestacc198@gmail.com','zupqwxwlerldqgcf' )



#get_pass_reset_link('softwaretestacc198@gmail.com','zupqwxwlerldqgcf' )
