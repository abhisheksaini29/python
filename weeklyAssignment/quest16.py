# Write a program to find the sum of the digits of a given number.

n=int(input("Enter a number:"))
sum=0
while(n>0):
    dig=n%10
    sum=sum+dig
    n=n//10
print("The total sum of digits is:",sum)