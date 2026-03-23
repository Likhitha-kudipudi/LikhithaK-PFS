'''
if statement : This (if  statement) is used to check any condition,if the condition becomes true then it will enter inside the (if statement) 

age = int(input("Enter your Age: "))
if age >= 18:
    print("Your Age is 18 or above")

student_attendance = int (input("enter semester attendance:"))
if student_attendance >= 75:
    print("you can write the exam")

    
----------------------------------------------------------------------

if-else statement :

Age = int (input("Enter your Age : "))
if Age >= 18 :
    print ("you can vote")
else:
    print(f"you can not vote and u have to wait {18-Age} years")
    
####################

total_amount = int (input("enter the total shopping money:"))
if total_amount >= 149:
    print ("no delivery cost")
else:
    print(f"add {149-total_amount} to your cart")


----------------------------------------------------------------------

if-elif-else statement : combination of if and else....in elif part, i can see more conditions


student_marks = int(input("enter your marks :"))
if student_marks >= 90:
    print("you got A+")
elif student_marks >= 75 and student_marks <90:
    print("you got A")
elif student_marks >=60 and student_marks <75:
    print("you got B+")
else:
    print("FAILED")
    
####################  

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
user_choice = input("enter your choice :")
if user_choice == "+":
    print(" the sum is " ,num1+num2)
elif user_choice == "-":
    print(" the sum is " ,num1-num2)
elif user_choice == "*":
    print(" the sum is " ,num1*num2)
elif user_choice == "/":
    print(" the sum is " ,num1/num2)

####################


num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
user_choice = int(input("enter your choice \n1.Add \n2.Sub \n3.Mul \n4.Div :"))
if user_choice == 1:
    print(num1 + num2)
elif user_choice == 2:
    print(num1 - num2)
elif user_choice == 3:
    print(num1 * num2)
elif user_choice == 4:
    print(num1 / num2)

'''
'''
user_choice = int(input("pls enter any number :"))
if user_choice % 2==0 :
    print(f"{user_choice} is even number")
else :
    print(f"{user_choice} is odd number")
'''






















    

