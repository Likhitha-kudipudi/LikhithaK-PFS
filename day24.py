'''

multi-level:

> This occurs when a class inherits from a child class,creating a grandparent >parent>child

Heirachical :

>

Hybrid inheritance-->this is a combination of two or more types of inheritance, such as sing.
multiple,multi-level, or hierachical all this in a single class.

class Grandparent:
    def Show_GrandParent(self):
        print("I'm Grandparent")

class Parent(Grandparent):
    def Show_Parent(self):
        print("I'm Parent")

class child(Parent):
    def Show_child(self):
        print("I'm child")

any = child()
any.Show_GrandParent()
any.Show_Parent()
any.Show_child()


class BaseApp:
    def Show_BaseFeatures(self):
        print("Base features: Login, Home Screen, Notifications")

class UpdatedApp(BaseApp):
    def Show_NewFeatures(self):
        print("theme: Dark Mode, Chat Support")

class LatestVersionApp(UpdatedApp):
    def Show_LatestFeatures(self):
        print("Add updates: AI Chat, UPI Payments, Offline Mode")

my_app = LatestVersionApp()
my_app.Show_BaseFeatures()      
my_app.Show_NewFeatures()       
my_app.Show_LatestFeatures()
    


class parent:
    def Parent_(self):
        print("I'm Parent")
class child_1(parent):
    def child_(Self):
        print("I'm 1st child")
class child_2(parent):
    def _child(self):
        print("I'm 2nd child") 
class child_3(child_1, child_2):
    def child(self):
        print("I'm the child")

thing = child_3()
thing.Parent_()
thing.child_()
thing._child()
thing.child()



class parent:
    def Parent_(self):
        print("I'm Parent")
        
class child_1(parent):
    def child_(Self):
        print("I'm 1st child")
        
class child_2(parent):
    def _child(self):
        print("I'm 2nd child")
        
class child_3(child_1, child_2):
    def child(self):
        print("I'm the child")

thing = child_3()
thing.Parent_()
thing.child_()
thing._child()
thing.child()

'''


















































