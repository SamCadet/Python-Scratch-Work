#! python3
'''
resizeAndAddLogo2.py - Resizes all images in current working directory
to fit in a 300x300 square and adds catlogo.png to the lower-right corner.
Added more features for practice project

# p. 460

Answer - https://github.com/kudeh/automate-the-boring-stuff-projects/blob/master/resize-add-logo/resizeAndAddLogo.py
'''

import os
from PIL import Image

# Step 1: Open the Logo Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)
# Step 2: Loop Over All Files and Open Images
for filename in os.listdir('.'):
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')
            or filename.lower().endswith('.gif') or filename.lower().endswith('.bmp')) \
            or filename == LOGO_FILENAME:
        continue  # skip non-image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size
    if not filename >= SQUARE_FIT_SIZE * 2:
        pass

# Step 3: Check if image needs to be resized.
if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
    # Calculate the new width and height to resize to.
    if width > height:
        height = int((SQUARE_FIT_SIZE / width) * height)
        width = SQUARE_FIT_SIZE
    else:
        width = int((SQUARE_FIT_SIZE / height) * width)
        height = SQUARE_FIT_SIZE

    # Resize the image.
    print('Resizing %s...' % (filename))
    im = im.resize((width, height))


# Step 4: Add the logo if it fits.
    imWidth, imHeight = im.size
    if imWidth < logoWidth * 2 and imHeight < logoHeight * 2:
        print('That logo is too large, whoadie. Skipping...')
    else:
        print('Adding logo to %s...' % (filename))
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

# Save changes.
im.save(os.path.join('withLogo', filename))
