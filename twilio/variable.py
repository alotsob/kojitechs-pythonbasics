
from twilio.rest import Client
from gtts import gTTS
from pprint import pprint
import os


def sending_sms(sending_to, message):
    try:
        account_sid = os.environ.get("ACCOUNT_SID") # AC80b95afbb503d667e3009c229367d2b4
        auth_Token = os.environ.get("AUTH_TOKEN") # 46124cc1d38e9ffb165ac8cbb00fb265
        twilio_number = os.environ.get("TWILIO_NUMBER") # +17153333722

        client = Client(account_sid, auth_Token)
        client.messages.create(
            to = sending_to,
            from_ = twilio_number,
            body = message   
        )

    except Exception as e: 
        print(e)   
    return None    

#calling sending sms from another function
"""
message = input('What is your message?: ')
sending_to = input('please enter phone number: ')
sending_sms(sending_to, message)
"""


def calling_function():
    try:
        message = input("please what is your message")
        sending_to = input("please enter phone number")
        sending_sms(sending_to, message)
    except Exception as e:
        print(e)    

if __name__ == "__main__":
    pass

def robbort (message):
    mytext = message
    language = 'en'
    voice = gTTS(
        text = mytext,
        lang = language,
        slow = False
    )
    voice.save("audio_recorder/voic.mp3")
    os.system("mpg321 audio_recorder/voic.mp3")
    return None

message = input("What is your message: ")
robbort(message)