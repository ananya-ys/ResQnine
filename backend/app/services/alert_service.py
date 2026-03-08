from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr
from twilio.rest import Client

conf = ConnectionConfig(
    MAIL_USERNAME="ananyays2625@gmail.com",
    MAIL_PASSWORD="rjjceecojgfloubk",
    MAIL_FROM="ananyays2625@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True
)

async def send_email_alert():

    message = MessageSchema(
        subject="🚨 ResQnine Emergency Alert",
        recipients=["aaryanraj23082001@gmail.com"],  # who receives alert
        body="Emergency alert triggered! Please check the user's location immediately.",
        subtype="plain"
    )

    fm = FastMail(conf)
    await fm.send_message(message)

account_sid = "ACf58414baa3c1afb79bf0d612e965ec76"
auth_token = "c94a41d703c0074950c9b43dd36159fa"

twilio_client = Client(account_sid, auth_token)

TWILIO_PHONE = "+19135137817"
CONTACTS = [
    "+918217465810",
    "+918809729001",
    "+917795731266"
]

def send_sms_alert(lat, lng):

    map_link = f"https://maps.google.com/?q={lat},{lng}"

    message_body = f"""
🚨 RESQNINE EMERGENCY ALERT

User may be in danger.

Live Location:
{map_link}
"""

    for contact in CONTACTS:
        twilio_client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE,
            to=contact
        )