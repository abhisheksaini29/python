# Write a program that asks the user for a score between 0 and 100 and prints the corresponding grade. The grading scheme is:

#     90-100: A
#     80-89: B
#     70-79: C
#     60-69: D
#     Below 60: F

user_input = int(input("Enter Score Between 0 and 100: "))

if user_input >= 90 and user_input <= 100:
    print("A")
elif user_input >= 80 and user_input <= 89:
    print("B")
elif user_input >= 70 and user_input <= 79:
    print("C")
elif user_input >= 60 and user_input <= 69:
    print("D")
else:
    print("F")