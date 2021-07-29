# p. 221-224

import pyinputplus as pyip
import random
import time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    # Pick two random numbers:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    try:
        # Right answers are handles by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                      blockRegexes=[('.*', 'WRONG!')],
                      timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Ya ran out of time, #myguy!')
    except pyip.RetryLimitException:
        print('Out of lives, dork!')
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Check...you\'re right!')
        correctAnswers += 1

    time.sleep(1)   # Brief pause to let user see the result.

print('Score: %s / %s' % (correctAnswers, numberOfQuestions))
