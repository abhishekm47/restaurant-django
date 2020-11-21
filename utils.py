from django.conf import settings
from twilio.rest import Client

def send_sms(message):
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN

    client = Client(account_sid, auth_token)

    response = client.messages.create(from_=settings.TWILIO_PHONE_NUMBER,
                      to='+31684995255',
                      body=message )
    return response