print("Welcome to the tip calculator.")

total_bill = input("What was the total bill?")
percentage = input("What percentage of tip would you like to leave?")
people_splitting = input("How many people are in the party?")

total_per_person = (float(total_bill) * float(f"1.{percentage}"))/ float(people_splitting)
print(f"Each person should pay: ${total_per_person:.2f}")
