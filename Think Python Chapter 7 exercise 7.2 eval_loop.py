#! python 3

'''
Write a function called eval_loop that iteratively prompts the user, takes the resulting
input and evaluates it using eval, and prints the result.
It should continue until the user enters 'done', and then return the value of the last expression it
evaluated.

Answer - https://github.com/MadCzarls/Think-Python-2e---my-solutions/blob/master/ex7/ex7.2.py

'''

import math
import pyinputplus as pyip

# TODO: Write a function called eval_loop


def eval_loop():
    while True:
        response = pyip.inputStr('Type a response #onhere: ')
        print(response)
        # TODO: Make it run until the user enters done to return the value of the last expression
        if response == 'done':
            print('OK, you\'re ' + response)
            break

    return response


eval_loop()
