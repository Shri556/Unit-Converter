##Converts various units between one another. The user enters the type of unit being entered, 
#the type of unit they want to convert to and then the value. 
#The program will then make the conversion.
import math

def ask():
    while True:
        intp = input("What to find?\n(Volume:1,\n Mass:2,\n density:3)")
        if intp in ('1','2','3'):
            intp = int(intp)
            break
        else:
            print("Please enter a valid input!!")

    return intp

def quest():
    a = ask()

    if a == 1:
        question = 'Volume'
    if a == 3:
        question = 'density'

    if a == 2:
        question = 'Mass'
    return question

def calcu():
    a = quest()

    if a == 'Volume':
        print("Using the Formula:\n Volume = Mass/density")
        while True:
            Mass = input("Mass in Kg: ")
            if Mass.isnumeric():
                Mass = int(Mass)
                break
            else:
                print("Enter Numeric value only")

        while True:
            density = input("DENSITY: ")
            if density.isnumeric():
                density = int(density)
                break
            else:
                print("Enter Numeric value only")

        print(f"VOLUME: {Mass/density}")


    if a == 'Mass':
        print("Using the Formula:\n Mass = Volume x density")
        while True:
            Volume = input("Volume: ")
            if Volume.isnumeric():
                Volume = int(Volume)
                break
            else:
                print("Enter Numeric value only")

        while True:
            density = input("DENSITY: ")
            if density.isnumeric():
                density = int(density)
                break
            else:
                print("Enter Numeric value only")

        print(f"Mass: {Volume * density}")

    if a == 'density':
        
        print("Using the Formula:\n density = Mass/Volume")
        while True:
            Mass = input("Mass in Kg: ")
            if Mass.isnumeric():
                Mass = int(Mass)
                break
            else:
                print("Enter Numeric value only")

        while True:
            Volume = input("Volume: ")
            if Volume.isnumeric():
                Volume = int(Volume)
                break
            else:
                print("Enter Numeric value only")


        print(f"DENSITY: {Mass * Volume}")

if __name__ == '__main__':
    calcu()