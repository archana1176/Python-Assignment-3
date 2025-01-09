#A certain cinema currently sells tickets for a full price of 6 pounds, but always sells tickets for half price to people who are less than 16 years old, and for a third of the price for people who are 60 years old or more.

age=int(input("Enter your age: "))
if age < 16:
    print("Your Ticket cost is £3")
elif age >60:
    print("Your Ticket cost is £2 ")
else:
    print("Your Ticket cost is £6")
