#Charlie Goodrich
#09/18/17
#rgbConverter.py - converts rgb to hex

rgb1 = int(input("Enter a number between 0 and 255: "))

dig1 = rgb1&16
dig2 = (rgb1//16)%16

if dig1 == 10:
    dig1 = "A"
