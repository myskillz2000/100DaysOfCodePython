"""Figure out the BMI of someone."""

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / float(height) ** 2
print("Your BMI is: " + str(round(bmi)))
