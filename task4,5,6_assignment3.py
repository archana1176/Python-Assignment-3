# Task 4
#Write a Python program to receive 3 numbers from the user and print the greatest among them

num1=input("enter 1st number")
num2=input("enter 2nd number")
num3=input("enter 3rd number")

if (num1 >= num2) and (num1 >= num3):
    print("greatest number is : ",num1)
elif (num2 >= num1) and (num2 >= num3):
    print("greatest number is : ",num2)
else:
    print("greatest number is : ",num3)



# Task 5
#Find the factorial of a given number using loops(note the number is received from the user)

numb=int(input("Enter a Number: "))
fact=1
for i in range(1, numb + 1):
    fact= fact*i

print("the factorial of",numb,"is :",fact)

# Task 6
#Reverse a number using while loop

number = int(input("Enter a number to reverse: "))
reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10

print(f"The reversed number is: {reversed_number}")



