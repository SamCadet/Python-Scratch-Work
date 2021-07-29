#! python3

# deleting_unneeded_files.py - finds and removes big files
# on your computer

import os

folder = input("Enter the absolute path of the folder you'd like to search: ")

threshold = input("Enter the maximum file size that you'd"
                  " like to ignore (in megabytes): ")

for folders, subfolders, filenames in os.walk(folder):

    for filename in filenames:

        size = os.path.getsize(os.path.join(folders, filename))

        if size > int(threshold) * 10 ** 6:   # MB to byte conversion
            print(filename, '| Size = ', size // 10 ** 6, 'MB' '| Path =',
                  os.path.join(folders, filename))

# https://github.com/IFinners/automate-the-boring-stuff-projects/blob/master/Chapter%2009/deleting_unneeded.py
