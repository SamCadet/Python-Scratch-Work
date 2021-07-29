#! python3
'''
customSeatingCards.py - stupid invitations for these weak ass MFs

p. 461

Answer - https://github.com/IFinners/automate-the-boring-stuff-projects/blob/master/Chapter%2017/custom-cards.py

'''

from PIL import Image
from PIL import ImageDraw
import os
from PIL import ImageFont
'''

# TODO: Create invitation template


def createInvitations(name):
    card = Image.new('RGBA', (360, 288), 'white')
    flower = Image.open('flower.png')
    card.paste(flower, (10, 40), flower)
    cut_guide = Image.new('RGBA', (364, 292), 'black')
    cut_guide.paste(card, (2, 2))

    draw_obj = ImageDraw.Draw(cut_guide)
    fonts_folder = 'C:\\Windows\\Fonts'
    custom_font = ImageFont.truetype(
        os.path.join(fonts_folder, 'arial.ttf'), 72)
    draw_obj.text((120, 100), name, fill='blue', font=custom_font)

    cut_guide.save('{}-invite.png'.format(name))

# Locate textfile and parse through it


with open('guests.txt') as f:
    guests = f.readlines()

# Parse through guest list from text file

for guest in guests:
    createInvitations(guest)

print('All invitations created yoooooo!!!!')

'''

# https://github.com/kudeh/automate-the-boring-stuff-projects/blob/master/custom-seating-cards/custom_cards.py


def make_cards(guestList):
    """Makes custom cards for each guest
    Args:
        guestList (str): Path to file containing guest list
    Returns:
        None
    """
    # make folder to store resulting images
    os.makedirs('imageCards', exist_ok=True)

    # load flower image
    flowerImg = Image.open('flower.png')

    # read each guest from file
    with open(guestList) as file:
        for line in file:
            guest = line[:-1]

            # create image
            card = Image.new('RGBA', (288, 360), 'white')
            # add flower image
            card.paste(flowerImg, (0, 0))

            # create border around image
            border = Image.new('RGBA', (291, 363), 'black')
            border.paste(card, (3, 3))

            # draw guest name
            draw_obj = ImageDraw.Draw(border)
            fonts_folder = 'C:\\Windows\\Fonts'
            card_font = ImageFont.truetype(
                os.path.join(fonts_folder, 'arial.ttf'), 72)
            draw_obj.text((120, 100), guest, fill='blue', font=card_font)

            # save resulting image
            imageName = '{}_card.png'.format(guest)
            border.save(os.path.join('imageCards', imageName))


if __name__ == "__main__":
    make_cards('guests.txt')
