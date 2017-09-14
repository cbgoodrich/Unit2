#Charlie Goodrich
#09/13/17
#unitConverter.py - converts units

print("1) Kilometers to miles")
print("2) Kilgrams to pounds")
print("3) Liters to gallons")
print("4) Celsius to Fahrenheit")

number = int(input("Choose a number: "))

if number == 1:
    distKM = float(input("Enter distance in kilometers: "))
    distMI = distKM * 0.621371
    print(distKM, "kilometers is", distMI, "miles")

elif number == 2:
    massKG = float(input("Enter a mass in kilograms: "))
    massLBS = massKG * 2.20462
    print(massKG, "kilograms is", massLBS, "pounds")
elif number == 3:
    volumeL = float(input("Enter a volume in liters: "))
    volumeGal = volumeL * 0.264172
    print(volumeL, "liters is", volumeGal, "gallons")
else:
    tempC = float(input("Enter a temperature in Celsius: "))
    tempF = tempC * 1.8 + 32
    print(tempC, "degrees Celsius is", tempF, "degrees Fahrenheit")

    
