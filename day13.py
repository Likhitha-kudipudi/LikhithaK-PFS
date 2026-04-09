
'''
-
---
-----

num = int(input("enter :"))
for j in range(num):
    for i in range(num):
     print("*",end = "")
    print()

-----
---
-

num = int(input("enter :"))
for j in range (num):
    for i in range(num - j):
        print("*",end = "")
    print()



                -
              -   -
             -  -  -

       
num = int(input("enter : "))
for j in range(num):
    print(" " *(num - j),end = "")
    for i in range(j+1):
        print("*",end = " ")
    print()



ICIC_likhi = {"Name" : "likhi",
                         "ATM PIN" : "0066",
                         "Balance" : 5000}
user_pin = input("Please enter your ATM Pin :")
if len (user_pin) == 4 :
    if user_pin in ICIC_likhi['ATM PIN']:
        user_choice = int(input("enter \n1.withdraw: "))
        if user_choice == 1:
            money_w = int(input("enter money to with draw:"))
            if money_w <= ICIC_likhi['Balance']:
                ICIC_likhi['Balance'] -= money_w         
                print(ICIC_likhi['Balance'])
            else :
                print ("insuff")
        elif user_choice == 2:
            Deposite_m = int(input("pls enter the money you want to deposite:")
            if  Deposite_m % 100 == 0 and Deposite_m >=5000:
                ICIC_likhi['Balance'] += Deposite_m
                print(f"you have deposited{Deposite_m} and the total is {ICIC_likhi}")
            else :
                print(f"
else :
    print("please enter 4 digit pin")

'''


ICIC_likhi_ = {"Name" : "Hema","ATM PIN" : "8074","Balance" : 5000}
user_pin = input("enter 4 digit pin: ")
if len(user_pin) == 4:
    if user_pin in ICIC_hema_['ATM PIN']:
        user_choice = int(input("enter \n1.Withdraw: \n2.Deposite"))
        if user_choice == 1:
            money_w = int(input("enter money you want to withdraw: "))
            if money_w <= ICIC_hema_['Balance']:
                ICIC_hema_['Balance'] -= money_w
                print(ICIC_hema_['Balance'])
            else:
                print("insuff")
        elif user_choice == 2:
            money_d= int(input("enter the amount you want to deposite: "))
            if money_d%100==0 and money_d>=5000:
                user_acc_details['balance']+=money_d
                print(user_acc_detials['Balance'])
            else:
                print("the money cannot be deposited")
    else:
        print("you have entered invalid pin")
else:
    print("check and enter your 4-digit pin")

















    
