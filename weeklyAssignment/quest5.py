# Write a program to create a list of the squares of the even numbers from 1 to 20.

even_number_square = []

for i in range(1,21):
    if i % 2 == 0:
        even_number_square.append(i**2)

print(even_number_square)