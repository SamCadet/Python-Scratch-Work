# raise Exception('This is the error message.')
# import traceback
# try:
#     raise Exception('This is the error message.')
# except:
#     errorFile = open('errorInfo.txt', 'w')
#     errorFile.write(traceback.format_exc())
#     errorFile.close()
#     print('The traceback info was written to errorInfo.txt.')

# podBayDoorStatus = 'open'
# assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
# podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
# assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'

# market_2nd = {'ns': 'green', 'ew': 'red'}
# mission_16th = {'ns': 'red', 'ew': 'green'}
#
#
# def switchLights(stoplight):
#     for key in stoplight.keys():
#         if stoplight[key] == 'green':
#             stoplight[key] = 'yellow'
#         elif stoplight[key] == 'yellow':
#             stoplight[key] = 'red'
#         elif stoplight[key] == 'red':
#             stoplight[key] = 'green'
#     assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
#
#
# switchLights(market_2nd)

# import logging

# logging.basicConfig(level=logging.DEBUG,
#                     format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug('Some debugging details')
#
#
# logging.info('The logging module is working.')
#
# logging.warning('An error message is about to be logged.')
#
# logging.error('An error has occurred.')
#
# logging.critical('The program is unable to recover!')


# logging.basicConfig(level=logging.DEBUG,
#                     format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug('Some debugging details')
#
# logging.critical('Critical error! Critical error!')
# logging.disable(logging.CRITICAL)
# logging.critical('Critical error! Critical error!')
# logging.error('Error! Error!')

# spam = 9
# assert spam >= 10, 'The spam variable is less than 10'

# eggs = 'hello'
# bacon = 'HELLO'

# assert eggs == bacon, 'These variables have the same values.'

# assert eggs.lower() != bacon.lower(), 'The eggs and bacon variables are the same!'

# assert eggs.upper() != bacon.upper(), 'The eggs and bacon variables are the same!'

# saying = 'Nah'

# assert saying == 'Yo', 'That ain\'t it.'

assert False, 'This assertion always triggers.'
