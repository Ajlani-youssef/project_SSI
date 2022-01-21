import random
import smtplib
import ssl

import config

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = config.email
password = config.email_password


def generate_code():
    code = random.choice(range(100000, 999999))  # generating 6-digit random code
    return code


def send_verification_code(receiver_email):
    otp = generate_code()
    message = f"""\
Subject: Verification code

    Hello This is your OTP code: {otp} """
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    return otp
