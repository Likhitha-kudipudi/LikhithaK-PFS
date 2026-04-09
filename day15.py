#ways to pass an arguments in calling function
'''
rime_num = int(input("enter no:"))
count = 0
for j in range (1,prime_num +1 ):
    print(j)
    if prime_num % j ==0 :
        count +=1
        print(count)
if count ==2 :
    print(f"{prime_num} is a prime number")
else :
    print(f"{prime_num} is not a prime number")
it should match same number variables in calling with def

Default arguments : it will take default values from the arguments
-----------------

num = 9
num_ = 10
def add(num,num_):
    print(num)
add(num,num_)

my_name = "likhitha"
def add(my_name):
    print(my_name)
add(my_name = " ")
add(my_name = "kudipudi")


num = int(input("enter num :"))
count = 0         
def prime_check(num,count):
    for i in range(1,num+1):
        if num % i == 0:
            count +=1
    if count == 2:
        print(f"{num} is prime")
    else:
        print(f"{num} is not a prime")
prime_check(num,count)
prime_check(num = 77,count = 0)


        
def any(num,num_2,num_3):
    print(f"num = {num},num_2 = {num_2},num_3 = {num_3}")
any(num_2 = 7,num =0,num_3 =90)



def name(*candidate_):
    print(candidate_)
name("likhi","kudipudi")



def name(*name_):
    print(name_)
name("likhitha"," kudipudi")

Amount_value =int(input("enter amount=")
interest =  5
time = 3
amount = Amount_value*(1+interest/100)**time
compound_interest = amount - Amount_value
print(compound_interest)
print(amount)

sentence= "my name is Likhitha Kudipudi iam from west godavari "
length= sentence.split(" ")
print(len(length))

'''


















