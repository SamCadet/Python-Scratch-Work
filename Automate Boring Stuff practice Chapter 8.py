import os

# print(os.path.join('usr', 'bin', 'plaintains'))
#
# print(os.getcwd())
# os.chdir('C:\\Windows\\System32')
# print(os.getcwd())
# os.chdir('C:\\Users\\Sam\\Documents\\Python Scratch Work')
# print(os.getcwd())
#
# print(os.path.abspath('.'))
# print(os.path.isabs(os.path.abspath('.')))
# print(os.path.abspath('.\\password'))
#
# print(os.path.relpath('C:\\Windows', 'C:\\'))
# print(os.path.relpath('C:\\Windows', 'C:\\Users\\Sam'))
# print(os.getcwd())
# path = 'C:\\Windows\\System32\\calc.exe'
# print(os.path.basename(path))
# print(os.path.dirname(path))
# calcfilepath = 'C:\\Windows\\System32\\calc.exe'
# print(os.path.split(calcfilepath))
# print(calcfilepath.split(os.path.sep))
# print(os.listdir('C:\\Users'))
# print(os.path.getsize('C:\\Program Files'))
#
# total_size = 0
#
# for filename in os.listdir('C:\\Program Files'):
#     total_size = total_size + \
#         os.path.getsize(os.path.join('C:\\Program Files', filename))
#
# print(os.path.exists('C:\\Windows'))
#
# print(os.path.exists('C:\\some_made_up_folder'))
#
# print(os.path.isdir('C:\\Windows\\System32'))
#
# print(os.path.isfile('C:\\Windows\\System32'))
#
# print(os.path.isdir('C:\\Windows\\System32\\calc.exe'))
#
# print(os.path.isfile('C:\\Windows\\System32\\calc.exe'))
#
# print(os.path.exists('D:\\'))

# ayo_file = open('C:\\Users\\Sam\\Ayo.txt')
# print(ayo_file)
# ayo_content = ayo_file.read()
# print(ayo_content)
#
# sonnet_file = open('C:\\Users\\Sam\\sonnet29.txt')
#
# print(sonnet_file.readlines())

# greeting_file = open('greeting.txt', 'w')
# print(greeting_file.write('YERRRR!!!\n'))
# greeting_file.close()
# greeting_file = open('greeting.txt', 'a')
# print(greeting_file.write('What\'s going on, #myguy?'))
# greeting_file.close()
# greeting_file = open('greeting.txt')
# content = greeting_file.read()
# greeting_file.close()
# print(content)

# import shelve
#
# shelf_file = shelve.open('mydata')
# dogs = ['Whoadie', 'Chopper', 'Blade']
# shelf_file['dogs'] = dogs
# shelf_file.close()
#
# print(os.getcwd())
#
# shelf_file = shelve.open('mydata')
# print(type(shelf_file))
# print(shelf_file['dogs'])
# shelf_file.close()
#
# shelf_file = shelve.open('mydata')
# print(list(shelf_file.keys()))
# print(list(shelf_file.values()))
# shelf_file.close()

import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'},
        {'name': 'Pooka', 'desc': 'fluffy'}]
print(pprint.pformat(cats))
file_obj = open('mycats.py', 'w')
print(file_obj.write('cats = ' + pprint.pformat(cats) + '\n'))

file_obj.close()

import mycats

print(mycats.cats)

print(mycats.cats[0])

print(mycats.cats[0]['name'])
