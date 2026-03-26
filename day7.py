'''
print(9+8)
print("python" + "language")
print([1,2] +[3,4])

concatenation: This is nothing but a (+) behaviour
-------------
case-1: integers--->this will act as addition for the int

case-2: note: if u try to add two different datatypes it will show concatenate error ***
print([1,2] + "likhi")

print( 1 + "likhi")
print([1,2] +["likhi", 2])

Tuple: it is a collection of different datatypes and this is represented by (), separated by(,)
-----
thing = (1,"likhi",[12,4],(6,7))
    
thing = (12,89,"python",(23,"likhi",[67,"python is a language",(7,8)],[8,("python",[34,9])]))
print(thing[3][2][1][9])


swapping numbers:
----------------
num = 9
num_2 = 90
print(f" before swapping {num, num_2}")
num,num_2=num_2,num
print(f" after swapping{num, num_2}")

leap year:
---------
leap_year = int(input("enter year:"))
if (leap_year % 4 ==0 and leap_year % 100!=0) or leap_year % 400 == 0:
    print(f" yes,{leap_year} is a leap year")
else:
     print(f" no,{leap_year} is not a leap year")
