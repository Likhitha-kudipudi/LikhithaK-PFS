'''

Recursive Function  :  Recursion is a programming technique where a function calls itself either directly or indirectly to solve a problem by breaking it into smaller,simpler subproblems.
--------------------      Recursion is especially useful for problems that can be divided into identical smaller tasks , such as mathematical calculations , tree traversals or divide-and-conquer
                                    algorithms.


def validate_pin(self):
    while self.remaining_attempts > 0 :
        user_pin = input("Enter 4 digit PIN: ")
        if len(user_pin) == 4 and user_pin == self.user_info["ATM PIN"]:
            print("welcome to the ATM")
            return True
        else:
            self.remaining_attempts -= 1
            if self.remaining_attempts > 0 :
                print(f"Invalid pin. Attempts left : {self.remaining_attempts}")
            else :
                print(f"Card blocked. Please contact customer care")
                return False
            

str_= "python is a Language"
vo_list = []
co_list=[]
def vo_con(str_,vo_list,co_list):
    for j in str_:
        if j in "AEIOUaeiou":
            vo_list.append(j)
        else:
            co_list.append(j)
    print(f"{vo_list} all of these are vowels in the string")
vo_con(str_,vo_list,co_list)


'''
num = int(input("enter num:"))
count = 0
def prime_num(num,count):
    for j in range(1,num+1):
        print(j)
        if num %j == 0:
            count +=1
            print(count)
    if count ==2 :
            print(f"{num} is a prime number")
else :
    print(f"{num} is not a prime number")
        
prime_num(num,count)














