# Task 7
#Finding the multiples of a number using loop

number = int(input("Enter the number for the multiplication table: "))

print("Multiplication Table for",number)
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")



# Task 8
#Write a program to print the inputted value as it is and break the loop if the value is 'done'.

while True:
    user_value = input(":")
    if user_value == 'done':
        print('Done')
        break
    else:
        print(user_value)


# Task 9
#Write a program that prints the numbers from 1 to 10. But for multiples of three print "Fizz" instead of the number and for the multiple of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"


for i in range(1,11):
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0 and i%5==0:
        print("FizzBuzz")
    else:
        print(i)



# Task 10
#Write a program to print the following pattern:

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1


for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

