#This gets user info to create a personal card

print('Hello Welcome To Your Personal Card Registeration.\n' \
'Input Your personal details below')

#The code below takes users info
first_name = input('Enter your first name: \n')
last_name = input('Enter your last name: \n')
age = input('Enter your age: \n')
location = input('Enter your location: \n')
hobby = input('What is your hobby: \n')

#The users personal card is generated and displayed
print('Personal Info Card')
print("...............................")
print("Name: " + first_name + " " + last_name)
print('Age: ' + age)
print('Location: ' + location)
print("Hobby: " + hobby)




