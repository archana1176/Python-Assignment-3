#Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year.
mon=int(input("Enter the month: "))
if mon==1:
    print("Month", mon, "is January")
elif mon==2:
    print("Month", mon, "is February")
elif mon == 3:
    print("Month", mon, "is March")
elif mon == 4:
    print("Month", mon, "is April")
elif mon==5:
    print("Month", mon, "is May")
elif mon==6:
    print("Month", mon, "is June")
elif mon==7:
    print("Month", mon, "is July")
elif mon==8:
    print("Month", mon, "is August")
elif mon==9:
    print("Month", mon, "is September")
elif mon==10:
    print("Month", mon, "is October")
elif mon==11:
    print("Month", mon, "is November")
elif mon==12:
    print("Month", mon, "is December")
else:
    print("invalid month number")