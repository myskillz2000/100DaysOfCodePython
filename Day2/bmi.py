"""Figure out the BMI of someone."""

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = round(float(weight) / float(height) ** 2)
print(f"Your BMI is: {bmi}.")
