# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#Splits the two digits
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

#checks the data type of each digits
print(type(first_digit))
print(type(second_digit))  

#changes the type to integer and calculate the total
total_num = int(first_digit) + int(second_digit)
print(type(total_num))

#changes the type of total_num
total_num = str(total_num)
print(type(total_num))
print("The sum of the two digits is " + total_num)
