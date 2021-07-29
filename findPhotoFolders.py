#! python3

'''
findPhotoFolders.py - Find certain folders on hard drive

p. 460

Answer - https://github.com/IFinners/automate-the-boring-stuff-projects/blob/master/Chapter%2017/photo_folder_finder.py
'''
import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('C:\\Users\\Sam\\Pictures'):
    photos = 0
    notPhotos = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')):
            notPhotos += 1
            continue

        try:
            im = Image.open(os.path.join(foldername, filename))
        except OSError:
            continue  # skip to next filename

        width, height = im.size

        # Check if width & height are larger than 500.

        if width > 500 and height > 500:  # Image is large enough to be considered a photo.
            photos += 1
        else:
            # Image is too small to be a photo.
            notPhotos += 1

# If more than half of files were photos,
# print the absolute path of the folder.

if photos > notPhotos:
    print(os.path.abspath(foldername))
