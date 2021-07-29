#! python3

# password.py - An insecure locker password locker program.

Passwords = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys.pyperclip
if len(sys.argv) < 2:
    print('Usage: python password.py [account] - cop account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in Passwords:
    pyperclip.copy(Passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
