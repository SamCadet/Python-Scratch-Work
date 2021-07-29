from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("C:\\Users\\Sam\\Downloads\\chromedriver.exe")

print(type(browser))

# browser.get('http://inventwithpython.com')

# try:
#     elem = browser.find_element_by_class_name('bookcover')
#     print('Found <%s> element with that class name!' % (elem.tag_name))
# except:
#     print('Was not able to find an element with that name.')

# link_elem = browser.find_element_by_link_text(
#     "See what's new in the second edition.")
#
# type(link_elem)
#
# link_elem.click()  # folows the "See what's new in the second edition" link

# browser.get('http://gmail.com')
# email_elem = browser.find_element_by_id('identifierId')
# email_elem.send_keys('not_my_real_email@gmail.com')
# password_elem = browser.find_element_by_id('Passwd')
# password_elem.send_keys('12345')
# password_elem.submit()

browser.get('http://nostarch.com')
html_elem = browser.find_element_by_tag_name('html')
html_elem.send_keys(Keys.END)       # scrolls to bottom
html_elem.send_keys(Keys.HOME)      # scrolls to top
