'''
table_num = 97
for j in range(1,11):
    print(f"{table_num} X {j} = {table_num * j}")


an = "pyThon Is a prograMming languAge "
count_u = 0
count_l = 0
for ch in an :
    if ch.isupper():
        count_u +=1
    elif ch.islower():
        count_l +=1
print(f"There are total {count_u} capital letters")
print(f"There are total {count_l} small letters")


an = "pyThon Is a prograMming languAge "
cap_l = []
small_l = []
for ch in an :
    if ch.isupper():zsa
        cap_l.append(ch)
    elif ch.islower():
        small_l.append(ch)
print(f" {cap_l} contains all capital letters")
print(f"{small_l} contains all small letters")

ICIC_likhi_ac_details = {"Name" : "likhi",
                         "ATM PIN" : "0066"}
print("welcome to ICIC ATM ")
print("Please Insert your ATM card")
ICIC_user_pin = input("Please enter your ATM Pin :")
if len (ICIC_user_pin) == 4 :
    if ICIC_user_pin in ICIC_likhi_ac_details['ATM PIN']:
        print("the pin is correct")
    else :
        print ("You have entered invalid pin")
else :
    print("please enter 4 digit pin")

'''
perfect_num = int (input("enter a number :"))
fact_all = 0
for j in range(1,perfect_num):
    if perfect_num % j == 0:
        fact_all += j
if fact_all == perfect_num:
    print(f"{perfect_num} is the perfect number")
else :
    print(f"{perfect_num} is not a perfect number")
    
