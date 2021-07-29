from functools import reduce

p = [1, 2, 3]
q = [1, 2, 3]

# print(p == q)

nums = [2, 3, 4, 6]

evens = list(filter(lambda n: n % 2 == 0, nums))

print(evens)

doubles = list(map(lambda n: n * 2, evens))

answer = reduce(lambda a, b: a + b, doubles)

print(doubles)
print(answer)


def disemvowel(string):

    lettersToRemove = {'A': 'A', 'a': 'a', 'E': 'E', 'e': 'e',
                       'I': 'I', 'i': 'i', 'O': 'O', 'o': 'o', 'U': 'U', 'u': 'u'}

    for letter, key in lettersToRemove.items():
        string = string.replace(key, '')

    return string


string = "This website is for losers LOL!"
print(disemvowel(string))
