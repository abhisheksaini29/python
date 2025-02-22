# Write a program to print all prime numbers between 1 and 100

for i in range(2,101):   
    for j in range(2,101):
        if i%j == 0:
            break
    if i == j:
        print(i,end=",")