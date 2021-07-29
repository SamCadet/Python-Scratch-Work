#! python 3

# autoUnsubscriber.py - finds unsubscribe links in emails and opens them in a browser.

import imapclient
import imaplib
import requests
import pyzmail
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4
import pyzmail
import webbrowser

'''
# Login to IMAP server with IMAP client

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login(input('Enter Email: '), input('Enter Password: '))
imapObj.select_folder('Inbox', readonly=True)

# Use requests to access site and parse through email with bs4

res = requests.get('https://mail.google.com/mail/u/1/#inbox')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'lxml')
unsubscribe_elem = soup.select('.unsubscribe')
links = []


for link in soup.findAll('a'):
    links.append(link.get(str(unsubscribe_elem)))
    print(links)

# Open browser and unsubscribe links with selenium


browser = webdriver.Chrome('C:\\Users\\Sam\\Downloads\\chromedriver.exe')

mail = browser.get('https://mail.google.com/mail/u/1/#inbox')

mail.find_element_by_class_name('whsOnd zHQkBf')
mail.send_keys('clonlineorders23')
mail.submit()
'''

# Answer - https://github.com/IFinners/automate-the-boring-stuff-projects/blob/master/Chapter%2016/auto_unsubscriber.py


def unsub_scan(user_name, user_pass):
    """Returns a list of the unsubscribe links in a Gmail inbox."""
    unsub_links = []
    imaplib._MAXLINE = 10000000
    imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imap_obj.login(user_name, user_pass)
    imap_obj.select_folder('INBOX', readonly=True)
    unique_ids = imap_obj.search(['ALL'])

    for identifier in unique_ids:
        raw_message = imap_obj.fetch([identifier], ['BODY[]', 'FLAGS'])
        message = pyzmail.PyzMessage.factory(
            raw_message[identifier][b'BODY[]'])
        html = message.html_part.get_payload().decode(message.html_part.charset)
        soup = bs4.BeautifulSoup(html, 'lxml')
        link_elems = soup.select('a')
        for selected in link_elems:
            if 'unsubscribe' in str(selected):
                unsub_links.append(selected.get('href'))

    imap_obj.logout()

    return unsub_links


email = input('Enter your email username: ')
password = input('Enter your email password: ')
links = unsub_scan(email, password)

for link in links:
    webbrowser.open(link)

print('All unsubscribe links have been opened.')
