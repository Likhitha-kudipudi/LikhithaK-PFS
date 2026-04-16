'''
OOP'S :
> Object-Oriented Programming Language is a style of Programming language ,
where we model real-world things as objects that contain both the data functions( )
>reusable of code
>scalable

Class :
>class is a blue-print or template , that defines what kind of data and behaviour
a certain type of object will have

Object :
>Instance of class or an object , is a real instance created from a class .
it is the actual thing that exists in the memory while the program runs

Attributes :
>These are variables that store data related to a class or object



class twice :
    def __init__( nayeon, nationality, single) :
        nayeon.nationality = nationality
        nayeon.single = single
twice_1 = twice("South_Korean","pop")
twice_2 = twice("Japan","ABCD")
print(twice_1.single)
'''

class car :
    wheels = 4
    def __init__(self,make,model,year):
        self.make = make
        self.model =  model
        self.year = year
        self.milage = 20
    def drive(self,miles):
        self.milage += miles
        return f"Drove {miles} miles. Total:{self.milage}"
    def info(self):
        return f"{self.make} {self.model} {self.year}"
car_1 = car(make:"Ford",model:"Mustang",year :"2008")
car_2 = car(make:"Toyota",model:"Camry",year :"2023")
print(car_1.info( ))
print(car_2.info( ))
print(car_2.drive( ))







