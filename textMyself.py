#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string.

# p. 438

from twilio.rest import Client
import os

twilioAccountSID = os.environ['twilioAccountSID']
twilioAuthToken = os.environ['twilioAuthToken']
myNumber = os.environ['myNumber']
twilioNumber = os.environ['twilioNumber']


def textmyself(message):
    twilioCli = Client(twilioAccountSID, twilioAuthToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
