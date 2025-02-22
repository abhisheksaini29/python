# Write a program that takes an integer input from the user and classifies it as positive, negative, or zero.

number = int(input("Enter Integer: "))


if number > 0:
    print(f"{number} is a Positive number.")
elif number == 0:
    print(f"{number} is a Zero.")
else:
    print(f"{number} is a Negative number.")