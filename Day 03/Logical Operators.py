print("Welcome to the Roller Coaster Ride!")
height = int(input("Please enter your height in cm: "))
bill = 0

#checks if the height is greater than or equal to 120cm
if height >= 120:
    print("You are tall enough to ride the roller coast")
    #checks the age to give price
    age = int(input("How old are you?: "))
    if age <= 12:
        bill = 4.0
        print(f" Child tickets are ${bill}")
    elif age <= 18:
        bill = 8.00
        print(f"Teenagers tickets are ${bill}")
    elif age >= 40 and age <= 55:
        bill = 0
        print("Everything is free")
    else:
        bill = 15
        print(f"Adult tickets are ${bill}")
    wants_photo = input("Do you want photo taken? Y or N. ")
    if wants_photo == "Y":
        #add 3 dollar to the bill
        bill += 3
        print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is ${bill}")
else:
    print("Sorry, you cannot ride the roller coaster")


