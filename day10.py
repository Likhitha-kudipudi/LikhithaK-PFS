
'''
prime_num = int(input("enter no:"))
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

for an in range(2,100):
    count = 0
    for j in range (1,an+1):
        if an %j == 0:
            count +=1
    if count ==2 :
        print(f"{an} is a prime")
    else :
        print(f"{an} is not a prime ") 

list_ = [1057,197,9,86,1767,29,97,57,28,96]
for an in list_ :
    count = 0
    for j in range(1,an +1):
        if an % j ==0:
            count +=1
    if count == 2 :
        print(f"{list_} is a prime")
    else :
        print(f"{list_} is not a prime")

any = [2,356,8,6,3,2,8]
empty= []
for j in any:
    if j not in empty :
        empty.append(j)
    print(empty)
        
'''
so = int(input("enter number :"))
length_ = len(str(so))
arms_ = 0
for j in str(so) :
    arms_ += int(j) ** length_
    print(arms_)
if arms_ == so:
    print(f"{so} is armstrong")
else :
    print(f"{so} is not an armstrong")
