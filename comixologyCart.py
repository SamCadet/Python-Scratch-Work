#! python3

# comixologyCart.py - automate adding comics to cart

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("C:\\Users\\Sam\\Downloads\\chromedriver.exe")
browser.get(
    'https://www.comixology.com/search/items?search=black+panther&subType=SINGLE_ISSUES')
'''
try:
    elem = browser.find_element_by_class_name('action-title')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
'''
addToCart = browser.find_element_by_class_name('action-title')

timeout = time.time() + 30 * 1

while True:
    addToCart.click()
    time.sleep(1)
    browser.execute_script("window.history.go(-1)")
    if time.time() > timeout:
        break
