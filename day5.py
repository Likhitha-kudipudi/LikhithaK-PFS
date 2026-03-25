'''
string--- it is a collection of characters which is reprented by " " or ' '
anything in b/w quotes comes under string

str="Python Programming"
print(str)

#we can also use index to find thespecific element in sequence
index palcement[]
str="Python Programming"
print(str[7])

str="Python Programming"
print(str[7:13])

str="Python Programming"
print(str[:13])

#immutable,we can't modify  on pqrticular var
str="Python Programming"
mod=str.replace("Python","Java")
print(str)
print(mod)

#negative indexing access from back starts with index [1]
str="Python Programming"
print(str[-6])

a_day="I'm Navya Sri from Visakhapatnam completed my Btech in Raghu Engineering College in the year 2025, currently a Data analytics trainee"
print(f"My name is {a_day[4:13]}")
print(f"My course is {a_day[-22:-1]}")
print(a_day[: : -2])

len()---to get the length of the string

str='123'
num=int(str)
print(type(num))

str="Python Programming"
print(len(str))  #length of a string

#slpit()---remove space, and it is converted into list[] it will give the seperated thing in each index
str="Python Programming   is a programming language"
print(str.split(" "))
print(str.split("   "))
print(str.split("Progamming"))

#lower()---covert string to lowercase char
str="pyTHon pRograMminG"
print(str.lower())

#upper()---covert string to uppercase char
str="pyTHon pRograMminG"
print(str.upper())

#replace()--used to replace old string with new string
str="Python Programming"
print(str.replace("Python","Java"))


str="python is a programming language"
if "python" in str:
    print("Yes")
else:
    print("NO")

#find out user enterd letter is vowel or not
user=input("Enter a letter:")
if user=='a' or user=='e'or user=='i' or user=='o'or user=='u':
    print(f"{user} is a vowel")
else:
    print(f"{user} is not a vowel")
--------------
Vowel_con = input("enter a letter:")

if Vowel_con in "AEIOUaeiou":
    print("vow")
else:
    print("con")
------------------------------

Time_aday = input("enter 24hrs time:")
parts_ = Time_aday.split(":")
hours_ = int(parts_[0])
min_ = int(parts_[1])
if hours_ >=13 and min_ <60:
    print(f"{Time_aday} converted into {hours_- 12}:{min_}pm")

'''



