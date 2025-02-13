#Ask user to input a number and show all even number upto that number starting from number 178

def evenRange(num):
    for i in range(1,num+1):
        if i % 2 == 0:
            print(i,end=" ")

number_range = int(input("Enter number: "))
evenRange(number_range)
print()





