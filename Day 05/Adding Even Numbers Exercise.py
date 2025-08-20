#Write your code below this row 👇
total_even = 0
for num in range(2,101,2):
    total_even += num

print(total_even)

#second method
total_even = 0
for num in range(1,101):
    if num % 2 == 0:
        total_even += num

print(total_even)