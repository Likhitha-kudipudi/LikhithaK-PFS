'''
constructor (__init__) :
--------------------
>A constructor is a special method used to initialize object data
> __init__( )

Access Specifiers:
1.Public :

> Syntax  -- name
>we can use it anywhere in the program

2.Protected :

>Syntax -- name
>This is only for internal use
3.Private :

>Syntax -- name
>This one is restricted

Self:
>This keyword is instance variable and unique for each object

class Twice :
    def __init__ (oldest, name,Age):
        oldest.name =  name
        oldest.Age = Age

    def display(oldest):
        print(oldest.name, oldest.Age)
Twi_1 = Twice("Im Nayeon", 29)
Twi_1.display()



class some:
    def __init__(self):
        self.public = "public"
        self.protected = "protected"
        self.private = "private"

any = some()
print(any.public)
print(any.protected)
print(any.private)

'''


user_acc_details={"Name":"likhi","ATM pin":"2110","Balance":70000, "Transaction History":[]}         #ATM 
print("welcome to Union Bank ATM")
print("please insert your card")
pin=input("enter your 4-digit pin: ")
if len(pin)==4:
    if pin in user_acc_details['ATM pin']:
        user_choice=int(input("enter \n 1. Withdraw \n 2. Deposit \n 3. Pin change \n 4. Transaction History"))
        if user_choice==1:
            money_w=int(input("enter the amount you want to withdraw: "))
            if money_w<=user_acc_details['Balance']:
                user_acc_details['Balance']-=money_w
                print(user_acc_details['Balance'])
            else:
                print("insuficient balance")
        elif user_choice==2:
            money_d=int(input("enter the amount you want to deposit: "))
            if money_d%100==0 and money_d>=5000:
                user_acc_details['Balance']+=money_d
                user_acc_details['Transaction History'].append(f"Deposited: {money_d}")
                print(user_acc_details['Balance'])
            else:
                print("the money cannot be deposited")
        elif user_choice==3 :
            attempts=3
            while attempts>0 :
                old_pin=input("enter your old_pin: ")
                if len(old_pin)==4 :
                    if old_pin in user_acc_details['ATM pin'] :
                        new_pin=input("enter the new pin: ")
                        if old_pin!=new_pin:
                            print("new pin is: ",new_pin)
                            break
                        else:
                            print("both pins cannot be the same")
                    else:
                        attempts-=1
                        print(f"you entered incorrect pin and you have {attempts} left")
                        if attempts==0 :
                            print("your card is blocked")
                else:
                    print("enter 4 digit pin")
    else:
        print("you have entered invalid pin")
else:
    print("check and enter your 4-digit pin")






















































