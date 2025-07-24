#The code below takes input form the user 
print("Welcome To The Tip Calculator ")
total_bill = input("What Was the Total bill? $")
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_people = input("How many people want to split the bill? ")

#converts input
total_bill = float(total_bill)
percentage_tip = int(percentage_tip) / 100
num_people = int(num_people)

#Calculate the tip
tip_amount = percentage_tip * total_bill

#calculate the total bill
total_bill = tip_amount + total_bill

#calculate the amount each has to pay
amount_each = total_bill / num_people

#round the amount to two decimal places
amount_each = round(amount_each,2)

#printing the amount each person has to pay
print(f"Each person should pay: ${amount_each}")