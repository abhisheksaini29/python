# Write a program that calculates the Body Mass Index (BMI) and categorizes it based on the following criteria:

#     BMI < 18.5: Underweight
#     18.5 <= BMI < 24.9: Normal weight
#     25 <= BMI < 29.9: Overweight
#     BMI >= 30: Obesity


weight=int(input("enter the weight:"))
height=int(input("enter the height:"))
bmi=weight/height**2
if bmi< 18.5:
 print("underweight")
elif 18.5 <= bmi< 24.9:
 print("normal weight")
elif 25 <= bmi< 29.9: 
 print("Overweight")
elif  bmi >= 30:
  print("Obesity")
else:
 print("not valid")