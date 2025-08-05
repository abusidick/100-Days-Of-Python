#checks height requirements for a roller coaster ride
print("Welcome to the Roller Coaster Ride!")
height = int(input("Please enter your height in cm: "))

#checks if the height is greater than or equal to 120cm
if height >= 120:
    print("You are tall enough to ride the roller coast")
    #checks the age to give price
    age = int(input("How old are you?: "))
    if age <= 12:
        print("Please pay $4.00")
    elif age <= 18:
        print("Please pay $8.00")
    else:
        print("Please pay $15.00")
else:
    print("Sorry, you cannot ride the roller coaster")


