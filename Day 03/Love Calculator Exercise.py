# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#changing the case
name1 = name1.lower()
name2 = name2.lower()

#concatenate the names
couple_name = name1 + name2

#calculate love meter
count_true = couple_name.count("t") + couple_name.count("r") + couple_name.count("u") + couple_name.count("e")
count_love = couple_name.count("l") + couple_name.count("o") + couple_name.count("v") + couple_name.count("e")

love_meter = int(str(count_true) + str(count_love))

if love_meter < 10 or love_meter > 90:
    print(f"Your score is {love_meter}, you go together like coke and mentos.")

elif love_meter >= 40 and love_meter <= 50:
    print(f"Your score is {love_meter}, you are alright together.")

else:
    print(f"Your score is {love_meter}.")

