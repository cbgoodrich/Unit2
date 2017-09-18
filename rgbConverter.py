#Charlie Goodrich
#09/18/17
#rgbConverter.py - converts rgb to hex

rgb1 = int(input("Enter a number between 0 and 255: "))
rgb2 = int(input("Enter a number between 0 and 255: "))
rgb2 = int(input("Enter a number between 0 and 255: "))

dig1 = rgb1&16
dig2 = (rgb1//16)%16
dig3 = rgb2&16
dig4 = (rgb2//16)%16
dig5 = rgb3&16
dig6 = (rgb3//16)%16

if dig1 