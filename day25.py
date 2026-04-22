'''
Polymorphism :

>This allows an object of different clsses to be treated as an instance of the same
   base class,with methods behaving differently based on the actual object type.
>print(len("python"))
>print(len([1,2,3]))

fmgwndnmegretjt
Method Overloading :

>This defines multiple methods with the same name but different parameters, it can be any datatype (number,type or order)
    
Method overriding :

>this occurs in the child class, redefining a parent class method with the same signature for runtime.

Operator Overloading-->this customizes operator like +, - for user-defined classes by implementing specific methods.
example:- __add__, __sub__

class calculator :
    def add(self, a,b =0,c =1):
        return a+b+c
cal = calculator( )
print(cal.add(-2))
print(cal.add(3,-4))
print(cal.add(5,-7,-8))

class calculator :
    def add(self, a,b =0,c =1):
        return a+b+c
cal = calculator( )
print(cal.add(2))
print(cal.add(3,4))
print(cal.add(5,7,8))


class calculator :
    def sub(self, a,b =0,c =1):
        return a-b-c
cal = calculator( )
print(cal.sub(2))
print(cal.sub(3,4))
print(cal.sub(5,7,8))



class animal:
    def speak(self):
        return"Sound"

class dog(animal):
    def speak(self):
        return"Woof"

DOG = dog()
print(DOG.speak())


class animal:
    def speak(self):
        return"Sound"
class cat(animal):
    def speak(self):
        return"Meow"
CAT = cat()
print(CAT.speak())



class parent:
    def speak(self):
        return"sound"

class mother(parent):
    def speak(self):
        return"chetha rascal"


class someone:
    def __init__(self, a, b):  #this constructor is constant
        self.a = a
        self.b = b

    def __add__(self, other):  #add fucntionality
        return someone(self.a + other.a, self.b + other.b)
    def __str__(self):
        return f"({self.a}, {self.b})"
any = someone(2,3)
so = someone(5,9)
print(any + so)



class someone:
    def __init__(self, a, b, c):  #this constructor is constant
        self.a = a
        self.b = b
        self.c = c

    def __sub__(self, other):  #add fucntionality
        return someone(self.a - other.a, self.b - other.b, self.c - other.c)
    def __str__(self):
        return f"({self.a}, {self.b}, {self.c})"
any = someone(2,3,9)
so = someone(5,9,6)
print(any - so)

from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2
circle = circle(5)
print(circle.area())
'''




















