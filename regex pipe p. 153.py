import re

# heroregex = re.compile(r'Batman|Tina Fey')
# mo1 = heroregex.search('Batman and Tina Fey.')
# print(mo1.group())
#
# mo2 = heroregex.search('Tina Fey and Batman.')
# print(mo2.group())
#
# batregex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batregex.search('Batmobile lost a wheel')
# print(mo.group())
# print(mo.group(1))

batregex = re.compile(r'Bat(wo)?man')
mo1 = batregex.search('The Adventures of Batman')

print(mo1.group())

mo2 = batregex.search('The Adventures of Batwoman')
print(mo2.group())

phoneregex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

mo1 = phoneregex.search('My number 415-555-4242')
print(mo1.group())

mo2 = phoneregex.search('My number is 555-4242')
print(mo2.group())
