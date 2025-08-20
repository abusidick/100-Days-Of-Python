# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
Total_Height = 0
Total_Student = 0
for height in student_heights:
  Total_Height += height
  Total_Student += 1
 
average_height = Total_Height/Total_Student
average_height = round(average_height)

print(f"The average height is : {average_height}")





