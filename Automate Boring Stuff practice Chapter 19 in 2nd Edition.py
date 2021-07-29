from PIL import ImageColor  # p. 442
from PIL import Image  # p. 443
from PIL import ImageDraw  # p. 456
from PIL import ImageFont  # p. 458
import os  # p. 458

# p. 441-442 Colors and RGBA Values

'''
Pillow offers the ImageColor.getcolor() function so you don’t have to memorize
RGBA values for the colors you want to use. This function takes a color name
string as its first argument, and the string 'RGBA' as its second argument,
and it returns an RGBA tuple.

print(ImageColor.getcolor('red', 'RGBA'))
print(ImageColor.getcolor('RED', 'RGBA'))
print(ImageColor.getcolor('Black', 'RGBA'))
print(ImageColor.getcolor('chocolate', 'RGBA'))
print(ImageColor.getcolor('CornflowerBlue', 'RGBA'))
print(ImageColor.getcolor('chartreuse', 'RGBA'))

# p. 443-44 Manipulating Images with Pillow


To load the image, import the Image module from Pillow and call Image.open(),
passing it the image’s filename. You can then store the loaded image in a
variable like CatIm.

catIm = Image.open('zophie.png')

print(catIm)



# p. 444-445 Working with the Image Data Type

An Image object has several useful attributes that give you basic information
about the image file it was loaded from: its width and height, the filename,
and the graphics format (such as JPEG, GIF, or PNG).


catIm = Image.open('zophie.png')
print(catIm.size)

width, height = catIm.size
print(width)
print(height)
print(catIm.filename)
print(catIm.format)
print(catIm.format_description)
catIm.save('zophie.jpg')

im = Image.new('RGBA', (100, 200), 'purple')
im.save('purpleImage.png')
im2 = Image.new('RGBA', (20, 20))
im2.save('transparentImage.png')

# p. 445-446 Cropping Images



catIm = Image.open('zophie.png')
croppedIm = catIm.crop((335, 345, 565, 560))
croppedIm.save('cropped.png')

# p. 446-447 Copying and Pasting Images onto Other Images

The copy() method will return a new Image object with the same image as
the Image object it was called on.



catIm = Image.open('zophie.png')
catCopyIm = catIm.copy()

The paste() method is called on an Image object and pastes another image
on top of it.



catIm = Image.open('zophie.png')
catCopyIm = catIm.copy()

faceIm = catIm.crop((335, 345, 565, 560))
catCopyIm.paste(faceIm, (0, 0))
catCopyIm.paste(faceIm, (400, 500))
catCopyIm.save('pasted.png')


Note that the paste() method modifies its Image object in place
it does not return an Image object with the pasted image. If you want to
call paste() but also keep an untouched version of the original image around,
you’ll need to first copy the image and then call paste() on that copy.
print(faceIm.size)


catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.copy()
for left in range(0, catImWidth, faceImWidth):
    for top in range(0, catImHeight, faceImHeight):
        print(left, top)
        catCopyTwo.paste(faceIm, (left, top))

catCopyTwo.save('tiled.png')

# p. 448 Resizing an Image

The resize() method is called on an Image object and returns a new Image object of the specified width and
height. It accepts a two-integer tuple argument, representing the new width and height of the returned
image.


catIm = Image.open('zophie.png')
width, height = catIm.size
quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
quartersizedIm.save('quartersized.png')
svelteIm = catIm.resize((width, height + 300))
svelteIm.save('svelte.png')

# p. 449-450 Rotating and Flipping Images

Images can be rotated with the rotate() method, which returns a new Image object
of the rotated image and leaves the original Image object unchanged. The
argument to rotate() is a single integer or float representing the number of
degrees to rotate the image counterclockwise.


catIm = Image.open('zophie.png')

catIm.rotate(90).save('rotated90.png')
catIm.rotate(180).save('rotated180.png')
catIm.rotate(270).save('rotated270.png')

Notice that the width and height of the image change when the image is
rotated 90 or 270 degrees. If you rotate an image by some other amount,
the original dimensions of the image are maintained.

catIm.rotate(6).save('rotated6.png')
catIm.rotate(6, expand=True).save('rotated6_expanded.png')


You can also get a “mirror flip” of an image with the transpose() method.
You must pass either Image.FLIP_LEFT_RIGHT or Image.FLIP_TOP_BOTTOM to the
transpose() method.


catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')



# p. 451 Changing Individual Pixels

The color of an individual pixel can be retrieved or set with the getpixel()
and putpixel() methods. These methods both take a tuple representing the
x - and y - coordinates of the pixel. The putpixel() method also takes an
additional tuple argument for the color of the pixel. This color argument is
a four - integer RGBA tuple or a three - integer RGB tuple.


im = Image.new('RGBA', (100, 100)
               )  # we make a new image that is a 100×100 transparent square.
# Calling getpixel() on some coordinates in this image returns (0, 0, 0, 0) because the image is transparent
print(im.getpixel((0, 0)))

for x in range(100):  # To color pixels in this image, we can use nested for loops to go through all the pixels in the top half of the image
    for y in range(50):
        # and color each pixel using putpixel(). Here we pass putpixel() the RGB tuple (210, 210, 210), a light gray.
        im.putpixel((x, y), (210, 210, 210))

for x in range(100):  # Loop through the pixels in the bottom half of the image
    for y in range(50, 100):
        im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))  # pass putpixel() the return value of ImageColor.getcolor() and you should now have an image that is light gray in its top half and dark gray in the bottom half

print(im.getpixel((0, 0)))
print(im.getpixel((0, 50)))
im.save('putPixel.png')


# p. 455-456 Drawing on Images

If you need to draw lines, rectangles, circles, or other simple shapes on an image, use Pillow’s ImageDraw
module.

im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)

# p. 456 Drawing Shapes


Points
The point(xy, fill) method draws individual pixels. The xy argument represents a list of the points you want
to draw. The list can be a list of x- and y-coordinate tuples, such as [(x, y), (x, y), ...], or a list of x- and ycoordinates
without tuples, such as [x1, y1, x2, y2, ...]. The fill argument is the color of the points and is
either an RGBA tuple or a string of a color name, such as 'red'. The fill argument is optional.

Lines
The line(xy, fill, width) method draws a line or series of lines. xy is either a list of tuples, such as [(x, y), (x,
y), ...], or a list of integers, such as [x1, y1, x2, y2, ...]. Each point is one of the connecting points on the
lines you’re drawing. The optional fill argument is the color of the lines, as an RGBA tuple or color name.
The optional width argument is the width of the lines and defaults to 1 if left unspecified.

Rectangles
The rectangle(xy, fill, outline) method draws a rectangle. The xy argument is a box tuple of the form (left,
top, right, bottom). The left and top values specify the x- and y-coordinates of the upper-left corner of the
rectangle, while right and bottom specify the lower-right corner. The optional fill argument is the color that
will fill the inside of the rectangle. The optional outline argument is the color of the rectangle’s outline.

Ellipses
The ellipse(xy, fill, outline) method draws an ellipse. If the width and height of the ellipse are identical, this
method will draw a circle. The xy argument is a box tuple (left, top, right, bottom) that represents a box that
precisely contains the ellipse. The optional fill argument is the color of the inside of the ellipse, and the
optional outline argument is the color of the ellipse’s outline.

Polygons
The polygon(xy, fill, outline) method draws an arbitrary polygon. The xy argument is a list of tuples, such as
[(x, y), (x, y), ...], or integers, such as [x1, y1, x2, y2, ...], representing the connecting points of the
polygon’s sides. The last pair of coordinates will be automatically connected to the first pair. The optional
fill argument is the color of the inside of the polygon, and the optional outline argument is the color of the
polygon’s outline.



im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)

draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
draw.rectangle((20, 30, 60, 60), fill='blue')
draw.ellipse((120, 30, 160, 60), fill='red')
draw.polygon(((57, 87), (79, 62), (94, 85),
              (120, 90), (103, 113)), fill='brown')
for i in range(100, 200, 10):
    draw.line([(i, 0), (200, i - 100)], fill='green')

im.save('drawing.png')


# p. 457- Drawing Text

im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)
draw.text((20, 150), 'Hello', fill='purple')
fontsFolder = 'C:\\Windows\\Fonts'
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 20)
draw.text((100, 150), '#MyGuy', fill='gray', font=arialFont)
im.save('text.png')
'''
