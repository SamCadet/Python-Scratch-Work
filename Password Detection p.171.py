import re

uppercheck = re.compile(r'[A-Z]')
lowercheck = re.compile(r'[a-z]')
digitscheck = re.compile(r'\d')


def good_password():
    while True:
        password = input('''Please enter a password that\'s at least 8 charcters long with at least

one capital letter, one lower case letter and one digit.''')

        if len(password) < 8:
            print('Your password needs to be at least 8 characters long.')
            continue
        elif not uppercheck.search(password):
            print('Your password needs at least one upper case letter.')
            continue
        elif not lowercheck.search(password):
            print('Your password needs at least one lower case letter.')
            continue
        elif not digitscheck.search(password):
            print('Your password needs at least one digit.')
            continue
        else:
            print('Your password is set, thanks!')
            break

    return True


if __name__ == '__main__':
    print(good_password())


# https://old.reddit.com/r/inventwithpython/comments/5nenix/automate_the_boring_stuff_chapter_7_strong/
