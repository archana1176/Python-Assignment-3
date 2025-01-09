Weight=float(input("Enter your weight(kg): "))
Height=float(input("Enter your Height(m): "))
bmi=float((Weight/(Height**2)))
print("Your BMI is :",bmi)
if bmi < 18.5:
    print("You are in the 'Underweight' range")
elif bmi >= 18.5 and bmi <=24.9:
    print("You are in the 'Normal' range")
elif bmi >=25 and bmi <= 29.9:
    print("You are in the 'Overweight' range")
else:
    print("You are in the 'Obese' range")