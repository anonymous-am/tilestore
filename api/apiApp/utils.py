import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings


# def generate_random_sequence(length):
#     characters = string.ascii_letters + string.digits  # includes both uppercase and lowercase letters, as well as digits
#     random_sequence = ''.join(random.choice(characters) for _ in range(length))
#     return random_sequence

def generate_random_sequence(length):
    letters = string.ascii_uppercase[:5]  # First 5 uppercase letters
    digits = string.digits
    first_part = ''.join(random.choice(letters) for _ in range(5))
    second_part = ''.join(random.choice(digits) for _ in range(length - 5))
    random_sequence = first_part + second_part
    return random_sequence

def send_email(to_email, subject, body):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = settings.SMTP_USERNAME
    smtp_password = settings.SMTP_PASSWORD
    from_email = settings.FROM_EMAIL
    # message = f'Subject: {subject}\n\n{body}'

    # Your email content
    # html_content = '<p>This is your HTML content</p>'
    html_content = body

    # Create the MIME object
    message = MIMEMultipart()
    message.attach(MIMEText(html_content, 'html'))
    message['Subject'] = 'New Order Received - Order ID: {}'.format(subject)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls()
            smtp.login(smtp_username, smtp_password)
            smtp.sendmail(from_email, to_email, message.as_string())
        return True  # Email sent successfully
    except Exception as e:
        print(f"An error occurred: {e}")
        return False  # Failed to send email


    # with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    #     smtp.starttls()
    #     smtp.login(smtp_username, smtp_password)
    #     smtp.sendmail(from_email, to_email, message)


