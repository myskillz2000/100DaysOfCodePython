

age = input("What is your current age?")


months_alive = int(age)*12
weeks_alive = int(age)*52
days_alive = int(age)*365.25

months_90 = 90*12
weeks_90 = 90*52
days_90 = 365.25 * 90

months_till_90 = months_90 - months_alive
weeks_till_90 = weeks_90 - weeks_alive
days_till_90 = days_90 - days_alive
print(f"You have {days_till_90} days, {weeks_till_90} weeks and {months_till_90} months left till 90 years old.")


