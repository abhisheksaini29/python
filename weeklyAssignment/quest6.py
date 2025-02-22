# Write a program to check if a given year is a leap year. A year is a leap year if it is divisible by 4, 
# but not by 100, unless it is also divisible by 400.


year=int(input("enter the year:"))
if (year%4==0 and year%100!=0) or (year%400==0) :
    print('its a leap year')
else: 
    print('not leap year')