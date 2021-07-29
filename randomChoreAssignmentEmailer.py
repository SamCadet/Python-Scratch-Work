#! python3

# randomChoreAssignmentEmailer.py - Assign random chores to folks

import smtplib
import random

# make a list of people's emails and a list of chores

people = ['Rashid@example.com', 'Akhbar@example.com',
          'Keisha@example.com', 'Greta@example.com']
chores = ['dishes', 'bathroom', 'vacuum', 'garbage']

# TODO: randomly assign chores to people

# randomChore = random.choice(chores)
# chores.remove(randomChore)  # this chore is now taken, so remove it


randomChore = random.choice(chores)
chores.remove(randomChore)
# this chore is now taken, so remove it

# TODO: send chores to people listed via email and take care of redundancies

email = input('Enter your email: ')
password = input('Enter your password: ')

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()

# Figure out why this won't run in command line, use app password in the meantime
smtpObj.login(email, password)

for i in people:
    body = '''Subject: %s Chores list \nDear %s, \nHere are your chores for the upcoming
    week. If you're mad, take it up with ya momma!'''
    print('Sending email to %s...' % people)
    sendmailStatus = smtpObj.sendmail(
        'clonlineorders23@gmail.com', body)

    if sendmailStatus != {}:
        print('There was a problem sending email to %s: %s' %
              (email, sendmailStatus))

smtpObj.quit()

# TODO: make the program run once a week
