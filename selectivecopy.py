#! python3

# selectivecopy.py - Walks through a folder tree,
# searches for files with a certain file extension
# and puts them in a new folder

import shutil
import os


folder = input('Enter the absolute filepath of'
               ' the directory you wish to copy from: ')

extension = input("Enter the extension you'd like to copy: ")

destination = input("Enter destination folder's absolute filepath: ")

for folders, subfolders, filenames in os.walk(folder):

    for filename in filenames:

        if filename.endswith('{}'.format(extension)):
            try:
                shutil.copy(os.path.join(folders, filename), destination)

            except shutil.SameFileError:
                pass


print('Selective copying has finished - all files of', extension, 'type have been copied from', os.path.basename(folder), 'to', os.path.basename(destination))

# https://github.com/IFinners/automate-the-boring-stuff-projects/blob/master/Chapter%2009/selective_copy.py
