height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

def to_bmi(height, weight):
    height = int(height)*int(height)
    weight = int(weight)
    return weight/height