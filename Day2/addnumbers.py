"""Add the first and second digits together.
This will not work if people input non-numbers though,
there is no validation or try block."""

two_digit_number = input("Type a two digit number:")

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[-1])

result = first_digit + second_digit

print(result)