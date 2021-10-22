from project_day2 import bmi

height = input("What is your height in meters? ")
weight = input("What is your weight in kg? ")

def test_to_bmi(height, weight):
    assert bmi.to_bmi(height,weight) == 25.66