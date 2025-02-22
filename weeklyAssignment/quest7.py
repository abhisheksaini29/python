# Write a program that takes the lengths of three sides of a triangle as input and determines
#  the type of triangle (equilateral, isosceles,  scalene or right angle tringle ).

side1=int(input("enter the first side:"))
side2=int(input("enter the second side:"))
side3=int(input("enter the third side:"))

if side1==side2==side3:
  print("equilateral triangle")
elif side1==side2 or side2==side3 or side3==side1:
 print("isosceles triangle")
elif side1!=side2 and side2!=side3 and side3!=side1:
  print("scalene triangle")
else:
 print("not a triangle")