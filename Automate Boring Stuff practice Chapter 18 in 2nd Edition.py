import ezgmail
import os
import imapclient
import pprint
import imaplib
import datetime
import pyzmail
from twilio.rest import Client

# p. 418-19 Enabling Gmail API

# ezgmail.init()

# sends email with the first argument as the title and the second as the body

# ezgmail.send('fakehustle@gmail.com', 'Hello', 'This is a test.')

# If you want to attach files to your email, you can provide an extra list argument to the send() function:

# ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email',
# ['attachment1.jpg', 'attachment2.mp3'])

# You can also supply the optional keyword arguments cc and bcc to send carbon copies and blind carbon
# copies:

# ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email',
# cc='friend@example.com', bcc='otherfriend@example.com,someoneelse@example.com')

# If you need to remember which Gmail address the token.json file is configured for, you can examine
# ezgmail.EMAIL_ADDRESS. Note that this variable is populated only after ezgmail.init() or any other EZGmail
# function is called:


# ezgmail.init()
# ezgmail.EMAIL_ADDRESS
# 'example@gmail.com'

# p. 420 Reading Mail from a Gmail Account

'''
unreadThreads = ezgmail.unread()  # List of GmailThread objects.

ezgmail.summary(unreadThreads)


unreadThreads = ezgmail.unread()  # List of GmailThread objects.

print(len(unreadThreads))
print(str(unreadThreads[0]))
print(len(unreadThreads[0].messages))
print(str(unreadThreads[0].messages[0]))
print(unreadThreads[0].messages[0].subject)
print(unreadThreads[0].messages[0].body)
print(unreadThreads[0].messages[0].timestamp)
print(unreadThreads[0].messages[0].sender)
print(unreadThreads[0].messages[0].recipient)


recentThreads = ezgmail.recent()
print(len(recentThreads))
recentThreads = ezgmail.recent(maxResults=100)
print(len(recentThreads))



# p. 420-421  Searching Mail form a Gmail Account

resultThreads = ezgmail.search('Sega')
print(len(resultThreads))
# print(ezgmail.summary(resultThreads))
resultThreads = ezgmail.search('label:UNREAD')
print(len(resultThreads))
print(ezgmail.summary(resultThreads))


# p. 421 Downloading Attachments from a Gmail Account

threads = ezgmail.search('vacation photos')  # search for photos

# print titles of attachments in the search results' first message
# of the first email thread
print(threads[0].messages[0].attachments)

# downloads the attachment from the results
threads[0].messages[0].downloadAttachment('tulips.jpg')

# downloads all of the attachments and puts them in a folder titled
# 'vacation2019' in the working directory
threads[0].messages[0].downloadAllAttachments(downloadFolder='vacation2019')

# If a file already exists with the attachment’s filename, the downloaded attachment will automatically
# overwrite it.


# p. 422-423 Sending email/Connecting to an SMTP Server

Once you have the domain name and port information for your email provider, create an SMTP object by
calling smptlib.SMTP(), passing the domain name as a string argument, and passing the port as an integer
argument. The SMTP object represents a connection to an SMTP mail server and has methods for sending
emails.

smtpObj = smtplib.SMTP('smtp.example.com', 587)
type(smtpObj)
<class 'smtplib.SMTP'>




# p. 423 Sending The SMTP "Hello" Message

Once you have the SMTP object, call its oddly named ehlo() method to “say hello” to the SMTP email server.
This greeting is the first step in SMTP and is important for establishing a connection to the server.

smtpObj.ehlo()
(250, b'mx.example.com at your service, [216.172.148.131]\nSIZE 35882577\
n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nCHUNKING')



# p. 423-424 Starting TLS Encryption

If you are connecting to port 587 on the SMTP server (that is, you’re using TLS encryption), you’ll need to
call the starttls() method next. This required step enables encryption for your connection. If you are
connecting to port 465 (using SSL), then encryption is already set up, and you should skip this step.

# The starttls() method puts your SMTP connection in TLS mode.
smtpObj.starttls()
(220, b'2.0.0 Ready to start TLS') # The 220 in the return value tells you
that the server is ready.


# p. 424 Logging In to the SMTP Server

Once your encrypted connection to the SMTP server is set up, you can log in with your username (usually
your email address) and email password by calling the login() method.

smtpObj.login('my_email_address@example.com', 'MY_SECRET_PASSWORD')
# The 235 in the return value means authentication was successful. Python raises an
(235, b'2.7.0 Accepted')
smtplib.SMTPAuthenticationError exception for incorrect passwords.



# Sending an Email

Once you are logged in to your email provider’s SMTP server, you can call the sendmail() method to actually
send the email.


smtpObj.sendmail('my_email_address@example.com
', 'recipient@example.com', 'Subject: So long.\nDear Alice, so long and thanks for all the fish.
Sincerely, Bob')
{}

# Disconnecting from the SMTP Server

smtpObj.quit() # disconnects your program from the SMTP server.

# p. 425-426 IMAP
Once you have the domain name of the IMAP server, call the imapclient.IMAPClient() function to create an
IMAPClient object. Most email providers require SSL encryption, so pass the ssl=True keyword argument.

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)

Logging In to the IMAP Server

Once you have an IMAPClient object, call its login() method, passing in the username (this is usually your
email address) and password as strings.

imapObj.login('my_email_address@example.com', 'MY_SECRET_PASSWORD')
'my_email_address@example.com Jane Doe authenticated (Success)'

Searching for Email

Once you’re logged on, actually retrieving an email that you’re interested in is a two-step process. First, you
must select a folder you want to search through. Then, you must call the IMAPClient object’s search() method,
passing in a string of IMAP search keywords.

# p.426-427 Selecting a folder


imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
# future reference - you need to generate an app password for third party apps
# use input("Enter password: ") as the second argument to guard password
imapObj.login('clonlineorders23@gmail.com', 'makzttadegpgnhmo')
# pprint.pprint(imapObj.list_folders())
# imapObj.select_folder('Inbox', readonly=True)
# need to import DATETIME, book is out of date.
UIDs = imapObj.search(['SINCE 05-Jul-2020'])
print(UIDs)

imaplib._MAXLINE = 10000000  # change the amount of memory allowed for IMAP programs

# p. 429 Fetching an Email and Marking It as Read

Once you have a list of UIDs, you can call the IMAPClient object’s fetch() method to get the actual email
content.

The list of UIDs will be fetch()’s first argument. The second argument should be the list ['BODY[]'], which
tells fetch() to download all the body content for the emails specified in your UID list.


imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('clonlineorders23@gmail.com', 'makzttadegpgnhmo')
imapObj.select_folder('Inbox', readonly=True)
# need to import DATETIME, book is out of date. https://www.reddit.com/r/learnpython/comments/8w7ppm/help_with_imapclient_date_syntax/
UIDs = imapObj.search(['SINCE', datetime.date(2019, 7, 5)])
print(UIDs)
# rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
# pprint.pprint(rawMessages)

# p. 430 Getting Email Addresses from a Raw Message
rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
message = pyzmail.PyzMessage.factory(rawMessages[161][b'BODY[]'])

print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))
print(message.get_addresses('cc'))
print(message.get_addresses('bcc'))



# p. 430-431 Getting the Body from a Raw Message

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('clonlineorders23@gmail.com', 'makzttadegpgnhmo')
imapObj.select_folder('Inbox', readonly=True)
# need to import DATETIME, book is out of date.
UIDs = imapObj.search(['SINCE', datetime.date(2019, 7, 5)])
print(UIDs)
rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
message = pyzmail.PyzMessage.factory(rawMessages[161][b'BODY[]'])

print(message.text_part != None)
print(message.text_part.get_payload().decode(message.text_part.charset))
print(message.html_part != None)
print(message.html_part.get_payload().decode(message.html_part.charset))

# Deleting Emails

To delete emails, pass a list of message UIDs to the IMAPClient object’s delete_messages() method. This marks
the emails with the \Deleted flag. Calling the expunge() method permanently deletes all emails with the
/Deleted flag in the currently selected folder.

imapObj.select_folder('INBOX', readonly=False)
UIDs = imapObj.search(['ON 09-Jul-2019'])
print(UIDs)
[40066]
imapObj.delete_messages(UIDs)
{40066: ('\\Seen', '\\Deleted')}
imapObj.expunge()
('Success', [(5452, 'EXISTS')])


# Disconnecting from the IMAP Server

When your program has finished retrieving or deleting emails, simply call the IMAPClient’s logout() method
to disconnect from the IMAP server.

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('clonlineorders23@gmail.com', 'makzttadegpgnhmo')
imapObj.select_folder('Inbox', readonly=True)
# need to import DATETIME, book is out of date.
UIDs = imapObj.search(['SINCE', datetime.date(2019, 7, 5)])
print(UIDs)
imapObj.logout()

p. 436-437 Signing Up for a Twilio Account/Sending Text Messages


accountSID = 'ACcf9eefd519df8417f82ae4b538c96feb'
authToken = '3e9137bf2cf277964a3e92fdeabfe222'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+16677715754'
myCellPhone = '‪+18622592031‬'
message = twilioCli.messages.create(
    body='This is just a test, #MyGuy.', from_=myTwilioNumber, to=myCellPhone)
print(message.to)
print(message.from_)
print(message.body)
print(message.status)
print(message.date_created)
print(message.date_sent == None)
print(message.sid)
# .get deprecated so you have to use message.fetch instead -  https://old.reddit.com/r/learnpython/comments/gkr5gm/problem_with_the_twilio_example_from_automate_the/
updatedMessage = twilioCli.messages(message.sid).fetch()
print(updatedMessage.status)
print(updatedMessage.date_sent)

'''

# p. 437-440 Project "Just Text Me" Module
