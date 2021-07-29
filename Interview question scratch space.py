'''
def digital_root(n):
    # ...
    stringN = str(n)
    result = []

    if len(stringN) == 1:
        return int(stringN)

    for num in stringN:
        result.append(int(num))

    while len(result) > 1:
        answer = str(sum(result))

        if len(answer) == 1:
            return answer

        result.clear()
        for num in answer:
            result.append(int(num))


n = 7
print(digital_root(n))


def add_length(string):
    # your code here
    newString = string.split()
    result = []

    for word in newString:
        word += ' ' + str(len(word))
        result.append(word)

    return result


string = 'bro cuzzo'

print(add_length(string))
'''

'''
def person(people):
    lookup = {'William': [21], 'Kate': [19], 'Bob': [33], 'Rose': [26]}

    for key, value in people.items():
        if key in lookup:
            lookup[key].append(value)
    return lookup


people = {'William': 'M', 'Kate': 'F', 'Bob': 'M', 'Rose': 'F'}

print(person(people))
'''


def solution(n):
    # TODO convert int to roman string
    # Answer source - https://www.programmersought.com/article/11615171632/
    # Visualization - https://tinyurl.com/cfhaw8vj
    roman_numerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                      90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    roman_string = ''
    for key in sorted(roman_numerals.keys(), reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string


n = 493

print(solution(n))
