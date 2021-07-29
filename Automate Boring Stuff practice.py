import re

# greedy_ha_regex = re.compile(r'(Ha){3,5}')
# mo1 = greedy_ha_regex.search('HaHaHaHaHa')
# print(mo1.group())
#
# nongreedy_ha_regex = re.compile(r'(Ha){3,5}?')
# mo2 = nongreedy_ha_regex.search('HaHaHaHaHa')
# print(mo2.group())
#
# phone_numregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phone_numregex.search('Cell: 415-555-9999 Work: 212-555-0000')
# print(mo.group())
#
# print(phone_numregex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
#
# phone_numregex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
# print(phone_numregex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
#
# xmas_regex = re.compile(r'\d+\s\w+')
# print(xmas_regex.findall(
#     '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
#
# vowel_regex = re.compile(r'[aeiouAEIOU]')
# print(vowel_regex.findall('RoBoCop eats baby food. BABY FOOD.'))
#
# consonant_regex = re.compile(r'[^aeiouAEIOU]')
# print(consonant_regex.findall('RoboCop eats baby food. BABY FOOD.'))

# begins_with_hello = re.compile(r'^Hello')
# print(begins_with_hello.search('Hello world!'))
# print(begins_with_hello.search('He said hello.') == None)
#
# ends_with_number = re.compile(r'\d$')
# print(ends_with_number.search('Your number is 42'))
# print(ends_with_number.search('Your number is forty two.') == None)
#
# whole_string_is_num = re.compile(r'^\d+$')
# print(whole_string_is_num.search('1234567890'))
# print(whole_string_is_num.search('12345xyz67890') == None)
# print(whole_string_is_num.search('12 34567890') == None)

# at_regex = re.compile(r'.at')
# print(at_regex.findall('The cat in the hat sat on the flat mat.'))
#
# name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
# mo = name_regex.search('First Name: Sam Last Name: Cadet')
# print(mo.group(1))
# print(mo.group(2))
#
# nongreedy_regex = re.compile(r'<.*?>')
# mo = nongreedy_regex.search('<To serve man> for dinner.>')
# print(mo.group())
#
# greedy_regex = re.compile(r'<.*>')
# mo = greedy_regex.search('<To serve man> for dinner.>')
# print(mo.group())

# no_newline_regex = re.compile('.*')
# print(no_newline_regex.search(
#     'Serve the public trust. \nProtect the innocent. \nUphold the law.').group())
#
# newline_regex = re.compile('.*', re.DOTALL)
# print(newline_regex.search(
#     'Serve the public trust. \nProtect the innocent. \nUphold the law.').group())
#
# robocop = re.compile(r'robocop', re.I)
# print(robocop.search('RoboCop is part man, part machine, all cop.').group())
#
# print(robocop.search('ROBOCOP protects the innocent.').group())
#
# print(robocop.search(
#     'Al, why does your programming book talk about robocop so much?').group())

names_regex = re.compile(r'Agent \w+')
print(names_regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

agent_names_regex = re.compile(r'Agent (\w)\w*')
print(agent_names_regex.sub(r'\1****',
                            'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))
