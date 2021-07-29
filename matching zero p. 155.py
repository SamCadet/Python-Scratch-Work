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

batregex = re.compile(r'Bat(wo)*man')
mo1 = batregex.search('The Adventures of Batman')

print(mo1.group())

mo2 = batregex.search('The Adventures of Batwoman')
print(mo2.group())

mo3 = batregex.search('The Adventures of Batwowowowoman')
print(mo3.group())

batregex = re.compile(r'Bat(wo)+man')
mo1 = batregex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batregex.search('The Adventures of Batwowowowoman')
print(mo2.group())

mo3 = batregex.search('The adventures of Batman')
print(mo3 == None)
