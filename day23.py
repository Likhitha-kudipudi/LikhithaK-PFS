''''
Encapsulation:
> the principle of bunding data (Attribute) and methods that operates on that data into a single unit,which is a class

Inheritance :
> his allows a child class(Subclass) to acquire the attributes and methods of a parent class (base) this is called inheritence
1. Single inheritence :

class parent :
    def display(self):
        print("this is a parent method")
class child(parent):
    def display(self):
        super().display()
        print("this is a child method")
obj = child()
obj.display()
        
2. Multiple :



class father :
    def skills(self):
        print("Hardwworking")

class mother :
    def skill_2(self):
        print("cooking")
class children(father, mother):
    def all(self):
        print("coding")
any = children()
any.skills()
any.skill_2()
any.all()
    
    
    

class Bankac :
    def __init__(self,balance) :
        self.__balance = balance
    def deposite(self,amount) :
        self.__balance += amount
    def get_balance(self) :
        return self.__balance
acc = Bankac(15000)
acc.deposite(7000)
print(acc.get_balance())



'''

