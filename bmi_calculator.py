from unittest import result


print("Welcome to the BMI calculator!")
height = float(input("What is your height in meters? "))
weight = float(input("What is your wheight in kg? "))

bmi = round(weight / height ** 2 )

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you are a normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese")
elif bmi > 35:
    print(f"Your BMI is {bmi}, you are clinically obese ") 