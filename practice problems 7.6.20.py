# practice problems from YouTube - https://youtu.be/lx7oqZ7Nl3k

# def sleep_in(weekday, vacation):
#     if weekday == False or vacation == True:
#         return True
#     else:
#         return False


# def sleep_in(weekday, vacation):
#     if not weekday or vacation:
#         return True
#     else:
#         return False


# My answer
# def string_times(x, y):
#     while True:
#         return x * y
#
#
# print(string_times('Hi', 1))

# Answer from Video


# def string_times(str, n):
#     return str * n
#
#
# print(string_times('Hi', 3))


# My answer
# name = 'Bob'
#
#
# def hello_name(name):
#     print('Hello ' + name + '!')
#
#
# hello_name(name)

# Answer from video

# def hello_name(name):
#     return('Hello ' + name + '!')

# Answer from video
# a = [1, 2, 6]

# print(a)
#
#
# def first_last6(a):
#     if a[0] == 6 or a[- 1] == 6:
#         return True
#     else:
#         return False
#
#
# print(first_last6(a))

# Answer from video

#a = 'Yo Bro'
#
#
# def double_char(str):
#    to_return = '' # makes an empty string that'll be replaced by c
#    for c in str: # basically saying use c as a variable for all of the characters in the string
#        to_return += c * 2 # takes empty string and multiplies each character in a by two
#    return to_return # returns new value of c * 2
#
#
# print(double_char(a))

# answer from video

a = [2, 1, 2, 3, 4]


def count_evens(a):
    count = 0  # initialize count as 0
    # makes a for loop that goes through each number (x) in the list (a)
    for x in a:
        if x % 2 == 0:  # the % operator is used to see if the divisor 2 leaves no remainder. This lets us know if the number's even.
            count += 1 # takes the even number and goes up the list to the next even number from the list in the for loop
    return count # returns the amount of even numbers from the list


print(count_evens(a))
