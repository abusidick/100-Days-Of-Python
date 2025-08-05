# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

Body_Mass_Index = weight/height**2
Body_Mass_Index = round(Body_Mass_Index,2)

print(f"Your BMI is : {Body_Mass_Index}")

if Body_Mass_Index < 18.5:
    print("You are underweight")
elif Body_Mass_Index < 25:
    print("You have normal weight")
elif Body_Mass_Index < 30:
    print("You are overweight")
elif Body_Mass_Index < 35:
    print("You are obese")
else:
    print("You are clinically obese")



