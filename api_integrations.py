"""
Handles integrations with third-party APIs like Twilio.
"""

from twilio.rest import Client
import secrets

client = Client(secrets.TWILIO_ACCOUNT_SID, secrets.TWILIO_AUTH_TOKEN)

def make_call(to_number):
    """
    Makes a call to the given number using Twilio.
    """
    try:
        call = client.calls.create(
            to=to_number, 
            from_=secrets.TWILIO_PHONE_NUMBER,
            url="http://demo.twilio.com/docs/voice.xml"  # A simple TwiML URL
        )
        print(f"Call initiated with SID: {call.sid}")
        return call.sid
    except Exception as e:
        print(f"Error making call: {e}")
        return None
