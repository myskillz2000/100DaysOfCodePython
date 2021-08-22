
""" This asks for your name and returns a hello and your
 name.  Then, we will get the length of your name. 
 Next, look at a way to switch variables after assignment
 and still have access to the initial values."""
name = input("What is your name?")
a = input("a: ")
b = input("b: ")

print("Hello " + name)
print(len(name))

# A concept to switch a and b variables.
c = a
a = b 
b = c

"""Everything until now was leading up to the following project.
In this project we are creating a greeting and asking the following
input means: City name and pet name.  Then the output will use
those two inputs to create a name."""

#1. Create a greeting for the program.
print("Welcome to this name generator project:")

#2. Ask for city name from the user.
city = input("Please enter a city name:\n")

#3. Ask for a pet name from the user.
petname = input("What is a pet name:\n")

#4. Combine the city and pet name to create a name for a band.
print(city + " " + petname)

#5. Make sure the cursor is on a new line with the inputs.
