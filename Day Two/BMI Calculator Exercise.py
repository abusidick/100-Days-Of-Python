# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weight = int(weight)
height = float(height)

Body_Mass_Index = weight/height**2
Body_Mass_Index = int(Body_Mass_Index)

Body_Mass_Index = str(Body_Mass_Index)

print("Your BMI is :" + Body_Mass_Index)