# Write a program to find the sum of the first n natural numbers.

num = int(input("Enter the number: "))

sum = 0

for i in range(1, num+1):
    sum+= i
print("sum is ",sum)