import shutil
import zipfile
import os

# print(os.chdir('C:\\'))

# print(shutil.copy('C:\\Users\\Sam\\Documents\\quiz.txt',
#                   'C:\\Users\\Sam\\Documents\\test.txt'))
# print(shutil.copy('C:\\Users\\Sam\\Documents\\riceandbeans.txt',
#                   'C:\\Users\\Sam\\Documents\\Delicious\\riceandbeans2.txt'))
#
# print(shutil.copytree('C:\\Users\\Sam\\Documents\\Plantains',
#                       'C:\\Users\\Sam\\Documents\\Plantains_Backup'))

# print(shutil.move('C:\\Users\\Sam\\Documents\\Plantains',
#                  'C:\\Users\\Sam\\Documents\\Delicious\\Plantains'))


# print(shutil.move('C:\\Users\\Sam\\Documents\\Delicious\\Plantains',
#                   'C:\\Users\\Sam\\Documents\\Delicious\\Sweet_Plantains'))

# print(shutil.move('C:\\Users\\Sam\\Documents\\Delicious\\Sweet_Plantains',
#                   'C:\\Users\\Sam\\Documents\\Tasty\\Sweet_Plantains'))

# shutil.move('C:\\Users\\Sam\\Documents\\Tasty\\Sweet_Plantains', 'c:\\does_not_exist\\eggs\\ham')

# import send2trash
# bacon_file = open('C:\\Users\\Sam\\Documents\\Tasty\\Marinad.txt',
#                   'a')  # creates the file
# bacon_file.write('Marinad is jammin\'.')
# bacon_file.close()
# send2trash.send2trash('C:\\Users\\Sam\\Documents\\Tasty\\Marinad.txt')

# for folder_name, subfolders, filenames in os.walk('C:\\Users\\Sam\\Documents\\Tasty'):
#     print('The current folder is ' + folder_name)
#
#     for subfolder in subfolders:
#         print('SUBFOLDER OF ' + folder_name + ': ' + subfolder)
#
#     for filename in filenames:
#         print('FILE INSIDE ' + folder_name + ': ' + filename)
#
#     print('')

# example_zip = zipfile.ZipFile('example.zip')
#
# print(example_zip.namelist())
#
#
# spam_info = example_zip.getinfo('spam.txt')
# print(spam_info.file_size)
#
# print(spam_info.compress_size)
#
# print('Compressed file size is %sx smaller' %
#       (round(spam_info.file_size / spam_info.compress_size, 2)))
#
# example_zip.close()

example_zip = zipfile.ZipFile('example.zip')
# example_zip.extractall()
# example_zip()

# print(example_zip.extract('spam.txt'))
#
# print(example_zip.extract('spam.txt', 'C:\\Users\\Sam\\Documents\\Dat FOLDA'))
#
# print(example_zip.close())

new_zip = zipfile.ZipFile('new.zip', 'w')

new_zip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()
