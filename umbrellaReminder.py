#! python3

# umbrellaReminder.py - Check if it's raining and, if so, tells you to pack an umbrella

import requests
import bs4
from twilio.rest import Client
import os


# Answers - https://github.com/kudeh/automate-the-boring-stuff-projects/blob/master/umbrella-reminder/umbrella_reminder.py
# and https://github.com/IFinners/automate-the-boring-stuff-projects/blob/master/Chapter%2016/umbrella-reminder.py
# Go to site


def checkRain():
    url = 'https://forecast.weather.gov/MapClick.php?CityName=Morristown&state=NJ&site=PHI&textField1=40.7967&textField2=-74.4776&e=0'
    rain = False

    try:
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        weather_elem = soup.select('.myforecast-current-sm')

        if 'rain' in weather_elem[0].text.lower():
            rain = True

    except Exception as exc:
        print(exc)

    return rain

# Text user to pack an umbrella before leaving the house


def textIfRaining(message):
    twilioAccountSID = os.environ['twilioAccountSID']
    twilioAuthToken = os.environ['twilioAuthToken']
    myNumber = os.environ['myNumber']
    twilioNumber = os.environ['twilioNumber']
    twilioCli = Client(twilioAccountSID, twilioAuthToken)
    twilioCli.messages.create(
        body=message, from_=twilioNumber, to=myNumber)


if checkRain():
    textIfRaining("Aye it's gonna rain so pack an umbrella, #MyGuy.")
