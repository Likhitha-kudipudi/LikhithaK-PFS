'''Modules:
---------
>a module in a python is simple file that contain python code(Functions,Variable,classes)
> To use modules, we have to use a keyword called import before the modules


Types of modules  :
-----------------
1. Built-in
2.User -define

User-defined module:
---------------------
>This is developed by the user or programer inside a file of python coding, and used by called import with filename..

syntax:
>import(keyword) file_name
  file_name.functionality


Built-in modules:
>already these comes with installation and are ready to use in the program
>this is developed by the developer


import moduless
print(moduless.addition(2,3))


import math
print(math.sqrt(16))

'''
import random
gen = random.randint(0,100)
user = int(input("Enter a  number :"))
if gen == user:
    print("won the match")
else:
    print("lost the match")
