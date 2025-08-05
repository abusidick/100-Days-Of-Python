# Dont change the code below 
print("Welcome to Abubakar Pizza deliveries!")
size = input("What size of pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# Dont change the code above👆

#Write your code below 👇

bill = 0
if size == "S":
    #calculating price for small pizza
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
    print(f"Your final bill is: ${bill}") 
elif size == "M":
    #calculating price for medium pizza
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f"Your final bill is: ${bill}") 
else:
    #calculating price for small pizza
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f"Your final bill is: ${bill}") 

