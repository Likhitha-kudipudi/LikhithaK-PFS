'''
Functions : This is a block of reusable code.
            two types
            1. Built-in / In-Built
            2. User-defined

1. Built-in :
            These are already defined
            ex. print(),sum(),map()

2. User-defined :
            These are defined / created by users
            it starts with the def keyword followed by function name
            it has calling function
            ex. def func_name():#(a,b)=parameters
                    -------
                    -------
                    -------
                func_name() #Arguments

user_in = int(input("Enter the limit :"))
num_1 = 0
num_2 = 1
print(num_1,num_2, end=" ")
for v in range(user_in + 1 ) :
    num_3 = num_1 +num_2
    num_1 = num_2
    num_2 = num_3
    print(num_3,end =" ")

a = 2
def ev_od (a):  #definition function
    if a % 2 ==0 :
        print(f"{a} is even")
    else:
        print(f"{a} is odd")
ev_od(a = 4)    #calling function


prime_num = 9
count = 0
def prime_check(num,k):
    for j in range (1,num+1):
        if num % j == 0 :
            k += 1
    if k == 2:
        print("prime")
    else:
        print("not prime")         
prime_check(prime_num,count)



innn = int(input())
num1 = 0
num2 = 1
def fabina(innn,num3):
    for k in range(innn + 1):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        print(num3, end = " ")
fabina(num3)

'''










