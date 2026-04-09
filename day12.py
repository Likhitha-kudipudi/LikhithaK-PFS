'''
Break:this is used to exit from a loop 

for j in range (1,10):
    print(j)
    if j == 5 :
        break
    

lis_ = [1,2,3,4]
for n in lis_:
    print(n)
    if n == 1 :
        break
continue : this is used to skip a particular value and continue the rest


for j in range(1,10):
    if j == 5 :
        continue
    print(j)
    
list_ = [1, "likhi" , 0.95, 2]
for n in list_ :
    if n == "likhi" :
        continue
    print(n)

pass : this is called as space holder incase any statement like (if , for , else , elif.....)
this shouldn't complete, if not we will get indentation error to avoid this , we use pass

for j in range(1,100):
    pass

else - for : it will fall back to else block , when all loops are completed
       
for m in range(1,10):
    print(m)
else :
    print("else block")

while : this a combination of for and if statements, if we did not end the loop in a proper way it will run
upto the memory space becomes empty

num =1
while num<5:
    print(num)
    num +=1
    
user_in = int(input("Enter the limit :"))
num_1 = 0
num_2 = 1
print(num_1,num_2, end=" ")
for v in range(user_in + 1 ) :
    num_3 = num_1 +num_2
    num_1 = num_2
    num_2 = num_3
    print(num_3,end =" ")
'''

    































    
