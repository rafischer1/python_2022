import smtplib
from email.message import EmailMessage

address_from = "fake1@fake.com"
address_to = "fake2@fake.com"
password = "password123"
# SIMPLE MAIL TRANSFER PROTOCOL
email = EmailMessage()

email['from'] = 'RAFIII'
email['to'] = address_to
email['subject'] = '💸 a million dollars 💸'

email.set_content('EMAIL CONTENT 🤓')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(address_from, password)
    smtp.send_message(email)
    print("EMAIL SENT")
