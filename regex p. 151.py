import re
#
# phonenumregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#
# mo = phonenumregex.search('My number is 415-555-4242.')
#
# print('Phone number found: ' + mo.group())

phonenumregex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phonenumregex.search('My number is 415-555-4242.')

print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())

print(mo.groups())

areacode, mainnumber = mo.groups()
print(areacode)
print(mainnumber)

phonenumregex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phonenumregex.search('My phone number is (415) 555-4242.')
print(mo.group(1))
