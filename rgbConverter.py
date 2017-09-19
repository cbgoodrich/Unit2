#Charlie Goodrich
#09/18/17
#rgbConverter.py - converts rgb to hex

rgb1 = int(input("Enter a number between 0 and 255: "))

dig1 = rgb1%16
dig2 = (rgb1//16)%16

if dig1 == 10: # testing to see if dig1 < 10 to print out letters
    dig1 = "A"
    if dig2 == 10:
        dig2 = "A"
        print(dig1, dig2)
    elif dig2 == 11:
        dig2 = "B"
        print(dig1, dig2)
    elif dig2 == 12:
        dig2 = "C"
        print(dig1, dig2)
    elif dig2 == 13:
        dig2 = "D"
        print(dig1, dig2)
    elif dig2 == 14:
        dig2 = "E"
        print(dig1, dig2)
    elif dig2 == 15:
        dig2 = "F"
        print(dig1, dig2)
    else:
        dig2 = dig2
    print(dig1, dig2)

elif dig1 == 11:
    dig1 = "B"
    if dig2 == 10:
        dig2 = "A"
        print(dig1, dig2)
    elif dig2 == 11:
        dig2 = "B"
        print(dig1, dig2)
    elif dig2 == 12:
        dig2 = "C"
        print(dig1, dig2)
    elif dig2 == 13:
        dig2 = "D"
        print(dig1, dig2)
    elif dig2 == 14:
        dig2 = "E"
        print(dig1, dig2)
    elif dig2 == 15:
        dig2 = "F"
        print(dig1, dig2)
    else:
        dig2 = dig2
    print(dig1, dig2)
    
elif dig1 == 12:
    dig1 = "C"
    if dig2 == 10:
        dig2 = "A"
        print(dig1, dig2)
    elif dig2 == 11:
        dig2 = "B"
        print(dig1, dig2)
    elif dig2 == 12:
        dig2 = "C"
        print(dig1, dig2)
    elif dig2 == 13:
        dig2 = "D"
        print(dig1, dig2)
    elif dig2 == 14:
        dig2 = "E"
        print(dig1, dig2)
    elif dig2 == 15:
        dig2 = "F"
        print(dig1, dig2)
    else:
        dig2 = dig2
    print(dig1, dig2)

elif dig1 == 13:
    dig1 = "D"
    if dig2 == 10:
        dig2 = "A"
        print(dig1, dig2)
    elif dig2 == 11:
        dig2 = "B"
        print(dig1, dig2)
    elif dig2 == 12:
        dig2 = "C"
        print(dig1, dig2)
    elif dig2 == 13:
        dig2 = "D"
        print(dig1, dig2)
    elif dig2 == 14:
        dig2 = "E"
        print(dig1, dig2)
    elif dig2 == 15:
        dig2 = "F"
        print(dig1, dig2)
    else:
        dig2 = dig2
    print(dig1, dig2)

elif dig1 == 14:
    dig1 = "E"
    if dig2 == 10:
        dig2 = "A"
        print(dig1, dig2)
    elif dig2 == 11:
        dig2 = "B"
        print(dig1, dig2)
    elif dig2 == 12:
        dig2 = "C"
        print(dig1, dig2)
    elif dig2 == 13:
        dig2 = "D"
        print(dig1, dig2)
    elif dig2 == 14:
        dig2 = "E"
        print(dig1, dig2)
    elif dig2 == 15:
        dig2 = "F"
        print(dig1, dig2)
    else:
        dig2 = dig2
    print(dig1, dig2)
    
elif dig1 == 15:
    dig1 = "F"
    if dig2 == 10:
        dig2 = "A"
        print(dig1, dig2)
    elif dig2 == 11:
        dig2 = "B"
        print(dig1, dig2)
    elif dig2 == 12:
        dig2 = "C"
        print(dig1, dig2)
    elif dig2 == 13:
        dig2 = "D"
        print(dig1, dig2)
    elif dig2 == 14:
        dig2 = "E"
        print(dig1, dig2)
    elif dig2 == 15:
        dig2 = "F"
        print(dig1, dig2)
    else:
        dig2 = dig2
    print(dig1, dig2)

else:
    print(dig1, dig2)